# Prompt-sync operator advisory (manifest-driven)

## Context

`scripts/prompt_sync.py` printed a hardcoded stderr notice naming Cursor and Superpowers after every successful CLI invocation. That implied prompt-sync is Cursor-specific, which conflicts with multi-platform `platforms/` and Codex-first bundles in `sync-manifest.yaml`.

## Goals

- Keep a **concise, visible** stderr reminder that optional tooling may be required; **do not** install anything from the sync script.
- Make copy **configuration-driven** via `sync-manifest.yaml`, not Python literals.
- Stay **platform-neutral** in tone: default text must not read as “this repo is only for Cursor.”

## Non-goals

- Auto-detect or auto-install extensions.
- i18n beyond what maintainers put in YAML.

## Design

### Manifest schema

- **Root (optional):** `default_operator_advisories` — list of non-empty strings. Each string is one line of operator-facing text (no automatic wrapping).
- **Per-bundle (optional):** under a bundle key, `operator_advisories` — same shape. When a CLI run resolves a `bundle_name`, the script prints **default lines first**, then **bundle lines** (order preserved; duplicates not deduplicated in v1).

If both are absent or all entries are empty/invalid after strip, **print nothing** (aside from `PROMPT_SYNC_SKIP_PLUGIN_ADVISORY` handling below).

Invalid entries (non-strings) are skipped; malformed lists are treated as empty for that scope.

### Runtime

- After `print(format_result(result))`, compute lines from `service.operator_advisory_lines(result.bundle_name)` and print a fixed-width ASCII border box to **stderr**.
- **`PROMPT_SYNC_SKIP_PLUGIN_ADVISORY`:** if set to any non-empty value, suppress the entire box (tests/CI).

### Import commands

- Use `OperationResult.bundle_name` the same way as export (already populated when the path is managed).

### Repository manifest

- Add `default_operator_advisories` to the real `sync-manifest.yaml` with neutral Chinese copy plus a pointer to `references/README.md`, and an **example** line that mentions Cursor/Superpowers without presenting it as the only tool.

### Documentation

- Update `prompt-sync` skills (`SKILL.md`, `references/workflow.md`) in `.cursor`, `.claude`, and `.codex` to describe manifest-driven advisories and the skip env var.

## Risks

- Operators who never read YAML may be surprised that text moved; skills and workflow reference mitigate this.
- Long lines in YAML may wrap in editors; keep strings short.

## Approval

User approved this design and committing on `main` (2026-03-21).
