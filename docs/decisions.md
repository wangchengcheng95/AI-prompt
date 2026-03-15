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
