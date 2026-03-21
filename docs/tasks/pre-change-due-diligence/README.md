---
task_id: pre-change-due-diligence
title: "[URGENT] Pre-change gate: authoritative docs and planning by importance"
status: archived
priority: urgent
kind: documentation
branch: null
issue: null
last_updated: 2026-03-21
next_step: "Reference this task only when revisiting why the due-diligence rule was promoted into docs/agent-iteration-contract.md or when reconsidering a root-level reminder."
promotion_targets:
  - docs/agent-iteration-contract.md
  - AGENTS.md
---

# Pre-Change Gate: Authoritative Docs and Planning

## Goal

Make importance-aware **due diligence** the default before repository changes: decide when to consult **authoritative online documentation** and when to **draft a plan first**, instead of editing immediately.

This task is now complete because the stable execution rule has been promoted into `docs/agent-iteration-contract.md`.

## Standing Checklist (apply before edits)

Treat this as an **urgent** recurring gate for repo-local maintenance work.

1. **Assess task importance** (scope, risk, reversibility, blast radius, familiarity with the APIs or tools involved).
2. **Authoritative sources** — When importance is non-trivial (unfamiliar stack, version-sensitive behavior, security, or publish/migration impact), **consult official or authoritative web documentation** (vendor docs, specs, release notes) before relying on memory or guesses.
3. **Planning** — When importance is non-trivial or multiple viable approaches exist, **produce a short plan first** (goal, constraints, steps, verification), then implement. For small, low-risk edits with a single obvious change, planning can be minimal but should still name what will be verified.

## Current Status

- Stable rule promoted into `docs/agent-iteration-contract.md`.
- No branch or PR was required for the task-local reminder itself.
- The task workspace now remains as historical context for why the rule was added.

## Confirmed Findings

- Importance is contextual: the same file change can be low-risk or high-risk depending on blast radius and uncertainty.
- Official docs reduce silent drift from training cutoffs and informal recall.
- The repo-local execution contract should explicitly require evaluating whether authoritative online sources are needed before implementation, not just whether a plan is needed.

## Open Questions

- Whether future usage proves `AGENTS.md` also needs a one-line reminder, or whether the task-time contract is the correct permanent home.

## Next Session Entrypoint

When revisiting this topic, open `docs/agent-iteration-contract.md` first and confirm the stable wording still matches actual repo-maintenance behavior.

## Promotion Targets

- `docs/agent-iteration-contract.md` — execution loop or feasibility gate
- `AGENTS.md` — working rules for Codex-maintainer behavior
