---
name: git-squash-merge-branch
description: Merge Branch
---
<!-- codex-migrate:owned source=.cursor/skills/git-squash-merge-branch/SKILL.md -->
# Merge Branch

Squash merge a branch into the current branch, combining all commits into one clean commit.

## Steps

1. **Verify state**
   - Confirm current branch: `git branch --show-current`
   - Check for uncommitted changes: `git status`
   - If dirty: stash, commit, or abort

2. **Fetch and validate**
   - Fetch latest: `git fetch origin`
   - If source branch not provided, ask user
   - Verify branch exists: `git branch -a | grep <branch>` or `git ls-remote --heads origin <branch>`

3. **Squash merge**
   - Run: `git merge --squash <source-branch>`
   - If conflicts, proceed to step 4; otherwise skip to step 5

4. **Resolve conflicts**
   - List conflicts: `git diff --name-only --diff-filter=U`
   - For each file, ask user: accept theirs, ours, or manual edit
     - Theirs: `git checkout --theirs <file>`
     - Ours: `git checkout --ours <file>`
   - Stage resolved: `git add <file>`

5. **Commit with summary**
   - Analyze source branch commits: `git log <current>..<source> --oneline`
   - Identify work type from commits and branch name:
     - `feature`: 新功能
     - `bugfix`/`fix`: 修复问题
     - `chore`: 构建/工具/配置相关
     - `enhance`: 功能增强
     - `refactor`: 重构
     - `test`: 测试相关
     - `docs`: 文档相关
   - Extract main content from commit messages and code changes
   - Create commit message in Chinese:
     ```bash
     git commit -m "<type>(<scope>): <中文描述>"
     ```
     - Example: `git commit -m "feat(user): 添加用户管理功能"`
     - Example: `git commit -m "fix(auth): 修复认证中间件无法获取上下文信息"`
     - Example: `git commit -m "chore(test): 添加单元测试"`
   - Verify: `git log -1 --stat`

## Rules

- **Always squash**: Use `--squash` to combine all commits
- **Summarize commits**: Analyze source branch commits to extract work type and content, use Chinese commit message with conventional format: `<type>(<scope>): <中文描述>`
- **Ask before conflict resolution**: Never auto-resolve
- **Abort if dirty**: Unless user chooses to stash/commit
- **Verify completion**: Check merge before done

## Error Handling

| Issue | Action |
|-------|--------|
| Uncommitted changes | Offer stash or commit |
| Branch not found | Check remote, offer fetch |
| Merge conflicts | Guide resolution step-by-step |
| Need to abort | `git merge --abort` |
