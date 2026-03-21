# Repository Maintenance Instructions

Authoritative entrypoint for maintaining this repository. See `docs/REPOSITORY-GOALS.md` for scope.

## Mission

Maintain this repository as a source/archive for cross-platform AI engineering configuration.
Keep Phase 1 focused on reducing duplicated maintenance at the project-entry level.

## Boundaries

- Root `AGENTS.md`, root `CLAUDE.md`, root `.claude/`, root `.cursor/`, and selected root `.codex/` assets are repo-maintenance entrypoints only.
- `platforms/` — external assets maintained for other repositories and tools
- `templates/` — tool-neutral assets meant to be copied into other repositories
- `docs/` — repo-maintenance knowledge: goals, architecture, decisions, contracts
- Shared template material must remain separate from repo-maintenance docs unless the user explicitly asks to relocate or delete it.

## Working Rules

- On branch `main`, do not `git commit` unless the user has explicitly allowed committing for that change set in the current conversation; otherwise use a task branch or hand off diffs for the user to commit
- English commit messages; repo-relative links; no machine-absolute paths
- Ask before deleting discussion records, templates, or user-authored material
- Before creating a new asset, search for an existing home and extend it instead
- Platform-specific content → `platforms/<tool>/`; tool-neutral content → `templates/`
- No backward-compatibility work unless explicitly requested
- When moving archived assets, verify internal references still resolve
- Doc layering: layer 1 (always-on) = root entry files (AGENTS.md, CLAUDE.md, README.md), stay minimal, no background knowledge; layer 2 (task-time) = agent-iteration-contract.md + skill files; layer 3 (reference) = docs/ files. Do not promote layer 3 content into layer 1.

## Read More

- Executing a task → `docs/agent-iteration-contract.md` (use `$repo-self-iteration`)
- User-stated exploration intensity → `docs/task-exploration-levels.md`
- Writing or revising `AGENTS.md` → `references/agents-writing-guides.md`
- Writing or revising skills → `references/skill-writing-guides.md` (use `$skill-creator`)
- Repo goals and scope → `docs/REPOSITORY-GOALS.md`
- Past decisions → `docs/decisions.md`
