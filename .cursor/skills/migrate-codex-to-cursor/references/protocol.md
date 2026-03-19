# Codex To Cursor Migration Protocol

## Goal

Reduce migration-time judgment by turning the repo-local Codex-to-Cursor move into a bounded protocol.

The protocol exists for this repository's maintenance entrypoints, not for archived downstream assets.

## Default Homes

- Source: root `.codex/`
- Target: root `.cursor/`
- Shared governance docs: root `.cursor/README.md`, `docs/REPOSITORY-GOALS.md`, `docs/agent-iteration-contract.md`, `docs/decisions.md`
- Out of scope by default: `platforms/`, `templates/`, and unrelated repository content

## Mapping Rules

- Migrate repo-local skills one directory at a time.
- Carry each skill's `SKILL.md`, `scripts/`, `references/`, and `assets/` together when they are part of the same workflow.
- Migrate rules only when they are required for Cursor-side repo maintenance behavior.
- Migrate agent or subagent shells only when a real repo-local source asset exists.
- Preserve semantic parity. Do not create empty or fake target folders just to match the source layout.

## Common Failure Modes

- Boundary confusion: mixing root `.cursor/` with archived assets under `platforms/cursor/.cursor/`.
- Partial migration: copying a skill file without its supporting script, reference, or asset.
- Path leakage: migrated Cursor assets still point at `.codex/` locations.
- Narrative drift: root docs still describe Codex as the only real maintainer after Cursor support lands.
- Shape chasing: inventing target agents or subagents that did not exist in the repo-local source.

## Verification Checklist

Run the smallest relevant checks for the scope you changed:

- Inventory the repo-local skill sets:
  `rg --files .codex/skills .cursor/skills`
- Search the target paths you actually migrated for stale Codex runtime references:
  `rg -n "\.codex/" <target-paths-you-migrated>`
- Check for whitespace and patch hygiene:
  `git diff --check`
- When scripts were migrated, verify permissions and path assumptions:
  `find .cursor/skills -path '*/scripts/*' -type f -maxdepth 4`

Treat a hit as actionable only when it leaves a Cursor-executed asset pointing at a Codex-local runtime path. Ignore intentional references that describe source scope, repo boundaries, or the migration protocol itself.

Add a real Cursor-side smoke test when the environment allows it. Repository-only checks are not a substitute for runtime trigger validation.

## Output Expectations

Report these items in the handoff:

- source scope inspected
- target assets created or updated
- intentional non-migrations and why they were skipped
- verification run
- residual gaps, especially any missing real Cursor runtime validation
