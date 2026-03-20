---
name: git-commit
description: Git Create Commit
---

# Git Create Commit

## Overview

Create a short, focused commit message and commit staged changes.

In this repository, use English commit subjects for repo-local maintenance work.

## Steps

1. **Review changes**
    - Check `git diff --cached` and `git diff` when both staged and unstaged changes may exist
    - Understand what changed and why before adjusting the index
2. **Ask for issue key (optional)**
    - Check the branch name for an issue key (Linear, Jira, GitHub issue, etc.)
    - If an issue key (for example `TASK-123`, `ISSUE-456`, `#123`) is not already available in the chat or commit context, optionally ask the user if they want to include one
    - This is optional; commits can be made without an issue key
3. **Stage changes intentionally**
    - Prefer `git add <path>...` for the exact files that belong in the commit
    - Use `git add -A` only when the entire worktree belongs to the same reviewed task
    - Re-check `git diff --cached` after staging so the commit matches the reviewed diff
4. **Create short commit message**
    - Base the message on the actual changes in the diff
    - Use English for the commit message
    - Example: `git commit -m "fix(auth): refresh expired token handling"`
    - Example with issue key: `git commit -m "TASK-123: fix(auth): refresh expired token handling"`

## Template

- `git commit -m "<type>(<scope>): <short summary>"`
- With issue key: `git commit -m "<issue-key>: <type>(<scope>): <short summary>"`

## Rules

- **Length:** <= 72 characters
- **Language:** Use English for commit messages
- **Imperative mood:** Use verbs such as `fix`, `add`, `update` (not `fixed`, `added`, `updated`)
- **No period:** Don't end the subject line with a period
- **Describe why:** Not just what; `fix issue` is too vague
