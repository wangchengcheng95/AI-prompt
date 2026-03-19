# Codex To Claude Migration Protocol

## Goal

Reduce migration-time judgment by turning the repo-local Codex-to-Claude move into a bounded protocol.

The protocol exists for this repository's maintenance entrypoints, not for archived downstream assets.

## Default Homes

- Source: root `.codex/`
- Target: root `.claude/`
- Shared governance docs: root `CLAUDE.md`, `docs/REPOSITORY-GOALS.md`, `docs/agent-iteration-contract.md`, `docs/decisions.md`
- Out of scope by default: `platforms/`, `templates/`, and unrelated repository content

## Mapping Rules

- Migrate repo-local skills one directory at a time.
- Carry each skill's `SKILL.md`, `scripts/`, `references/`, and `assets/` together when they are part of the same workflow.
- Do not migrate `agents/openai.yaml` shells; Claude has no equivalent agent shell format.
- Do not migrate `.cursor/rules/*.mdc` files; Claude rules belong in `CLAUDE.md` as Claude-specific additions.
- Migrate agent or subagent shells only when a real repo-local source asset exists.
- Preserve semantic parity. Do not create empty or fake target folders just to match the source layout.

## Common Failure Modes

- Boundary confusion: mixing root `.claude/` with archived assets under `platforms/claude/`.
- Partial migration: copying a skill file without its supporting script, reference, or asset.
- Path leakage: migrated Claude assets still point at `.codex/` or `.cursor/` locations.
- Narrative drift: root docs still describe Codex as the only real maintainer after Claude support lands.
- Shape chasing: inventing target agents or subagents that did not exist in the repo-local source.
- Rule format mismatch: trying to copy `.mdc` rule files into `.claude/` instead of expressing rules in `CLAUDE.md`.

## Verification Checklist

Run the smallest relevant checks for the scope you changed:

- Inventory the repo-local skill sets:
  `find .codex/skills .claude/skills -name 'SKILL.md'`
- Search the target paths you actually migrated for stale Codex or Cursor runtime references:
  `grep -rn "\.codex/\|\.cursor/" .claude/skills/`
- Check for whitespace and patch hygiene:
  `git diff --check`
- When scripts were migrated, verify permissions and path assumptions:
  `find .claude/skills -path '*/scripts/*' -type f`

Treat a hit as actionable only when it leaves a Claude-executed asset pointing at a Codex-local or Cursor-local runtime path. Ignore intentional references that describe source scope, repo boundaries, or the migration protocol itself.

## Output Expectations

Report these items in the handoff:

- source scope inspected
- target assets created or updated
- intentional non-migrations and why they were skipped
- verification run
- residual gaps, especially any missing real Claude runtime validation
