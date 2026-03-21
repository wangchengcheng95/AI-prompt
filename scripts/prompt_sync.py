#!/usr/bin/env python3
"""Manifest-driven prompt sync and backflow for local sibling workspaces."""

from __future__ import annotations

import argparse
import hashlib
import os
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any

import yaml

EXIT_OK = 0
EXIT_ERROR = 1
EXIT_BLOCKED = 2
STATE_DIR = ".ai-prompt-sync"
STATE_FILE = f"{STATE_DIR}/state.yaml"
BLOCKING_CLASSIFICATIONS = {"drift-local", "conflict", "unmanaged", "missing-target"}

ADVISORY_RULE_WIDTH = 80


class SyncError(Exception):
    """Raised when config or invocation is invalid."""


@dataclass(frozen=True)
class SourceRule:
    source_rel: str
    destination_rel: str
    is_dir: bool


@dataclass(frozen=True)
class MappingEntry:
    bundle_name: str
    source_rel: str
    target_rel: str


@dataclass
class SyncItem:
    classification: str
    bundle_name: str
    source_rel: str | None
    target_rel: str
    note: str = ""


@dataclass
class OperationResult:
    command: str
    bundle_name: str | None
    target_name: str
    items: list[SyncItem]
    changed: int = 0

    def blocking_items(self) -> list[SyncItem]:
        return [item for item in self.items if item.classification in BLOCKING_CLASSIFICATIONS]

    def actionable_items(self) -> list[SyncItem]:
        return [item for item in self.items if item.classification in {"create", "update-safe"}]

    def has_blockers(self) -> bool:
        return bool(self.blocking_items())

    def is_noop(self) -> bool:
        return not self.items


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_relative_path(raw_path: str, label: str) -> str:
    path = PurePosixPath(raw_path)
    if raw_path in {"", "."}:
        raise SyncError(f"{label} must be a non-empty relative path")
    if path.is_absolute():
        raise SyncError(f"{label} must be relative: {raw_path}")
    if ".." in path.parts:
        raise SyncError(f"{label} must not escape its root: {raw_path}")
    normalized = path.as_posix()
    if normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized


def normalize_optional_relative_path(raw_path: str | None, label: str) -> str | None:
    if raw_path is None:
        return None
    return normalize_relative_path(raw_path, label)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


class PromptSyncService:
    def __init__(self, repo_root: Path) -> None:
        self.repo_root = repo_root.resolve()
        self.manifest_path = self.repo_root / "sync-manifest.yaml"
        self.targets_path = self.repo_root / "sync-targets.local.yaml"
        self.manifest = self._load_yaml(self.manifest_path, required=True)
        self.targets = self._load_yaml(self.targets_path, required=True)

    def _load_yaml(self, path: Path, required: bool) -> dict[str, Any]:
        if not path.exists():
            if required:
                raise SyncError(f"Missing required YAML file: {path}")
            return {}
        with path.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle) or {}
        if not isinstance(data, dict):
            raise SyncError(f"Expected a mapping in {path}")
        return data

    def _write_yaml(self, path: Path, data: dict[str, Any]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            yaml.safe_dump(data, handle, sort_keys=False, allow_unicode=False)

    def _bundles(self) -> dict[str, dict[str, Any]]:
        bundles = self.manifest.get("bundles")
        if not isinstance(bundles, dict):
            raise SyncError("sync-manifest.yaml must define a top-level 'bundles' mapping")
        return bundles

    def _bundle(self, bundle_name: str) -> dict[str, Any]:
        bundle = self._bundles().get(bundle_name)
        if not isinstance(bundle, dict):
            raise SyncError(f"Unknown bundle: {bundle_name}")
        return bundle

    def _target(self, target_name: str) -> dict[str, Any]:
        targets = self.targets.get("targets")
        if not isinstance(targets, dict):
            raise SyncError("sync-targets.local.yaml must define a top-level 'targets' mapping")
        target = targets.get(target_name)
        if not isinstance(target, dict):
            raise SyncError(f"Unknown target: {target_name}")
        return target

    def _target_root(self, target_name: str) -> tuple[Path, dict[str, Any]]:
        target = self._target(target_name)
        target_path = Path(target.get("path", "")).expanduser()
        if not target_path.is_absolute():
            raise SyncError(f"Target path must be absolute for {target_name}")
        if not target_path.exists():
            raise SyncError(f"Target path does not exist for {target_name}: {target_path}")
        return target_path, target

    def _bundle_matches_target(self, bundle: dict[str, Any], target: dict[str, Any]) -> bool:
        candidates = bundle.get("default_targets")
        if not isinstance(candidates, list):
            raise SyncError("Bundle is missing default_targets")
        for candidate in candidates:
            if not isinstance(candidate, dict):
                continue
            if candidate.get("type") == target.get("type") and candidate.get("tool") == target.get("tool"):
                return True
        return False

    def _source_rules(self, bundle_name: str) -> list[SourceRule]:
        rules: list[SourceRule] = []
        bundle = self._bundle(bundle_name)
        raw_sources = bundle.get("sources")
        if not isinstance(raw_sources, list):
            raise SyncError(f"Bundle '{bundle_name}' is missing a sources list")
        for raw_rule in raw_sources:
            if not isinstance(raw_rule, dict):
                raise SyncError(f"Bundle '{bundle_name}' has an invalid source rule")
            source_rel = normalize_relative_path(str(raw_rule.get("path", "")), "source path")
            destination_rel = normalize_relative_path(str(raw_rule.get("destination", "")), "destination path")
            source_abs = self.repo_root / source_rel
            if not source_abs.exists():
                raise SyncError(f"Bundle '{bundle_name}' references a missing source path: {source_rel}")
            rules.append(SourceRule(source_rel=source_rel, destination_rel=destination_rel, is_dir=source_abs.is_dir()))
        return rules

    def _managed_paths(self, bundle_name: str) -> list[str]:
        bundle = self._bundle(bundle_name)
        managed = bundle.get("managed_paths")
        if not isinstance(managed, list):
            raise SyncError(f"Bundle '{bundle_name}' is missing managed_paths")
        return [normalize_relative_path(str(path), "managed path") for path in managed]

    def _is_managed_path(self, bundle_name: str, target_rel: str) -> bool:
        for managed in self._managed_paths(bundle_name):
            if target_rel == managed or target_rel.startswith(f"{managed}/"):
                return True
        return False

    def _state_path(self, target_root: Path) -> Path:
        return target_root / STATE_FILE

    def _load_state(self, target_root: Path) -> dict[str, Any]:
        state_path = self._state_path(target_root)
        if not state_path.exists():
            return {"version": 1, "entries": {}}
        with state_path.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle) or {}
        if not isinstance(data, dict):
            raise SyncError(f"Expected a mapping in state file: {state_path}")
        data.setdefault("version", 1)
        data.setdefault("entries", {})
        if not isinstance(data["entries"], dict):
            raise SyncError(f"State file entries must be a mapping: {state_path}")
        return data

    def _save_state(self, target_root: Path, state: dict[str, Any]) -> None:
        self._write_yaml(self._state_path(target_root), state)

    def _entry_state(self, state: dict[str, Any], target_rel: str) -> dict[str, Any] | None:
        entries = state.get("entries", {})
        value = entries.get(target_rel)
        if isinstance(value, dict):
            return value
        return None

    def _expand_rule_for_export(self, bundle_name: str, rule: SourceRule) -> list[MappingEntry]:
        source_abs = self.repo_root / rule.source_rel
        if not rule.is_dir:
            return [
                MappingEntry(
                    bundle_name=bundle_name,
                    source_rel=rule.source_rel,
                    target_rel=rule.destination_rel,
                )
            ]
        mappings: list[MappingEntry] = []
        for file_path in sorted(path for path in source_abs.rglob("*") if path.is_file()):
            suffix = file_path.relative_to(source_abs).as_posix()
            mappings.append(
                MappingEntry(
                    bundle_name=bundle_name,
                    source_rel=PurePosixPath(rule.source_rel, suffix).as_posix(),
                    target_rel=PurePosixPath(rule.destination_rel, suffix).as_posix(),
                )
            )
        return mappings

    def _export_entries(self, bundle_name: str) -> list[MappingEntry]:
        entries: list[MappingEntry] = []
        for rule in self._source_rules(bundle_name):
            entries.extend(self._expand_rule_for_export(bundle_name, rule))
        return entries

    def _classify_export_entry(
        self,
        entry: MappingEntry,
        target_root: Path,
        state: dict[str, Any],
    ) -> SyncItem | None:
        source_abs = self.repo_root / entry.source_rel
        target_abs = target_root / entry.target_rel
        source_hash = sha256_file(source_abs)
        target_exists = target_abs.exists()
        target_hash = sha256_file(target_abs) if target_exists and target_abs.is_file() else None
        last = self._entry_state(state, entry.target_rel)

        if not target_exists:
            return SyncItem("create", entry.bundle_name, entry.source_rel, entry.target_rel)
        if target_hash == source_hash:
            return None
        if last is None:
            return SyncItem("drift-local", entry.bundle_name, entry.source_rel, entry.target_rel, "No sync state")
        last_source_hash = last.get("last_source_hash")
        last_target_hash = last.get("last_target_hash")
        if target_hash == last_target_hash and source_hash != last_source_hash:
            return SyncItem("update-safe", entry.bundle_name, entry.source_rel, entry.target_rel)
        if target_hash != last_target_hash and source_hash == last_source_hash:
            return SyncItem("drift-local", entry.bundle_name, entry.source_rel, entry.target_rel)
        return SyncItem("conflict", entry.bundle_name, entry.source_rel, entry.target_rel)

    def preview_export(self, bundle_name: str, target_name: str) -> OperationResult:
        target_root, target = self._target_root(target_name)
        bundle = self._bundle(bundle_name)
        if not self._bundle_matches_target(bundle, target):
            raise SyncError(f"Bundle '{bundle_name}' does not support target '{target_name}'")
        state = self._load_state(target_root)
        items = [
            item
            for entry in self._export_entries(bundle_name)
            if (item := self._classify_export_entry(entry, target_root, state)) is not None
        ]
        return OperationResult(command="preview-export", bundle_name=bundle_name, target_name=target_name, items=items)

    def export(self, bundle_name: str, target_name: str) -> OperationResult:
        result = self.preview_export(bundle_name, target_name)
        if result.has_blockers() or result.is_noop():
            return result
        target_root, _ = self._target_root(target_name)
        state = self._load_state(target_root)
        for item in result.actionable_items():
            self._copy_repo_file(item.source_rel, target_root / item.target_rel)
            self._update_state_entry(state, item, target_root, mode="export")
            result.changed += 1
        self._save_state(target_root, state)
        result.command = "export"
        return result

    def _copy_repo_file(self, source_rel: str | None, target_abs: Path) -> None:
        if source_rel is None:
            raise SyncError("Cannot copy without a source path")
        source_abs = self.repo_root / source_rel
        target_abs.parent.mkdir(parents=True, exist_ok=True)
        target_abs.write_bytes(source_abs.read_bytes())

    def _update_state_entry(self, state: dict[str, Any], item: SyncItem, target_root: Path, mode: str) -> None:
        if item.source_rel is None:
            raise SyncError("Cannot write state without a source path")
        target_abs = target_root / item.target_rel
        entries = state.setdefault("entries", {})
        entries[item.target_rel] = {
            "bundle": item.bundle_name,
            "source_path": item.source_rel,
            "target_path": item.target_rel,
            "last_source_hash": sha256_file(self.repo_root / item.source_rel),
            "last_target_hash": sha256_file(target_abs),
            "last_sync_at": utc_now(),
            "last_sync_mode": mode,
        }

    def check_drift(self, bundle_name: str, target_name: str) -> OperationResult:
        result = self.preview_export(bundle_name, target_name)
        result.command = "check-drift"
        return result

    def _resolve_import_candidates(
        self,
        target_name: str,
        target_rel: str,
    ) -> tuple[str, list[tuple[SourceRule, str]]]:
        target_root, target = self._target_root(target_name)
        requested_abs = target_root / target_rel
        if not requested_abs.exists():
            return "", []

        matches: list[tuple[str, list[tuple[SourceRule, str]]]] = []
        for bundle_name, bundle in self._bundles().items():
            if not bundle.get("backflow", {}).get("enabled", False):
                continue
            if not self._bundle_matches_target(bundle, target):
                continue
            if not self._is_managed_path(bundle_name, target_rel):
                continue
            resolved: list[tuple[SourceRule, str]] = []
            for rule in self._source_rules(bundle_name):
                if rule.is_dir:
                    dest_root = rule.destination_rel
                    if target_rel == dest_root or target_rel.startswith(f"{dest_root}/"):
                        suffix = "" if target_rel == dest_root else PurePosixPath(target_rel).relative_to(PurePosixPath(dest_root)).as_posix()
                        resolved.append((rule, suffix))
                elif target_rel == rule.destination_rel:
                    resolved.append((rule, ""))
            if resolved:
                matches.append((bundle_name, resolved))

        if len(matches) > 1:
            raise SyncError(f"Target path matches multiple bundles: {target_rel}")
        if not matches:
            return "", []
        return matches[0]

    def _expand_import_entries(
        self,
        target_name: str,
        target_rel: str,
        dest_override: str | None,
    ) -> tuple[str, list[MappingEntry]]:
        target_root, _ = self._target_root(target_name)
        requested_abs = target_root / target_rel
        bundle_name, candidates = self._resolve_import_candidates(target_name, target_rel)
        if not bundle_name:
            return "", []
        entries: list[MappingEntry] = []
        override_rel = normalize_optional_relative_path(dest_override, "destination override")
        if requested_abs.is_file():
            rule, suffix = candidates[0]
            source_rel = override_rel or self._import_destination(rule, suffix)
            entries.append(MappingEntry(bundle_name=bundle_name, source_rel=source_rel, target_rel=target_rel))
            return bundle_name, entries

        for file_path in sorted(path for path in requested_abs.rglob("*") if path.is_file()):
            suffix_from_request = file_path.relative_to(requested_abs).as_posix()
            rule, base_suffix = candidates[0]
            combined_suffix = base_suffix
            if suffix_from_request != ".":
                combined_suffix = (
                    PurePosixPath(base_suffix, suffix_from_request).as_posix()
                    if base_suffix
                    else suffix_from_request
                )
            source_rel = override_rel
            if source_rel is None:
                source_rel = self._import_destination(rule, combined_suffix)
            else:
                source_rel = (
                    PurePosixPath(source_rel, suffix_from_request).as_posix()
                    if suffix_from_request
                    else source_rel
                )
            target_file_rel = (
                PurePosixPath(target_rel, suffix_from_request).as_posix()
                if suffix_from_request
                else target_rel
            )
            entries.append(MappingEntry(bundle_name=bundle_name, source_rel=source_rel, target_rel=target_file_rel))
        return bundle_name, entries

    def _import_destination(self, rule: SourceRule, suffix: str) -> str:
        if not rule.is_dir:
            return rule.source_rel
        return PurePosixPath(rule.source_rel, suffix).as_posix() if suffix else rule.source_rel

    def _classify_import_entry(
        self,
        entry: MappingEntry,
        target_root: Path,
        state: dict[str, Any],
    ) -> SyncItem | None:
        target_abs = target_root / entry.target_rel
        if not target_abs.exists():
            return SyncItem("missing-target", entry.bundle_name, entry.source_rel, entry.target_rel)

        target_hash = sha256_file(target_abs)
        upstream_abs = self.repo_root / entry.source_rel
        upstream_exists = upstream_abs.exists()
        upstream_hash = sha256_file(upstream_abs) if upstream_exists and upstream_abs.is_file() else None
        last = self._entry_state(state, entry.target_rel)

        if not upstream_exists:
            return SyncItem("create", entry.bundle_name, entry.source_rel, entry.target_rel)
        if upstream_hash == target_hash:
            return None
        if last is None:
            return SyncItem("conflict", entry.bundle_name, entry.source_rel, entry.target_rel, "No sync state")
        last_source_hash = last.get("last_source_hash")
        last_target_hash = last.get("last_target_hash")
        if target_hash != last_target_hash and upstream_hash == last_source_hash:
            return SyncItem("update-safe", entry.bundle_name, entry.source_rel, entry.target_rel)
        if target_hash == last_target_hash and upstream_hash != last_source_hash:
            return SyncItem("conflict", entry.bundle_name, entry.source_rel, entry.target_rel, "Upstream changed")
        return SyncItem("conflict", entry.bundle_name, entry.source_rel, entry.target_rel)

    def preview_import(self, target_name: str, target_rel: str, dest_override: str | None) -> OperationResult:
        target_rel = normalize_relative_path(target_rel, "target path")
        target_root, _ = self._target_root(target_name)
        requested_abs = target_root / target_rel
        if not requested_abs.exists():
            item = SyncItem("missing-target", "", None, target_rel)
            return OperationResult(command="preview-import", bundle_name=None, target_name=target_name, items=[item])

        bundle_name, entries = self._expand_import_entries(target_name, target_rel, dest_override)
        if not bundle_name:
            item = SyncItem("unmanaged", "", None, target_rel)
            return OperationResult(command="preview-import", bundle_name=None, target_name=target_name, items=[item])
        state = self._load_state(target_root)
        items = [
            item
            for entry in entries
            if (item := self._classify_import_entry(entry, target_root, state)) is not None
        ]
        return OperationResult(command="preview-import", bundle_name=bundle_name, target_name=target_name, items=items)

    def import_backflow(self, target_name: str, target_rel: str, dest_override: str | None) -> OperationResult:
        result = self.preview_import(target_name, target_rel, dest_override)
        if result.has_blockers() or result.is_noop():
            return result
        target_root, _ = self._target_root(target_name)
        state = self._load_state(target_root)
        for item in result.actionable_items():
            self._copy_target_file(target_root / item.target_rel, item.source_rel)
            self._update_state_entry(state, item, target_root, mode="import-backflow")
            result.changed += 1
        self._save_state(target_root, state)
        result.command = "import-backflow"
        return result

    def _copy_target_file(self, target_abs: Path, destination_rel: str | None) -> None:
        if destination_rel is None:
            raise SyncError("Cannot backflow without a destination path")
        destination_abs = self.repo_root / destination_rel
        destination_abs.parent.mkdir(parents=True, exist_ok=True)
        destination_abs.write_bytes(target_abs.read_bytes())

    def operator_advisory_lines(self, bundle_name: str | None) -> list[str]:
        """Lines from sync-manifest.yaml: default_operator_advisories plus optional bundle operator_advisories."""
        lines: list[str] = []
        default = self.manifest.get("default_operator_advisories")
        if isinstance(default, list):
            for item in default:
                if isinstance(item, str):
                    text = item.strip()
                    if text:
                        lines.append(text)
        if bundle_name:
            bundle = self._bundles().get(bundle_name)
            if isinstance(bundle, dict):
                extra = bundle.get("operator_advisories")
                if isinstance(extra, list):
                    for item in extra:
                        if isinstance(item, str):
                            text = item.strip()
                            if text:
                                lines.append(text)
        return lines


def format_operator_advisory_box(lines: list[str]) -> str:
    if not lines:
        return ""
    border = "=" * ADVISORY_RULE_WIDTH
    body = "\n".join(lines)
    return f"\n{border}\n{body}\n{border}\n"


def emit_operator_advisory(service: PromptSyncService, bundle_name: str | None) -> None:
    """Print manifest-driven operator notes to stderr (optional tooling); never installs anything."""
    if os.environ.get("PROMPT_SYNC_SKIP_PLUGIN_ADVISORY", "").strip():
        return
    boxed = format_operator_advisory_box(service.operator_advisory_lines(bundle_name))
    if boxed:
        print(boxed, file=sys.stderr, end="")


def format_result(result: OperationResult) -> str:
    lines = [f"{result.command}: target={result.target_name}"]
    if result.bundle_name:
        lines[0] += f" bundle={result.bundle_name}"
    if result.is_noop():
        lines.append("No changes.")
        return "\n".join(lines)

    counts: dict[str, int] = {}
    for item in result.items:
        counts[item.classification] = counts.get(item.classification, 0) + 1
    summary = ", ".join(f"{name}={count}" for name, count in sorted(counts.items()))
    lines.append(f"Summary: {summary}")
    for item in result.items:
        source = f" <= {item.source_rel}" if item.source_rel else ""
        note = f" ({item.note})" if item.note else ""
        lines.append(f"- {item.classification}: {item.target_rel}{source}{note}")
    if result.changed:
        lines.append(f"Applied changes: {result.changed}")
    if result.has_blockers():
        lines.append("Blocked: resolve drift/conflicts before writing.")
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    for command in ("preview-export", "export", "check-drift"):
        sub = subparsers.add_parser(command)
        sub.add_argument("--bundle", required=True)
        sub.add_argument("--target", required=True)

    for command in ("preview-import", "import-backflow"):
        sub = subparsers.add_parser(command)
        sub.add_argument("--from-target", required=True, dest="from_target")
        sub.add_argument("--path", required=True)
        sub.add_argument("--dest")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        repo_root = Path(os.environ.get("PROMPT_SYNC_REPO_ROOT", Path(__file__).resolve().parents[1]))
        service = PromptSyncService(repo_root)
        if args.command == "preview-export":
            result = service.preview_export(args.bundle, args.target)
        elif args.command == "export":
            result = service.export(args.bundle, args.target)
        elif args.command == "check-drift":
            result = service.check_drift(args.bundle, args.target)
        elif args.command == "preview-import":
            result = service.preview_import(args.from_target, args.path, args.dest)
        elif args.command == "import-backflow":
            result = service.import_backflow(args.from_target, args.path, args.dest)
        else:
            parser.error(f"Unsupported command: {args.command}")
            return EXIT_ERROR
    except SyncError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return EXIT_ERROR

    print(format_result(result))
    emit_operator_advisory(service, result.bundle_name)
    return EXIT_BLOCKED if result.has_blockers() else EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
