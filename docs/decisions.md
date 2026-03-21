# Decisions

## Purpose

This document records confirmed design decisions and why they replaced, narrowed, or reordered earlier ideas.

## Decision Log

### 2026-03-21 No agent commits on `main` without explicit permission

- Decision: Agents must not run `git commit` while on `main` unless the user explicitly allows that change set to be committed in the current conversation. Documented in root `AGENTS.md`, `docs/agent-iteration-contract.md`, `.cursor/rules/git-main-no-commit.mdc`, and repo-local `git-commit` skills (Cursor, Claude, Codex).
- Why: The user wants `main` protected from unprompted agent commits; task branches or user-run commits remain the default outlet.
- Impact: Routine maintenance should use `$git-start-task` (or equivalent) before committing, or hand off diffs and a proposed message for a user commit on `main`.

### 2026-03-21 Pull request metadata changes require explicit user intent

- Decision: Preparing or refreshing PR title/body text does not, by itself, authorize editing an existing pull request. Agents should only create a PR or mutate PR metadata when the user explicitly asks for that operation.
- Why: Frequent PR mutation adds interaction overhead and forces the agent to spend effort on a user-facing surface that often does not need to change.
- Impact: PR handoff can still prepare suggested title/body text, but existing PR metadata should stay untouched by default.

### 2026-03-21 Operative exploration levels (phase 1)

- Decision: Introduce `docs/task-exploration-levels.md` as the operative mapping when the user states task exploration intensity; add a short pointer in `docs/agent-iteration-contract.md`; link from `AGENTS.md`. Other collaboration dimensions are intentionally not adopted in phase 1.
- Why: Ships a concrete agent-visible playbook for one axis without expanding layer-1 entry files or making scope/urgency/risk/authority operative yet.
- Impact: Tagged exploration overrides default due-diligence *style* per level doc; untagged behavior stays the prior contract default (equivalent to medium).

### 2026-03-21 Record owner–AI maintenance as a stable system fact

- Decision: Record in `docs/system-overview.md` that routine maintenance is an owner–AI collaboration loop, with authoritative contracts in `docs/REPOSITORY-GOALS.md` and `docs/agent-iteration-contract.md` and task state under `docs/tasks/`.
- Why: `docs/system-overview.md` is the stable-facts index; the operational model should be discoverable there without relying only on task workspaces or chat context.
- Impact: Task `human-ai-collaborative-maintenance` cross-links these sources; future changes to the collaboration model should update REPOSITORY-GOALS, agent-iteration-contract, and this overview together.

### 2026-03-15 Root AGENTS remains a rules entrypoint

- Decision: Root `AGENTS.md` is the rules entrypoint for maintaining this repository, not the single total entrypoint for all repository knowledge.
- Why: Repository contract, sequencing, and evolution goals need their own stable governance documents instead of being merged into the runtime rule file.
- Impact: Repository purpose lives in `docs/REPOSITORY-GOALS.md`; root `AGENTS.md` stays focused on maintenance rules.

### 2026-03-15 Claude keeps a native shell entrypoint

- Decision: Claude keeps a native `CLAUDE.md` shell that references shared rules instead of replacing the Claude entry model with `AGENTS.md`.
- Why: This preserves native Claude compatibility while still allowing shared project-level guidance to converge.
- Impact: Cross-platform consistency is achieved through shared baseline content plus platform-native shells, not by collapsing every platform into the same entry file.

### 2026-03-15 Platforms directory is the archive/source home

- Decision: External tool assets are maintained under `platforms/` rather than in the root tool directories.
- Why: This cleanly separates repository-maintenance entrypoints from the archived assets this repository exists to maintain.
- Impact: Root tool directories stay minimal and repo-specific; distributable or archived platform content lives under platform-specific homes.

### 2026-03-15 Phase 1 favors low-friction maintenance reduction

- Decision: Phase 1 reduces duplicated maintenance first and does not immediately introduce core/adapters/generated automation.
- Why: The repository first needs stable asset homes and entrypoint boundaries before investing in generation architecture.
- Impact: The long-term generated model remains valid, but it is deferred to later phases.

### 2026-03-15 Cross-platform unification order is rules, then skills, then agents

- Decision: Later semantic alignment will handle shared rules first, high-frequency skills second, and agents or sub-agents last.
- Why: Rules and skills are more reusable across platforms, while agents and sub-agents vary the most by platform and are the highest-risk layer for premature abstraction.
- Impact: Future cross-platform work should not start by forcing agent parity across Cursor, Claude, and Codex.

### 2026-03-15 Repo-local self-iteration starts with a collaboration contract

- Decision: Repo-local Codex self-iteration should first be defined as a documented goal-to-ready-to-merge collaboration contract rather than as a dedicated skill, agent, or fixed template system.
- Why: The repository needs a stable execution boundary for intake, scope control, branch and commit expectations, and pull request handoff before deciding whether repeated behavior deserves stronger abstraction.
- Impact: Root `AGENTS.md` can stay concise, `docs/agent-iteration-contract.md` can hold the stable loop, and later skill or agent extraction can remain optional.

### 2026-03-19 Multi-session task context lives under docs/tasks

- Decision: Cross-session repo-maintenance task context should live under `docs/tasks/` instead of `docs/tmp/`.
- Why: `docs/tmp/` suggests disposable scratch work, while unfinished task research and handoff notes need a versioned, resumable home with clearer lifecycle semantics.
- Impact: `docs/tasks/` becomes the standard place for task workspaces; stable conclusions must still be promoted into standard docs or maintained assets when confirmed.

### 2026-03-19 Repo-authored docs avoid machine-specific absolute paths

- Decision: Repository-authored docs and task workspaces should not commit machine-specific absolute filesystem paths such as `/root/github/...` or `/workspace/...`.
- Why: These paths break portability across local clones, CI, GitHub rendering, and future sessions in different environments.
- Impact: Committed docs should use repo-relative links and repo-relative paths by default; environment-specific absolute paths are only acceptable when the user explicitly asks for debugging material tied to one machine.

### 2026-03-19 Local task index is the AI-first todo source

- Decision: `docs/tasks/index.yaml` is the canonical todo ledger for repo-maintenance tasks, while each tracked task keeps a local `docs/tasks/<task-slug>/README.md` context entrypoint.
- Why: AI resumes most reliably from versioned local files with stable paths and predictable fields, while GitHub issues and project boards are better treated as optional collaboration mirrors.
- Impact: New multi-session tasks should be added to `docs/tasks/index.yaml` before they sprawl across comments or ad hoc notes, and other docs should prefer linking back to tracked tasks instead of carrying standalone follow-up lists.

### 2026-03-19 Repo-local maintenance commits use English subjects

- Decision: Repo-local maintenance commits in this repository should use English commit subjects.
- Why: The repository already keeps its governance and maintenance documentation English-first, and commit history should stay aligned with that stable operating language instead of switching with the chat language.
- Impact: Repo-local commit workflows, including the local `git-commit` skill, should generate English commit subjects by default.

### 2026-03-19 Claude repo-local migration stops at skills

- Decision: Root `.claude/` should gain repo-local workflow skills, but it should not invent repo-local Claude agents just to mirror Codex or Cursor.
- Why: Claude Code reads `CLAUDE.md` natively and does not use `.mdc` rule files or `agents/openai.yaml` shells. Rules are expressed directly in `CLAUDE.md`. The high-value layer is workflow skills, which are fully portable.
- Impact: Claude can maintain this repository through `CLAUDE.md` rules and `.claude/skills/` now. The `agents/openai.yaml` shells from `.codex/` have no Claude equivalent and were intentionally omitted.

### 2026-03-19 Cursor repo-local migration stops at rules and skills

- Decision: Root `.cursor/` should gain repo-local maintenance rules and workflow skills, but it should not invent repo-local Cursor agents or sub-agents just to mirror Codex.
- Why: The repository already treats rules and skills as the higher-leverage shared layer, while there are currently no repo-local Codex sub-agents to migrate.
- Impact: Cursor can maintain this repository through repo-local rules and skills now, while dedicated repo-local Cursor agents remain optional future work.
