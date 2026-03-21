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

### `claude-code`

- Upstream: <https://github.com/anthropics/claude-code>
- Local checkout path: `references/external/claude-code`
- Why it is tracked here: official upstream for the Claude Code agent product; useful baseline when comparing community mirrors, templates, and this repository's maintained outputs under `platforms/claude/`
- Current usage focus:
  - compare upstream-recommended skills, hooks, and packaging conventions against archived or adapted assets in this repository
  - study release-facing defaults and documentation without treating the checkout as a maintained or distributable copy of Claude Code itself
  - extract stable integration ideas while keeping `references/external/` as read-only local study material

### `claude-plugins-official`

- Upstream: <https://github.com/anthropics/claude-plugins-official>
- Local checkout path: `references/external/claude-plugins-official`
- Why it is tracked here: official Anthropic catalog of Claude Code plugins; baseline for marketplace layout, plugin metadata, and bundled skills versus third-party marketplaces and this repository's maintained outputs under `platforms/claude/`
- Current usage focus:
  - compare official plugin packaging and discovery patterns before adapting repo-owned platform assets
  - study how upstream groups skills, hooks, and docs inside plugin-shaped bundles
  - extract stable conventions without treating the checkout as redistributable marketplace content

### `anthropic-skills`

- Upstream: <https://github.com/anthropics/skills>
- Local checkout path: `references/external/anthropic-skills` (manifest name disambiguates this repository's own skill trees under `.cursor/skills/` and similar)
- Why it is tracked here: official Anthropic reference collection for Agent Skills documentation and examples; complements `claude-code` and `claude-plugins-official` when aligning maintained outputs under `platforms/claude/`
- Current usage focus:
  - compare upstream skill authoring patterns, front matter conventions, and worked examples
  - study how official samples structure `SKILL.md` and supporting material before adapting ideas locally
  - extract stable conventions without treating the checkout as a maintained asset of this repository

### `gstack`

- Upstream: <https://github.com/garrytan/gstack>
- Local checkout path: `references/external/gstack`
- Why it is tracked here: comparative reference for Claude Code skill packaging, role-oriented workflows, and review or QA command design that may inform maintained outputs under `platforms/`
- Current usage focus:
  - compare repo-distributed skill layouts and setup patterns for local tool installation
  - study role-based slash-command workflows for planning, review, QA, and release handoff
  - extract reusable ideas about orchestration and guardrails without treating the upstream checkout as a maintained asset

### `planning-with-files`

- Upstream: <https://github.com/OthmanAdi/planning-with-files>
- Local checkout path: `references/external/planning-with-files`
- Why it is tracked here: comparative reference for filesystem-backed planning (markdown task plans, hooks, multi-IDE Agent Skills packaging) that may inform maintained outputs under `platforms/`
- Current usage focus:
  - study the three-file planning pattern and hook-driven re-read / completion checks across Claude Code, Cursor, Codex, and related tool layouts
  - compare skill and plugin packaging without treating the upstream checkout as a maintained asset

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

```bash
bash scripts/sync-references.sh --only planning-with-files
```

```bash
bash scripts/sync-references.sh --only claude-code
```

```bash
bash scripts/sync-references.sh --only claude-plugins-official
```

```bash
bash scripts/sync-references.sh --only anthropic-skills
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
git clone https://github.com/OthmanAdi/planning-with-files.git references/external/planning-with-files
```

```bash
git clone https://github.com/obra/superpowers.git references/external/superpowers
```

```bash
git clone https://github.com/anthropics/claude-code.git references/external/claude-code
```

```bash
git clone https://github.com/anthropics/claude-plugins-official.git references/external/claude-plugins-official
```

```bash
git clone https://github.com/anthropics/skills.git references/external/anthropic-skills
```

Update an existing checkout:

```bash
git -C references/external/everything-claude-code pull --ff-only origin main
```

```bash
git -C references/external/gstack pull --ff-only origin main
```

```bash
git -C references/external/planning-with-files pull --ff-only origin master
```

```bash
git -C references/external/superpowers pull --ff-only origin main
```

```bash
git -C references/external/claude-code pull --ff-only origin main
```

```bash
git -C references/external/claude-plugins-official pull --ff-only origin main
```

```bash
git -C references/external/anthropic-skills pull --ff-only origin main
```

## Notes

- This directory is designed for stable local placement across environments.
- Pulling this repository does not automatically clone or update the referenced upstream repositories.
- Use `scripts/sync-references.sh` when setting up a new environment or refreshing local reference checkouts.
- If later automation is desired, add an explicit wrapper or hook around the sync script rather than moving these checkouts into `platforms/`.
- When using a checkout under `references/external/`, prefer summarizing reusable ideas into maintained `platforms/` assets rather than treating the checkout itself as distributable repository content.
