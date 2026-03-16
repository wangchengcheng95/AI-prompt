---
name: create-pr
description: Create an actual GitHub pull request for a repo-local task branch using gh when the branch is ready for review. Use when the user explicitly wants the PR created rather than only prepared for handoff.
---
# Create PR

## Overview

Create an actual GitHub pull request for a repo-local task branch with `gh`.

Use this skill after implementation, verification, commit creation, and branch push are done, or after `$pr-handoff` has already prepared the review-ready title and summary.

This skill complements `$pr-handoff`.

- `$pr-handoff` owns the review-ready handoff.
- `$create-pr` owns the final `gh pr create` step when the environment supports it.

## Preconditions

- the current branch is the intended task branch, not `main`
- required task changes are committed
- the branch is pushed or can be pushed safely
- the base branch and destination remote are known
- a concise PR title and body can be reused from prior handoff or derived from the actual diff

## Workflow

1. Confirm the current branch, remote, and base branch target.
2. Review `git status --short` and stop if required changes are still unstaged or uncommitted.
3. Ensure the branch exists on the remote and push with upstream tracking if needed.
4. Verify `gh` is installed and authenticated for the target host.
5. Reuse an existing PR title and body when available; otherwise derive them from the actual change and format the title in Conventional Commits style.
6. Create the PR with `gh pr create`, preferring explicit `--base`, `--head`, `--title`, and `--body` arguments.
7. Return the PR URL plus the exact title and body used.
8. If PR creation is blocked, return the exact failure, the prepared title and body, and a manual creation path such as a compare URL.

## PR Title Rules

- Format the PR title as `<type>(<optional-scope>): <short summary>` or `<type>: <short summary>`.
- Prefer `feat` for new repository capabilities, `fix` for bug fixes, and `docs` for documentation-only changes.
- Use other standard types such as `refactor`, `test`, `build`, `ci`, `perf`, `style`, or `chore` only when they better match the actual change.
- Use `!` only when the change introduces a real breaking contract or workflow change.
- Keep the summary short, concrete, and aligned with the actual diff.

## Environment Rules

- Prefer using already-prepared handoff text instead of inventing new framing.
- Prefer `gh` for PR creation and avoid browser-only steps when CLI creation works.
- If `gh` is missing, unauthenticated, or network-blocked, surface the exact command result and the next manual step.
- Do not merge the PR, auto-approve it, or modify branch protection settings.
- Do not guess reviewers, labels, milestones, or draft state unless the user explicitly asks for them or repository conventions make them unambiguous.

## Suggested Command Shape

```bash
gh pr create --base <base-branch> --head <branch-name> --title "<pr-title>" --body "<pr-body>"
```

## Stop And Ask

Stop and ask the user before continuing when:

- the base branch, destination remote, or PR target is unclear
- the branch contains unrelated commits or mixed-scope changes
- pushing would expose work the user has not approved to publish
- required verification is still missing
- PR creation requires repo-specific metadata the user must choose, such as reviewers, labels, milestones, or draft vs ready state

## Output

Return:

- branch name
- base branch
- commit hash
- PR title
- PR body or summary used
- verification status if known
- PR URL, compare URL, or explicit blocking reason
- the next manual step if automatic creation failed
