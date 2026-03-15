# Evolution Goals

## Purpose

This document records the post-Phase-1 goals that were intentionally deferred while Phase 1 focuses on reducing duplicated maintenance at the project-entry level.

## Current Baseline

Phase 1 establishes the repository split between repo-maintenance entrypoints and archived external platform assets.

Phase 1 deliberately prioritizes low-friction maintenance reduction over immediate generation. The repository keeps stable platform homes first, then evolves toward a stronger shared model later.

The next phases are ordered to protect correctness before scale:

1. semantic consistency
2. auditability and historical traceability
3. platform expansion

## Near-Term Repo-Maintenance Skill Sequencing

Current near-term skill work is limited to repo-local skills that help maintain this repository itself.

This near-term track does not include platform-facing agents, sub-agents, or platform asset skills under `platforms/`.

Initial repo-local skill focus:

- cross-doc consistency checking across the standard repository-maintenance documents
- asset-boundary checking so new material lands in the correct root, `platforms/`, `templates/`, or `docs/` home

Deferred repo-local skill backlog:

- repo-doc normalization for turning discussion outcomes into the standard docs set
- maintenance-change review for checking proposed repository updates against Phase 1 boundaries and repository scope
- repository intake triage for deciding whether new maintenance material extends an existing asset or deserves a new home

## Long-Term Direction

The long-term direction is a platform-neutral source model with explicit mapping layers:

- core source for shared rules, skills, agents, and project-level context
- adapters for tool-specific mapping into Cursor, Claude, and Codex
- generated outputs for platform-specific deliverables that should not be maintained by hand

This direction remains deferred until the repository has stable platform homes and a clearer shared semantic model.

The repository should evolve by synchronizing semantic units rather than platform-specific prose. Shared intent should be modeled once and then mapped into each platform’s native carrier.

## Phase 2: Semantic Consistency

Goal: ensure shared rules and workflows mean the same thing across platforms, even when the file format or delivery mechanism differs.

Expected outcomes:

- shared rule entities with stable identifiers
- clearer mapping between common intent and platform-specific expression
- fewer silent drifts between Cursor, Claude, and Codex assets

Reason for sequencing: this should happen after Phase 1 creates stable homes for the assets, not before.

Implementation order inside this phase:

- unify shared rules first
- unify high-frequency skills second
- handle agents and sub-agents last

Agents and sub-agents remain last because platform differences are largest there and premature unification would create unnecessary design weight.

## Phase 3: Auditability And History

Goal: make configuration evolution explainable, reviewable, and recoverable over time.

Expected outcomes:

- explicit decision records for structural changes
- traceable asset evolution instead of undocumented rewrites
- clearer rationale for platform-specific exceptions

Reason for sequencing: governance is more valuable after the repository contract and asset locations stop moving rapidly.

## Phase 4: Platform Expansion

Goal: make it easier to add new tool targets without reworking the repository contract again.

Expected outcomes:

- a clearer source model for shared concepts
- stable adapter boundaries for future tools
- lower marginal cost when onboarding a new platform

Reason for sequencing: expansion should build on a stable semantic model and a traceable history, not replace them.
