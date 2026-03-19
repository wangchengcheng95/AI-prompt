---
name: repo-self-iteration
description: Intake a repo-local maintenance goal and drive it toward ready-to-merge by applying the repository collaboration contract, choosing accept, shrink, or stop, then using git-start-task, git-commit, repo-doc-simplifier, pr-handoff, and pr-operator at the right points. Use when Cursor receives a concrete repository task and should run the default self-iteration loop instead of only giving advice.
---

# Repo Self Iteration

## Overview

Use this as the repo-local entry skill for goal-driven work in this repository.

It decides whether the task should proceed now, be shrunk, or stop for user input, then routes execution through the existing Git skills rather than re-explaining those steps from scratch.

## Intake Gate

Classify the goal before editing anything:

- `accept` when the task is clear, bounded, and can credibly reach ready-to-merge in one pass
- `shrink` when the goal is valid but too large or too ambiguous for one bounded task
- `stop` when required information, ownership, permissions, or risk must be resolved by the user

Prefer the smallest useful slice that can still be reviewed as a normal pull request candidate.

## Default Loop

When the task is `accept` or `shrink`, follow this order:

1. Use `$git-start-task` to start from updated `main` and create the task branch.
2. Form a concise executable plan based on the accepted task slice.
3. Implement the repository change.
4. If the task changed a repo-maintenance Markdown file in the repository root or `docs/`, use `$repo-doc-simplifier` when the updated document has become longer, more repetitive, or otherwise needs compression.
5. Run the most relevant verification available.
6. Summarize the acceptance status, assumptions, and residual risks.
7. Use `$git-commit` to create a focused commit.
8. Use `$pr-handoff` to prepare the pull request handoff, and let `$pr-operator` perform the actual PR operations when needed.

## Interaction Budget

- Default to no more than three user interactions for one task.
- Spend those interactions only on decisions that materially change scope, risk, or permissions.
- Otherwise, continue with reasonable assumptions and surface them in the handoff.

## Skill Routing

- Use `$git-start-task` for switching to `main`, updating it, and creating the task branch.
- Use `$git-commit` for commit message formation and the commit itself.
- Use `$repo-doc-simplifier` as a conditional cleanup step for repo-maintenance Markdown in the repository root or `docs/`, not for every Markdown file.
- Use `$pr-handoff` for PR text and review-ready delivery.
- Use `$pr-operator` for actual PR push, create, view, and edit operations when the handoff needs them.
- Do not duplicate the detailed Git procedures from those skills here unless a gap is discovered.

## Stop And Ask

Stop and ask the user when:

- the goal cannot be reduced to a reviewable slice
- the task needs repository-boundary or ownership decisions
- destructive changes or unclear user-authored material are involved
- branch, verification, commit, or push steps are blocked by tooling or permissions

## Output

Return a ready-to-merge handoff that includes:

- the task classification and scope used
- the branch name
- the plan actually followed
- verification and outcome
- commit identifier
- PR title and summary
- risks, assumptions, and any remaining manual steps
