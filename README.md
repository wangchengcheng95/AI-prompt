# Cross-Platform AI Configuration Archive

This repository maintains archived/source AI configuration assets for multiple AI coding tools. It is not a backend-only prompt collection and it does not optimize for backward compatibility during this reorganization.

Phase 1 focuses on one outcome: reduce duplicated maintenance at the project-entry level by separating repo-maintenance entrypoints from the external platform assets this repository maintains.

## Repository Layout

- `AGENTS.md` - Codex entrypoint for maintaining this repository
- `CLAUDE.md` - Claude entrypoint for maintaining this repository
- `.cursor/` - minimal Cursor entrypoints for maintaining this repository
- `platforms/codex/AGENTS.md` and `platforms/codex/.codex/` - archived external Codex assets
- `platforms/claude/CLAUDE.md` - archived external Claude entry asset
- `platforms/cursor/.cursor/` - archived external Cursor assets
- `docs/REPOSITORY-GOALS.md` - active repository mission, scope, and success criteria
- `docs/EVOLUTION-GOALS.md` - post-Phase-1 evolution goals
- `docs/讨论.md` - archived discussion and rationale input

## Current Contract

- Root entrypoints exist only to maintain this repository itself.
- External tool assets live under `platforms/` and are maintained there as content.
- The repository may delete obsolete or redundant root-level material directly when it conflicts with the new contract.

## Start Here

- Read `docs/REPOSITORY-GOALS.md` for repository scope.
- Read `docs/EVOLUTION-GOALS.md` for the next phases after Phase 1.
- Go to `platforms/` when you are editing assets intended for other repositories or tools.
