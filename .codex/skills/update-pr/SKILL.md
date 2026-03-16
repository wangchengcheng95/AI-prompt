---
name: update-pr
description: Update an existing GitHub pull request for a repo-local task branch through the repo wrapper script. Use when the user wants an already-open PR title or body adjusted without handling unrelated repository changes.
---
# Update PR

## Overview

Update an existing GitHub pull request for this repository through `scripts/prctl`.

Use this skill when the PR already exists and the user wants to change the title, body, or both without widening scope into broader implementation work.

## Preconditions

- the target PR number is known
- the intended title and/or body change is clear
- the change stays within normal PR metadata updates and does not require merge or reviewer-policy changes

## Workflow

1. Confirm the target PR number and the intended metadata change.
2. Derive or validate the PR title in Conventional Commits style when the title is being changed.
3. Prepare a body file if the PR body needs to be updated.
4. Run `scripts/prctl edit` with the needed arguments.
5. Run `scripts/prctl view` to confirm the resulting PR state.
6. Return the updated PR URL plus the final title and/or body used.

## PR Title Rules

- Format the PR title as `<type>(<optional-scope>): <short summary>` or `<type>: <short summary>`.
- Prefer `feat` for new repository capabilities, `fix` for bug fixes, and `docs` for documentation-only changes.
- Use other standard types such as `refactor`, `test`, `build`, `ci`, `perf`, `style`, or `chore` only when they better match the actual change.
- Use `!` only when the change introduces a real breaking contract or workflow change.
- Keep the summary short, concrete, and aligned with the actual diff or PR purpose.

## Environment Rules

- Prefer `scripts/prctl` over raw `gh` commands so approvals can be scoped to one stable entrypoint.
- Only update PR metadata that the user asked to change.
- If authentication, network access, or API compatibility blocks the update, surface the exact command result and the next manual step.
- Do not merge, close, reopen, approve, or otherwise change review state unless the user explicitly asks for that workflow.

## Suggested Command Shape

```bash
./scripts/prctl edit --pr <pr-number> --title "<pr-title>" --body-file <pr-body-file>
```

## Stop And Ask

Stop and ask the user before continuing when:

- the target PR is ambiguous or unknown
- the requested title or body change is unclear
- the request would modify reviewers, labels, milestones, or merge state rather than only title/body

## Output

Return:

- PR number
- PR URL
- final PR title if changed
- final PR body summary if changed
- exact blocking reason and next step if the update failed
