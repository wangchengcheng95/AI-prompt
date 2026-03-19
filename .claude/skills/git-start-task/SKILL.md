---
name: git-start-task
description: Start a new repo-local task from the latest main branch by checking worktree safety, switching to main, fast-forwarding from origin, and creating a focused task branch. Use when Claude is about to begin implementation or documentation work in this repository and needs a clean Git baseline.
---

# Git Start Task

## Overview

Start a new repository task from a clean and current `main` branch.

Use this skill to make the task branch setup repeatable and safe before editing files.

## Workflow

1. Inspect the current worktree with `git status --short`.
2. Stop if there are uncommitted changes that do not belong to the new task.
3. Switch to `main`.
4. Update `main` with `git pull --ff-only origin main`.
5. Create a focused branch name in short hyphen-case based on the task goal.
6. Create and switch to the new branch with `git checkout -b <branch-name>`.
7. Report the branch name and starting commit to the user before making substantial edits.

## Branch Naming

- Prefer short, descriptive names such as `add-git-task-skills` or `docs-agent-contract`
- Use lowercase letters and hyphens only
- Keep the name scoped to one task or one reviewable slice

## Stop And Ask

Stop and ask the user before continuing when:

- the worktree contains unrelated or unclear local changes
- `main` cannot be updated cleanly
- the task needs a branch name with project-specific tracking data that is not available
- switching branches would interfere with user-owned in-progress work

## Output

Return:

- the branch name
- the base commit hash
- any blocking Git constraint if the workflow could not be completed
