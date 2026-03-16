# AGENTS.md Writing Guidance Links

This file records high-signal references for writing or revising `AGENTS.md` assets in this repository.

Keep this list short. Prefer official guidance and ecosystem-level references over opinionated blog posts.

## Primary References

### OpenAI Codex

- Link: <https://developers.openai.com/codex/guides/agents-md>
- Why it matters: official Codex behavior for discovering and applying `AGENTS.md`
- Use it for: scope, precedence, file placement, and Codex-specific semantics

### AGENTS.md

- Link: <https://agents.md/>
- Why it matters: ecosystem-level format and usage guidance across multiple coding agents
- Use it for: deciding what belongs in `AGENTS.md`, common section choices, and nested-file strategy

### GitHub Copilot

- Link: <https://docs.github.com/en/copilot/how-tos/copilot-cli/add-custom-instructions>
- Why it matters: evidence that `AGENTS.md` is used beyond Codex and how another major agent platform treats it
- Use it for: cross-tool compatibility checks and repository instruction expectations

### ASDLC

- Link: <https://asdlc.io/practices/agents-md-spec/>
- Why it matters: strong guidance on signal density, falsifiable instructions, and keeping `AGENTS.md` minimal
- Use it for: reviewing drafts for overbreadth, duplicated rules, or instruction bloat

## Repository Usage Rule

When this repository creates or revises an `AGENTS.md` asset, review these links first and keep only the instructions that are:

- stable across repeated work
- actionable for an agent
- not already enforced better by tooling, code, or existing docs
