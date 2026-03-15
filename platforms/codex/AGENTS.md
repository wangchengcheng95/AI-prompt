# Codex Project Instructions

This file is the authoritative project instruction entry for Codex in this repository.

If this file conflicts with higher-priority system or developer instructions, follow the higher-priority instructions.

<!-- codex-migrate:start:00-overview -->
## Overview

### Goals
- Make the assistant behave like a reliable engineering agent: safe, correct, pragmatic, and easy to review.
- Keep rules **actionable**, **non-conflicting**, and **minimal**.

### Priority (when rules conflict)
```
Safety > Correctness > Maintainability > Performance > Convenience
```

### Applicability
- **Always**: `ai-boundary`, `architecture`, `engineering-doctrine`, `go-backend`, `memory-management`, `testing`.
- **Optional (opt-in)**: `ai-interaction`, `clean-code`.
- **When reviewing or explaining**: you may reference current implementation and provide summaries if it improves correctness and reviewability.

### Conflict resolution
- More specific rule wins over generic rule.
- If still unclear, **stop and ask** with a concrete option set (A/B) and the minimal required context.

### Change presentation
- Multi-file changes: present diffs **file-by-file**.
- Within one file: provide the full final edit for that file (avoid multi-step partial edits).
<!-- codex-migrate:end:00-overview -->

<!-- codex-migrate:start:ai-boundary -->
## AI Scope and Boundaries

### Default rule: change radius
- **Only modify files explicitly mentioned by the user**.
- **Do not extend the scope of requirements** — implement only what is explicitly requested, without adding "helpful" features or assumptions.
- **Do not** refactor/reformat unrelated code.
- **Do not** invent business rules or assumptions.
- **Do not** introduce new dependencies unless explicitly allowed.

### When additional files are required
If the task cannot be completed correctly without changing extra files (e.g. tests, shared interfaces, wiring/DI, configs):
- **STOP** and propose a minimal file list to change, with reasons for each file.
- Wait for the user's approval before proceeding.

### When requirements are unclear (STOP and ASK)
**Immediately stop and ask** instead of guessing or assuming, when:
- The instruction is ambiguous or unclear
- Essential context is missing (e.g. file paths, business rules, expected behavior)
- Multiple reasonable implementations exist and user preference is unknown
- You are uncertain about the user's true intent
- The task scope is not well-defined

**How to ask**:
- State concisely what you are uncertain about
- Provide A/B options for the user to choose (when applicable)
- **Do not** generate code while asking — wait for clarification first
- **Do not** say "I assume you want..." and proceed anyway

### Security & secrets
- Never print or hardcode secrets/tokens/credentials.
- Prefer configuration injection (env/config structs) over constants for sensitive values.
<!-- codex-migrate:end:ai-boundary -->

<!-- codex-migrate:start:architecture -->
## Project Architecture

This is a business-oriented application.

Architecture principles:
- Clear separation of layers
- No cross-layer access
- Dependencies must point inward

Backend layers:
- handler: HTTP / transport layer only
- service: business logic
- repository: data access

Frontend layers:
- pages: route-level components
- components: pure UI, no business logic
- hooks: business logic and data orchestration

Rules:
- Business logic must not be in handlers or UI components
- IO code must not contain business rules
<!-- codex-migrate:end:architecture -->

<!-- codex-migrate:start:engineering-doctrine -->
## Engineering Doctrine

Priority:
```
Safety > Correctness > Maintainability > Performance > Convenience
```

### Assume failure by default
- Assume retries, duplication, partial failure, concurrency.
- Network / external systems can fail, timeout, return stale data.
- Operations may be interrupted mid-execution.

### Write operations: protection & idempotency
- Externally visible write operations must be **idempotent**.
- Protect write paths explicitly (distributed lock or fencing token) when needed.
- Document idempotency keys and deduplication strategy.

### No implicit behavior
- No implicit retries or hidden side effects.
- No timing-based correctness assumptions.
- No background goroutines without clear ownership.
- No `time.Sleep` for synchronization (use context, timers, or explicit state checks).

### Error handling
- Never ignore returned errors.
- Wrap errors with context: `fmt.Errorf("operation: %w", err)`.
- Prefer typed errors; do not rely on string matching.

### Context propagation
- `context.Context` must propagate end-to-end.
- All I/O must accept and respect context cancellation.
- Use timeouts/deadlines for I/O boundaries.

### Repository boundaries
- No SQL outside repository layer.
- Cross-repository transactions require explicit coordination.

### Concurrency & goroutines
- Every goroutine has a clear owner responsible for lifecycle and shutdown.
- Prefer `errgroup.WithContext` for managed goroutine lifecycles.
- Use `select { case <-ctx.Done(): ... }` for cancellation checks.

### Distributed locks (if used)
- Acquire with timeout; handle acquisition failure gracefully.
- Always release in `defer` and surface release failures to the caller.
- **Logging policy**: service/business logic should not log; return errors and let upper layers decide logging.

### If any constraint cannot be satisfied
STOP, explain the conflict, propose alternatives, and do not silently violate rules.
<!-- codex-migrate:end:engineering-doctrine -->

<!-- codex-migrate:start:go-backend -->
## Go Backend Engineering

### Language & runtime
- Go version: **1.24**
- No `panic` (handle errors explicitly).
- No global variables.

### Layering & responsibilities
- Follow the project architecture rules for layer boundaries and dependency direction.
- Go-specific enforcement:
  - Keep business logic in **service** layer.
  - Handlers are transport orchestration only.
  - Repositories are data access only.
  - Do not access DB directly from handlers.

### Context & I/O
- Use `context.Context` for all I/O operations.
- Follow the engineering doctrine rules for end-to-end context propagation and I/O timeouts/deadlines.

### Error handling
- Follow the engineering doctrine rules for error wrapping, typed errors, and "never ignore errors".

### Concurrency
- No unmanaged goroutines; every goroutine must have a lifecycle owner.
- Prefer `errgroup` when you need cancellation + error propagation.
- No `time.Sleep` for synchronization (tests only with explicit justification).

### Logging
- Do not log inside business logic (service layer). Return errors; upper layers decide logging.

### Code quality
- Prefer small, focused, testable functions.
- Use dependency injection; avoid tight coupling.
- Avoid hard-coded values; use config structs/env injection when appropriate.

### Code language standards
- Identifiers (variables/functions/types/packages) must be in **English**.
- Error messages and error types must be in **English** (searchability/tooling).
- Code comments may be in **Chinese** for team understanding.
- Internal documentation may be in **Chinese**.

### Output expectations
- Code must be production-ready, compile, and be testable.
<!-- codex-migrate:end:go-backend -->

<!-- codex-migrate:start:memory-management -->
## Memory Management

### Triggers

**Must run Memory Bank update immediately** when the user says (or equivalent):
- update memory / 更新记忆 / sync memory / 更新 memory bank / 同步记忆体
- mem:update / /update-memory / refresh memory

**Suggest (do not auto-run) update** after:
- Completing a feature or user story
- Major refactor or architecture change
- Architecture/design decision is confirmed
- New dependency or significant config change
- User says "remember this", "this is important", "write this down", "add to memory"

### Update behavior

- Use the repository memory update workflow when available.
- **File names**: English with numeric prefix (`01_xxx.md`, `02_xxx.md`, …).
- **Entries**: Each important decision/change must have a date heading, e.g. `#### 2026-03-03 …`.
- **active_context.md**: Strictly **≤ 800 words**; keep it concise.
- **Large files**: If any file is near or over ~1200 lines, propose summarizing and trimming (archive or changelog); give a concrete plan.
- **Incremental only**: Add or edit only relevant sections; do not rewrite unrelated content.
- **No secrets**: Never store API keys, passwords, or confidential data in Memory Bank.

### Other

- Memory Bank files should be in git unless they contain secrets.
- Memory workflows and project rules should be kept in git.
- After changing the memory workflow, validate it with the repository memory update command.
<!-- codex-migrate:end:memory-management -->

<!-- codex-migrate:start:plan-mode-todos -->
## Planning

### Scope

- Applies only when editing implementation plans.

### Todo list

- **Required**: every plan must have a Markdown checklist (`- [ ] ...`).
- Generate and maintain todos by default. If the user says they do not want todos, still suggest a minimal executable list and briefly explain why.

### TDD usage

- **Prefer** planning with `/test-driven-development` (test-first → minimal implementation → refactor).
- If TDD is clearly not suitable (e.g. docs-only, scheduling, communication), briefly state why and use normal planning.

### Checklist structure

- Use a **single flat** checklist.
- First items: feature / test / implementation steps (optionally ordered by TDD).
- **Only when the plan involves code changes** (any language), append these 6 items at the **end**, in order:
  1. Use `/run-all-tests-and-fix` to run tests and fix failures
  2. Use `/verification-phase` for acceptance
  3. Use `/go-refactor-design` to refactor the written code for design patterns
  4. Use `/go-refactor-conventions` to refactor new Go code for conventions
  5. Use `/clean-code` to clean up new code
  6. Use `/update-solution-design` to update the solution design document
<!-- codex-migrate:end:plan-mode-todos -->

<!-- codex-migrate:start:design-docs -->
## Design and Spec Document Constraints

- **Use definitive wording for decided behavior.** For any agreed design or contract, write in definitive form (e.g. “when X then Y”, “Z also does A and B”). Do **not** use suggestive language (“建议”, “可考虑”, “推荐”) or vague qualifiers (“一般”, “通常”, “可能”, “酌情”) for decided behavior; use “不” / “仅” / “须” as appropriate.
- **Exception:** Content that is truly optional or TBD must be labeled (e.g. “可选”) or placed in a “待确认” / optional section.

Example (Chinese design docs):
- ❌ 4xx 建议同样 fail-open 并打 ERROR
- ✅ 4xx 同样 fail-open 并记录 ERROR 日志
- ❌ 图片一般不脱敏
- ✅ 仅文本支持脱敏，图片不脱敏
<!-- codex-migrate:end:design-docs -->

<!-- codex-migrate:start:english-prompt -->
## English Prompt Enforcement

**Scope**: ALL Chinese inputs — including tasks, questions, and information queries. **No exceptions.**

When the user provides instructions primarily in Chinese:

1. **Do NOT immediately execute the task.**

2. First, rewrite the user's input into a high-quality English prompt suitable for large language models.
   - Preserve the original intent exactly.
   - Improve clarity, structure, and explicitness.
   - Use concise, professional, engineering-oriented English.
   - Prefer imperative instructions and clear constraints.

3. Output the rewritten English prompt in a clearly marked section:
   ```
   Rewritten English Prompt:
   ```

4. Then ask a single, short confirmation question:
   ```
   Shall I proceed using this prompt?
   ```

5. Only proceed with task execution after confirmation, unless the user explicitly says to always proceed automatically.

### Rewritten prompt requirements

All rewritten English prompts must:
- Be structured (sections or bullet points)
- Avoid unnecessary politeness
- Avoid verbosity
- Be suitable for backend / system / infrastructure tasks
<!-- codex-migrate:end:english-prompt -->

<!-- codex-migrate:start:testing -->
## Testing

### Backend (Go)
- Prefer unit tests over integration tests.
- Use table-driven tests for multiple cases.
- Cover success + failure paths; assert error wrapping/context.
- Tests must be deterministic: no network/external services in unit tests.

#### Concurrency tests
- Use `-race` in CI.
- No timing-based assertions; synchronize explicitly.
- Use `go test -count=N` to detect flakes.

#### Mocking
- Mock external dependencies at **repository boundary** only.
- Prefer real implementations over mocks when practical.
- Document mock behavior expectations.

### Frontend
- Use React Testing Library.
- Test user-visible behavior; avoid implementation details.

### General
- Tests must be independent; avoid shared mutable state.
- Use `t.Parallel()` where safe to detect hidden dependencies.
- Use clear, specific assertions.
<!-- codex-migrate:end:testing -->

## Change Presentation

- For multi-file changes, present results file-by-file.
- For single-file changes, provide the final edit clearly.

## Project Skills

Project skills are stored under `.codex/skills/`.

Use these skills when explicitly named or when task intent clearly matches.
