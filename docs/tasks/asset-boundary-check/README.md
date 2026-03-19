---
task_id: asset-boundary-check
title: Repo-local asset boundary checking workflow
status: proposed
priority: high
kind: skill
branch: null
issue: null
pr: null
last_updated: 2026-03-19
next_step: Define the minimum rules for routing new material into root entrypoints, docs, templates, references, or platforms before implementing any checker.
promotion_targets:
  - docs/EVOLUTION-GOALS.md
  - .codex/
---

# Repo-local Asset Boundary Checking Workflow

## Goal

Design a repo-local workflow or skill that helps route new material into the correct repository home instead of letting content drift across root entrypoints, `docs/`, `templates/`, `references/`, and `platforms/`.

## Current Status

This work is proposed but not started. It was named in [docs/EVOLUTION-GOALS.md](../../EVOLUTION-GOALS.md) as one of the initial repo-local skill priorities.

## Confirmed Findings

- The repository boundary model is already documented, but placement decisions still depend on repeated manual judgment.
- Boundary mistakes are costly because they blur the line between repo-maintenance entrypoints, archived external assets, and reusable templates.
- This should remain a repo-local maintenance asset, not a platform-facing skill.

## Open Questions

- Which routing rules are strict enough to automate and which still require human judgment.
- Whether the first version should operate as a checklist, a reusable skill, or a script-backed validator.
- How to handle edge cases such as reference notes, local sync control files, and mixed repo-local versus platform-facing material.

## Next Session Entrypoint

Start by enumerating the repository homes that accept authored content and write one routing rule for each of: root entrypoints, `docs/`, `templates/`, `references/`, and `platforms/`.

## Promotion Targets

- `.codex/`
- `docs/EVOLUTION-GOALS.md`
