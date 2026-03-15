# Evolution Goals

## Purpose

This document records the post-Phase-1 goals that were intentionally deferred while Phase 1 focuses on reducing duplicated maintenance at the project-entry level.

## Current Baseline

Phase 1 establishes the repository split between repo-maintenance entrypoints and archived external platform assets.

The next phases are ordered to protect correctness before scale:

1. semantic consistency
2. auditability and historical traceability
3. platform expansion

## Phase 2: Semantic Consistency

Goal: ensure shared rules and workflows mean the same thing across platforms, even when the file format or delivery mechanism differs.

Expected outcomes:

- shared rule entities with stable identifiers
- clearer mapping between common intent and platform-specific expression
- fewer silent drifts between Cursor, Claude, and Codex assets

Reason for sequencing: this should happen after Phase 1 creates stable homes for the assets, not before.

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
