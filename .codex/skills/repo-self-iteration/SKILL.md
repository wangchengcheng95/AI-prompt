---
name: repo-self-iteration
description: Intake a repo-local maintenance goal and drive it toward ready-to-merge by applying the repository collaboration contract, choosing accept/shrink/stop, then using git-start-task, git-commit, and pr-handoff at the right points. Use when Codex receives a concrete repository task and should run the default self-iteration loop instead of only giving advice.
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
4. Run the most relevant verification available.
5. Summarize the acceptance status, assumptions, and residual risks.
6. Use `$git-commit` to create a focused commit.
7. Use `$pr-handoff` to push the branch and prepare the pull request handoff.

## Interaction Budget

- Default to no more than three user interactions for one task.
- Spend those interactions only on decisions that materially change scope, risk, or permissions.
- Otherwise, continue with reasonable assumptions and surface them in the handoff.

## Skill Routing

- Use `$git-start-task` for switching to `main`, updating it, and creating the task branch.
- Use `$git-commit` for commit message formation and the commit itself.
- Use `$pr-handoff` for push, PR text, and review-ready delivery.
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
