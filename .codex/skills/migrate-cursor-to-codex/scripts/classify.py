#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Classify discovered Cursor migration sources.")
    parser.add_argument("--inventory", required=True, help="Inventory JSON path from discover.py")
    parser.add_argument("--output", help="Optional classified JSON output path")
    return parser.parse_args()


def load_json(path: str) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def is_delegated_agent(unit: dict[str, Any]) -> bool:
    description = unit.get("description", "").lower()
    body = unit.get("body", "")
    return (
        body.startswith("You are")
        and ("## Workflow" in body or "## Core responsibilities" in body or "## Rules" in body)
        and ("use when" in description or "expert" in description or "verifier" in unit.get("name", ""))
    )


def classify_rule(unit: dict[str, Any]) -> dict[str, Any]:
    normalized = unit["normalized"]
    classification = "transform" if normalized.get("changed") else "direct"
    return {
        "classification": classification,
        "reason": "Rule content requires Codex-oriented phrasing" if classification == "transform" else "Rule is portable as-is",
        "targets": [
            {
                "target_kind": "agents_md_section",
                "target_path": "AGENTS.md",
                "section_key": normalized["section_key"],
            }
        ],
    }


def classify_skill(unit: dict[str, Any], skill_target_root: str) -> dict[str, Any]:
    normalized = unit["normalized"]
    classification = "transform" if normalized.get("requires_split") else "direct"
    return {
        "classification": classification,
        "reason": "Skill should be split into references or scripts" if classification == "transform" else "Skill can be copied directly",
        "targets": [
            {
                "target_kind": "codex_skill",
                "target_path": f"{skill_target_root}/{unit['name']}/SKILL.md",
            }
        ],
    }


def classify_agent(unit: dict[str, Any]) -> dict[str, Any]:
    role_id = unit["normalized"]["role_id"]
    if is_delegated_agent(unit):
        classification = "direct"
        reason = "Agent is a true delegated role"
        targets = [
            {
                "target_kind": "codex_agent_config",
                "target_path": ".codex/config.toml",
                "role_id": role_id,
            },
            {
                "target_kind": "codex_agent_role",
                "target_path": f".codex/agents/{role_id}.toml",
                "role_id": role_id,
            },
        ]
    elif "cursor" in unit["body"].lower():
        classification = "discard"
        reason = "Agent is Cursor-specific and should not migrate"
        targets = []
    else:
        classification = "transform"
        reason = "Agent content is better represented as a skill"
        targets = [
            {
                "target_kind": "codex_skill",
                "target_path": f".codex/skills/{unit['name']}/SKILL.md",
            }
        ]
    return {
        "classification": classification,
        "reason": reason,
        "targets": targets,
    }


def classify_inventory(inventory: dict[str, Any]) -> dict[str, Any]:
    skill_target_root = inventory.get("skill_target_root", ".codex/skills")
    classified_units: list[dict[str, Any]] = []
    for unit in inventory["units"]:
        if unit["kind"] == "rule":
            migration = classify_rule(unit)
        elif unit["kind"] == "skill":
            migration = classify_skill(unit, skill_target_root)
        else:
            migration = classify_agent(unit)
        enriched = dict(unit)
        enriched["migration"] = migration
        classified_units.append(enriched)
    return {
        "version": 1,
        "classified_at": datetime.now(timezone.utc).isoformat(),
        "repo_root": inventory["repo_root"],
        "skill_target_root": skill_target_root,
        "units": classified_units,
    }


def dump_json(payload: dict[str, Any], output: str | None) -> None:
    text = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if output:
        Path(output).write_text(text, encoding="utf-8")
        return
    sys.stdout.write(text)


def main() -> int:
    args = parse_args()
    inventory = load_json(args.inventory)
    classified = classify_inventory(inventory)
    dump_json(classified, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
