#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import render

BANNED_RULE_PHRASES = (".cursor/plans", "Plan Mode", "Make Cursor behave")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify migration dry-run or applied outputs.")
    parser.add_argument("--classified", required=True, help="Classified JSON path")
    parser.add_argument("--plan", required=True, help="Plan JSON path")
    parser.add_argument("--manifest", required=True, help="Manifest JSON path")
    parser.add_argument("--report-file", required=True, help="Dry-run report path")
    parser.add_argument("--repo-root", default=".", help="Repository root")
    parser.add_argument("--output", help="Optional JSON output path")
    return parser.parse_args()


def load_json(path: str) -> dict[str, Any]:
    payload = Path(path)
    if not payload.exists():
        return {}
    return json.loads(payload.read_text(encoding="utf-8"))


def check(condition: bool, name: str, details: str) -> dict[str, Any]:
    return {
        "name": name,
        "passed": condition,
        "details": details,
    }


def verify_inventory(classified: dict[str, Any]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    checks: list[dict[str, Any]] = []
    unique = True
    for unit in classified.get("units", []):
        if unit["id"] in seen:
            unique = False
            break
        seen.add(unit["id"])
    checks.append(check(unique, "unique-source-ids", "All classified source IDs are unique"))
    checks.append(
        check(
            all("migration" in unit and "classification" in unit["migration"] for unit in classified.get("units", [])),
            "migration-metadata-present",
            "Every source unit includes migration metadata",
        )
    )
    return checks


def verify_plan(classified: dict[str, Any], plan: dict[str, Any], repo_root: Path) -> list[dict[str, Any]]:
    units = render.unit_map(classified)
    checks: list[dict[str, Any]] = []
    valid_sources = all(action["source_id"] in units for action in plan.get("actions", []))
    checks.append(check(valid_sources, "plan-source-ids", "Every action references a discovered source"))

    rule_outputs_clean = True
    for action in plan.get("actions", []):
        if action["kind"] != "rule":
            continue
        preview = render.render_rule_section(units[action["source_id"]])
        if any(phrase in preview for phrase in BANNED_RULE_PHRASES):
            rule_outputs_clean = False
            break
    checks.append(check(rule_outputs_clean, "semantic-leakage", "Rendered rule outputs do not retain Cursor-only phrases"))

    unmanaged_skill_conflicts = True
    for action in plan.get("actions", []):
        if action["kind"] != "skill":
            continue
        for target in action["targets"]:
            target_path = repo_root / target["target_path"]
            if target_path.exists() and action["status"] != "conflict":
                unmanaged_skill_conflicts = False
                break
    checks.append(check(unmanaged_skill_conflicts, "skill-conflict-detection", "Pre-existing unmanaged target skills are reported as conflicts"))

    report_only_for_agends = True
    agents_path = repo_root / "AGENTS.md"
    if agents_path.exists() and agents_path.read_text(encoding="utf-8").strip():
        for action in plan.get("actions", []):
            if action["kind"] == "rule" and action["status"] != "conflict":
                report_only_for_agends = False
                break
    checks.append(check(report_only_for_agends, "agents-md-conflict-detection", "Existing unmanaged AGENTS.md blocks rule apply actions"))
    return checks


def verify_manifest(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    checks = [
        check(manifest.get("version") == 1, "manifest-version", "Manifest uses schema version 1"),
        check("skill_target_root" in manifest, "manifest-skill-root", "Manifest records the configured skill target root"),
        check(isinstance(manifest.get("entries", []), list), "manifest-entries", "Manifest entries are stored as a list"),
    ]
    return checks


def verify_report(report_path: Path) -> list[dict[str, Any]]:
    text = report_path.read_text(encoding="utf-8") if report_path.exists() else ""
    required_sections = ("# Cursor-to-Codex Migration Dry Run", "## Summary", "## Inventory", "## Planned Actions", "## Orphans")
    checks = [
        check(report_path.exists(), "report-exists", "Dry-run report file exists"),
        check(all(section in text for section in required_sections), "report-sections", "Dry-run report contains the required sections"),
    ]
    return checks


def verify_current_targets(repo_root: Path) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    config_path = repo_root / ".codex/config.toml"
    if config_path.exists():
        text = config_path.read_text(encoding="utf-8")
        checks.append(
            check(
                "# codex-migrate:start:agents" in text and "# codex-migrate:end:agents" in text,
                "managed-agents-block",
                "Existing config.toml contains a managed agents block",
            )
        )
    return checks


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    classified = load_json(args.classified)
    plan = load_json(args.plan)
    manifest = load_json(args.manifest)
    report_path = Path(args.report_file)

    checks: list[dict[str, Any]] = []
    checks.extend(verify_inventory(classified))
    checks.extend(verify_plan(classified, plan, repo_root))
    checks.extend(verify_manifest(manifest))
    checks.extend(verify_report(report_path))
    checks.extend(verify_current_targets(repo_root))

    payload = {
        "passed": all(item["passed"] for item in checks),
        "checks": checks,
    }

    text = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0 if payload["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
