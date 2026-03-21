---
task_id: learn-code-simplifier
title: Learn code and doc simplification discipline
status: proposed
priority: high
kind: research
branch: null
issue: null
last_updated: 2026-03-21
next_step: "Read `.cursor/skills/repo-doc-simplifier/SKILL.md` (and `.claude/skills/` mirror if you use Claude Code); apply it once to one bloated doc, then list one simplification rule you will reuse for code edits."
promotion_targets:
  - .cursor/skills/repo-doc-simplifier/SKILL.md
  - docs/
---

# Learn code and doc simplification discipline

## Status

- State: proposed (owner learning track)
- Branch: none unless you change maintained skills or docs
- Last updated: 2026-03-21

## Original Goal

Internalize **simplification** as an explicit skill: remove duplication and dead weight while preserving true constraints—starting from this repository’s doc simplifier skill and extending the same mindset to code.

## Current Slice

- Study repo-local skill: `.cursor/skills/repo-doc-simplifier/SKILL.md`.
- Apply: one controlled pass on a single maintenance Markdown file that has grown repetitive.
- Reflect: translate one technique to code (for example delete redundant branches, collapse parallel explanations, preserve public behavior).

## Current Status

- Task registered; no applied simplification logged here yet.

## Confirmed Findings

- This repository already defines a focused process for compressing repo-maintenance Markdown without dropping constraints.

## Open Questions

- Should “simplifier” practice stay doc-only here, or do you want a separate code-focused checklist skill later?

## Promotion Targets

- Improvements to the simplifier skill itself → same skill file under `.cursor/skills/` / `.claude/skills/` with normal PR review.
- General engineering habits → personal notes only unless they become repo policy.

## Next Session Entrypoint

1. Open `.cursor/skills/repo-doc-simplifier/SKILL.md` and follow it literally once.
2. Record before/after takeaway in **Confirmed Findings** (one or two bullets, no essay).
