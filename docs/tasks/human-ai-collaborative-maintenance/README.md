---
task_id: human-ai-collaborative-maintenance
title: Human-and-AI collaborative repository maintenance
status: archived
priority: medium
kind: documentation
branch: null
issue: null
last_updated: 2026-03-21
next_step: "Reference this task when the owner-AI maintenance contract changes materially or when revisiting why those stable facts were promoted into the standard docs set."
promotion_targets:
  - docs/REPOSITORY-GOALS.md
  - docs/agent-iteration-contract.md
  - docs/system-overview.md
  - docs/decisions.md
---

# Human-and-AI collaborative repository maintenance

## Standing context

This repository is maintained collaboratively by the owner (personal) and AI assistants. The owner sets goals, approves material scope or risk changes, and owns final integration decisions; AI agents propose and apply changes, run standing checklists, and keep task state in `docs/tasks/` honest.

## Authoritative references

- [Repository contract and collaboration framing](../REPOSITORY-GOALS.md) — primary objective and boundaries
- [Goal-to-ready-to-merge loop](../agent-iteration-contract.md) — execution and handoff expectations
- [Stable system facts](../system-overview.md) — includes the owner–AI maintenance constraint
- [Decision log](../decisions.md) — dated rationale for promoting this model into system overview

## Related tasks

- [`ai-friendly-repo`](../ai-friendly-repo/README.md) — AI-friendly structure, indexing, and promotion flow

## Notes

- This entry records the maintenance model as archived standing context; it is not a standalone delivery backlog.
- Use other tasks in [`docs/tasks/index.yaml`](../index.yaml) for concrete, completable work.
