#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

RULE_TITLE_OVERRIDES = {
    "plan-mode-todos": "Planning",
}

RULE_TEXT_REPLACEMENTS = (
    ("Make Cursor behave like a reliable **vibe engineering** agent", "Make the assistant behave like a reliable engineering agent"),
    ("Make Cursor behave like a reliable vibe engineering agent", "Make the assistant behave like a reliable engineering agent"),
    ("Plan Mode", "Planning"),
    ("`.cursor/plans/*.plan.md`", "implementation plans"),
    (".cursor/plans/*.plan.md", "implementation plans"),
    ("Follow `architecture.mdc` for layer boundaries and dependency direction.", "Follow the project architecture rules for layer boundaries and dependency direction."),
    ("Follow `engineering-doctrine.mdc` for end-to-end context propagation and I/O timeouts/deadlines.", "Follow the engineering doctrine rules for end-to-end context propagation and I/O timeouts/deadlines."),
    ("Follow `engineering-doctrine.mdc` for error wrapping, typed errors, and “never ignore errors”.", "Follow the engineering doctrine rules for error wrapping, typed errors, and \"never ignore errors\"."),
    ("Use the **memory-bank-update** skill workflow (or `.cursor/commands/update-memory` if present).", "Use the repository memory update workflow when available."),
    ("Memory Bank (`.cursor/memory/` or `docs/memory_bank/`) should be in git unless it contains secrets.", "Memory Bank files should be in git unless they contain secrets."),
    ("`.cursor/commands/` and `.cursor/rules/` must be in git.", "Memory workflows and project rules should be kept in git."),
    ("After creating or changing this rule, test with `/update-memory` or \"update memory bank\" to confirm behavior.", "After changing the memory workflow, validate it with the repository memory update command."),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Discover Cursor migration sources.")
    parser.add_argument("--repo-root", default=".", help="Repository root to scan")
    parser.add_argument("--skill-target-root", default=".codex/skills", help="Target skill root")
    parser.add_argument("--output", help="Optional JSON output path")
    return parser.parse_args()


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    match = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.DOTALL)
    if not match:
        return {}, text

    frontmatter_text = match.group(1)
    body = match.group(2)
    frontmatter: dict[str, Any] = {}
    for raw_line in frontmatter_text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, raw_value = line.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        if raw_value.startswith(("'", '"')) and raw_value.endswith(("'", '"')) and len(raw_value) >= 2:
            value: Any = raw_value[1:-1]
        elif raw_value.lower() == "true":
            value = True
        elif raw_value.lower() == "false":
            value = False
        else:
            value = raw_value
        frontmatter[key] = value
    return frontmatter, body


def content_hash(text: str) -> str:
    return f"sha256:{hashlib.sha256(text.encode('utf-8')).hexdigest()}"


def extract_title(body: str, fallback: str) -> str:
    for line in body.splitlines():
        match = re.match(r"^#\s+(.*)$", line.strip())
        if match:
            return match.group(1).strip()
    return fallback


def shift_headings(markdown: str, delta: int) -> str:
    shifted: list[str] = []
    for line in markdown.splitlines():
        match = re.match(r"^(#{1,6})(\s+.*)$", line)
        if not match:
            shifted.append(line)
            continue
        hashes, suffix = match.groups()
        shifted.append(f"{'#' * min(6, len(hashes) + delta)}{suffix}")
    return "\n".join(shifted)


def remove_top_heading(body: str, title: str) -> str:
    lines = body.splitlines()
    if lines and lines[0].strip() == f"# {title}".strip():
        return "\n".join(lines[1:]).lstrip("\n")
    return body


def normalize_role_id(name: str) -> str:
    return name.replace("-", "_")


def normalize_rule_unit(name: str, title: str, body: str) -> dict[str, Any]:
    normalized_title = RULE_TITLE_OVERRIDES.get(name, title)
    normalized_body = remove_top_heading(body.strip(), title)
    for old, new in RULE_TEXT_REPLACEMENTS:
        normalized_body = normalized_body.replace(old, new)
    normalized_body = shift_headings(normalized_body, 1).strip()
    return {
        "title": normalized_title,
        "body": normalized_body,
        "section_key": name,
        "changed": normalized_title != title or normalized_body != body.strip(),
    }


def normalize_skill_unit(name: str, title: str, body: str) -> dict[str, Any]:
    requires_split = body.count("\n") > 250 or "See [" in body
    return {
        "title": title,
        "body": body.strip(),
        "section_key": name,
        "requires_split": requires_split,
        "changed": False,
    }


def normalize_agent_unit(name: str, title: str, body: str) -> dict[str, Any]:
    return {
        "title": title,
        "body": body.strip(),
        "role_id": normalize_role_id(name),
        "section_key": normalize_role_id(name),
        "changed": False,
    }


def relative_path(repo_root: Path, path: Path) -> str:
    return path.relative_to(repo_root).as_posix()


def build_source_unit(repo_root: Path, path: Path, kind: str) -> dict[str, Any]:
    text = load_text(path)
    frontmatter, body = parse_frontmatter(text)
    name = str(frontmatter.get("name") or path.stem)
    description = str(frontmatter.get("description") or "")
    title = extract_title(body, name.replace("-", " ").title())
    rel_path = relative_path(repo_root, path)
    if kind == "rule":
        normalized = normalize_rule_unit(path.stem, title, body)
        unit_name = path.stem
    elif kind == "skill":
        normalized = normalize_skill_unit(name, title, body)
        unit_name = name
    else:
        normalized = normalize_agent_unit(name, title, body)
        unit_name = name

    return {
        "id": f"{kind}:{unit_name}",
        "kind": kind,
        "source_path": rel_path,
        "name": unit_name,
        "description": description,
        "title": title,
        "frontmatter": frontmatter,
        "body": body.strip(),
        "content_hash": content_hash(text),
        "normalized": normalized,
    }


def discover_repo(repo_root: Path, skill_target_root: str) -> dict[str, Any]:
    units: list[dict[str, Any]] = []
    for path in sorted((repo_root / ".cursor" / "rules").glob("*.mdc")):
        units.append(build_source_unit(repo_root, path, "rule"))
    for path in sorted((repo_root / ".cursor" / "skills").glob("*/SKILL.md")):
        units.append(build_source_unit(repo_root, path, "skill"))
    for path in sorted((repo_root / ".cursor" / "agents").glob("*.md")):
        units.append(build_source_unit(repo_root, path, "agent"))
    return {
        "version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "repo_root": str(repo_root.resolve()),
        "skill_target_root": skill_target_root,
        "units": units,
    }


def dump_json(payload: dict[str, Any], output: str | None) -> None:
    text = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if output:
        Path(output).write_text(text, encoding="utf-8")
        return
    sys.stdout.write(text)


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    inventory = discover_repo(repo_root, args.skill_target_root)
    dump_json(inventory, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
