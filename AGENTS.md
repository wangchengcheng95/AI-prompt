# Repository Maintenance Instructions

This file is the authoritative Codex entrypoint for maintaining this repository.

This repository maintains archived/source AI configuration assets for multiple tools. The archived external Codex asset lives under `platforms/codex/` and is not the instruction source for maintaining this repository itself.

## Mission

- Maintain this repository as a source/archive for cross-platform AI engineering configuration.
- Keep Phase 1 focused on reducing duplicated maintenance at the project-entry level.
- Use `docs/REPOSITORY-GOALS.md` as the canonical statement of repository purpose and scope.

## Repository Boundaries

- Root `AGENTS.md`, root `CLAUDE.md`, root `.cursor/`, and selected root `.codex/` assets are repo-maintenance entrypoints only.
- `platforms/` stores the external assets this repository maintains for other repositories and tools.
- `templates/` stores tool-neutral reusable assets that are meant to be copied into other repositories.
- `docs/REPOSITORY-GOALS.md` defines the active repository contract.
- `docs/EVOLUTION-GOALS.md` records post-Phase-1 follow-up work.
- `docs/agent-iteration-contract.md` defines the repo-local goal-to-ready-to-merge collaboration contract for Codex maintenance tasks.
- `docs/system-overview.md`, `docs/architecture.md`, and `docs/decisions.md` hold the normalized repository-maintenance knowledge that was previously gathered through discussion.
- Shared template material must remain separate from repo-maintenance docs unless the user explicitly asks to relocate or delete it.

## Working Rules

- Keep governance and repo-maintenance docs English-first.
- For repo-local Codex maintenance tasks, drive work toward a ready-to-merge handoff by following `docs/agent-iteration-contract.md`.
- For repo-local goal-driven tasks, prefer using `$repo-self-iteration` as the default entry workflow.
- Inside that workflow, prefer `$git-start-task` for branch setup, `$git-commit` for commit creation, `$repo-doc-simplifier` as a conditional cleanup step for repo-maintenance docs, `$pr-handoff` for review handoff, and `$pr-operator` for actual PR operations.
- When discussing, proposing, or reviewing skills, agents, or sub-agents, explicitly state whether they are repo-local assets for maintaining this repository or archived external platform assets under `platforms/`.
- When creating or revising any `AGENTS.md` asset, consult `references/agents-writing-guides.md` first.
- When presenting the user with implementation or design options, anchor the comparison in industry best practices when available, give a clear recommendation, and explain the recommendation briefly.
- If content is platform-specific and meant to be consumed by another repository or tool, store it under `platforms/<tool>/`.
- If content is tool-neutral and meant to be copied into another repository, store it under `templates/`.
- Keep root tool-specific directories repo-specific and minimal.
- Keep root `.codex/` limited to the smallest set of skills or config needed to maintain this repository.
- Do not do backward-compatibility work unless the user explicitly asks for it.
- Before creating a new asset or document, search for an existing home and extend it instead of duplicating it.
- When moving archived assets, verify that internal references still point to valid locations inside their new platform home.
- Ask before deleting discussion records, templates, or other user-authored material whose ownership is unclear.

## Output Expectations

- Distinguish clearly between repo-maintenance entrypoints and archived external assets.
- Call out any filesystem or tooling constraint that prevents the intended cleanup.
