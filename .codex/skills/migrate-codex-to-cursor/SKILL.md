---
name: migrate-codex-to-cursor
description: Migrate this repository's repo-local maintenance assets from root `.codex/` to root `.cursor/` with low-decision, semantic-parity rules. Use when the user explicitly asks to migrate or refresh Codex-maintenance workflows, skills, scripts, or related docs for Cursor in this repository.
---

# Migrate Codex To Cursor

## Overview

Use this skill only for repo-local maintenance migration in this repository.

The default source is root `.codex/`. The default target is root `.cursor/`.

Treat `platforms/` as archived external assets unless the user explicitly expands scope.

## Default Scope

- repo-local workflow skills, scripts, references, and assets needed for Cursor to maintain this repository
- repo-local Cursor rules or entrypoint docs that must change so migrated assets actually work
- maintenance docs in `docs/` when they still imply Codex-only ownership or entry
- no archived external platform assets
- no backward-compatibility work unless the user explicitly asks for it

## Workflow

1. Inventory only the repo-local source and target homes that matter for this migration.
2. Build an explicit source-to-target mapping before editing anything.
3. Migrate by workflow behavior, not by folder symmetry.
4. Carry each migrated skill directory together with its bundled `scripts/`, `references/`, and `assets/`.
5. Rewrite target-local paths, wording, and execution assumptions so Cursor can actually run the migrated assets.
6. Validate with the checklist in [references/protocol.md](references/protocol.md).
7. Summarize the migrated scope, deliberate omissions, verification, and any remaining runtime gaps.

## Hard Rules

- Do not treat `platforms/cursor/.cursor/` as the default target for repo-local maintenance migration.
- Do not invent target assets only to mirror source shape.
- Migrate subagents or agents only when a real repo-local source asset exists.
- Do not leave migrated Cursor assets pointing at `.codex/` paths when that would block execution.
- When editing any `SKILL.md` as part of the migration, use `$skill-creator` first and keep the migrated skill concise.
- Prefer repo-relative paths and links in committed docs.
- Record material scope cuts or intentional non-migrations in `docs/decisions.md`.

## Stop And Ask

Stop and ask the user when:

- the requested scope mixes repo-local maintenance entrypoints with archived external assets
- ownership of a source asset is unclear
- a rewrite would relocate or delete user-authored material with unclear ownership
- true Cursor runtime validation is required but unavailable in the current environment

## References

Load [references/protocol.md](references/protocol.md) for the migration checklist, failure modes, and recommended verification commands.
