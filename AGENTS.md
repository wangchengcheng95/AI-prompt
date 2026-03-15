# Repository Maintenance Instructions

This file is the authoritative Codex entrypoint for maintaining this repository.

This repository maintains archived/source AI configuration assets for multiple tools. The archived external Codex asset lives under `platforms/codex/` and is not the instruction source for maintaining this repository itself.

## Mission

- Maintain this repository as a source/archive for cross-platform AI engineering configuration.
- Keep Phase 1 focused on reducing duplicated maintenance at the project-entry level.
- Use `docs/REPOSITORY-GOALS.md` as the canonical statement of repository purpose and scope.

## Repository Boundaries

- Root `AGENTS.md`, root `CLAUDE.md`, and root `.cursor/` are repo-maintenance entrypoints only.
- `platforms/` stores the external assets this repository maintains for other repositories and tools.
- `docs/REPOSITORY-GOALS.md` defines the active repository contract.
- `docs/EVOLUTION-GOALS.md` records post-Phase-1 follow-up work.
- `docs/讨论.md` and untracked template material are rationale inputs and must be preserved unless the user explicitly asks to relocate or delete them.

## Working Rules

- Keep governance and repo-maintenance docs English-first.
- If content is meant to be consumed by another repository or tool, store it under `platforms/<tool>/`.
- Keep root tool-specific directories repo-specific and minimal.
- Do not do backward-compatibility work unless the user explicitly asks for it.
- Before creating a new asset or document, search for an existing home and extend it instead of duplicating it.
- When moving archived assets, verify that internal references still point to valid locations inside their new platform home.
- Ask before deleting discussion records, templates, or other user-authored material whose ownership is unclear.

## Output Expectations

- Distinguish clearly between repo-maintenance entrypoints and archived external assets.
- Call out any filesystem or tooling constraint that prevents the intended cleanup.
