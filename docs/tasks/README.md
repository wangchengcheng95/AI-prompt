# Task Workspaces

## Purpose

`docs/tasks/` stores multi-session task workspaces for repo-maintenance work that is not yet fully resolved.

Use this area when a task needs to survive across:

- multiple chats
- multiple commits
- multiple branches or pull requests

This directory is for task context, not for stable repository policy.

## Active Task Index

Open one of these entrypoints first when resuming ongoing task work:

### Active

- `ai-friendly-repo`
  - Entry: `docs/tasks/ai-friendly-repo/README.md`
  - State: active
  - Branch: `docs-ai-friendly-repo-positioning`
  - PR: `#15`
  - Resume here when working on AI-friendly repository structure, indexing, or promotion-flow rules.

### Ongoing Research Context

- `ecc-skill-research`
  - Entry: `docs/tasks/ecc-skill-research/README.md`
  - State: research context retained
  - Branch/PR: see the task README and current Git state
  - Resume here when continuing the external skill research thread or the `verifier` evolution context tied to it.

### Historical Context

- `custom-user-agents-md`
  - Entry: `docs/tasks/custom-user-agents-md/2026-03-18-custom-user-agents-md.md`
  - State: historical context retained
  - Notes: this task predates the preferred `README.md` entrypoint shape

When a task becomes active, add it to this index. When it becomes stable history, move it to the historical section rather than deleting the context immediately.

## What Belongs Here

Use `docs/tasks/` for materials such as:

- task-level research notes
- handoff notes for the next session
- open questions and decision checkpoints
- a task-local index that points to the current branch, PR, and next entrypoint

## What Does Not Belong Here

Do not use `docs/tasks/` for:

- stable repository rules
- long-term architecture or decision records
- platform assets under `platforms/`
- one-off scratch notes that can be discarded immediately

Stable conclusions should be promoted into the standard docs set or into the relevant maintained asset once confirmed.

Disposable scratch work should stay out of Git or remain under `docs/tmp/` only when it does not need cross-session continuity.

## Recommended Structure

For each task, prefer one directory:

- `docs/tasks/<task-slug>/README.md`

Use `README.md` as the task entrypoint. It should make the next session cheap to resume.

If a task still uses an older non-`README.md` entrypoint, record that explicitly in the active task index until the task is normalized or retired.

Optional supporting files may sit beside it, for example:

- research notes
- comparison notes
- implementation checklists
- handoff notes

## Minimum Task README Content

Each task workspace `README.md` should usually include:

- original goal
- current slice
- current status
- branch and PR
- confirmed findings
- open questions
- next session entrypoint
- promotion targets for stable conclusions

## Active Task README Contract

For any task that appears in the active task index, prefer these top-level sections in this order:

1. `Status`
2. `Original Goal`
3. `Current Slice`
4. `Current Status`
5. `Confirmed Findings`
6. `Open Questions`
7. `Promotion Targets`
8. `Next Session Entrypoint`

The section titles do not need to be the only sections in the file, but these fields should be easy to find near the top so an AI can resume work without scanning the entire document first.

## Field Intent

- `Status`
  - record the task state, current branch, PR, and last-updated date
- `Original Goal`
  - preserve the longer-running task identity even when the current slice changes
- `Current Slice`
  - state the exact bounded scope for the current phase or next implementation step
- `Current Status`
  - summarize what has already been achieved and what remains true right now
- `Confirmed Findings`
  - capture validated conclusions that should not need to be rediscovered next session
- `Open Questions`
  - expose unresolved choices, missing information, or scope decisions
- `Promotion Targets`
  - say where stable conclusions should move when they stop being task-local
- `Next Session Entrypoint`
  - tell the next session what to open first and what decision or slice should come next

## Update Triggers

Update an active task README when any of the following changes:

- the task state changes, such as `active`, `blocked`, `research context retained`, or `historical context retained`
- the working branch or PR changes
- the current slice changes
- a new durable finding is confirmed
- an open question is resolved, replaced, or newly discovered
- the next best resume point changes
- a conclusion becomes stable enough to promote into the standard docs set or a maintained asset

When updating the README, prefer editing the summary sections first and leaving longer historical notes below them.

## Lifecycle

1. Create a task workspace when the work is likely to span more than one session or PR-sized slice.
2. Add or update the task in the active task index when its working status changes.
3. Keep the task `README.md` current as conclusions or scope change.
4. Promote stable conclusions into standard docs or maintained assets as they become real repository knowledge.
5. Remove or archive the task workspace only after it no longer holds unique context needed for future work.

## Naming

- Use short, stable task slugs.
- Prefer one task directory per real task thread.
- Avoid date-based directories unless the date is part of the task identity.
