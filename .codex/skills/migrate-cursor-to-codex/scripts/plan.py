#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a migration plan from classified sources.")
    parser.add_argument("--classified", required=True, help="Classified JSON path from classify.py")
    parser.add_argument("--manifest", required=True, help="Manifest JSON path")
    parser.add_argument("--repo-root", default=".", help="Repository root")
    parser.add_argument("--output", help="Optional plan JSON output path")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def manifest_default(skill_target_root: str) -> dict[str, Any]:
    return {
        "version": 1,
        "skill_target_root": skill_target_root,
        "entries": [],
    }


def source_map(units: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {unit["source_path"]: unit for unit in units}


def has_rule_marker(text: str, section_key: str) -> bool:
    return f"<!-- codex-migrate:start:{section_key} -->" in text and f"<!-- codex-migrate:end:{section_key} -->" in text


def has_any_rule_marker(text: str) -> bool:
    return "<!-- codex-migrate:start:" in text


def owned_skill(path: Path, source_path: str) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    marker = f"<!-- codex-migrate:owned source={source_path} -->"
    return marker in text


def owned_agent_file(path: Path, source_path: str) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    marker = f"# codex-migrate:owned source={source_path}"
    return marker in text


def config_block_managed(text: str) -> bool:
    return "# codex-migrate:start:agents" in text and "# codex-migrate:end:agents" in text


def evaluate_conflicts(repo_root: Path, unit: dict[str, Any], target: dict[str, Any]) -> list[dict[str, str]]:
    path = repo_root / target["target_path"]
    source_path = unit["source_path"]

    if target["target_kind"] == "agents_md_section":
        if not path.exists():
            return []
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            return []
        section_key = target["section_key"]
        if has_rule_marker(text, section_key) or has_any_rule_marker(text):
            return []
        return [{"target_path": target["target_path"], "reason": "AGENTS.md exists without migration ownership markers"}]

    if target["target_kind"] == "codex_skill":
        if not path.exists():
            return []
        if owned_skill(path, source_path):
            return []
        return [{"target_path": target["target_path"], "reason": "Target skill already exists and is unmanaged"}]

    if target["target_kind"] == "codex_agent_config":
        if not path.exists():
            return []
        text = path.read_text(encoding="utf-8")
        if not text.strip() or config_block_managed(text):
            return []
        return [{"target_path": target["target_path"], "reason": "config.toml exists without a managed agents block"}]

    if target["target_kind"] == "codex_agent_role":
        if not path.exists():
            return []
        if owned_agent_file(path, source_path):
            return []
        return [{"target_path": target["target_path"], "reason": "Agent role file already exists and is unmanaged"}]

    return []


def build_plan(classified: dict[str, Any], manifest: dict[str, Any], repo_root: Path) -> dict[str, Any]:
    if not manifest:
        manifest = manifest_default(classified.get("skill_target_root", ".codex/skills"))

    entries = {entry["source_path"]: entry for entry in manifest.get("entries", [])}
    actions: list[dict[str, Any]] = []
    for unit in classified["units"]:
        targets = unit["migration"]["targets"]
        target_paths = [target["target_path"] for target in targets]
        manifest_entry = entries.get(unit["source_path"])
        conflicts: list[dict[str, str]] = []
        for target in targets:
            conflicts.extend(evaluate_conflicts(repo_root, unit, target))

        target_exists = all((repo_root / target_path).exists() for target_path in target_paths) if target_paths else False
        if (
            manifest_entry
            and manifest_entry.get("content_hash") == unit["content_hash"]
            and manifest_entry.get("target_paths") == target_paths
            and target_exists
        ):
            action = "noop"
            status = "noop"
        else:
            action = "upsert"
            status = "conflict" if conflicts else "planned"

        actions.append(
            {
                "action": action,
                "status": status,
                "source_id": unit["id"],
                "source_path": unit["source_path"],
                "kind": unit["kind"],
                "classification": unit["migration"]["classification"],
                "targets": targets,
                "target_paths": target_paths,
                "conflicts": conflicts,
            }
        )

    active_sources = set(source_map(classified["units"]).keys())
    orphans: list[dict[str, Any]] = []
    for entry in manifest.get("entries", []):
        if entry["source_path"] in active_sources:
            continue
        orphan = dict(entry)
        orphan["status"] = "orphaned"
        orphan["cleanup_required"] = True
        orphans.append(orphan)

    plan = {
        "version": 1,
        "planned_at": datetime.now(timezone.utc).isoformat(),
        "repo_root": str(repo_root.resolve()),
        "skill_target_root": classified.get("skill_target_root", ".codex/skills"),
        "actions": actions,
        "orphans": orphans,
        "summary": {
            "sources": len(classified["units"]),
            "planned": sum(1 for action in actions if action["status"] == "planned"),
            "conflicts": sum(1 for action in actions if action["status"] == "conflict"),
            "noop": sum(1 for action in actions if action["status"] == "noop"),
            "orphans": len(orphans),
        },
    }
    return plan


def dump_json(payload: dict[str, Any], output: str | None) -> None:
    text = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if output:
        Path(output).write_text(text, encoding="utf-8")
        return
    sys.stdout.write(text)


def main() -> int:
    args = parse_args()
    classified = load_json(Path(args.classified))
    manifest = load_json(Path(args.manifest))
    plan = build_plan(classified, manifest, Path(args.repo_root).resolve())
    dump_json(plan, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
