import io
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import yaml

from scripts.prompt_sync import (
    EXIT_BLOCKED,
    EXIT_OK,
    PromptSyncService,
    emit_operator_advisory,
    format_operator_advisory_box,
    main,
)


class PromptSyncTest(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.repo_root = Path(self.tempdir.name) / "repo"
        self.repo_root.mkdir()
        (self.repo_root / "platforms/codex/home").mkdir(parents=True)
        (self.repo_root / "platforms/codex/.codex/skills/sample").mkdir(parents=True)
        (self.repo_root / "platforms/codex/home/AGENTS.md").write_text("home v1\n", encoding="utf-8")
        (self.repo_root / "platforms/codex/AGENTS.md").write_text("repo v1\n", encoding="utf-8")
        (self.repo_root / "platforms/codex/.codex/config.toml").write_text("config=v1\n", encoding="utf-8")
        (self.repo_root / "platforms/codex/.codex/skills/sample/SKILL.md").write_text("skill v1\n", encoding="utf-8")
        (self.repo_root / "sync-manifest.yaml").write_text(
            """
default_operator_advisories:
  - sync-test-default-advisory

bundles:
  codex-home:
    kind: user-home
    conflict_policy: preview_stop
    sources:
      - path: platforms/codex/home/AGENTS.md
        destination: AGENTS.md
    default_targets:
      - tool: codex
        type: workspace
    managed_paths:
      - AGENTS.md
    operator_advisories:
      - sync-test-bundle-advisory
    backflow:
      enabled: true
      default_destination: platforms/codex/home/AGENTS.md
  codex-platform-core:
    kind: repo-platform
    conflict_policy: preview_stop
    sources:
      - path: platforms/codex/AGENTS.md
        destination: AGENTS.md
      - path: platforms/codex/.codex
        destination: .codex
    default_targets:
      - tool: codex
        type: repo
    managed_paths:
      - AGENTS.md
      - .codex
    backflow:
      enabled: true
      default_destination_root: platforms/codex
""".strip()
            + "\n",
            encoding="utf-8",
        )
        self.workspace_target = Path(self.tempdir.name) / "workspace-target"
        self.workspace_target.mkdir()
        self.repo_target = Path(self.tempdir.name) / "repo-target"
        self.repo_target.mkdir()
        (self.repo_root / "sync-targets.local.yaml").write_text(
            f"""
targets:
  local-codex-home:
    path: {self.workspace_target}
    type: workspace
    tool: codex
  sample-repo:
    path: {self.repo_target}
    type: repo
    tool: codex
""".strip()
            + "\n",
            encoding="utf-8",
        )
        self.service = PromptSyncService(self.repo_root)

    def tearDown(self):
        self.tempdir.cleanup()

    def state_entries(self, target_root: Path):
        state_path = target_root / ".ai-prompt-sync/state.yaml"
        data = yaml.safe_load(state_path.read_text(encoding="utf-8"))
        return data["entries"]

    def test_export_codex_home_into_empty_workspace(self):
        result = self.service.export("codex-home", "local-codex-home")
        self.assertEqual(result.changed, 1)
        self.assertEqual((self.workspace_target / "AGENTS.md").read_text(encoding="utf-8"), "home v1\n")
        self.assertIn("AGENTS.md", self.state_entries(self.workspace_target))

    def test_export_codex_platform_core_into_empty_repo(self):
        result = self.service.export("codex-platform-core", "sample-repo")
        self.assertEqual(result.changed, 3)
        self.assertEqual((self.repo_target / "AGENTS.md").read_text(encoding="utf-8"), "repo v1\n")
        self.assertEqual((self.repo_target / ".codex/config.toml").read_text(encoding="utf-8"), "config=v1\n")
        self.assertEqual(
            (self.repo_target / ".codex/skills/sample/SKILL.md").read_text(encoding="utf-8"),
            "skill v1\n",
        )

    def test_preview_export_produces_no_writes(self):
        result = self.service.preview_export("codex-home", "local-codex-home")
        self.assertEqual([item.classification for item in result.items], ["create"])
        self.assertFalse((self.workspace_target / "AGENTS.md").exists())

    def test_export_is_noop_on_second_run(self):
        self.service.export("codex-home", "local-codex-home")
        second = self.service.export("codex-home", "local-codex-home")
        self.assertTrue(second.is_noop())
        self.assertEqual(second.changed, 0)

    def test_target_local_edit_becomes_drift_local(self):
        self.service.export("codex-home", "local-codex-home")
        (self.workspace_target / "AGENTS.md").write_text("local change\n", encoding="utf-8")
        preview = self.service.preview_export("codex-home", "local-codex-home")
        self.assertEqual([item.classification for item in preview.items], ["drift-local"])

    def test_upstream_edit_with_unchanged_target_becomes_update_safe(self):
        self.service.export("codex-home", "local-codex-home")
        (self.repo_root / "platforms/codex/home/AGENTS.md").write_text("home v2\n", encoding="utf-8")
        preview = self.service.preview_export("codex-home", "local-codex-home")
        self.assertEqual([item.classification for item in preview.items], ["update-safe"])

    def test_simultaneous_upstream_and_target_edits_become_conflict(self):
        self.service.export("codex-home", "local-codex-home")
        (self.repo_root / "platforms/codex/home/AGENTS.md").write_text("home v2\n", encoding="utf-8")
        (self.workspace_target / "AGENTS.md").write_text("local change\n", encoding="utf-8")
        preview = self.service.preview_export("codex-home", "local-codex-home")
        self.assertEqual([item.classification for item in preview.items], ["conflict"])

    def test_import_backflow_updates_default_upstream_destination(self):
        self.service.export("codex-platform-core", "sample-repo")
        (self.repo_target / ".codex/skills/sample/SKILL.md").write_text("skill v2\n", encoding="utf-8")
        preview = self.service.preview_import("sample-repo", ".codex/skills/sample/SKILL.md", None)
        self.assertEqual([item.classification for item in preview.items], ["update-safe"])
        applied = self.service.import_backflow("sample-repo", ".codex/skills/sample/SKILL.md", None)
        self.assertEqual(applied.changed, 1)
        self.assertEqual(
            (self.repo_root / "platforms/codex/.codex/skills/sample/SKILL.md").read_text(encoding="utf-8"),
            "skill v2\n",
        )

    def test_import_backflow_honors_destination_override(self):
        self.service.export("codex-platform-core", "sample-repo")
        (self.repo_target / ".codex/skills/sample/SKILL.md").write_text("skill override\n", encoding="utf-8")
        applied = self.service.import_backflow(
            "sample-repo",
            ".codex/skills/sample/SKILL.md",
            "platforms/codex/.codex/skills/copied/SKILL.md",
        )
        self.assertEqual(applied.changed, 1)
        self.assertEqual(
            (self.repo_root / "platforms/codex/.codex/skills/copied/SKILL.md").read_text(encoding="utf-8"),
            "skill override\n",
        )

    def test_unmanaged_path_is_rejected(self):
        (self.repo_target / "README.md").write_text("hello\n", encoding="utf-8")
        preview = self.service.preview_import("sample-repo", "README.md", None)
        self.assertEqual([item.classification for item in preview.items], ["unmanaged"])

    def test_missing_target_registry_or_path_fails_clearly(self):
        with self.assertRaisesRegex(Exception, "Unknown target"):
            self.service.preview_export("codex-home", "missing-target")

    def test_recursive_dot_codex_mapping_works(self):
        preview = self.service.preview_export("codex-platform-core", "sample-repo")
        self.assertEqual(sorted(item.target_rel for item in preview.items), [
            ".codex/config.toml",
            ".codex/skills/sample/SKILL.md",
            "AGENTS.md",
        ])

    def test_format_operator_advisory_box_empty(self):
        self.assertEqual(format_operator_advisory_box([]), "")

    def test_operator_advisory_lines_merge_default_and_bundle(self):
        home_lines = self.service.operator_advisory_lines("codex-home")
        self.assertEqual(
            home_lines,
            ["sync-test-default-advisory", "sync-test-bundle-advisory"],
        )
        core_lines = self.service.operator_advisory_lines("codex-platform-core")
        self.assertEqual(core_lines, ["sync-test-default-advisory"])

    def test_emit_operator_advisory_prints_to_stderr(self):
        stderr = io.StringIO()
        popped = os.environ.pop("PROMPT_SYNC_SKIP_PLUGIN_ADVISORY", None)
        try:
            with patch.object(sys, "stderr", stderr):
                emit_operator_advisory(self.service, "codex-home")
        finally:
            if popped is not None:
                os.environ["PROMPT_SYNC_SKIP_PLUGIN_ADVISORY"] = popped
        out = stderr.getvalue()
        self.assertIn("sync-test-default-advisory", out)
        self.assertIn("sync-test-bundle-advisory", out)
        self.assertLess(out.index("sync-test-default-advisory"), out.index("sync-test-bundle-advisory"))

    def test_emit_operator_advisory_respects_skip_env(self):
        stderr = io.StringIO()
        with patch.dict(os.environ, {"PROMPT_SYNC_SKIP_PLUGIN_ADVISORY": "1"}):
            with patch.object(sys, "stderr", stderr):
                emit_operator_advisory(self.service, "codex-home")
        self.assertEqual(stderr.getvalue(), "")

    def test_emit_silent_when_manifest_has_no_advisories(self):
        path = self.repo_root / "sync-manifest.yaml"
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        data.pop("default_operator_advisories", None)
        for bundle in (data.get("bundles") or {}).values():
            if isinstance(bundle, dict):
                bundle.pop("operator_advisories", None)
        path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")
        bare = PromptSyncService(self.repo_root)
        stderr = io.StringIO()
        with patch.object(sys, "stderr", stderr):
            emit_operator_advisory(bare, "codex-home")
        self.assertEqual(stderr.getvalue(), "")

    def test_cli_exit_codes(self):
        original_repo_root = os.environ.get("PROMPT_SYNC_REPO_ROOT")
        original_skip = os.environ.get("PROMPT_SYNC_SKIP_PLUGIN_ADVISORY")
        try:
            os.environ["PROMPT_SYNC_REPO_ROOT"] = str(self.repo_root)
            os.environ["PROMPT_SYNC_SKIP_PLUGIN_ADVISORY"] = "1"
            exit_code = main(["preview-export", "--bundle", "codex-home", "--target", "local-codex-home"])
            self.assertEqual(exit_code, EXIT_OK)
            self.service.export("codex-home", "local-codex-home")
            (self.workspace_target / "AGENTS.md").write_text("local drift\n", encoding="utf-8")
            blocked_code = main(["preview-export", "--bundle", "codex-home", "--target", "local-codex-home"])
            self.assertEqual(blocked_code, EXIT_BLOCKED)
        finally:
            if original_repo_root is None:
                os.environ.pop("PROMPT_SYNC_REPO_ROOT", None)
            else:
                os.environ["PROMPT_SYNC_REPO_ROOT"] = original_repo_root
            if original_skip is None:
                os.environ.pop("PROMPT_SYNC_SKIP_PLUGIN_ADVISORY", None)
            else:
                os.environ["PROMPT_SYNC_SKIP_PLUGIN_ADVISORY"] = original_skip

    def test_cli_stderr_includes_advisory_when_not_skipped(self):
        original_repo_root = os.environ.get("PROMPT_SYNC_REPO_ROOT")
        popped = os.environ.pop("PROMPT_SYNC_SKIP_PLUGIN_ADVISORY", None)
        stderr = io.StringIO()
        try:
            os.environ["PROMPT_SYNC_REPO_ROOT"] = str(self.repo_root)
            with patch.object(sys, "stderr", stderr):
                code = main(["preview-export", "--bundle", "codex-home", "--target", "local-codex-home"])
            self.assertEqual(code, EXIT_OK)
        finally:
            if popped is not None:
                os.environ["PROMPT_SYNC_SKIP_PLUGIN_ADVISORY"] = popped
            if original_repo_root is None:
                os.environ.pop("PROMPT_SYNC_REPO_ROOT", None)
            else:
                os.environ["PROMPT_SYNC_REPO_ROOT"] = original_repo_root
        self.assertIn("sync-test-default-advisory", stderr.getvalue())
        self.assertIn("sync-test-bundle-advisory", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
