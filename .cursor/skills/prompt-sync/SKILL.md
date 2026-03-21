---
name: prompt-sync
description: Preview and run manifest-driven prompt asset sync and backflow for this repository. Use when Cursor needs to copy archived platform assets from this repo into a local sibling workspace or repository, check drift for a managed target, or backflow a user-specified managed file or directory from a local target back into this upstream repository.
---

# Prompt Sync

## Overview

Use this skill to operate the repo-local prompt sync system for this repository.

The skill keeps operator guidance under the Cursor skill directory, while the sync system itself remains repo-local infrastructure.

The system treats this repository as the only upstream and uses explicit bundle mappings from `sync-manifest.yaml` together with local target definitions from `sync-targets.local.yaml`.

## Workflow

1. Read `sync-manifest.yaml` to identify the bundle, managed target paths, and backflow destination rules.
2. Copy `assets/sync-targets.local.yaml.example` to `sync-targets.local.yaml`, then read `sync-targets.local.yaml` to resolve the local target name to an absolute path and tool or type metadata.
3. Use `python3 scripts/prompt_sync.py preview-export ...` or `preview-import ...` before any write.
4. Refuse unmanaged paths and stop on `drift-local`, `conflict`, or `missing-target`.
5. Use `export` or `import-backflow` only when the preview output contains only safe changes.
6. Summarize the exact classifications, applied paths, and any remaining blockers.
7. After a successful CLI run, `scripts/prompt_sync.py` may print a stderr advisory box built from `sync-manifest.yaml`: root `default_operator_advisories` plus optional per-bundle `operator_advisories` (this tool never installs plugins or external tools). Set `PROMPT_SYNC_SKIP_PLUGIN_ADVISORY=1` to suppress it (for tests or automation).

## Boundaries

- Treat this as repo-local maintenance infrastructure.
- Treat `platforms/` content as archived external assets that may be exported downstream.
- Treat root `.cursor/` and root `.codex/` repo-maintenance assets as local by default; do not export them unless the manifest explicitly says so.
- Do not guess destination paths or infer unmanaged mappings.
- Do not bypass preview to force a write in v1.

## Commands

- Preview export:
  `python3 scripts/prompt_sync.py preview-export --bundle <bundle> --target <target>`
- Apply export:
  `python3 scripts/prompt_sync.py export --bundle <bundle> --target <target>`
- Check drift:
  `python3 scripts/prompt_sync.py check-drift --bundle <bundle> --target <target>`
- Preview backflow:
  `python3 scripts/prompt_sync.py preview-import --from-target <target> --path <target-path> [--dest <repo-path>]`
- Apply backflow:
  `python3 scripts/prompt_sync.py import-backflow --from-target <target> --path <target-path> [--dest <repo-path>]`

## Classification Rules

- `create`: file does not exist on the write side yet
- `update-safe`: managed file changed only on the read side since last sync
- `drift-local`: managed file changed only on the target since last sync
- `conflict`: managed file changed on both sides or lacks safe provenance
- `unmanaged`: requested path is outside manifest-managed targets
- `missing-target`: requested target or file does not exist

Load [references/workflow.md](references/workflow.md) when you need the canonical bundle list, target-state location, example target config path, or operator guidance for the supported user scenarios.
