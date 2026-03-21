# Prompt-sync manifest-driven operator advisory — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Replace hardcoded Cursor/Superpowers stderr copy with `sync-manifest.yaml`-driven `default_operator_advisories` and optional per-bundle `operator_advisories`, preserving `PROMPT_SYNC_SKIP_PLUGIN_ADVISORY`.

**Architecture:** `PromptSyncService` collects strings from the manifest; a small formatter builds the bordered stderr block; `main()` passes `result.bundle_name` into the emitter.

**Tech stack:** Python 3, PyYAML (existing), `unittest` (existing).

---

### Task 1: Manifest + formatter API

**Files:**

- Modify: `scripts/prompt_sync.py`
- Modify: `sync-manifest.yaml`
- Test: `tests/test_prompt_sync.py`

**Steps:**

1. Remove `OPTIONAL_PLUGIN_ADVISORY` and `emit_optional_plugin_advisory()`.
2. Add `format_operator_advisory_box(lines: list[str]) -> str` (empty list → empty string; use an 80-column `=` border consistent with prior UX).
3. Add `PromptSyncService.operator_advisory_lines(self, bundle_name: str | None) -> list[str]` reading `default_operator_advisories` and optional bundle `operator_advisories`.
4. Add `emit_operator_advisory(service: PromptSyncService, bundle_name: str | None) -> None` respecting `PROMPT_SYNC_SKIP_PLUGIN_ADVISORY`.
5. Wire `main()` to call `emit_operator_advisory(service, result.bundle_name)` after `format_result`.
6. Add root `default_operator_advisories` to `sync-manifest.yaml` (neutral Chinese + `references/README.md` + example Cursor/Superpowers line).

**Verify:** `python3 -m unittest tests.test_prompt_sync -v`

---

### Task 2: Tests for advisory behavior

**Files:**

- Modify: `tests/test_prompt_sync.py`

**Steps:**

1. Extend the temporary `sync-manifest.yaml` in `setUp` with `default_operator_advisories` containing a unique sentinel string used in assertions.
2. Replace old `OPTIONAL_PLUGIN_ADVISORY` tests with:
   - `format_operator_advisory_box` / `operator_advisory_lines` expectations.
   - One test that adds per-bundle `operator_advisories` under `codex-home` and asserts order (default then bundle).
   - One test that `emit_operator_advisory` prints nothing when lists are empty (manifest without keys in a tiny alternate repo, or strip-only strings).
3. Keep `PROMPT_SYNC_SKIP_PLUGIN_ADVISORY=1` on `test_cli_exit_codes`; add `test_cli_stderr_includes_advisory_when_not_skipped` with patched `sys.stderr`.

**Verify:** `python3 -m unittest tests.test_prompt_sync -v`

---

### Task 3: Skill + workflow docs

**Files:**

- Modify: `.cursor/skills/prompt-sync/SKILL.md`, `references/workflow.md`
- Modify: `.claude/skills/prompt-sync/SKILL.md`, `references/workflow.md`
- Modify: `.codex/skills/prompt-sync/SKILL.md`, `references/workflow.md`

**Steps:**

1. Replace step 7 / Operational Rules text that refers to hardcoded Superpowers with: advisories come from `sync-manifest.yaml` (`default_operator_advisories`, optional per-bundle `operator_advisories`); `PROMPT_SYNC_SKIP_PLUGIN_ADVISORY` still suppresses output.

**Verify:** Manual read for parity across the three tool trees.

---

### Task 4: Commit

**Steps:**

1. `git add` design + plan + code + manifest + tests + skills.
2. Commit on `main` with English subject, e.g. `refactor(prompt-sync): Drive operator advisories from sync manifest`.

**Verify:** `git status` clean; tests pass.
