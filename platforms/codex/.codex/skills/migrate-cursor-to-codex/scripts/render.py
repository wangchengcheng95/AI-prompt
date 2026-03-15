#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OWNED_SKILL_TEMPLATE = "<!-- codex-migrate:owned source={source_path} -->"
OWNED_AGENT_TEMPLATE = "# codex-migrate:owned source={source_path}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render or apply Cursor migration outputs.")
    parser.add_argument("--classified", required=True, help="Classified JSON path")
    parser.add_argument("--plan", required=True, help="Plan JSON path")
    parser.add_argument("--manifest", required=True, help="Manifest JSON path")
    parser.add_argument("--repo-root", default=".", help="Repository root")
    parser.add_argument("--mode", choices=("dry-run", "apply"), default="dry-run")
    parser.add_argument("--report-file", help="Optional markdown report path")
    parser.add_argument("--only-kind", action="append", choices=("rule", "skill", "agent"), help="Apply only the selected source kind")
    parser.add_argument("--only-source-id", action="append", help="Apply only the selected source IDs")
    return parser.parse_args()


def load_json(path: str) -> dict[str, Any]:
    payload = Path(path)
    if not payload.exists():
        return {}
    return json.loads(payload.read_text(encoding="utf-8"))


def dump_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def unit_map(classified: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {unit["id"]: unit for unit in classified["units"]}


def build_frontmatter(name: str, description: str) -> str:
    return f"---\nname: {name}\ndescription: {json.dumps(description, ensure_ascii=False)}\n---"


def render_rule_section(unit: dict[str, Any]) -> str:
    normalized = unit["normalized"]
    section_key = normalized["section_key"]
    title = normalized["title"]
    body = normalized["body"].strip()
    return "\n".join(
        [
            f"<!-- codex-migrate:start:{section_key} -->",
            f"## {title}",
            "",
            body,
            f"<!-- codex-migrate:end:{section_key} -->",
            "",
        ]
    ).strip() + "\n"


def render_skill_file(unit: dict[str, Any]) -> str:
    frontmatter = build_frontmatter(unit["name"], unit.get("description", ""))
    marker = OWNED_SKILL_TEMPLATE.format(source_path=unit["source_path"])
    body = unit["body"].strip()
    return "\n".join([frontmatter, marker, body, ""]).lstrip()


def render_agent_role_file(unit: dict[str, Any]) -> str:
    model = str(unit["frontmatter"].get("model") or "inherit")
    marker = OWNED_AGENT_TEMPLATE.format(source_path=unit["source_path"])
    instructions = unit["body"].strip().replace('"""', '\\"\\"\\"')
    return "\n".join(
        [
            marker,
            f'model = "{model}"',
            'developer_instructions = """',
            instructions,
            '"""',
            "",
        ]
    )


def render_agents_block(agent_units: list[dict[str, Any]]) -> str:
    lines = ["# codex-migrate:start:agents"]
    for unit in sorted(agent_units, key=lambda item: item["normalized"]["role_id"]):
        role_id = unit["normalized"]["role_id"]
        description = unit.get("description", "").replace('"', '\\"')
        lines.extend(
            [
                f"[agents.{role_id}]",
                f'description = "{description}"',
                f'config_file = "agents/{role_id}.toml"',
                "",
            ]
        )
    lines.append("# codex-migrate:end:agents")
    lines.append("")
    return "\n".join(lines)


def upsert_marked_section(existing: str, section_key: str, rendered: str) -> str:
    pattern = re.compile(
        rf"<!-- codex-migrate:start:{re.escape(section_key)} -->.*?<!-- codex-migrate:end:{re.escape(section_key)} -->\n?",
        re.DOTALL,
    )
    if pattern.search(existing):
        return pattern.sub(rendered, existing)
    if existing.strip():
        if "<!-- codex-migrate:start:" not in existing:
            raise ValueError("AGENTS.md exists without migration markers")
        return existing.rstrip() + "\n\n" + rendered
    return rendered


def upsert_agents_block(existing: str, rendered: str) -> str:
    pattern = re.compile(r"# codex-migrate:start:agents.*?# codex-migrate:end:agents\n?", re.DOTALL)
    if pattern.search(existing):
        return pattern.sub(rendered, existing)
    if existing.strip():
        raise ValueError("config.toml exists without a managed agents block")
    return rendered


def preview_block(text: str, max_lines: int = 18) -> str:
    lines = text.strip().splitlines()
    if len(lines) <= max_lines:
        return text.strip()
    return "\n".join(lines[:max_lines] + ["..."])


def build_report(plan: dict[str, Any], classified: dict[str, Any], previews: dict[str, list[dict[str, str]]]) -> str:
    units = unit_map(classified)
    lines = [
        "# Cursor-to-Codex Migration Dry Run",
        "",
        f"- Generated at: {datetime.now(timezone.utc).isoformat()}",
        f"- Repo root: `{plan['repo_root']}`",
        "",
        "## Summary",
        "",
        f"- Sources: {plan['summary']['sources']}",
        f"- Planned writes: {plan['summary']['planned']}",
        f"- Conflicts: {plan['summary']['conflicts']}",
        f"- Noop: {plan['summary']['noop']}",
        f"- Orphans: {plan['summary']['orphans']}",
        "",
        "## Inventory",
        "",
    ]
    for action in plan["actions"]:
        unit = units[action["source_id"]]
        lines.append(
            f"- `{action['source_id']}`: kind=`{unit['kind']}`, classification=`{action['classification']}`, status=`{action['status']}`"
        )
    lines.extend(["", "## Planned Actions", ""])
    for action in plan["actions"]:
        unit = units[action["source_id"]]
        lines.append(f"### `{action['source_id']}`")
        lines.append("")
        lines.append(f"- Source: `{unit['source_path']}`")
        lines.append(f"- Status: `{action['status']}`")
        lines.append(f"- Targets: `{', '.join(action['target_paths']) or 'none'}`")
        if action["conflicts"]:
            lines.append("- Conflicts:")
            for conflict in action["conflicts"]:
                lines.append(f"  - `{conflict['target_path']}`: {conflict['reason']}")
        if previews.get(action["source_id"]):
            lines.append("- Proposed outputs:")
            for preview in previews[action["source_id"]]:
                lines.append(f"  - `{preview['target_path']}`")
                lines.append("")
                lines.append("```text")
                lines.append(preview["content"])
                lines.append("```")
        lines.append("")
    lines.extend(["## Orphans", ""])
    if not plan["orphans"]:
        lines.append("- None")
    else:
        for orphan in plan["orphans"]:
            lines.append(f"- `{orphan['source_path']}` -> cleanup proposal for `{', '.join(orphan['target_paths'])}`")
    lines.append("")
    return "\n".join(lines)


def collect_previews(plan: dict[str, Any], classified: dict[str, Any]) -> dict[str, list[dict[str, str]]]:
    units = unit_map(classified)
    previews: dict[str, list[dict[str, str]]] = {}
    direct_agents = [units[action["source_id"]] for action in plan["actions"] if action["kind"] == "agent" and action["status"] == "planned"]
    agents_block = render_agents_block(direct_agents) if direct_agents else ""

    for action in plan["actions"]:
        unit = units[action["source_id"]]
        action_previews: list[dict[str, str]] = []
        for target in action["targets"]:
            if target["target_kind"] == "agents_md_section":
                content = render_rule_section(unit)
            elif target["target_kind"] == "codex_skill":
                content = render_skill_file(unit)
            elif target["target_kind"] == "codex_agent_config":
                content = agents_block
            elif target["target_kind"] == "codex_agent_role":
                content = render_agent_role_file(unit)
            else:
                continue
            action_previews.append({"target_path": target["target_path"], "content": preview_block(content)})
        previews[action["source_id"]] = action_previews
    return previews


def update_manifest(plan: dict[str, Any], classified: dict[str, Any], manifest: dict[str, Any]) -> dict[str, Any]:
    units = unit_map(classified)
    manifest_entries = {entry["source_path"]: entry for entry in manifest.get("entries", [])}
    now = datetime.now(timezone.utc).isoformat()
    for action in plan["actions"]:
        if action["status"] != "planned":
            continue
        unit = units[action["source_id"]]
        manifest_entries[unit["source_path"]] = {
            "source_path": unit["source_path"],
            "kind": unit["kind"],
            "content_hash": unit["content_hash"],
            "classification": action["classification"],
            "target_paths": action["target_paths"],
            "last_migrated_at": now,
            "last_verified_at": "",
        }
    for orphan in plan["orphans"]:
        entry = manifest_entries.setdefault(orphan["source_path"], orphan)
        entry["status"] = "orphaned"
    manifest["entries"] = sorted(manifest_entries.values(), key=lambda item: item["source_path"])
    return manifest


def action_selected(action: dict[str, Any], only_kinds: set[str] | None, only_source_ids: set[str] | None) -> bool:
    if only_kinds and action["kind"] not in only_kinds:
        return False
    if only_source_ids and action["source_id"] not in only_source_ids:
        return False
    return True


def select_actions(plan: dict[str, Any], only_kinds: set[str] | None = None, only_source_ids: set[str] | None = None) -> list[dict[str, Any]]:
    return [action for action in plan["actions"] if action_selected(action, only_kinds, only_source_ids)]


def apply_actions(
    repo_root: Path,
    plan: dict[str, Any],
    classified: dict[str, Any],
    manifest_path: Path,
    only_kinds: set[str] | None = None,
    only_source_ids: set[str] | None = None,
) -> None:
    units = unit_map(classified)
    selected_actions = select_actions(plan, only_kinds=only_kinds, only_source_ids=only_source_ids)

    if any(action["status"] == "conflict" for action in selected_actions):
        raise RuntimeError("apply mode refused due to unmanaged conflicts")
    if not selected_actions:
        return

    agent_units = [units[action["source_id"]] for action in selected_actions if action["kind"] == "agent" and action["status"] == "planned"]
    agent_block = render_agents_block(agent_units) if agent_units else ""
    config_actions = [action for action in selected_actions if any(target["target_kind"] == "codex_agent_config" for target in action["targets"])]
    if config_actions:
        config_path = repo_root / ".codex/config.toml"
        existing = config_path.read_text(encoding="utf-8") if config_path.exists() else ""
        config_path.parent.mkdir(parents=True, exist_ok=True)
        config_path.write_text(upsert_agents_block(existing, agent_block), encoding="utf-8")

    for action in selected_actions:
        if action["status"] != "planned":
            continue
        unit = units[action["source_id"]]
        for target in action["targets"]:
            path = repo_root / target["target_path"]
            path.parent.mkdir(parents=True, exist_ok=True)
            if target["target_kind"] == "agents_md_section":
                existing = path.read_text(encoding="utf-8") if path.exists() else ""
                rendered = render_rule_section(unit)
                path.write_text(upsert_marked_section(existing, target["section_key"], rendered), encoding="utf-8")
            elif target["target_kind"] == "codex_skill":
                path.write_text(render_skill_file(unit), encoding="utf-8")
            elif target["target_kind"] == "codex_agent_role":
                path.write_text(render_agent_role_file(unit), encoding="utf-8")

    manifest = load_json(str(manifest_path)) or {
        "version": 1,
        "skill_target_root": classified.get("skill_target_root", ".codex/skills"),
        "entries": [],
    }
    filtered_plan = dict(plan)
    filtered_plan["actions"] = selected_actions
    filtered_plan["orphans"] = []
    dump_json(manifest_path, update_manifest(filtered_plan, classified, manifest))


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    classified = load_json(args.classified)
    plan = load_json(args.plan)
    manifest_path = Path(args.manifest)
    previews = collect_previews(plan, classified)
    report = build_report(plan, classified, previews)

    if args.report_file:
        report_path = Path(args.report_file)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(report, encoding="utf-8")
    else:
        sys.stdout.write(report)

    if args.mode == "apply":
        only_kinds = set(args.only_kind or [])
        only_source_ids = set(args.only_source_id or [])
        apply_actions(
            repo_root,
            plan,
            classified,
            manifest_path,
            only_kinds=only_kinds or None,
            only_source_ids=only_source_ids or None,
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
