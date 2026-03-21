---
task_id: cross-doc-consistency-check
title: Repo-local cross-doc consistency checking workflow
status: proposed
priority: high
kind: skill
branch: null
issue: null
last_updated: 2026-03-19
next_step: Define the minimum check surface across REPOSITORY-GOALS, architecture, system-overview, decisions, and agent-iteration-contract before implementing any repo-local checker.
promotion_targets:
  - docs/EVOLUTION-GOALS.md
  - .codex/
---

# Repo-local Cross-Doc Consistency Checking Workflow

## Goal

Design a repo-local workflow or skill that checks whether the standard repository-maintenance documents still agree on the active repository contract, boundaries, and execution model.

## Current Status

This work is proposed but not started. It was named in [docs/EVOLUTION-GOALS.md](../../EVOLUTION-GOALS.md) as one of the initial repo-local skill priorities.

## Confirmed Findings

- The repository already relies on several standard docs with distinct responsibilities.
- Cross-doc drift is a real maintenance risk because the same repository concepts appear in multiple files.
- This should remain a repo-local maintenance asset, not a platform asset under `platforms/`.

## Open Questions

- Which files form the minimum consistency set for the first version.
- Whether the first version should be a documented checklist, a skill, or a lightweight script-backed workflow.
- Which differences should be treated as true drift versus intentional document specialization.

## Next Session Entrypoint

Start by comparing `docs/REPOSITORY-GOALS.md`, `docs/architecture.md`, `docs/system-overview.md`, `docs/decisions.md`, and `docs/agent-iteration-contract.md` and write down the exact assertions that should stay aligned.

## Promotion Targets

- `.codex/`
- `docs/EVOLUTION-GOALS.md`
