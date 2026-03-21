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

## Active Task Index

Use this as a quick human-readable resume guide.

The canonical task ledger is `docs/tasks/index.yaml`. The list below is a compact entrypoint map for the highest-signal current tasks.

Open one of these entrypoints first when resuming ongoing task work:

### Active

- `ai-friendly-repo`
  - Entry: `docs/tasks/ai-friendly-repo/README.md`
  - State: active
  - Branch: `docs-ai-friendly-repo-positioning`
  - PR: `#15`
  - Resume here when working on AI-friendly repository structure, indexing, or promotion-flow rules.

- `human-ai-collaborative-maintenance`
  - Entry: `docs/tasks/human-ai-collaborative-maintenance/README.md`
  - State: active
  - Standing note: this repository is maintained collaboratively by the owner and AI assistants; use other tasks for executable backlog items.

### Ongoing Research Context

- `ecc-skill-research`
  - Entry: `docs/tasks/ecc-skill-research/README.md`
  - State: research context retained
  - Branch/PR: see the task README and current Git state
  - Resume here when continuing the external skill research thread or the `verifier` evolution context tied to it.

### Historical Context

- `custom-user-agents-md`
  - Entry: `docs/tasks/custom-user-agents-md/README.md`
  - State: historical context retained
  - Notes: durable conclusions were promoted and the task remains as reference context

When a task becomes active, add it to this index. When it becomes stable history, move it to the historical section rather than deleting the context immediately.

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

If a task still uses an older non-`README.md` entrypoint, record that explicitly in the active task index until the task is normalized or retired.

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
- phase (for active and proposed tasks)
- task type
- task doc path
- branch
- PR or issue reference when relevant
- next step
- last updated date

If a task is represented on GitHub, store the GitHub link as a reference only. Do not force AI to reconstruct the task by reading GitHub comments first.

Recommended phase values (for active and proposed tasks; omit for done/deferred):

- `phase-1-active` — currently in progress
- `phase-1-near-term` — next up, explicitly sequenced in `docs/EVOLUTION-GOALS.md`
- `phase-1-backlog` — proposed but not yet ordered for near-term pickup

Recommended status values:

- `proposed`
- `active`
- `blocked`
- `deferred`
- `done`
- `archived`

Recommended priority values:

- `high`
- `medium`
- `low`

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
- current slice
- current status
- confirmed findings
- open questions
- next session entrypoint
- promotion targets for stable conclusions

For active or resumable tasks, prefer these top-level body sections near the top of the file, in this order:

1. `Status`
2. `Original Goal`
3. `Current Slice`
4. `Current Status`
5. `Confirmed Findings`
6. `Open Questions`
7. `Promotion Targets`
8. `Next Session Entrypoint`

The section titles do not need to be the only sections in the file, but these fields should be easy to find without scanning the whole narrative history first.

Use [TEMPLATE.md](./TEMPLATE.md) when creating a new task workspace.

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

Update an active or resumable task README when any of the following changes:

- the task state changes
- the working branch or PR changes
- the current slice changes
- a new durable finding is confirmed
- an open question is resolved, replaced, or newly discovered
- the next best resume point changes
- a conclusion becomes stable enough to promote into the standard docs set or a maintained asset

When updating the README, prefer editing the summary sections first and leaving longer historical notes below them.

## Lifecycle

1. Add the task to `docs/tasks/index.yaml` when the work is likely to span more than one session or PR-sized slice.
2. Create or update `docs/tasks/<task-slug>/README.md` as the task context entrypoint.
3. Add or update the task in the human-readable active task index when its working status changes.
4. Keep both the index entry and the task README current as conclusions or scope change.
5. Promote stable conclusions into standard docs or maintained assets as they become real repository knowledge.
6. Mark the task `done` or `archived` in `index.yaml` once it no longer needs active continuation.

## Writing Rules

- Use short, stable task slugs.
- Prefer one task directory per real task thread.
- Avoid date-based directories unless the date is part of the task identity.
- In other docs, prefer linking back to the tracked task instead of creating a second standalone todo list.
- Use repo-relative paths in committed task docs unless environment-specific debugging material is explicitly required.
