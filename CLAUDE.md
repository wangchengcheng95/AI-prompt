# CLAUDE.md

@AGENTS.md

## Claude-specific additions

- Use this file only for maintaining this repository.
- The archived external Claude asset lives at `platforms/claude/CLAUDE.md`.
- Keep shared repo-maintenance rules in root `AGENTS.md`.
- Repo-local workflow skills live under `.claude/skills/`. See `.claude/README.md` for the full list.

## Repo Maintenance Rules

- For goal-driven repo-local maintenance tasks, classify scope as `accept`, `shrink`, or `stop` before editing.
- Prefer the smallest reviewable slice that can credibly reach ready-to-merge in one pass.
- Follow `docs/agent-iteration-contract.md` for the execution loop, handoff fields, and stop conditions.
- When the user states an exploration level for the task, follow `docs/task-exploration-levels.md`.
- Prefer the repo-local Claude skills under `.claude/skills/` for `repo-self-iteration`, `git-start-task`, `git-commit`, `repo-doc-simplifier`, `pr-handoff`, `pr-operator`, and `prompt-sync` when they match the task.
- Use English commit subjects for repo-local maintenance commits in this repository.
- Keep explicit user interactions for decisions that materially change scope, risk, or permissions; otherwise continue with stated assumptions.

## Asset Boundary

- Root `AGENTS.md`, root `CLAUDE.md`, and root `.claude/` are repo-maintenance entrypoints only.
- `platforms/claude/` stores the archived external Claude asset maintained by this repository.
- Do not place distributable external platform assets in root `.claude/`.
- Before creating a new asset, search for an existing home and extend it instead of duplicating.
