# Evolution Goals

## Purpose

This document records the post-Phase-1 goals that were intentionally deferred while Phase 1 focuses on reducing duplicated maintenance at the project-entry level.

## Current Baseline

Phase 1 establishes the repository split between repo-maintenance entrypoints and archived external platform assets.

Phase 1 deliberately prioritizes low-friction maintenance reduction over immediate generation. The repository keeps stable platform homes first, then evolves toward a stronger shared model later.

Before deeper semantic normalization, the repository may also tighten its repo-local maintenance loop so Codex can intake a goal and drive it toward a ready-to-merge result with limited user intervention.

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

## Near-Term Repo-Local Iteration Contract

Goal: let Codex drive repo-maintenance tasks from user goal intake to ready-to-merge handoff without first freezing that workflow into rigid templates.

Expected outcomes:

- a documented intake gate for `accept`, `shrink`, and `stop`
- a default interaction budget that keeps user participation low
- a consistent repo-local handoff standard for branch, verification, commit, and pull request preparation

Reason for sequencing: this improves execution reliability for this repository itself without prematurely committing to cross-platform semantic automation.

## Long-Term Direction

The long-term direction is a platform-neutral source model with explicit mapping layers:

- core source for shared rules, skills, agents, and project-level context
- adapters for tool-specific mapping into Cursor, Claude, and Codex
- generated outputs for platform-specific deliverables that should not be maintained by hand

This direction remains deferred until the repository has stable platform homes and a clearer shared semantic model.

The repository should evolve by synchronizing semantic units rather than platform-specific prose. Shared intent should be modeled once and then mapped into each platform’s native carrier.

## External Reference Repositories

This section records external repositories that may be useful comparative references for later evolution work. These references do not change the active repository contract or the current Phase 1 boundaries.

### 2026-03-15 `affaan-m/everything-claude-code`

- Repository: <https://github.com/affaan-m/everything-claude-code>
- Observed on 2026-03-15: the repository presents itself as a cross-tool AI coding configuration or plugin-style package for direct downstream use rather than as a repo-local maintenance source/archive.
- Relevant overlap: it appears to address a similar cross-platform configuration problem space across tools such as Claude Code and Codex.
- Important difference: this repository is currently structured as a source/archive repository that separates repo-maintenance entrypoints, archived external platform assets under `platforms/`, and tool-neutral reusable templates under `templates/`.
- Why keep this reference: it may be useful later when evaluating packaging boundaries, installation ergonomics, test surface, and downstream distribution patterns for cross-platform AI engineering assets.
- Current implication: treat it as an external comparative example for future evolution work, not as a replacement for the active Phase 1 repository model.

Borrowable points for later phases:

- clearer packaging boundaries between source material and downstream-consumable deliverables
- more explicit downstream installation or enablement paths once this repository eventually owns a delivery surface
- stronger validation expectations for distributed assets, including tests around packaging or activation behavior
- a more deliberate inventory of asset types that may eventually need separate mapping or delivery treatment

Points not to borrow into the current repository model:

- reframing this repository around direct end-user installation as the primary purpose of the root
- collapsing repo-maintenance entrypoints into the same shape as downstream platform deliverables
- treating a plugin-style distribution model as a prerequisite for Phase 1 cleanup or Phase 2 semantic alignment
- expanding platform-specific surface area before the repository has a stronger shared semantic model

Documentation clarification check:

- Yes: the repository should keep stating that it is a source/archive repository first, not yet a unified installable distribution.
- Yes: external reference repositories should remain comparative inputs for evolution work rather than implicit target architecture.

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
