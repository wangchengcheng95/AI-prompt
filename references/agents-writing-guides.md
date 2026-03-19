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

- Link: <https://docs.github.com/en/copilot/concepts/prompting/response-customization>
- Why it matters: official guidance on keeping agent instructions short, self-contained, and path-specific when needed
- Use it for: cross-tool compatibility checks, scope control, and avoiding instruction sprawl

### GitHub Blog

- Link: <https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/>
- Why it matters: high-signal public analysis of more than 2,500 `agents.md` files with practical guidance on what effective files actually contain
- Use it for: checking section choices, signal density, command placement, and common failure modes in real repositories

### ASDLC

- Link: <https://asdlc.io/practices/agents-md-spec/>
- Why it matters: strong guidance on signal density, falsifiable instructions, and keeping `AGENTS.md` minimal
- Use it for: reviewing drafts for overbreadth, duplicated rules, or instruction bloat

## Repository Usage Rule

When this repository creates or revises an `AGENTS.md` asset:

1. Review the links in this file first.
2. Then search for any newer or more authoritative public guidance before drafting. Prefer official product documentation and ecosystem-level references over opinionated blog posts.
3. If a newly found source is clearly higher-signal or more authoritative than the current list, update this file before relying on it in a draft.

After that, keep only the instructions that are:

- stable across repeated work
- actionable for an agent
- not already enforced better by tooling, code, or existing docs
