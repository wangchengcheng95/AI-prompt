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
