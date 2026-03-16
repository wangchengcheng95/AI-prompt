---
name: pr-operator
description: Manage repo-local GitHub pull request operations with a bundled wrapper script. Use when Codex needs to push a task branch for PR work, create a pull request, view an existing pull request, or update a pull request title or body.
---
# PR Operator

## Overview

Own the actual GitHub pull request operations for this repository through the bundled wrapper `scripts/prctl`.

Use this skill when the user wants a PR created, viewed, or edited, or when a task branch needs to be pushed as part of PR work.

This skill complements `$pr-handoff`.

- `$pr-handoff` owns the review-ready handoff and PR text preparation.
- `$pr-operator` owns the deterministic push and GitHub mutation steps.

## Bundled Script

- Use `scripts/prctl` relative to this skill folder.
- From the repository root, invoke it as `./.codex/skills/pr-operator/scripts/prctl`.

## Preconditions

- the current branch and base branch are known for create or push operations
- required task changes are committed before push or create
- the target PR number is known for view or edit operations
- the intended PR title and body are already prepared or can be derived from the actual change

## Workflow

1. Confirm whether the task is `push`, `create`, `view`, or `edit`.
2. Validate the required inputs for that operation.
3. Use the bundled `scripts/prctl` command instead of raw `gh` or ad hoc shell snippets.
4. For create or edit, validate the PR title in Conventional Commits style.
5. Return the resulting PR URL or the exact blocking failure plus the next manual step.

## Operations

### Push

- Use when the branch needs upstream tracking before PR work.
- Run `./.codex/skills/pr-operator/scripts/prctl push --branch <branch-name>`.

### Create

- Check for an existing PR for the branch first with `find-head`.
- Then create the PR with explicit base branch, head branch, title, and body file.

### View

- Use to confirm PR number, title, state, URL, base branch, or head branch.

### Edit

- Use to update only the PR title, body, or both.
- Prefer this path over raw `gh pr edit` because the wrapper uses the lower-level API path that avoids older CLI compatibility issues.

## PR Title Rules

- Format the PR title as `<type>(<optional-scope>): <short summary>` or `<type>: <short summary>`.
- Prefer `feat` for new repository capabilities, `fix` for bug fixes, and `docs` for documentation-only changes.
- Use other standard types such as `refactor`, `test`, `build`, `ci`, `perf`, `style`, or `chore` only when they better match the actual change.
- Use `!` only when the change introduces a real breaking contract or workflow change.
- Keep the summary short, concrete, and aligned with the actual diff or PR purpose.

## Suggested Command Shapes

```bash
PRCTL="./.codex/skills/pr-operator/scripts/prctl"
"${PRCTL}" push --branch <branch-name>
"${PRCTL}" find-head --head <branch-name>
"${PRCTL}" create --base <base-branch> --head <branch-name> --title "<pr-title>" --body-file <pr-body-file>
"${PRCTL}" edit --pr <pr-number> --title "<pr-title>" --body-file <pr-body-file>
"${PRCTL}" view --pr <pr-number>
```

## Environment Rules

- Prefer this bundled wrapper over repo-root scripts or raw `gh` commands so the workflow stays migratable with the skill.
- Only mutate the PR fields the user asked to change.
- If authentication, network access, or API compatibility blocks the operation, surface the exact command result and the next manual step.
- Do not merge, close, reopen, approve, or otherwise change review state unless the user explicitly asks for that workflow.

## Stop And Ask

Stop and ask the user before continuing when:

- the target branch, base branch, or PR number is unclear
- required verification is still missing before opening the PR
- the requested change would modify reviewers, labels, milestones, draft state, or merge state rather than only the normal PR metadata this skill owns

## Output

Return:

- operation performed
- branch name or PR number, as applicable
- PR URL if available
- final PR title if used or changed
- final PR body summary if used or changed
- exact blocking reason and next step if the operation failed
