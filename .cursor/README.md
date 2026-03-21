# Cursor Repository Entry

This `.cursor/` directory exists only to help maintain this repository.

Archived external Cursor assets live under `platforms/cursor/.cursor/`.

## Skills in this workspace (no separate install)

For **this repository**, repo-local Agent skills live under `.cursor/skills/`. Cursor picks them up when **this repository root** is the opened workspace folder. There is no marketplace or global install step for these files.

**Checklist**

1. **File** → **Open Folder** (or add folder) → choose **this repository’s root directory** (the folder that contains `AGENTS.md` and `.cursor/`), not a parent directory that only contains it as a subfolder.
2. Use **Cursor Agent** in a context that includes this workspace; skills are defined by each `SKILL.md` (name and description in the YAML front matter).

**Repo-local skills (current)**

| Directory | Purpose |
|-----------|---------|
| `skills/brainstorming/` | Creative or behavioral work before implementation |
| `skills/git-start-task/` | Clean task branch from updated `main` |
| `skills/git-commit/` | Focused commits with English subjects |
| `skills/migrate-codex-to-cursor/` | Codex → root `.cursor/` migration |
| `skills/prompt-sync/` | Manifest-driven sync with external workspaces |
| `skills/repo-doc-simplifier/` | Shorten maintenance Markdown safely |
| `skills/repo-self-iteration/` | Default maintenance loop for concrete repo tasks |
| `skills/pr-handoff/` | Push branch and PR handoff notes |
| `skills/pr-operator/` | PR create/update via bundled script |

Task-time loop and stop conditions: `docs/agent-iteration-contract.md`.

**Not in this directory**

- Distributable or template Cursor bundles for *other* repositories → `platforms/cursor/.cursor/`. Copy from there when seeding another project; do not treat that tree as the live entrypoint for maintaining this repo.

## Scope

- repo-maintenance rules for this repository
- repo-local workflow skills for maintaining this repository in Cursor
- optional repo-local agent or sub-agent shells only when a future task proves they are worth the maintenance surface
- no distributable external Cursor assets
- English-first governance and maintenance documentation
