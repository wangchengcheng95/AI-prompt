---
task_id: cursor-repo-maintenance-followups
title: Cursor repo-local maintenance follow-ups
status: proposed
priority: medium
kind: documentation
branch: null
issue: null
last_updated: 2026-03-19
next_step: Review the recorded migration findings, then decide whether the next slice should add a Cursor quickstart, real Cursor-side trigger validation, or a dedicated repo-local agent shell.
promotion_targets:
  - .cursor/
  - docs/decisions.md
  - docs/REPOSITORY-GOALS.md
---

# Cursor Repo-Local Maintenance Follow-Ups

## Goal

Capture the confirmed findings and unresolved follow-ups from the root `.cursor/` migration so they can be discussed and executed later without rediscovering the same context.

## Current Status

The initial migration is complete enough for Cursor to maintain this repository through repo-local rules and skills. Follow-up work remains unscoped and should be discussed before implementation.

## Confirmed Findings

- The real migration target was the root repo-maintenance entrypoint under `.cursor/`, not the archived external Cursor assets under `platforms/cursor/.cursor/`.
- The stable, high-value layer was repo-local rules plus workflow skills; there were no root repo-local Codex sub-agents to migrate one-for-one.
- Partial migration is risky: if a migrated skill still points back to `.codex/`, Cursor remains operationally blocked.
- Some repository docs still carried Codex-first wording and had to be generalized so Cursor was not treated as a second-class maintainer.
- Structural parity is less important than semantic parity: the reusable asset is the maintenance loop and workflow behavior, not a forced mirror of every platform-specific shell.

## Open Questions

- Whether root `.cursor/` now needs a short maintainer quickstart so future sessions can enter the Cursor workflow with lower token cost.
- Whether the migrated Cursor skills should be validated end-to-end inside a real Cursor session instead of relying only on repository-side structure checks.
- Whether a dedicated repo-local Cursor agent shell is worth adding later, or whether rules plus skills are the right stopping point.

## Next Session Entrypoint

Open this file together with `docs/decisions.md` and root `.cursor/` if the next discussion is about improving the Cursor maintenance experience instead of expanding external platform assets.

## Promotion Targets

- `.cursor/`
- `docs/decisions.md`
- `docs/REPOSITORY-GOALS.md`
