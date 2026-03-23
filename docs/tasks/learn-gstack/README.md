---
task_id: learn-gstack
title: Learn gstack (garrytan/gstack reference)
status: in_progress
priority: high
kind: research
branch: null
issue: null
last_updated: 2026-03-21
next_step: "Use vendored platforms/gstack + bash scripts/bootstrap-gstack.sh after clone; compare gstack workflows with .cursor/skills/ when promoting patterns; sync references/external/gstack then rsync to platforms/gstack when bumping upstream."
promotion_targets:
  - platforms/
  - docs/decisions.md
  - references/README.md
---

# Learn gstack (garrytan/gstack)

## Status

- State: proposed (owner learning track)
- Branch: none unless you promote patterns into maintained platform assets
- Last updated: 2026-03-21

## Original Goal

Study the **`gstack`** comparative reference checkout at `references/external/gstack`: how it packages Claude Code–oriented skills, role-based slash-command workflows (planning, review, QA, release handoff), and guardrails—then decide what is reusable for this repository versus upstream-only behavior.

## Current Slice

- Ensure the tree exists: `references/external/gstack` (manifest: `references/repos.manifest.tsv`; sync: `references/README.md` § `gstack`).
- Skim upstream `README.md` and map where commands, skills, and setup instructions live.
- Capture one concrete takeaway (layout, orchestration, or a single command pattern) under **Confirmed Findings**.

## Current Status

- Task registered; no study notes logged here yet.

## Confirmed Findings

- This repository already documents why `gstack` is tracked and how to sync it in `references/README.md`.
- **Installed for Cursor-style discovery:** vendored copy at `platforms/gstack/`, workspace symlinks under `.agents/skills/gstack*` → `platforms/gstack` (and generated `gstack-*` skill dirs). One-time local build: `bash scripts/bootstrap-gstack.sh` (Bun; `browse/dist/` and `node_modules/` stay gitignored). Documented in root `AGENTS.md`.

## Open Questions

- Which patterns belong in `platforms/claude/` (or another platform home) versus staying as reference-only notes?

## Dead Ends

<!-- Record approaches that were tried and ruled out, so the next session does not repeat them. -->

| Approach | Attempt | Outcome |
|----------|---------|---------|
|          |         |         |

## Promotion Targets

- Durable integration or contrast notes → `docs/decisions.md` or the relevant `platforms/<tool>/` tree.
- Optional cross-links → `references/README.md` only when they reduce future sync or study friction.

## Next Session Entrypoint

1. Run or verify: `bash scripts/sync-references.sh --only gstack` (when network and policy allow).
2. Open `references/external/gstack/README.md` and list top-level directories that define skills, commands, or install steps.
3. Pick one workflow (for example review or QA) and note how it differs from this repo’s maintenance skills under `.cursor/skills/`.
4. Add bullets under **Confirmed Findings** for anything you would actually reuse.
