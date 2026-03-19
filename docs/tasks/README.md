# Task Workspaces

## Purpose

`docs/tasks/` is the local, AI-first task memory for unfinished repo-maintenance work.

Use this area when a task needs to survive across:

- multiple chats
- multiple commits
- multiple branches or pull requests

This directory is for task state and task context. It is not the home for stable repository policy.

## Canonical Sources

`docs/tasks/` now uses two layers:

- `index.yaml` is the canonical todo ledger for task discovery, status, priority, and next-step lookup
- `docs/tasks/<task-slug>/README.md` is the canonical context entrypoint for one task

GitHub issues, pull requests, or project cards may mirror this information for human collaboration, but they are optional external surfaces. They are not the primary source of truth for AI resume.

## What Belongs Here

Use this area for materials such as:

- task status and priority in `index.yaml`
- task-level research notes
- handoff notes for the next session
- open questions and decision checkpoints
- a task-local entrypoint that points to the current branch, PR, and next action

## What Does Not Belong Here

Do not use `docs/tasks/` for:

- stable repository rules
- long-term architecture or decision records
- platform assets under `platforms/`
- one-off scratch notes that can be discarded immediately

Stable conclusions should be promoted into the standard docs set or into the relevant maintained asset once confirmed.

Disposable scratch work should stay out of Git or remain under `docs/tmp/` only when it does not need cross-session continuity.

## Required Structure

For each task, prefer one directory:

- `docs/tasks/<task-slug>/README.md`

Use `README.md` as the task entrypoint. It should make the next session cheap to resume.

Optional supporting files may sit beside it, for example:

- research notes
- comparison notes
- implementation checklists
- handoff notes

## Index Contract

Every tracked task should appear in `docs/tasks/index.yaml`.

Each entry should include at least:

- stable task id
- title
- status
- priority
- task type
- task doc path
- branch
- PR or issue reference when relevant
- next step
- last updated date

If a task is represented on GitHub, store the GitHub link as a reference only. Do not force AI to reconstruct the task by reading GitHub comments first.

## Task README Contract

Each task workspace `README.md` should start with YAML front matter so both humans and AI can recover the task quickly.

The front matter should usually include:

- `task_id`
- `title`
- `status`
- `priority`
- `kind`
- `branch`
- `issue`
- `pr`
- `last_updated`
- `next_step`
- `promotion_targets`

The body should usually include:

- original goal
- current status
- confirmed findings
- open questions
- next session entrypoint
- promotion targets for stable conclusions

Use [TEMPLATE.md](./TEMPLATE.md) when creating a new task workspace.

## Lifecycle

1. Add the task to `docs/tasks/index.yaml` when the work is likely to span more than one session or PR-sized slice.
2. Create or update `docs/tasks/<task-slug>/README.md` as the task context entrypoint.
3. Keep both the index entry and the task README current as conclusions or scope change.
4. Promote stable conclusions into standard docs or maintained assets as they become real repository knowledge.
5. Mark the task `done` or `archived` in `index.yaml` once it no longer needs active continuation.

## Writing Rules

- Use short, stable task slugs.
- Prefer one task directory per real task thread.
- Avoid date-based directories unless the date is part of the task identity.
- In other docs, prefer linking back to the tracked task instead of creating a second standalone todo list.
- Use repo-relative paths in committed task docs unless environment-specific debugging material is explicitly required.
