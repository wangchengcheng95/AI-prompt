---
task_id: learn-code-simplifier
title: Learn code-simplifier plugin (claude-plugins-official)
status: proposed
priority: high
kind: research
branch: null
issue: null
last_updated: 2026-03-22
next_step: "Ensure references/external/claude-plugins-official is synced (see references/README.md); read plugins/code-simplifier/.claude-plugin/plugin.json and plugins/code-simplifier/agents/code-simplifier.md; note one adoptable simplification rule and how it differs from repo Markdown simplification."
promotion_targets:
  - references/README.md
  - .cursor/skills/repo-doc-simplifier/SKILL.md
  - docs/
---

# Learn code-simplifier plugin (claude-plugins-official)

## Status

- State: proposed (owner learning track)
- Branch: none unless you change maintained skills or docs
- Last updated: 2026-03-22

## Original Goal

Understand Anthropic’s upstream **`code-simplifier`** plugin: how the agent is scoped, what “simplify” means there (clarity and maintainability without behavior change), and what is reusable versus project-specific—**primary source** is the local reference checkout under `references/external/claude-plugins-official/plugins/code-simplifier/`.

## Current Slice

- Sync or verify checkout: `references/external/claude-plugins-official` (manifest: `references/repos.manifest.tsv`; instructions: `references/README.md` § `claude-plugins-official`).
- Read: `plugins/code-simplifier/.claude-plugin/plugin.json` and `plugins/code-simplifier/agents/code-simplifier.md`.
- Contrast (optional): `.cursor/skills/repo-doc-simplifier/SKILL.md` for **Markdown** constraint-preserving compression versus **code** refinement in the upstream agent prompt.

## Current Status

- Task scope corrected to the official plugin path; no study notes logged here yet.

## Confirmed Findings

- Upstream layout (when synced): plugin metadata plus `agents/code-simplifier.md` (subagent/agent definition: preserve functionality, apply project standards from `CLAUDE.md`, focus on recently modified code unless told otherwise).
- This repository’s `repo-doc-simplifier` skill addresses **maintenance docs**, not the same artifact as the upstream **code** simplifier agent.

## Open Questions

- Which parts of the upstream prompt are portable into a repo-local skill or rule versus left as Claude Code runtime behavior only?

## Promotion Targets

- Durable integration ideas → `docs/decisions.md` or relevant `platforms/<tool>/` notes.
- Optional cross-link or contrast notes → `references/README.md` only if it helps future sync/study, not redundant catalog text.

## Next Session Entrypoint

1. Run or verify: `bash scripts/sync-references.sh --only claude-plugins-official` (when network and policy allow).
2. Open `references/external/claude-plugins-official/plugins/code-simplifier/agents/code-simplifier.md` and skim `plugin.json`.
3. Add one or two bullets under **Confirmed Findings** (concrete rules or boundaries you will reuse).
