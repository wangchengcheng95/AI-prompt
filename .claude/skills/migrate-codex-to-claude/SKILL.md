---
name: migrate-codex-to-claude
description: Migrate this repository's repo-local maintenance assets from root `.codex/` to root `.claude/` with low-decision, semantic-parity rules. Use when the user explicitly asks to migrate or refresh Codex-maintenance workflows, skills, scripts, or related docs for Claude Code in this repository.
---

# Migrate Codex To Claude

## Overview

Use this skill only for repo-local maintenance migration in this repository.

The default source is root `.codex/`. The default target is root `.claude/`.

Treat `platforms/` as archived external assets unless the user explicitly expands scope.

## Default Scope

- repo-local workflow skills, scripts, references, and assets needed for Claude to maintain this repository
- repo-local Claude entrypoint docs that must change so migrated assets actually work
- maintenance docs in `docs/` when they still imply Codex-only ownership or entry
- no archived external platform assets
- no backward-compatibility work unless the user explicitly asks for it

## Workflow

1. Inventory only the repo-local source and target homes that matter for this migration.
2. Build an explicit source-to-target mapping before editing anything.
3. Migrate by workflow behavior, not by folder symmetry.
4. Carry each migrated skill directory together with its bundled `scripts/`, `references/`, and `assets/`.
5. Rewrite target-local paths, wording, and execution assumptions so Claude can actually run the migrated assets.
6. Validate with the checklist in [references/protocol.md](references/protocol.md).
7. Summarize the migrated scope, deliberate omissions, verification, and any remaining runtime gaps.

## Key Differences From Cursor Migration

- Claude does not use `.mdc` rule files. Rules are expressed as additions to `CLAUDE.md` instead.
- Claude reads `CLAUDE.md` natively; skill references belong there as Claude-specific additions.
- The `agents/openai.yaml` shells in `.codex/skills/` have no Claude equivalent and should not be migrated.
- Use `.claude/` as the target root, not `.cursor/`.

## Hard Rules

- Do not treat `platforms/claude/` as the default target for repo-local maintenance migration.
- Do not invent target assets only to mirror source shape.
- Do not leave migrated Claude assets pointing at `.codex/` or `.cursor/` paths when that would block execution.
- Prefer repo-relative paths and links in committed docs.
- Record material scope cuts or intentional non-migrations in `docs/decisions.md`.

## Stop And Ask

Stop and ask the user when:

- the requested scope mixes repo-local maintenance entrypoints with archived external assets
- ownership of a source asset is unclear
- a rewrite would relocate or delete user-authored material with unclear ownership

## References

Load [references/protocol.md](references/protocol.md) for the migration checklist, failure modes, and recommended verification commands.
