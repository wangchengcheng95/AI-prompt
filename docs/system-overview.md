# System Overview

## Purpose

This document records the stable facts about what this repository is, why it exists, and which asset categories it maintains.

## System Boundary

This repository exists because the same engineering constraints and workflows must be maintained across multiple AI coding tools, but each tool carries them in different structures and entrypoints.

The core problem is not simple file synchronization. The real problem is semantic drift: similar engineering intent must be maintained across Cursor, Claude, and Codex without repeatedly hand-editing parallel platform texts.

The repository therefore serves as a source/archive for cross-platform AI engineering configuration, with a clear split between:

- repo-local entrypoints used only to maintain this repository
- archived external platform assets maintained for use in other repositories or tools
- shared reusable templates maintained for copying into other repositories

## Maintained Asset Categories

The repository maintains these asset categories:

- project-level rules and entry files
- skills that encode repeatable task workflows
- agent or sub-agent definitions where the platform supports them
- tool-neutral reusable templates for downstream repositories
- governance and repository-maintenance documentation
- task workspaces for multi-session repo-maintenance handoff context, discovered through a local task index

The repository does not treat every category equally. Shared rules and high-frequency skills are the highest-leverage cross-platform assets. Agent and sub-agent definitions are more platform-specific and therefore less suitable for early unification.

## Stable Constraints

- Root entrypoints remain repo-specific.
- Archived external assets live under `platforms/`.
- Shared reusable templates live under `templates/`.
- Multi-session repo-maintenance task context may live under `docs/tasks/` until its stable conclusions are promoted.
- `docs/tasks/index.yaml` acts as the local AI-first todo ledger, while task-local `README.md` files hold deeper context.
- Shared semantics matter more than textual similarity between platforms.
- Phase 1 optimizes for reduced duplicated maintenance, not for immediate generation or full semantic normalization.
