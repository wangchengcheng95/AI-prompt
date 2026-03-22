---
task_id: learn-code-review
title: Learn systematic code review (agent and human)
status: proposed
priority: high
kind: research
branch: null
issue: null
last_updated: 2026-03-21
next_step: "Study `references/external/claude-code/plugins/code-review` (README, plugin manifest, `commands/code-review.md`); note how multi-agent PR review and confidence scoring differ from the archived Cursor checklist command."
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

- Primary study: Claude Code **Code Review** plugin checkout at `references/external/claude-code/plugins/code-review` (parallel agents, confidence threshold, PR-oriented flow).
- Secondary reference: archived Cursor checklist at `platforms/cursor/.cursor/commands/general/code-review.md` for contrast after the plugin pass.
- Outcome: summarize one takeaway (for example agent split, scoring, or skip rules) under **Confirmed Findings**; optional second slice is still a real diff walkthrough with the Cursor command.

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

1. Open `references/external/claude-code/plugins/code-review/README.md`, then `commands/code-review.md` and `.claude-plugin/plugin.json`.
2. Note command arguments, agent roles, confidence cutoff, and skip conditions; compare mentally to a single-agent checklist review.
3. When ready, either run `/code-review` in a Claude Code context that has the plugin, or defer execution and still capture design notes under **Confirmed Findings**.
4. Later: use `platforms/cursor/.cursor/commands/general/code-review.md` on a real diff if you want the Cursor-side baseline exercise.
