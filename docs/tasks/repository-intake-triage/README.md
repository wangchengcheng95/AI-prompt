---
task_id: repository-intake-triage
title: Repository intake triage workflow
status: deferred
priority: medium
kind: skill
branch: null
issue: null
last_updated: 2026-03-19
next_step: Return after repeated maintenance tasks show that new-material placement decisions still need a dedicated intake workflow.
promotion_targets:
  - docs/EVOLUTION-GOALS.md
  - .codex/
---

# Repository Intake Triage Workflow

## Goal

Design a repo-local workflow or skill that decides whether new maintenance material should extend an existing asset or create a new home.

## Current Status

This work is explicitly deferred in [docs/EVOLUTION-GOALS.md](../../EVOLUTION-GOALS.md).

## Confirmed Findings

- The repository already prefers extending existing homes over creating duplicates.
- A dedicated intake workflow is only worth the maintenance cost if this decision keeps recurring.

## Open Questions

- Which intake questions are stable enough to encode.
- Whether the workflow should remain guidance inside the iteration contract or become a separate repo-local skill.

## Next Session Entrypoint

Return after several maintenance tasks show repeated ambiguity around whether new content belongs in an existing home or needs a new tracked asset.

## Promotion Targets

- `.codex/`
- `docs/EVOLUTION-GOALS.md`
