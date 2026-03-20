---
task_id: ai-native-repo-design-principles
title: Archive and evaluate the AI-native repository design-principles draft
status: proposed
priority: high
kind: documentation
branch: work
issue: null
pr: null
last_updated: 2026-03-20
next_step: Review the archived draft and decide whether any part should be promoted into stable repo-maintenance docs.
promotion_targets:
  - docs/REPOSITORY-GOALS.md
  - docs/architecture.md
  - docs/decisions.md
  - README.md
---

# Archive and evaluate the AI-native repository design-principles draft

## Status

- State: proposed
- Branch: `work`
- PR: none yet
- Last updated: 2026-03-20

## Original Goal

Archive the supplied "AI 原生工程仓库设计原则（Draft v0.1）" in the repository so it can be discussed as a bounded repo-maintenance task before any stable guidance is promoted into the active docs set.

## Current Slice

Save the draft under `docs/tasks/` as task-local context, track the discussion as a repo-maintenance task, and explicitly defer any internalization into root entrypoints or stable `docs/` references until a later decision is made.

## Current Status

The draft is now stored as task material in this workspace rather than as an active repository guidance document. The repository-level `README.md` and `docs/REPOSITORY-GOALS.md` are intentionally not updated to present the draft as already-adopted policy.

## Confirmed Findings

- The supplied design-principles draft is valuable as discussion input, but it is not yet approved as stable repository guidance.
- The right short-term home is a tracked task workspace under `docs/tasks/`, not the standard docs set.
- Any future promotion should be selective and should map stable conclusions into the smallest fitting maintained document instead of importing the whole draft wholesale.
- The original draft is preserved in `design-principles-draft-v0.1.md` for later review.

## Open Questions

- Which parts of the draft describe durable repository policy versus broader AI-native repository theory?
- Should future promotion create a dedicated stable doc, or should conclusions be split across `README.md`, `docs/REPOSITORY-GOALS.md`, `docs/architecture.md`, and `docs/decisions.md`?
- What acceptance criteria should be used before any draft content becomes active repository guidance?

## Promotion Targets

- `docs/REPOSITORY-GOALS.md`
- `docs/architecture.md`
- `docs/decisions.md`
- `README.md`

## Next Session Entrypoint

Open `docs/tasks/ai-native-repo-design-principles/README.md` first, then review `design-principles-draft-v0.1.md` and decide whether the next slice is evaluation, simplification, or selective promotion.
