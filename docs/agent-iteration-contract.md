# Agent Iteration Contract

## Purpose

This document defines the behavioral contract for goal-driven repo-maintenance work in this repository.

It governs how the agent should intake work, decide whether to proceed, execute it, and hand it back in a `ready-to-merge` state without freezing one exact template for plans, reviews, or pull request text.

## Scope

This contract applies to repo-maintenance work performed from the root entrypoints for this repository.

It does not define the behavior of archived external platform assets under `platforms/`, and it does not require a dedicated repo-local skill or agent unless later usage proves that abstraction is worth the maintenance cost.

## Target Outcome

The target outcome for a task is `ready-to-merge`, not automatic merge. Final merge authority remains with the user.

Goals may come from either:

- a user-specified subset of `docs/EVOLUTION-GOALS.md`
- an ad hoc repository-maintenance goal raised during collaboration

The agent should first decide whether the goal is suitable for one bounded task in this repository.

A goal is a good fit when it:

- stays within current repository boundaries
- can be completed without large amounts of missing user-only information
- can reach a concrete acceptance conclusion
- does not require more than a small number of explicit user decisions

## Feasibility Gate

The agent should classify each incoming goal using one of three outcomes:

- `accept`: the goal is clear and small enough to execute now
- `shrink`: the goal is reasonable but should be reduced to a smaller deliverable for this turn
- `stop`: the goal depends on missing information, hidden ownership, or risk that the agent should not resolve alone

When the result is `shrink`, the agent should propose and execute the smallest useful slice that can still reach `ready-to-merge`.

## Interaction Budget

The default collaboration target is no more than three user interactions for one task.

The agent should only spend explicit interaction budget on decisions that materially change risk or scope, such as:

- unresolved goal ambiguity
- multiple implementation paths with non-obvious consequences
- permission or tooling boundaries that block execution
- destructive or ownership-sensitive changes

Outside those cases, the agent should make reasonable assumptions, continue execution, and state those assumptions in the final handoff.

## Pre-Execution Due Diligence

Before entering implementation, the agent should explicitly evaluate whether the task needs extra due diligence.

This check should cover:

- task importance, including scope, reversibility, blast radius, and familiarity with the tools or APIs involved
- whether the work depends on unfamiliar, version-sensitive, vendor-specific, security-relevant, or publish/migration-sensitive behavior
- whether the task has a single obvious path or needs a short discussion or plan first

When the task is non-trivial, the agent should consult authoritative online sources before relying on memory or guesses.

Preferred sources are the relevant official or authoritative sites for the task, such as:

- vendor or product documentation
- API references and framework documentation
- specifications or standards documents
- release notes, migration guides, or security advisories

When the task is non-trivial or multiple viable approaches exist, the agent should produce a concise plan before editing.

For small, low-risk changes with one obvious path, both research and planning may stay minimal, but the agent should still make the evaluation explicitly rather than skipping it by default.

## User-stated exploration level

When the user states an exploration level for the task, follow `docs/task-exploration-levels.md`. When they do not, use that document’s default (**medium**), which matches the due-diligence expectations above.

## Execution Loop

Once a goal is accepted for execution, the default loop is:

1. evaluate task importance, due-diligence needs, and scope reduction
2. consult authoritative online sources and form a concise plan when the task warrants it
3. create or switch to a task branch
4. register or refresh the task in `docs/tasks/` when the work is likely to span multiple sessions, multiple commits, or a follow-up PR-sized slice
5. implement the change
6. run the most relevant verification available
7. summarize acceptance status and residual risks
8. create at least one focused commit
9. refresh the tracked task state and next step in `docs/tasks/` before handoff when the task remains active, blocked, deferred, or spawns follow-up work
10. prepare pull request text and hand the work off for review

The agent should not stop at analysis if it can continue safely within this loop.

When the repo-local Git skills are available, prefer using:

- `$repo-self-iteration` as the entry workflow for goal-driven tasks
- `$git-start-task` for branch setup
- `$git-commit` for commit creation
- `$pr-handoff` for push and pull request handoff

Skills live under `.claude/skills/` for Claude Code and `.cursor/skills/` for Cursor.

## Ready-to-Merge Definition

Work is `ready-to-merge` when all of the following are true:

- the scoped goal has been implemented or narrowed to a clearly finished slice
- the repository changes are reviewable and attributable to a single task branch
- verification has been performed to the extent available in the current environment
- the current state, risks, and assumptions are visible to the user
- the user can review the result as a normal pull request candidate without needing the agent to explain missing basic context

For handoff, the agent should provide:

- the branch name used for the work, or the blocking reason if branch creation is prevented by tooling constraints
- a concise record of the plan actually followed
- the implemented repository changes
- the verification performed and its outcome
- the commit identifier, or the blocking reason if commit creation is prevented by tooling constraints
- the updated `docs/tasks/index.yaml` entry and task workspace `README.md` when the task is tracked in `docs/tasks/` or needs cross-session continuation
- pull request title and summary text suitable for review
- explicit assumptions, known risks, and any remaining manual steps

Preparing pull request text does not, by itself, authorize mutating an existing GitHub pull request. Unless the user explicitly asks to create a pull request or change pull request metadata, the agent should keep title and summary updates as handoff output only.

## Stop Conditions

The agent should stop and ask the user when any of the following applies:

- the goal is too large to credibly finish as one bounded task
- required information is controlled by the user and cannot be inferred safely
- the work would cross repository boundaries in a way that changes ownership or archive policy
- the task requires deletion or irreversible changes to user-authored material with unclear ownership
- repository or tool constraints prevent required branch, verification, commit, or pull request steps

## Follow-Up

After handoff, follow-up requests should normally continue on the same task branch, refine the existing work, refresh verification, and update the commit history through additional normal commits unless the user explicitly asks for a different workflow.

## Future Evolution

This contract should be validated through repeated real tasks before introducing stronger abstraction.

Later repo-local skills or dedicated agents may be added if the collaboration contract stabilizes and repeated task patterns justify the extra maintenance surface.
