---
task_id: learn-ralph-loop
title: Learn the Ralph-style agent iteration loop
status: proposed
priority: high
kind: research
branch: null
issue: null
last_updated: 2026-03-21
next_step: "Read `docs/agent-iteration-contract.md` and compare it to one external 'Ralph loop' write-up you trust; write three bullets: same intent, different mechanics, and risks to avoid."
promotion_targets:
  - docs/agent-iteration-contract.md
  - .cursor/skills/repo-self-iteration/SKILL.md
---

# Learn the Ralph-style agent iteration loop

## Status

- State: proposed (owner learning track)
- Branch: none unless you change repo iteration contract or skills
- Last updated: 2026-03-21

## Original Goal

Understand **Ralph loop** style workflows: repeated agent cycles over a fixed spec or ticket until tests pass or a stop condition fires—then map that pattern to safe practice in real repositories (branching, verification, handoff).

## Current Slice

- Internal baseline: `docs/agent-iteration-contract.md` and `.cursor/skills/repo-self-iteration/SKILL.md` (accept / shrink / stop, branch discipline, verification, handoff).
- External: read one current description of a Ralph-style loop from a source you consider authoritative for your stack.
- Deliverable: a short comparison under **Confirmed Findings** (intent alignment, operational differences, failure modes).

## Current Status

- Task registered; no external source chosen or comparison written yet.

## Confirmed Findings

- This repository already encodes a bounded iteration contract aimed at merge-ready handoffs rather than unbounded autonomous loops.

## Open Questions

- Will you run looped automation only locally, or in CI with explicit secrets and resource caps?
- What stop conditions are non-negotiable for your org (for example max iterations, max tokens, human gate on merge)?

## Promotion Targets

- If you refine how this repo should behave → update `docs/agent-iteration-contract.md` or the self-iteration skill via normal PR.
- Personal automation scripts stay outside this repository unless they become maintained assets under an appropriate `platforms/` home.

## Next Session Entrypoint

1. Skim `docs/agent-iteration-contract.md` (feasibility gate and execution loop).
2. Pick one external Ralph-loop article or repository README to read critically.
3. Fill **Confirmed Findings** with the three-bullet comparison described in **Current Slice**.
