# Repository Goals

## Primary Objective

This repository is a source/archive repository for cross-platform AI engineering configuration and reusable repository assets.

It maintains the configuration assets, entry files, skills, rules, and supporting documentation that are intended to be deployed into other repositories or consumed by other AI coding tools. It also keeps a small set of repo-local entrypoints that exist only to maintain this repository itself.

This repository is also an AI-friendly collaboration workspace for the user and the AI maintaining it together: the user brings goals, the AI organizes and indexes repository knowledge, proposes options, executes bounded work, and asks for user decisions when needed.

## Active Repository Contract

### Repo-maintenance entrypoints

These files and directories exist only to maintain this repository:

- root `AGENTS.md`
- root `CLAUDE.md`
- root `.cursor/`
- selected root `.codex/` assets that are explicitly kept for repo maintenance

Repo-local maintenance may be driven through the active root entrypoints, including root `AGENTS.md`, root `.cursor/`, and the minimal repo-local `.codex/` assets that are intentionally kept for maintaining this repository.

Root `AGENTS.md` is the rules entrypoint for maintaining this repository. It is not the single document that also owns repository positioning, sequencing, or evolution goals. Repository positioning lives in this document by design.

### Archived external platform assets

These are the maintained content assets for other tools and repositories:

- `platforms/codex/AGENTS.md`
- `platforms/codex/.codex/`
- `platforms/claude/CLAUDE.md`
- `platforms/cursor/.cursor/`

These assets are content under maintenance. They are not the active root entrypoints for this repository.

### Shared reusable templates

These are tool-neutral assets that are intended to be copied into other repositories:

- `templates/go-single-service-docs/`
- `templates/progressive-disclosure/`

These templates are maintained content assets. They are not repo-maintenance docs and they are not tied to any single AI tool.

### Local external reference workspaces

This repository may also keep a versioned reference index under `references/` together with gitignored local checkouts of third-party repositories used for comparative study.

The reference index is repo-maintenance support material. The third-party checkouts themselves are not maintained repository assets, are not part of `platforms/`, and are not distributable content of this repository.

### Standard repository-maintenance documents

The standard repository-maintenance documents under `docs/` are:

- `docs/REPOSITORY-GOALS.md` for the active repository contract
- `docs/EVOLUTION-GOALS.md` for deferred future-facing direction
- `docs/agent-iteration-contract.md` for the repo-local goal-to-ready-to-merge collaboration contract
- `docs/system-overview.md` for stable system facts
- `docs/architecture.md` for stable structure and mapping rules
- `docs/decisions.md` for dated design decisions

The repository may also keep multi-session task workspaces under `docs/tasks/` when a repo-maintenance task needs versioned handoff context before its stable conclusions are promoted elsewhere.

## Phase 1 Objective

Phase 1 optimizes for priority `A`: reduce duplicated maintenance across project-entry files.

Phase 1 must:

- make root entrypoints repo-specific
- move external platform assets out of the root tool directories
- preserve the maintained assets in stable platform-specific homes
- stop describing this repository as a backend-only prompt collection

Phase 1 does not attempt to:

- introduce generation pipelines
- package the repository as a single installable downstream distribution
- unify every platform-specific behavior
- preserve the old root layout for backward compatibility

## Scope

### In scope

- repository contract and governance documents
- repo-local goal intake and ready-to-merge collaboration rules
- separation between repo-maintenance entrypoints and archived external assets
- platform-specific homes under `platforms/`
- shared reusable templates under `templates/`
- reference indexing for third-party comparison repositories under `references/`
- cleanup of stale migration and obsolete root-level explanatory material

### Out of scope

- automated adapters or code generation
- semantic unification of all rules and skills across platforms
- onboarding additional platforms beyond the current Cursor, Claude, and Codex assets
- preserving discussion-style design notes when their surviving conclusions have been normalized into the standard docs or relevant maintained assets

## Success Criteria

1. Root `AGENTS.md`, root `CLAUDE.md`, root `.cursor/`, and selected root `.codex/` assets describe maintenance of this repository only.
2. Archived external assets live under `platforms/` and remain navigable there.
3. Shared reusable templates live under `templates/` and remain distinct from repo-maintenance docs and platform-specific assets.
4. Core repository docs no longer position the repository as a backend-only prompt collection.
5. Standard docs distinguish active contract, deferred evolution, stable facts, stable structure, and dated decisions.
6. Repo-local maintenance can be driven from a user goal to a ready-to-merge handoff with a documented collaboration contract through the active root entrypoints.
7. Removed discussion-style notes do not retain unique design information outside the standard docs set.
