# Architecture

## Purpose

This document records the stable maintenance model, mapping rules, and current-versus-deferred architecture for this repository.

## Maintenance Model

The repository uses a three-part architecture in the current state:

- repo-maintenance entrypoints at the repository root
- archived external platform assets under `platforms/`
- tool-neutral reusable templates under `templates/`

The repository may also keep a lightweight support area under `references/`:

- versioned reference notes that explain which third-party repositories are useful to compare against
- gitignored local checkouts of those third-party repositories for study across environments

Root entrypoints exist to operate on this repository itself. Archived platform assets are maintained content and are not the active runtime instructions for maintaining this repository. Shared templates are maintained content assets intended to be copied into other repositories, but they are not tied to any single platform carrier.

Reference checkouts under `references/` are not maintained outputs of this repository. They exist only as local comparison material and must not be treated as `platforms/` assets or template content.

Repo-maintenance execution also uses a two-layer control model:

- root `AGENTS.md` for runtime maintenance rules
- `docs/agent-iteration-contract.md` for the repo-local goal-to-ready-to-merge collaboration contract

The rule entrypoint and the collaboration contract are intentionally separate so the repository can tighten execution behavior without turning the runtime rule file into a long planning document.

## Content Model

The repository maintains three main cross-platform content types:

### Rules

Rules capture durable constraints that should remain stable across repeated work. They describe shared engineering expectations and should not be mixed with task-specific procedures.

### Skills

Skills capture repeatable workflows or SOP-style task guidance. They are often more reusable across platforms than agent definitions and therefore are a higher-priority target for later semantic alignment.

### Agents

Agents or sub-agents capture role-specific behavior. This layer has the greatest platform variance and should be handled last when cross-platform normalization is introduced.

### Templates

Templates capture reusable repository assets that are meant to be copied into other repositories without being bound to a single AI tool. They should remain separate from both repo-maintenance docs and platform-specific carriers.

## Mapping Principles

- Shared semantics should be maintained once and mapped into platform-native carriers.
- Platform-native entrypoints should remain native where that improves compatibility.
- `AGENTS.md` provides project-level baseline constraints.
- `docs/agent-iteration-contract.md` defines the repo-local maintenance loop from goal intake to ready-to-merge handoff.
- Role-specific instructions belong in agent or sub-agent definitions rather than in the shared baseline.
- Claude keeps a native shell entrypoint that can reference shared rules rather than being replaced by a raw `AGENTS.md` entry.
- Tool-neutral reusable templates belong under `templates/`, not under `docs/` or `platforms/`.
- Third-party reference checkouts belong under `references/`, not under `platforms/` or root tool directories.

## Local Sync Control

The repository may use a repo-local sync control plane to copy archived external assets from `platforms/` into local sibling workspaces or repositories and to backflow selected managed changes into this repository.

This sync layer is maintenance infrastructure for this repository itself, not an archived external platform asset. Its mappings should remain explicit, preview-first, and scoped to manifest-managed paths. Machine-local target paths should stay outside Git, while per-target sync provenance may be written into the target itself so drift and conflict checks remain local and auditable.

## Current Versus Deferred Architecture

### Current

The repository currently relies on explicit platform homes and minimal repo-local entrypoints. This is the active Phase 1 architecture.

### Deferred

The deferred long-term architecture is:

- core source for shared semantics
- adapters for platform-specific mapping
- generated outputs for platform deliverables

This deferred model remains valid as a long-term direction, but it is not the implementation target for Phase 1.
