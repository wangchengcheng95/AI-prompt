# External Reference Workspaces

This directory records which third-party repositories are useful comparative references for this repository and where to place their local checkouts.

The checked-out repositories under `references/external/` are intentionally gitignored. They are local study material only. They are not maintained assets of this repository, and they do not belong under `platforms/`.

The current intent of this area is to support comparative study while building or revising maintained assets under `platforms/`. In practice, that means reviewing useful third-party skills, hooks, sub-agents, and adjacent configuration patterns, then selectively adapting the underlying ideas into this repository's own platform outputs.

## Layout

- `references/README.md`: versioned reference index and usage notes
- `references/agents-writing-guides.md`: guidance links for writing or revising `AGENTS.md` assets
- `references/repos.manifest.tsv`: machine-readable reference repository list for the sync script
- `references/external/`: local gitignored checkouts of third-party repositories
- `references/external/README.md`: path-local guidance for agents reading the external checkouts

## Reference Repositories

### `everything-claude-code`

- Upstream: <https://github.com/affaan-m/everything-claude-code>
- Local checkout path: `references/external/everything-claude-code`
- Why it is tracked here: comparative reference for cross-tool AI engineering assets that can inform maintained outputs under `platforms/`
- Current usage focus:
  - compare third-party skill, hook, and sub-agent patterns before adapting repo-owned platform assets
  - compare platform-native packaging and layout choices that may translate well into `platforms/`
  - extract stable ideas and workflows rather than copying upstream assets wholesale

### `gstack`

- Upstream: <https://github.com/garrytan/gstack>
- Local checkout path: `references/external/gstack`
- Why it is tracked here: comparative reference for Claude Code skill packaging, role-oriented workflows, and review or QA command design that may inform maintained outputs under `platforms/`
- Current usage focus:
  - compare repo-distributed skill layouts and setup patterns for local tool installation
  - study role-based slash-command workflows for planning, review, QA, and release handoff
  - extract reusable ideas about orchestration and guardrails without treating the upstream checkout as a maintained asset

### `superpowers`

- Upstream: <https://github.com/obra/superpowers>
- Local checkout path: `references/external/superpowers`
- Why it is tracked here: comparative reference for Claude Code skill conventions, composable workflows, and plugin-style capabilities that may inform maintained outputs under `platforms/`
- Current usage focus:
  - compare skill naming, invocation patterns, and cross-skill composition
  - study workflow-oriented skills (planning, git worktrees, execution discipline) before adapting ideas locally
  - extract reusable patterns without treating the upstream checkout as a maintained asset

## Official Documentation Links

### AGENTS.md Writing Guidance

- Link index: `references/agents-writing-guides.md`
- Why it is tracked here: stable reference set for writing or reviewing `AGENTS.md` assets across platforms

## Sync Script

Sync all declared references:

```bash
bash scripts/sync-references.sh
```

Sync only one reference:

```bash
bash scripts/sync-references.sh --only everything-claude-code
```

```bash
bash scripts/sync-references.sh --only gstack
```

```bash
bash scripts/sync-references.sh --only superpowers
```

The script reads `references/repos.manifest.tsv`, clones a repository if it is missing, and otherwise updates it with a fast-forward-only pull.

## Clone Or Update Manually

Clone if missing:

```bash
git clone https://github.com/affaan-m/everything-claude-code.git references/external/everything-claude-code
```

```bash
git clone https://github.com/garrytan/gstack.git references/external/gstack
```

```bash
git clone https://github.com/obra/superpowers.git references/external/superpowers
```

Update an existing checkout:

```bash
git -C references/external/everything-claude-code pull --ff-only origin main
```

```bash
git -C references/external/gstack pull --ff-only origin main
```

```bash
git -C references/external/superpowers pull --ff-only origin main
```

## Notes

- This directory is designed for stable local placement across environments.
- Pulling this repository does not automatically clone or update the referenced upstream repositories.
- Use `scripts/sync-references.sh` when setting up a new environment or refreshing local reference checkouts.
- If later automation is desired, add an explicit wrapper or hook around the sync script rather than moving these checkouts into `platforms/`.
- When using a checkout under `references/external/`, prefer summarizing reusable ideas into maintained `platforms/` assets rather than treating the checkout itself as distributable repository content.
