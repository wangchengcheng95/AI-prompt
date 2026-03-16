# Prompt Sync Workflow Reference

## Supported Bundles

- `codex-home`: exports `platforms/codex/home/AGENTS.md` into `AGENTS.md` at a Codex workspace root.
- `codex-platform-core`: exports `platforms/codex/AGENTS.md` and `platforms/codex/.codex/**` into a project repository's native `AGENTS.md` and `.codex/**` paths.

## Local Configuration

- `sync-manifest.yaml` is the authoritative bundle and path mapping.
- Copy `.codex/skills/prompt-sync/assets/sync-targets.local.yaml.example` to `sync-targets.local.yaml` before first use.
- `sync-targets.local.yaml` is machine-local and resolves target aliases to absolute local filesystem paths.
- Each target stores provenance in `.ai-prompt-sync/state.yaml`.

## Operational Rules

- Always preview before writing.
- Stop on `drift-local`, `conflict`, `unmanaged`, or `missing-target`.
- Only backflow paths that are already managed by the manifest, unless the user first updates the manifest.
- Use `--dest` only when the user explicitly wants to override the default upstream landing path for this run.

## Scenario Mapping

- New work environment: preview and export `codex-home` to a `workspace` target.
- New project repository: preview and export `codex-platform-core` to a `repo` target.
- Backflow from a project repository: preview-import the specific managed file or directory, then import-backflow if the preview is safe.
