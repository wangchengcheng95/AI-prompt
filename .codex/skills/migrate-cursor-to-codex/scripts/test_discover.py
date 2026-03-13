from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import discover


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


class DiscoverTests(unittest.TestCase):
    def test_parse_frontmatter_and_discover_units(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(
                root / ".cursor/rules/plan-mode-todos.mdc",
                "---\ndescription: Todos\nalwaysApply: false\n---\n# Plan Mode: Todos & Closing Steps\n\nApplies only when editing `.cursor/plans/*.plan.md`.\n",
            )
            write(
                root / ".cursor/skills/sample/SKILL.md",
                "---\nname: sample\ndescription: Sample skill\n---\n# Sample\n\nBody\n",
            )
            write(
                root / ".cursor/agents/debugger.md",
                "---\nname: debugger\ndescription: Go debugger\nmodel: inherit\n---\nYou are a debugger.\n\n## Workflow\n\n1. Inspect\n",
            )

            inventory = discover.discover_repo(root, ".codex/skills")
            self.assertEqual(len(inventory["units"]), 3)

            by_kind = {unit["kind"]: unit for unit in inventory["units"]}
            rule = by_kind["rule"]
            self.assertEqual(rule["normalized"]["title"], "Planning")
            self.assertNotIn(".cursor/plans", rule["normalized"]["body"])
            self.assertNotIn("Plan Mode", rule["normalized"]["body"])

            agent = by_kind["agent"]
            self.assertEqual(agent["normalized"]["role_id"], "debugger")

    def test_rule_normalization_table(self) -> None:
        cases = [
            {
                "name": "00-overview",
                "title": "Overview",
                "body": "# Overview\n\nMake Cursor behave like a reliable **vibe engineering** agent.\n",
                "contains": "Make the assistant behave like a reliable engineering agent",
            },
            {
                "name": "plan-mode-todos",
                "title": "Plan Mode: Todos & Closing Steps",
                "body": "# Plan Mode: Todos & Closing Steps\n\nApplies only when editing `.cursor/plans/*.plan.md`.\n",
                "contains": "implementation plans",
            },
            {
                "name": "go-backend",
                "title": "Go Backend Engineering",
                "body": "# Go Backend Engineering\n\n- Follow `architecture.mdc` for layer boundaries and dependency direction.\n- Follow `engineering-doctrine.mdc` for error wrapping, typed errors, and “never ignore errors”.\n",
                "contains": "Follow the project architecture rules for layer boundaries and dependency direction.",
            },
            {
                "name": "memory-management",
                "title": "Memory Management",
                "body": "# Memory Management\n\nUse the **memory-bank-update** skill workflow (or `.cursor/commands/update-memory` if present).\nMemory Bank (`.cursor/memory/` or `docs/memory_bank/`) should be in git unless it contains secrets.\n",
                "contains": "Use the repository memory update workflow when available.",
            },
        ]
        for case in cases:
            with self.subTest(case=case["name"]):
                normalized = discover.normalize_rule_unit(case["name"], case["title"], case["body"])
                self.assertIn(case["contains"], normalized["body"])
                self.assertNotIn(".cursor/", normalized["body"])
                self.assertNotIn(".mdc", normalized["body"])


if __name__ == "__main__":
    unittest.main()
