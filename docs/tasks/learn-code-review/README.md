---
task_id: learn-code-review
title: Learn systematic code review (agent and human)
status: proposed
priority: high
kind: research
branch: null
issue: null
last_updated: 2026-03-21
next_step: "Walk through `platforms/cursor/.cursor/commands/general/code-review.md` once with a real small diff; extend the checklist with one project-specific risk you care about."
promotion_targets:
  - platforms/cursor/.cursor/commands/general/code-review.md
  - .cursor/skills/
---

# Learn systematic code review

## Status

- State: proposed (owner learning track)
- Branch: none unless you extend maintained command or skill assets
- Last updated: 2026-03-21

## Original Goal

Practice **code review** as a repeatable discipline: scope comprehension, correctness, maintainability, security, and actionable feedback—whether you review as a human or delegate to an agent.

## Current Slice

- Internal reference: archived Cursor command at `platforms/cursor/.cursor/commands/general/code-review.md`.
- Outcome: complete at least one full pass (understand change → validate behavior → quality → security) on a real PR-sized diff and record one lesson learned.

## Current Status

- Task registered; no completed review exercises logged here yet.

## Confirmed Findings

- This repository already ships a general review outline suitable for Cursor-style command use.

## Open Questions

- Do you want a repo-local Cursor **skill** mirroring that command, or keep review prompts project-specific?
- Should security review depth vary by subsystem (for example credentials vs docs-only changes)?

## Promotion Targets

- Reusable review prompt or skill text → root `.cursor/skills/` or `platforms/cursor/` only if you decide to maintain it for distribution.
- Repo governance conclusions → `docs/decisions.md`.

## Next Session Entrypoint

1. Open `platforms/cursor/.cursor/commands/general/code-review.md`.
2. Pick one recent or staged change set in any repository you maintain.
3. Run the checklist; add bullets under **Confirmed Findings** for patterns you want to reuse.
