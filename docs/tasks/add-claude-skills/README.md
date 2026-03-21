---
task_id: add-claude-skills
title: Migrate repo-local Codex maintenance skills to Claude Code
status: done
priority: high
kind: skill
branch: add-claude-skills
issue: null
last_updated: 2026-03-19
next_step: No further repository changes are needed unless the Claude-side maintenance assets need another migration or wording pass.
promotion_targets:
  - CLAUDE.md
  - AGENTS.md
  - docs/REPOSITORY-GOALS.md
  - docs/decisions.md
---

# Add Claude Skills

## Goal

Migrate repo-local Codex maintenance workflow skills to Claude Code by creating `.claude/skills/` and updating entrypoint docs so Claude can maintain this repository with the same capability as Cursor.

## Completed

- Created `.claude/skills/` with 9 skills: `brainstorming`, `git-commit`, `git-start-task`, `pr-handoff`, `pr-operator` (with `scripts/prctl`), `prompt-sync` (with `references/` and `assets/`), `repo-doc-simplifier`, `repo-self-iteration`, `migrate-codex-to-claude`
- Created `.claude/README.md` with scope and skill index
- Updated `CLAUDE.md` with skill references and repo maintenance rules
- Updated `AGENTS.md`, `docs/REPOSITORY-GOALS.md`, `docs/agent-iteration-contract.md`, `docs/decisions.md`

## Intentional Omissions

- `agents/openai.yaml` shells — Claude Code has no equivalent agent shell format
- `.cursor/rules/*.mdc` files — Claude does not use MDC format; rules expressed in `CLAUDE.md`
