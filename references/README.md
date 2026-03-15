# External Reference Workspaces

This directory records which third-party repositories are useful comparative references for this repository and where to place their local checkouts.

The checked-out repositories under `references/external/` are intentionally gitignored. They are local study material only. They are not maintained assets of this repository, and they do not belong under `platforms/`.

## Layout

- `references/README.md`: versioned reference index and usage notes
- `references/repos.manifest.tsv`: machine-readable reference repository list for the sync script
- `references/external/`: local gitignored checkouts of third-party repositories

## Reference Repositories

### `everything-claude-code`

- Upstream: <https://github.com/affaan-m/everything-claude-code>
- Local checkout path: `references/external/everything-claude-code`
- Why it is tracked here: comparative reference for cross-tool AI engineering assets, especially Go backend `rules`, `agents`, and `skills`
- Current usage focus:
  - compare Go backend rule structure and enforcement detail
  - compare Go-focused agent roles such as reviewer and build resolver
  - compare skill coverage for Go patterns and testing workflows

## Sync Script

Sync all declared references:

```bash
bash scripts/sync-references.sh
```

Sync only one reference:

```bash
bash scripts/sync-references.sh --only everything-claude-code
```

The script reads `references/repos.manifest.tsv`, clones a repository if it is missing, and otherwise updates it with a fast-forward-only pull.

## Clone Or Update Manually

Clone if missing:

```bash
git clone https://github.com/affaan-m/everything-claude-code.git references/external/everything-claude-code
```

Update an existing checkout:

```bash
git -C references/external/everything-claude-code pull --ff-only origin main
```

## Notes

- This directory is designed for stable local placement across environments.
- Pulling this repository does not automatically clone or update the referenced upstream repositories.
- Use `scripts/sync-references.sh` when setting up a new environment or refreshing local reference checkouts.
- If later automation is desired, add an explicit wrapper or hook around the sync script rather than moving these checkouts into `platforms/`.
