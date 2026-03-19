---
task_id: codex-home-agents-path-constraint
title: Carry repo path-portability rule into platforms/codex/home/AGENTS.md
status: proposed
priority: medium
kind: documentation
branch: null
issue: null
pr: null
last_updated: 2026-03-19
next_step: Review platforms/codex/home/AGENTS.md and decide whether the repo-local no-absolute-path rule should be copied as a stable platform-asset constraint.
promotion_targets:
  - platforms/codex/home/AGENTS.md
  - references/agents-writing-guides.md
---

# Carry Repo Path-Portability Rule Into `platforms/codex/home/AGENTS.md`

## Goal

Decide whether the repository rule against committing machine-specific absolute filesystem paths should also be expressed in the user-level Codex home `AGENTS.md` asset under `platforms/codex/home/`.

## Current Status

This work is proposed but not started. It was called out as a follow-up during the ECC skill research task, but was intentionally kept out of that task's scope.

## Confirmed Findings

- The repo-local rule already exists in stable repository docs.
- The follow-up would change a platform asset under `platforms/codex/`, not only repo-local maintenance docs.
- The right answer depends on whether the constraint should be treated as a durable cross-project user-level default.

## Open Questions

- Whether the user-level home `AGENTS.md` should carry this portability rule explicitly.
- Whether adding the rule would improve downstream portability without overfitting to this repository's maintenance style.
- Whether a stronger or weaker wording is appropriate for a user-level asset.

## Next Session Entrypoint

Read `platforms/codex/home/AGENTS.md`, compare it with the repo-local path-portability rule, and decide whether the constraint belongs in that platform asset.

## Promotion Targets

- `platforms/codex/home/AGENTS.md`
- `references/agents-writing-guides.md`
