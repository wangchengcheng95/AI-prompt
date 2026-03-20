# Progressive Disclosure Template

This template provides a ready-to-copy progressive disclosure rule for AI coding tools.

Progressive disclosure organizes documentation in layers so agents load only what is needed for the current task, instead of loading all context upfront.

## Layer Model

| Layer | Content | Load timing |
|---|---|---|
| Layer 1 | Root entry files: AGENTS.md, CLAUDE.md, README.md, overview rules | Always-on |
| Layer 2 | Task contracts, skill files, workflow docs | When executing a specific task |
| Layer 3 | Goals, architecture, decisions, other docs/ files | On demand |

Layer 1 files should contain only: mission, non-negotiable constraints, and routing links to layer 2/3. No background knowledge.

## Files

- `cursor-rule.mdc` — Cursor rule, copy to `.cursor/rules/progressive-disclosure.mdc` in the target repository

## Codex / Claude (AGENTS.md)

Add the following rule to the Working Rules section of the target repository's `AGENTS.md`:

```
- Doc layering: layer 1 (always-on) = root entry files, stay minimal, no background knowledge; layer 2 (task-time) = task contracts + skill files; layer 3 (reference) = docs/ files. Do not promote layer 3 content into layer 1.
```

## References

- <https://emsenn.net/technology/disciplines/computing/software/claude-code/concepts/progressive-disclosure>
- <https://greeto.me/blog/claude-md-progressive-disclosure-for-fast-teams>
- <https://understandingdata.com/posts/progressive-disclosure-context/>
- <https://micheallanham.substack.com/p/agent-skills-the-architectural-shift>
- <https://www.aihero.dev/a-complete-guide-to-agents-md>
