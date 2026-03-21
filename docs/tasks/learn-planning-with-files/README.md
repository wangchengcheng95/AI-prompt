---
task_id: learn-planning-with-files
title: Learn planning-with-files (filesystem-backed planning)
status: proposed
priority: high
kind: research
branch: null
issue: null
last_updated: 2026-03-21
next_step: "Clone or sync `references/external/planning-with-files` via `references/README.md`, read the three-file planning pattern, and note one concrete workflow you will try on a real task."
promotion_targets:
  - references/README.md
  - docs/decisions.md
---

# Learn planning-with-files

## Status

- State: proposed (owner learning track)
- Branch: none; open a task branch only if you promote findings into maintained assets
- Last updated: 2026-03-21

## Original Goal

Build a working understanding of **planning-with-files**: markdown-backed plans, hooks, and multi-IDE skill packaging, so you can apply filesystem-backed planning on real work without treating the upstream checkout as a maintained repo asset.

## Current Slice

- Confirm local reference availability: `references/external/planning-with-files` (see `references/README.md` and `references/repos.manifest.tsv`).
- Study upstream: <https://github.com/OthmanAdi/planning-with-files>
- Extract: file roles, when to rewrite vs append, and how hooks enforce re-read / completion.

## Current Status

- Task registered; no study notes committed yet.

## Confirmed Findings

- This repository already documents intent and sync paths under `references/README.md` (`planning-with-files` section).

## Open Questions

- Which editor or agent runtime will you standardize on for the first applied experiment?
- Do any conclusions belong in `platforms/` versus staying personal workflow only?

## Promotion Targets

- Durable, repo-wide conclusions → `docs/decisions.md` or relevant `platforms/<tool>/` notes.
- Reference hygiene only → `references/README.md` updates.

## Next Session Entrypoint

1. Open `references/README.md` (section `planning-with-files`).
2. Run or verify sync: `bash scripts/sync-references.sh --only planning-with-files` (when network and policy allow).
3. Read the upstream README and skill definitions in the external checkout; capture findings under **Confirmed Findings** above.
