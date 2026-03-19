# Task Workspaces

## Purpose

`docs/tasks/` stores multi-session task workspaces for repo-maintenance work that is not yet fully resolved.

Use this area when a task needs to survive across:

- multiple chats
- multiple commits
- multiple branches or pull requests

This directory is for task context, not for stable repository policy.

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

Optional supporting files may sit beside it, for example:

- research notes
- comparison notes
- implementation checklists
- handoff notes

## Minimum Task README Content

Each task workspace `README.md` should usually include:

- original goal
- current status
- branch and PR
- confirmed findings
- open questions
- next session entrypoint
- promotion targets for stable conclusions

## Lifecycle

1. Create a task workspace when the work is likely to span more than one session or PR-sized slice.
2. Keep the task `README.md` current as conclusions or scope change.
3. Promote stable conclusions into standard docs or maintained assets as they become real repository knowledge.
4. Remove or archive the task workspace only after it no longer holds unique context needed for future work.

## Naming

- Use short, stable task slugs.
- Prefer one task directory per real task thread.
- Avoid date-based directories unless the date is part of the task identity.
