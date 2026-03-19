---
task_id: custom-user-agents-md
title: Custom User AGENTS Task
status: done
priority: medium
kind: documentation
branch: custom-user-agents-md
issue: null
pr: null
last_updated: 2026-03-19
next_step: Review platforms/codex/home/AGENTS.md only if another wording pass or one more durable engineering constraint is needed.
promotion_targets:
  - platforms/codex/home/AGENTS.md
  - references/agents-writing-guides.md
---

# Custom User AGENTS Task

## Status

- State: formal asset created
- Branch: `custom-user-agents-md`
- Primary artifact: `platforms/codex/home/AGENTS.md`
- Supporting reference: `references/agents-writing-guides.md`
- PR status: do not create yet
- Last updated: 2026-03-19

## Goal

Create a user-level Codex `AGENTS.md` that captures stable cross-project engineering defaults without turning into either a project-specific handbook or a profile narrative.

## Outcome

- The reviewed draft was promoted into `platforms/codex/home/AGENTS.md`.
- The final direction is constraint-driven rather than biography-driven.
- The repository rule for future `AGENTS.md` work now requires:
  - reading `references/agents-writing-guides.md` first
  - checking for newer or more authoritative public guidance before drafting
  - updating that reference file when a better source is found

## Core Decisions

- Keep the user-level file thin but opinionated.
- Let more local project or path instructions override it when they are more specific.
- Treat security-sensitive handling as a soft default.
- Use language and engineering rules as soft defaults:
  - `Go` for production services and long-lived internal tools
  - `Shell` for simple orchestration and glue work
  - `Python` for data shaping, text processing, and short analysis utilities
- Prefer solution and architecture analysis before non-trivial execution.
- For non-trivial work, confirm the plan before implementation.
- Ask only about ambiguity that materially changes scope, risk, design choice, or acceptance criteria.
- Treat local private references as formal working inputs.
- Reuse and extend existing documentation before creating new notes.
- Record durable decisions and reusable conclusions in an appropriate existing documentation home instead of leaving them only in conversation.

## Research Summary

The public guidance and examples used in this task consistently favored:

- short, actionable instruction files
- concrete boundaries over vague preferences
- user-level files for stable cross-project defaults
- project-level or nested files for repository-specific commands, structure, and workflow

This supported moving from profile narration toward a small set of reusable engineering constraints.

## Retained Working Preferences

- Lead with concise conclusions and expand only on request.
- Compare two to three viable options before recommending one.
- Use a mixed review format: one-line conclusion, severity-ordered findings, concise recommendations.
- Keep delivery concise and high-density.

## Next Step

- Review `platforms/codex/home/AGENTS.md` directly.
- If needed, do one more wording pass or add one or two remaining engineering constraints.
- Otherwise, keep this task directory as historical context only.
