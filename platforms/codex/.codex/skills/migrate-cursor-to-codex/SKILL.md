---
name: migrate-cursor-to-codex
description: Migrate `.cursor/rules`, `.cursor/skills`, and `.cursor/agents` into Codex-native instructions, skills, and multi-agent outputs with incremental dry-run planning and conflict detection.
---

# Migrate Cursor To Codex

Use this skill when the repository still treats `.cursor/**` as the canonical source for rules, skills, or agents and needs Codex-native targets.

## Defaults

- Source of truth: `.cursor/rules/**`, `.cursor/skills/**`, `.cursor/agents/**`
- Skill target root: `.codex/skills`
- Conflict policy: report-only when a target exists without migration ownership markers
- Deletion policy: generate cleanup proposals and mark manifest entries orphaned; do not delete targets automatically

## Workflow

1. Run `scripts/discover.py` to collect all source units and their normalized metadata.
2. Run `scripts/classify.py` to assign each unit a migration mode and target mapping.
3. Run `scripts/plan.py` against `.codex/migration/cursor-manifest.json` to compute `planned`, `conflict`, `noop`, and `orphan` outcomes.
4. Run `scripts/render.py --mode dry-run` to produce a Markdown report under `.codex/migration/reports/`.
5. Run `scripts/verify.py` to validate inventory integrity, conflict detection, semantic cleanup, manifest shape, and report completeness.
6. Only run `scripts/render.py --mode apply` after the dry-run report has been reviewed and unmanaged conflicts are accepted or cleared.
7. If only a conflict-free subset should be applied, limit apply scope with `--only-kind` or `--only-source-id`. A common first step is `--only-kind agent`.

## Stop Conditions

- Stop before a full apply if `AGENTS.md` already exists without `codex-migrate` ownership markers.
- Stop before a full apply if any target skill or agent file already exists without migration ownership markers.
- Stop before apply if the dry-run report shows semantic leakage of Cursor-only wording.
- Scoped apply is allowed only for selected planned actions whose targets are conflict-free.

## References

- For rule mappings, read `references/rules-mapping.md`.
- For skill mappings and ownership rules, read `references/skills-mapping.md`.
- For multi-agent conversion rules, read `references/agents-mapping.md`.

## Smoke Workflow

Run this non-mutating pipeline from the repository root:

```bash
python3 .codex/skills/migrate-cursor-to-codex/scripts/discover.py --repo-root . --output /tmp/cursor-discover.json
python3 .codex/skills/migrate-cursor-to-codex/scripts/classify.py --inventory /tmp/cursor-discover.json --output /tmp/cursor-classified.json
python3 .codex/skills/migrate-cursor-to-codex/scripts/plan.py --classified /tmp/cursor-classified.json --manifest .codex/migration/cursor-manifest.json --repo-root . --output /tmp/cursor-plan.json
python3 .codex/skills/migrate-cursor-to-codex/scripts/render.py --classified /tmp/cursor-classified.json --plan /tmp/cursor-plan.json --manifest .codex/migration/cursor-manifest.json --repo-root . --mode dry-run --report-file .codex/migration/reports/latest-dry-run.md
python3 .codex/skills/migrate-cursor-to-codex/scripts/verify.py --classified /tmp/cursor-classified.json --plan /tmp/cursor-plan.json --manifest .codex/migration/cursor-manifest.json --report-file .codex/migration/reports/latest-dry-run.md --repo-root .
```

Apply only planned agent actions:

```bash
python3 .codex/skills/migrate-cursor-to-codex/scripts/render.py --classified /tmp/cursor-classified.json --plan /tmp/cursor-plan.json --manifest .codex/migration/cursor-manifest.json --repo-root . --mode apply --only-kind agent
```
