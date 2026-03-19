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

### Progressive Disclosure

- Link: <https://emsenn.net/technology/disciplines/computing/software/claude-code/concepts/progressive-disclosure>
- Why it matters: concise explanation of the layered instruction model for agent root files
- Use it for: deciding what belongs in layer 1 vs layer 2 vs layer 3

- Link: <https://greeto.me/blog/claude-md-progressive-disclosure-for-fast-teams>
- Why it matters: practical four-layer breakdown for CLAUDE.md / AGENTS.md with length discipline guidance
- Use it for: reviewing whether the root file is routing correctly or accumulating rules it should delegate

- Link: <https://understandingdata.com/posts/progressive-disclosure-context/>
- Why it matters: token budget analysis and three-layer architecture with concrete implementation patterns
- Use it for: evaluating token cost of always-on vs task-time vs on-demand content

- Link: <https://micheallanham.substack.com/p/agent-skills-the-architectural-shift>
- Why it matters: industry-level framing of the shift from mega-prompts to progressive disclosure with skill directory structure
- Use it for: understanding the physical layout of skills and why metadata-only layer 1 matters

- Link: <https://www.aihero.dev/a-complete-guide-to-agents-md>
- Why it matters: opinionated but high-signal guide on what the root AGENTS.md file should and should not contain
- Use it for: checking whether rules in the root file are truly non-negotiable or should be routed elsewhere

## Repository Usage Rule

When this repository creates or revises an `AGENTS.md` asset:

1. Review the links in this file first.
2. Then search for any newer or more authoritative public guidance before drafting. Prefer official product documentation and ecosystem-level references over opinionated blog posts.
3. If a newly found source is clearly higher-signal or more authoritative than the current list, update this file before relying on it in a draft.

After that, keep only the instructions that are:

- stable across repeated work
- actionable for an agent
- not already enforced better by tooling, code, or existing docs
