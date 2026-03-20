---
task_id: pre-change-due-diligence
title: "[URGENT] Pre-change gate: authoritative docs and planning by importance"
status: active
priority: urgent
kind: documentation
branch: null
issue: null
pr: null
last_updated: 2026-03-20
next_step: "Before any repo-local maintenance edit, run the standing checklist below; promote conclusions into agent-iteration-contract or AGENTS.md when they stabilize."
promotion_targets:
  - docs/agent-iteration-contract.md
  - AGENTS.md
---

# Pre-Change Gate: Authoritative Docs and Planning

## Goal

Make importance-aware **due diligence** the default before repository changes: decide when to consult **authoritative online documentation** and when to **draft a plan first**, instead of editing immediately.

## Standing Checklist (apply before edits)

Treat this as an **urgent** recurring gate for repo-local maintenance work.

1. **Assess task importance** (scope, risk, reversibility, blast radius, familiarity with the APIs or tools involved).
2. **Authoritative sources** — When importance is non-trivial (unfamiliar stack, version-sensitive behavior, security, or publish/migration impact), **consult official or authoritative web documentation** (vendor docs, specs, release notes) before relying on memory or guesses.
3. **Planning** — When importance is non-trivial or multiple viable approaches exist, **produce a short plan first** (goal, constraints, steps, verification), then implement. For small, low-risk edits with a single obvious change, planning can be minimal but should still name what will be verified.

## Current Status

Evergreen process reminder tracked in the task index. No branch or PR required until this is folded into stable maintainer docs.

## Confirmed Findings

- Importance is contextual: the same file change can be low-risk or high-risk depending on blast radius and uncertainty.
- Official docs reduce silent drift from training cutoffs and informal recall.

## Open Questions

- Whether to merge this gate verbatim into `docs/agent-iteration-contract.md` or keep it task-local until usage proves the wording.

## Next Session Entrypoint

When maintaining the repo, open `docs/tasks/index.yaml`, confirm this task remains `active`, and apply the checklist before the first edit of the session when the work is not trivial.

## Promotion Targets

- `docs/agent-iteration-contract.md` — execution loop or feasibility gate
- `AGENTS.md` — working rules for Codex-maintainer behavior
