from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import classify
import discover
import plan as migration_plan
import render
import verify


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


class PipelineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        write(
            self.root / ".cursor/rules/ai-boundary.mdc",
            "---\ndescription: boundary\nalwaysApply: true\n---\n# AI Scope and Boundaries\n\n## Default rule: change radius\n\n- Only modify files explicitly mentioned by the user.\n",
        )
        write(
            self.root / ".cursor/skills/sample/SKILL.md",
            "---\nname: sample\ndescription: Sample skill\n---\n# Sample\n\nBody\n",
        )
        write(
            self.root / ".cursor/agents/debugger.md",
            "---\nname: debugger\ndescription: Go debugger. Use when a panic happens.\nmodel: inherit\n---\nYou are a debugger.\n\n## Workflow\n\n1. Inspect\n",
        )
        write(self.root / ".codex/migration/cursor-manifest.json", json.dumps({"version": 1, "skill_target_root": ".codex/skills", "entries": []}))

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def classify_repo(self) -> dict:
        inventory = discover.discover_repo(self.root, ".codex/skills")
        return classify.classify_inventory(inventory)

    def test_conflict_detection_for_unmanaged_targets(self) -> None:
        write(self.root / "AGENTS.md", "# Existing\n")
        write(self.root / ".codex/skills/sample/SKILL.md", "---\nname: sample\ndescription: Existing\n---\n# Existing\n")

        classified = self.classify_repo()
        manifest = json.loads((self.root / ".codex/migration/cursor-manifest.json").read_text(encoding="utf-8"))
        plan = migration_plan.build_plan(classified, manifest, self.root)

        statuses = {action["source_id"]: action["status"] for action in plan["actions"]}
        self.assertEqual(statuses["rule:ai-boundary"], "conflict")
        self.assertEqual(statuses["skill:sample"], "conflict")
        self.assertEqual(statuses["agent:debugger"], "planned")

    def test_apply_updates_targets_and_idempotence(self) -> None:
        classified = self.classify_repo()
        manifest = json.loads((self.root / ".codex/migration/cursor-manifest.json").read_text(encoding="utf-8"))
        plan = migration_plan.build_plan(classified, manifest, self.root)

        report_file = self.root / ".codex/migration/reports/dry-run.md"
        render.apply_actions(self.root, plan, classified, self.root / ".codex/migration/cursor-manifest.json")

        config_text = (self.root / ".codex/config.toml").read_text(encoding="utf-8")
        self.assertIn("[agents.debugger]", config_text)
        skill_text = (self.root / ".codex/skills/sample/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("codex-migrate:owned", skill_text)

        manifest = json.loads((self.root / ".codex/migration/cursor-manifest.json").read_text(encoding="utf-8"))
        second_plan = migration_plan.build_plan(classified, manifest, self.root)
        self.assertTrue(all(action["status"] == "noop" for action in second_plan["actions"]))

        report = render.build_report(second_plan, classified, render.collect_previews(second_plan, classified))
        report_file.parent.mkdir(parents=True, exist_ok=True)
        report_file.write_text(report, encoding="utf-8")
        result_checks = verify.verify_report(report_file)
        self.assertTrue(all(item["passed"] for item in result_checks))

    def test_orphan_detection(self) -> None:
        manifest = {
            "version": 1,
            "skill_target_root": ".codex/skills",
            "entries": [
                {
                    "source_path": ".cursor/skills/deleted/SKILL.md",
                    "kind": "skill",
                    "content_hash": "sha256:deadbeef",
                    "classification": "direct",
                    "target_paths": [".codex/skills/deleted/SKILL.md"],
                    "last_migrated_at": "2026-03-13T00:00:00Z",
                    "last_verified_at": "2026-03-13T00:00:00Z",
                }
            ],
        }
        classified = self.classify_repo()
        plan = migration_plan.build_plan(classified, manifest, self.root)
        self.assertEqual(len(plan["orphans"]), 1)
        self.assertEqual(plan["orphans"][0]["status"], "orphaned")

    def test_apply_agent_subset_with_other_conflicts(self) -> None:
        write(self.root / "AGENTS.md", "# Existing\n")
        write(self.root / ".codex/skills/sample/SKILL.md", "---\nname: sample\ndescription: Existing\n---\n# Existing\n")

        classified = self.classify_repo()
        manifest = json.loads((self.root / ".codex/migration/cursor-manifest.json").read_text(encoding="utf-8"))
        plan = migration_plan.build_plan(classified, manifest, self.root)

        render.apply_actions(
            self.root,
            plan,
            classified,
            self.root / ".codex/migration/cursor-manifest.json",
            only_kinds={"agent"},
        )

        self.assertTrue((self.root / ".codex/config.toml").exists())
        self.assertTrue((self.root / ".codex/agents/debugger.toml").exists())
        self.assertEqual((self.root / "AGENTS.md").read_text(encoding="utf-8"), "# Existing\n")
        self.assertIn("# Existing", (self.root / ".codex/skills/sample/SKILL.md").read_text(encoding="utf-8"))

        manifest_after = json.loads((self.root / ".codex/migration/cursor-manifest.json").read_text(encoding="utf-8"))
        self.assertEqual([entry["kind"] for entry in manifest_after["entries"]], ["agent"])


if __name__ == "__main__":
    unittest.main()
