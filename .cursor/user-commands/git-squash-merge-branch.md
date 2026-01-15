# Merge Branch

## Overview

Merge a specified branch into the current branch using squash merge. Combine all commits from the source branch into a single commit to keep history clean. Handle conflicts and verify the merge state.

## Steps

1. **Identify current branch**
   - Get current branch: `git branch --show-current`
   - Confirm it's the target branch for the merge

2. **Verify working directory is clean**
   - Check `git status` for uncommitted changes
   - If dirty, ask user to: stash (`git stash`), commit first, or abort

3. **Fetch latest changes**
   - Run `git fetch origin` to update local repository
   - Optionally fetch specific branch: `git fetch origin <source-branch>`

4. **Validate source branch**
   - If not provided, ask: "Which branch do you want to merge into the current branch?"
   - Check branch exists: `git branch -a | grep <branch-name>`
   - If not local, check remote: `git ls-remote --heads origin <branch-name>`

5. **Perform squash merge**
   - Run `git merge --squash <source-branch>`
   - `--squash` combines all changes but doesn't auto-commit
   - If conflicts occur, proceed to step 6; otherwise proceed to step 7

6. **Resolve conflicts (if any)**
   - List conflicted files: `git status` or `git diff --name-only --diff-filter=U`
   - For each file:
     - Show conflicts: `git diff <file>`
     - Ask user preference: accept theirs, accept ours, or manual edit
     - Apply resolution:
       - Accept theirs: `git checkout --theirs <file>`
       - Accept ours: `git checkout --ours <file>`
       - Manual: open file and show conflict markers
   - Stage resolved files: `git add <file>`

7. **Generate commit summary from source branch**
   - Get commits unique to source branch: `git log <current-branch>..<source-branch> --oneline`
   - Get detailed commit messages: `git log <current-branch>..<source-branch> --pretty=format:"%s%n%b"`
   - Analyze and summarize:
     - Group related changes (features, fixes, refactors)
     - Extract key changes from commit messages
     - Create concise summary (2-5 bullet points)

8. **Commit squashed changes with summary**
   - Check staged changes: `git status`
   - Create commit with summarized message:
     ```
     git commit -m "$(cat <<'EOF'
     merge: <source-branch> into <current-branch>

     Summary of changes:
     - [key change 1 from commits]
     - [key change 2 from commits]
     - [key change 3 from commits]
     EOF
     )"
     ```
   - Review commit: `git log -1 --stat`
   - Verify merge: `git log --oneline -5`

## Rules

- **Always use `--squash`**: Combine all source branch commits into a single commit
- **Summarize commits**: Generate commit message by analyzing all commits from source branch, not a generic message
- **Manual commit required**: Squash merge doesn't auto-commit; always create a commit after merge
- **Ask before resolving conflicts**: Never auto-resolve conflicts without user preference
- **Safety first**: Abort if working directory is dirty and user doesn't want to stash/commit
- **Always verify**: Check merge completion before considering task done

## Error Handling

- **Uncommitted changes**: Offer to stash or commit before merge
- **Branch not found**: Check remote branches and offer to fetch
- **Merge conflicts**: Guide user through resolution step by step
- **Aborted merge**: Clean up with `git merge --abort` if needed

## Common Commands

```bash
# Check current branch
git branch --show-current

# Check status
git status

# Fetch latest
git fetch origin

# Squash merge (requires manual commit)
git merge --squash <source-branch>

# Get commits to summarize
git log <current-branch>..<source-branch> --oneline

# Commit with summary
git commit -m "merge: <source-branch> into <current-branch>

Summary of changes:
- [summarized from branch commits]"

# Abort merge
git merge --abort

# View conflicts
git diff --name-only --diff-filter=U
```
