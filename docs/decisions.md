# Decisions

## Purpose

This document records confirmed design decisions and why they replaced, narrowed, or reordered earlier ideas.

## Decision Log

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
