# Architecture

## Purpose

This document records the stable maintenance model, mapping rules, and current-versus-deferred architecture for this repository.

## Maintenance Model

The repository uses a two-level architecture in the current state:

- repo-maintenance entrypoints at the repository root
- archived external platform assets under `platforms/`

Root entrypoints exist to operate on this repository itself. Archived platform assets are maintained content and are not the active runtime instructions for maintaining this repository.

## Content Model

The repository maintains three main cross-platform content types:

### Rules

Rules capture durable constraints that should remain stable across repeated work. They describe shared engineering expectations and should not be mixed with task-specific procedures.

### Skills

Skills capture repeatable workflows or SOP-style task guidance. They are often more reusable across platforms than agent definitions and therefore are a higher-priority target for later semantic alignment.

### Agents

Agents or sub-agents capture role-specific behavior. This layer has the greatest platform variance and should be handled last when cross-platform normalization is introduced.

## Mapping Principles

- Shared semantics should be maintained once and mapped into platform-native carriers.
- Platform-native entrypoints should remain native where that improves compatibility.
- `AGENTS.md` provides project-level baseline constraints.
- Role-specific instructions belong in agent or sub-agent definitions rather than in the shared baseline.
- Claude keeps a native shell entrypoint that can reference shared rules rather than being replaced by a raw `AGENTS.md` entry.

## Current Versus Deferred Architecture

### Current

The repository currently relies on explicit platform homes and minimal repo-local entrypoints. This is the active Phase 1 architecture.

### Deferred

The deferred long-term architecture is:

- core source for shared semantics
- adapters for platform-specific mapping
- generated outputs for platform deliverables

This deferred model remains valid as a long-term direction, but it is not the implementation target for Phase 1.
