# Repository Goals

## Primary Objective

This repository is a source/archive repository for cross-platform AI engineering configuration.

It maintains the configuration assets, entry files, skills, rules, and supporting documentation that are intended to be deployed into other repositories or consumed by other AI coding tools. It also keeps a small set of repo-local entrypoints that exist only to maintain this repository itself.

## Repository Responsibilities

### 1. Repo-maintenance entrypoints

These files and directories exist only to maintain this repository:

- root `AGENTS.md`
- root `CLAUDE.md`
- root `.cursor/`

Codex maintenance is driven by root `AGENTS.md`. Phase 1 does not require additional repo-local `.codex/` assets.

### 2. Archived external platform assets

These are the maintained content assets for other tools and repositories:

- `platforms/codex/AGENTS.md`
- `platforms/codex/.codex/`
- `platforms/claude/CLAUDE.md`
- `platforms/cursor/.cursor/`

These assets are content under maintenance. They are not the active root entrypoints for this repository.

### 3. Governance and rationale documentation

Repository mission, sequencing, and rationale live in:

- `docs/REPOSITORY-GOALS.md`
- `docs/EVOLUTION-GOALS.md`
- `docs/讨论.md`

## Phase 1 Objective

Phase 1 optimizes for priority `A`: reduce duplicated maintenance across project-entry files.

Phase 1 must:

- make root entrypoints repo-specific
- move external platform assets out of the root tool directories
- preserve the maintained assets in stable platform-specific homes
- stop describing this repository as a backend-only prompt collection

Phase 1 does not attempt to:

- introduce generation pipelines
- unify every platform-specific behavior
- preserve the old root layout for backward compatibility

## Scope

### In scope

- repository contract and governance documents
- separation between repo-maintenance entrypoints and archived external assets
- platform-specific homes under `platforms/`
- cleanup of stale migration and obsolete root-level explanatory material

### Out of scope

- automated adapters or code generation
- semantic unification of all rules and skills across platforms
- onboarding additional platforms beyond the current Cursor, Claude, and Codex assets
- rewriting user-authored discussion archives unless explicitly requested

## Success Criteria

1. Root `AGENTS.md`, root `CLAUDE.md`, and root `.cursor/` describe maintenance of this repository only.
2. Archived external assets live under `platforms/` and remain navigable there.
3. Core repository docs no longer position the repository as a backend-only prompt collection.
4. Post-Phase-1 work is recorded separately so follow-up decisions are not lost.
5. Ambiguous user-authored rationale or template material is preserved until explicitly changed.
