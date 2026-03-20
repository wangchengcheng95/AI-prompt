---
name: pr-handoff
description: Push a repo-local task branch and prepare a ready-to-review pull request handoff, including title, summary, verification notes, risks, and the PR link or creation path. Use when Codex has finished work on a task branch and needs to hand the result to the user without performing the final merge.
---
# PR Handoff

## Overview

Turn a completed task branch into a review-ready handoff for the user.

Use this skill after implementation and verification are done and the branch is ready to be pushed and presented as a pull request candidate.

Hand actual PR push, create, view, and edit operations to `$pr-operator`.

## Workflow

1. Confirm the current branch is the intended task branch, not `main`.
2. Review `git status --short` and stop if required task changes are still unstaged or uncommitted.
3. Capture the branch name and current commit hash.
4. Push the branch with upstream tracking if it is not already on the remote, preferably through `$pr-operator`.
5. Check the branch with `$pr-operator find-head` before creating a PR.
6. If an open PR already exists for the branch, reuse it and only edit metadata when needed.
7. If no open PR exists, prepare a concise PR title and body based on the actual change, using a Conventional Commits style title.
8. Create the PR if the environment supports it.
9. If automatic PR creation is unavailable, return a PR link or creation path plus the prepared title and body.

## PR Title Rules

- Format the PR title as `<type>(<optional-scope>): <short summary>` or `<type>: <short summary>`.
- Prefer `feat` for new repository capabilities, `fix` for bug fixes, and `docs` for documentation-only changes.
- Use other standard types such as `refactor`, `test`, `build`, `ci`, `perf`, `style`, or `chore` only when they better match the actual change.
- Use `!` only when the change introduces a real breaking contract or workflow change.
- Keep the summary short, concrete, and aligned with the actual diff.

## Handoff Content

Include:

- branch name
- commit hash
- PR title
- PR summary of what changed
- verification performed and outcome
- assumptions, known risks, and any manual follow-up
- PR URL, compare URL, or explicit blocking reason

## Environment Rules

- Prefer creating the PR directly when the required tooling and authentication are available.
- Prefer using `$pr-operator find-head` before `create` so reruns stay idempotent.
- Prefer delegating actual PR operations to `$pr-operator`.
- Do not block handoff on missing `gh` or similar tooling if a branch can still be pushed.
- If push or PR creation fails, surface the exact command result and the next manual step.
- Do not merge the PR unless the user explicitly asks for that workflow.

## Stop And Ask

Stop and ask the user before continuing when:

- the branch contains unrelated commits or mixed-scope changes
- the branch is not ready for review because required verification is still missing
- pushing would expose work the user has not approved to send to the remote
- the repository remote or destination PR target is unclear
