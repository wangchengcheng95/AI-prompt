# Git Create Commit

## Overview

Create a short, focused commit message and commit staged changes.

## Steps

1. **Review changes**
    - Check the diff: `git diff --cached` (if changes are staged) or `git diff` (if unstaged)
    - Understand what changed and why
2. **Ask for issue key (optional)**
    - Check the branch name for an issue key (Linear, Jira, GitHub issue, etc.)
    - If an issue key (e.g., TASK-123, ISSUE-456, #123) is not already available in the chat or commit context, optionally ask the user if they want to include one
    - This is optional - commits can be made without an issue key
3. **Stage changes (if not already staged)**
    - `git add -A`
4. **Create short commit message**
    - Base the message on the actual changes in the diff
    - Use Chinese for the commit message
    - Example: `git commit -m "fix(auth): 处理过期令牌刷新"`
    - Example with issue key: `git commit -m "TASK-123: fix(auth): 处理过期令牌刷新"`

## Template

- `git commit -m "<type>(<scope>): <简短摘要>"`
- With issue key: `git commit -m "<issue-key>: <type>(<scope>): <简短摘要>"`

## Rules

- **Length:** <= 72 characters
- **Language:** Use Chinese for commit messages
- **Imperative mood:** Use "修复", "添加", "更新" (not "修复了", "添加了", "更新了")
- **No period:** Don't end the subject line with a period
- **Describe why:** Not just what - "修复问题" is meaningless
