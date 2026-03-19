---
task_id: pr-workflow-token-efficiency
title: Reduce token overhead in repo-local PR interaction workflow
status: proposed
priority: high
kind: skill
branch: null
issue: null
pr: null
last_updated: 2026-03-19
next_step: Measure where token cost currently comes from across pr-handoff and pr-operator, then define a low-token default path that preserves deterministic PR operations.
promotion_targets:
  - .codex/skills/pr-handoff/
  - .codex/skills/pr-operator/
  - docs/decisions.md
---

# Reduce Token Overhead In Repo-Local PR Interaction Workflow

## Goal

Design a lower-token repo-local PR workflow that keeps the deterministic push and GitHub mutation path intact while reducing how much context the agent has to load or regenerate during PR handoff.

## Current Status

This work is proposed but not started. It was identified after reviewing the current PR interaction skills and noticing that the main token cost comes from handoff summarization rather than the wrapped PR operations themselves.

## Confirmed Findings

- `pr-operator` is a narrow execution-layer skill with bounded operations such as `push`, `create`, `view`, and `edit`.
- `pr-handoff` costs more tokens because it requires a human-readable PR summary, verification recap, and risk notes based on the actual change.
- The main optimization target is not raw GitHub mutation, but the amount of diff, verification, and narrative context that must be reloaded to prepare review-ready PR text.
- Any optimization should remain repo-local and should not weaken the review handoff contract for this repository.

## Open Questions

- Which PR handoff fields are mandatory for every repository task versus optional when the diff is small or purely documentation-focused.
- Whether a low-token mode should live as a documented convention, a skill update, or a separate helper workflow.
- How much structured templating can be added before the handoff becomes too lossy for reviewers.

## Next Session Entrypoint

Start by measuring the current information surface for `pr-handoff` and `pr-operator`, then propose a default path that keeps `pr-operator` as the execution layer and narrows `pr-handoff` to the minimum review-safe summary shape.

## Promotion Targets

- `.codex/skills/pr-handoff/`
- `.codex/skills/pr-operator/`
- `docs/decisions.md`
