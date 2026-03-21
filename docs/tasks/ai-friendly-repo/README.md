---
task_id: ai-friendly-repo
title: AI-Friendly Repo Task
status: active
priority: high
kind: documentation
branch: null
issue: null
last_updated: 2026-03-21
next_step: Decide whether the next slice should add a repository-level start-here index or formalize promotion guidance from task workspaces into stable docs.
promotion_targets:
  - docs/system-overview.md
  - docs/architecture.md
  - docs/agent-iteration-contract.md
  - docs/decisions.md
---

# AI-Friendly Repo Task

## Status

- State: active
- Branch: none currently; start a fresh task branch when resuming implementation
- Last updated: 2026-03-21

## Original Goal

Acknowledge that this repository is not only an archive of cross-platform AI assets, but also the working repository for human-and-AI collaboration where the user provides goals and the AI is expected to organize information, index knowledge, drive execution, and ask for decisions at the right points.

## Current Slice

Turn the task workspace into an executable entrypoint for the next phase:

- define the working meaning of "AI-friendly repository"
- identify the concrete workstreams needed to move toward that goal
- prioritize indexing and promotion flow before any large structure refactor

## Current Status

- The canonical positioning now explicitly includes the repository's human-and-AI collaboration role.
- The stable change is intentionally small and does not yet redefine the standard docs set or task workflow.
- This task workspace is now the aggregation point for both the theme and the next execution slices.
- The next recommended implementation focus is indexing and promotion rules, not directory restructuring.
- `docs/tasks/README.md` now includes an active task index so AI task discovery no longer depends on directory scanning alone.
- `docs/tasks/README.md` now also defines the minimum contract and update triggers for active task READMEs.
- `docs/tasks/ecc-skill-research/README.md` has been normalized at the top of the file so indexed recovery does not depend on scanning the whole historical narrative.

## Working Definition

For this repository, "AI-friendly" currently means:

- retrievable: an AI can find the right document, asset, or task entrypoint with low search cost
- resumable: an AI can continue a task across sessions without depending on chat history alone
- decision-oriented: user decisions, open questions, and blocked choices are explicit rather than buried in narrative text
- promotable: temporary task conclusions can be moved into stable repository docs without re-deriving them from scratch

## Workstreams

The current task should be advanced through these workstreams, in this order:

1. Definition and scope
2. Indexing and navigation
3. Task workspace normalization
4. Promotion rules from task docs into stable docs
5. Structure changes only if repeated use proves they are needed

## Workstream Details

### 1. Definition and scope

- Keep validating whether the working definition above is sufficient.
- Avoid expanding "AI-friendly" into abstract principles that do not change repository behavior.
- Record only repository-relevant criteria, not general AI product ideas.

### 2. Indexing and navigation

- Define which repository entrypoints an AI should read first for common intents.
- Add explicit indexes where discovery cost is still high.
- Favor compact navigation aids over long narrative guides.

### 3. Task workspace normalization

- Make task workspaces easy for AI to resume without scanning old chats.
- Keep one clear entrypoint per task thread.
- Standardize which task fields must stay current during ongoing work.

### 4. Promotion rules

- Decide when a conclusion is still task-local versus stable enough for the standard docs set.
- Reduce the chance that durable knowledge stays trapped in task workspaces.
- Make the promotion target obvious for each class of conclusion.

### 5. Structure changes

- Delay major directory or doc-set refactors until the earlier workstreams expose repeated pain.
- Prefer proving the need through actual tasks before introducing new repository-wide structure.

## Indexing Checklist

The next indexing work should likely cover:

- repository root navigation:
  - what an AI should read first for repository purpose, rules, and current task work
- task navigation:
  - which tasks are active
  - which task README is the entrypoint for each thread
  - what the next session should open first
- decision navigation:
  - which conclusions are already stable
  - where each stable conclusion lives
- promotion navigation:
  - where a validated task conclusion should move next
  - which doc owns that conclusion class

## Promotion Guidance Draft

Use this draft rule until a stronger version is validated:

- keep active execution context, open questions, and tentative ideas in `docs/tasks/`
- move stable repository facts into `docs/system-overview.md`
- move stable structure and mapping rules into `docs/architecture.md`
- move dated confirmed choices into `docs/decisions.md`
- move stable repo-local execution behavior into `docs/agent-iteration-contract.md`

## Confirmed Findings

- The existing repository contract strongly emphasizes asset boundaries and archive structure.
- The current docs do not yet treat AI-oriented information organization as a first-class repository design principle.
- `docs/tasks/` is now the correct home for multi-session work that needs continuity before stable conclusions are promoted.
- The next high-value change is to reduce information discovery cost before changing the repository's physical layout.

## Follow-Up Work To Land Later

- Build a first repository navigation index if current entrypoints remain too implicit.
- Apply the active task README contract to other relevant ongoing task workspaces when needed.
- Validate the draft promotion rules through repeated real tasks.
- Evaluate whether repository-level indexes, decision ledgers, or promotion rules should be added after repeated use proves they help.

## Open Questions

- Which repository information should become explicitly index-first rather than narrative-first?
- How much of the future AI-friendly structure belongs in stable governance docs versus task workspaces?
- Whether the repo-local collaboration contract should later require stronger task aggregation and promotion rules.
- Whether a repository-wide active task index is enough, or whether deeper intent-based indexes are needed.

## Promotion Targets

- Promote only validated, repeated conclusions into the standard docs set.
- Keep exploratory structure ideas inside this task workspace until they prove useful across real tasks.

## Next Session Entrypoint

- Re-open this task workspace first when continuing the AI-friendly repository thread.
- Decide whether the next slice is:
  - extend indexing beyond `docs/tasks/` if repository root discovery is still too implicit
  - decide whether a repository-level start-here index is now justified
  - formalize the draft promotion guidance after one or two more real uses
