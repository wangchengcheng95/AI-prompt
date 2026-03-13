# Rules Mapping

This migration keeps `.cursor/rules/*.mdc` as the source of truth and renders their Codex-native form into `AGENTS.md`.

## Fixed mappings

- `00-overview.mdc` maps to a managed `Overview` section in `AGENTS.md`.
- `ai-boundary.mdc` maps to a managed `AI Scope and Boundaries` section in `AGENTS.md`.
- `architecture.mdc` maps to a managed `Project Architecture` section in `AGENTS.md`.
- `engineering-doctrine.mdc` maps to a managed `Engineering Doctrine` section in `AGENTS.md`.
- `go-backend.mdc` maps to a managed `Go Backend Engineering` section in `AGENTS.md`.
- `memory-management.mdc` maps to a managed `Memory Management` section in `AGENTS.md`.
- `testing.mdc` maps to a managed `Testing` section in `AGENTS.md`.
- `design-docs.mdc` maps to a managed `Design and Spec Document Constraints` section in `AGENTS.md`.
- `english-prompt.mdc` maps to a managed `English Prompt Enforcement` section in `AGENTS.md`.
- `plan-mode-todos.mdc` maps to a managed `Planning` section in `AGENTS.md`.

## Normalization rules

- The migration removes Cursor-only phrasing from rendered output.
- `Plan Mode` is rewritten to `Planning`.
- `.cursor/plans/*.plan.md` is rewritten to `implementation plans`.
- Existing Markdown headings below the top-level title are shifted down by one level when rendered into `AGENTS.md`.

## Ownership

- Every managed rule section is wrapped with `<!-- codex-migrate:start:<section_key> -->` and `<!-- codex-migrate:end:<section_key> -->`.
- If `AGENTS.md` exists without any migration markers, the migration plan reports a conflict and apply mode must not modify the file.
