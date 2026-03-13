# Skills Mapping

This migration copies Cursor skills into the configured Codex skill root, which defaults to `.codex/skills`.

## Fixed mappings

- `.cursor/skills/<name>/SKILL.md` maps to `<skill_target_root>/<name>/SKILL.md`.
- The target `SKILL.md` preserves the original body and rewrites the frontmatter to contain only `name` and `description`.
- Ownership is recorded inside the generated `SKILL.md` with `<!-- codex-migrate:owned source=... -->`.

## Transformation rules

- A skill is classified as `direct` by default.
- A skill is classified as `transform` when it is large enough to require splitting into `references/` or `scripts/`.
- Existing unmanaged target skills are never overwritten automatically.

## Conflict handling

- If `<skill_target_root>/<name>/SKILL.md` already exists and lacks the ownership marker for the same source path, the plan must report a conflict.
- Apply mode may update only skill files that it created or that already contain the matching ownership marker.
