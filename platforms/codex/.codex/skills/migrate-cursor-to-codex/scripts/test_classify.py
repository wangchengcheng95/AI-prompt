from __future__ import annotations

import unittest

import classify


class ClassifyTests(unittest.TestCase):
    def test_rule_skill_agent_classification(self) -> None:
        cases = [
            {
                "unit": {
                    "id": "rule:plan-mode-todos",
                    "kind": "rule",
                    "name": "plan-mode-todos",
                    "source_path": ".cursor/rules/plan-mode-todos.mdc",
                    "normalized": {"changed": True, "section_key": "plan-mode-todos"},
                },
                "skill_target_root": ".codex/skills",
                "expected": "transform",
            },
            {
                "unit": {
                    "id": "skill:sample",
                    "kind": "skill",
                    "name": "sample",
                    "source_path": ".cursor/skills/sample/SKILL.md",
                    "normalized": {"requires_split": False},
                },
                "skill_target_root": ".codex/skills",
                "expected": "direct",
            },
            {
                "unit": {
                    "id": "agent:verifier",
                    "kind": "agent",
                    "name": "verifier",
                    "source_path": ".cursor/agents/verifier.md",
                    "description": "Strict verifier. Use when a task is done.",
                    "body": "You are a verifier.\n\n## Workflow\n",
                    "normalized": {"role_id": "verifier"},
                },
                "skill_target_root": ".codex/skills",
                "expected": "direct",
            },
        ]

        for case in cases:
            with self.subTest(case=case["unit"]["id"]):
                unit = case["unit"]
                if unit["kind"] == "rule":
                    migration = classify.classify_rule(unit)
                elif unit["kind"] == "skill":
                    migration = classify.classify_skill(unit, case["skill_target_root"])
                else:
                    migration = classify.classify_agent(unit)
                self.assertEqual(migration["classification"], case["expected"])

    def test_non_delegated_agent_transforms(self) -> None:
        unit = {
            "id": "agent:notes",
            "kind": "agent",
            "name": "notes",
            "source_path": ".cursor/agents/notes.md",
            "description": "Helper notes",
            "body": "This file explains a process.\n",
            "normalized": {"role_id": "notes"},
        }
        migration = classify.classify_agent(unit)
        self.assertEqual(migration["classification"], "transform")


if __name__ == "__main__":
    unittest.main()
