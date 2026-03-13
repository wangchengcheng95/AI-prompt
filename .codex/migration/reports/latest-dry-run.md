# Cursor-to-Codex Migration Dry Run

- Generated at: 2026-03-13T06:14:16.086630+00:00
- Repo root: `/root/build/llm_detector_codex`

## Summary

- Sources: 27
- Planned writes: 3
- Conflicts: 24
- Noop: 0
- Orphans: 0

## Inventory

- `rule:00-overview`: kind=`rule`, classification=`transform`, status=`conflict`
- `rule:ai-boundary`: kind=`rule`, classification=`transform`, status=`conflict`
- `rule:architecture`: kind=`rule`, classification=`transform`, status=`conflict`
- `rule:design-docs`: kind=`rule`, classification=`transform`, status=`conflict`
- `rule:engineering-doctrine`: kind=`rule`, classification=`transform`, status=`conflict`
- `rule:english-prompt`: kind=`rule`, classification=`transform`, status=`conflict`
- `rule:go-backend`: kind=`rule`, classification=`transform`, status=`conflict`
- `rule:memory-management`: kind=`rule`, classification=`transform`, status=`conflict`
- `rule:plan-mode-todos`: kind=`rule`, classification=`transform`, status=`conflict`
- `rule:testing`: kind=`rule`, classification=`transform`, status=`conflict`
- `skill:add-error-handling`: kind=`skill`, classification=`direct`, status=`conflict`
- `skill:ai-interaction`: kind=`skill`, classification=`direct`, status=`conflict`
- `skill:brainstorming`: kind=`skill`, classification=`direct`, status=`conflict`
- `skill:clean-code`: kind=`skill`, classification=`direct`, status=`conflict`
- `skill:database-migration`: kind=`skill`, classification=`direct`, status=`conflict`
- `skill:design-rest-api`: kind=`skill`, classification=`direct`, status=`conflict`
- `skill:docker-logs`: kind=`skill`, classification=`direct`, status=`conflict`
- `skill:generate-api-docs`: kind=`skill`, classification=`direct`, status=`conflict`
- `skill:generate-crud-operations`: kind=`skill`, classification=`direct`, status=`conflict`
- `skill:git-commit`: kind=`skill`, classification=`direct`, status=`conflict`
- `skill:git-squash-merge-branch`: kind=`skill`, classification=`direct`, status=`conflict`
- `skill:onboard-new-developer`: kind=`skill`, classification=`direct`, status=`conflict`
- `skill:optimize-database-queries`: kind=`skill`, classification=`direct`, status=`conflict`
- `skill:write-integration-tests`: kind=`skill`, classification=`direct`, status=`conflict`
- `agent:debugger`: kind=`agent`, classification=`direct`, status=`planned`
- `agent:test-runner`: kind=`agent`, classification=`direct`, status=`planned`
- `agent:verifier`: kind=`agent`, classification=`direct`, status=`planned`

## Planned Actions

### `rule:00-overview`

- Source: `.cursor/rules/00-overview.mdc`
- Status: `conflict`
- Targets: `AGENTS.md`
- Conflicts:
  - `AGENTS.md`: AGENTS.md exists without migration ownership markers
- Proposed outputs:
  - `AGENTS.md`

```text
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
...
```

### `rule:ai-boundary`

- Source: `.cursor/rules/ai-boundary.mdc`
- Status: `conflict`
- Targets: `AGENTS.md`
- Conflicts:
  - `AGENTS.md`: AGENTS.md exists without migration ownership markers
- Proposed outputs:
  - `AGENTS.md`

```text
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
...
```

### `rule:architecture`

- Source: `.cursor/rules/architecture.mdc`
- Status: `conflict`
- Targets: `AGENTS.md`
- Conflicts:
  - `AGENTS.md`: AGENTS.md exists without migration ownership markers
- Proposed outputs:
  - `AGENTS.md`

```text
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
...
```

### `rule:design-docs`

- Source: `.cursor/rules/design-docs.mdc`
- Status: `conflict`
- Targets: `AGENTS.md`
- Conflicts:
  - `AGENTS.md`: AGENTS.md exists without migration ownership markers
- Proposed outputs:
  - `AGENTS.md`

```text
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
```

### `rule:engineering-doctrine`

- Source: `.cursor/rules/engineering-doctrine.mdc`
- Status: `conflict`
- Targets: `AGENTS.md`
- Conflicts:
  - `AGENTS.md`: AGENTS.md exists without migration ownership markers
- Proposed outputs:
  - `AGENTS.md`

```text
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

...
```

### `rule:english-prompt`

- Source: `.cursor/rules/english-prompt.mdc`
- Status: `conflict`
- Targets: `AGENTS.md`
- Conflicts:
  - `AGENTS.md`: AGENTS.md exists without migration ownership markers
- Proposed outputs:
  - `AGENTS.md`

```text
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
...
```

### `rule:go-backend`

- Source: `.cursor/rules/go-backend.mdc`
- Status: `conflict`
- Targets: `AGENTS.md`
- Conflicts:
  - `AGENTS.md`: AGENTS.md exists without migration ownership markers
- Proposed outputs:
  - `AGENTS.md`

```text
<!-- codex-migrate:start:go-backend -->
## Go Backend Engineering

### Language & runtime
- Go version: **1.24**
- No `panic` (handle errors explicitly).
- No global variables.

### Layering & responsibilities
- Follow `architecture.mdc` for layer boundaries and dependency direction.
- Go-specific enforcement:
  - Keep business logic in **service** layer.
  - Handlers are transport orchestration only.
  - Repositories are data access only.
  - Do not access DB directly from handlers.

### Context & I/O
- Use `context.Context` for all I/O operations.
...
```

### `rule:memory-management`

- Source: `.cursor/rules/memory-management.mdc`
- Status: `conflict`
- Targets: `AGENTS.md`
- Conflicts:
  - `AGENTS.md`: AGENTS.md exists without migration ownership markers
- Proposed outputs:
  - `AGENTS.md`

```text
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

...
```

### `rule:plan-mode-todos`

- Source: `.cursor/rules/plan-mode-todos.mdc`
- Status: `conflict`
- Targets: `AGENTS.md`
- Conflicts:
  - `AGENTS.md`: AGENTS.md exists without migration ownership markers
- Proposed outputs:
  - `AGENTS.md`

```text
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
...
```

### `rule:testing`

- Source: `.cursor/rules/testing.mdc`
- Status: `conflict`
- Targets: `AGENTS.md`
- Conflicts:
  - `AGENTS.md`: AGENTS.md exists without migration ownership markers
- Proposed outputs:
  - `AGENTS.md`

```text
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
...
```

### `skill:add-error-handling`

- Source: `.cursor/skills/add-error-handling/SKILL.md`
- Status: `conflict`
- Targets: `.codex/skills/add-error-handling/SKILL.md`
- Conflicts:
  - `.codex/skills/add-error-handling/SKILL.md`: Target skill already exists and is unmanaged
- Proposed outputs:
  - `.codex/skills/add-error-handling/SKILL.md`

```text
---
name: add-error-handling
description: "Add Error Handling"
---
<!-- codex-migrate:owned source=.cursor/skills/add-error-handling/SKILL.md -->
# Add Error Handling

## Overview

Implement comprehensive error handling for the current Go code to make it robust and resilient to failures while maintaining good user experience.

## Steps

1. **Error Detection**
    - Identify potential failure points and edge cases
    - Find unhandled errors and error conditions
    - Detect missing validation and boundary checks
    - Analyze async operations, network calls, and I/O operations
...
```

### `skill:ai-interaction`

- Source: `.cursor/skills/ai-interaction/SKILL.md`
- Status: `conflict`
- Targets: `.codex/skills/ai-interaction/SKILL.md`
- Conflicts:
  - `.codex/skills/ai-interaction/SKILL.md`: Target skill already exists and is unmanaged
- Proposed outputs:
  - `.codex/skills/ai-interaction/SKILL.md`

```text
---
name: ai-interaction
description: "AI interaction guidelines (review-friendly)"
---
<!-- codex-migrate:owned source=.cursor/skills/ai-interaction/SKILL.md -->
# AI Interaction Guidelines

## Truthfulness
- Verify before asserting; if uncertain, say so and ask for the missing info.
- Do not invent business rules or hidden behavior (follow `ai-boundary.mdc` as the source of truth).

## Reviewability
- Present changes **file-by-file**.
- For each changed file, provide a complete final edit for that file (avoid partial multi-step edits).
- Call out any user decision points explicitly (trade-offs, risks, required approvals).

## Communication style
- Keep responses concise and high-signal.
...
```

### `skill:brainstorming`

- Source: `.cursor/skills/brainstorming/SKILL.md`
- Status: `conflict`
- Targets: `.codex/skills/brainstorming/SKILL.md`
- Conflicts:
  - `.codex/skills/brainstorming/SKILL.md`: Target skill already exists and is unmanaged
- Proposed outputs:
  - `.codex/skills/brainstorming/SKILL.md`

```text
---
name: brainstorming
description: "You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation."
---
<!-- codex-migrate:owned source=.cursor/skills/brainstorming/SKILL.md -->
# Brainstorming Ideas Into Designs

## Overview

Help turn ideas into fully formed designs and specs through natural collaborative dialogue.

Start by understanding the current project context, then ask questions one at a time to refine the idea. Once you understand what you're building, present the design in small sections (200-300 words), checking after each section whether it looks right so far.

## The Process

**Understanding the idea:**
- Check out the current project state first (files, docs, recent commits)
- Ask questions one at a time to refine the idea
...
```

### `skill:clean-code`

- Source: `.cursor/skills/clean-code/SKILL.md`
- Status: `conflict`
- Targets: `.codex/skills/clean-code/SKILL.md`
- Conflicts:
  - `.codex/skills/clean-code/SKILL.md`: Target skill already exists and is unmanaged
- Proposed outputs:
  - `.codex/skills/clean-code/SKILL.md`

```text
---
name: clean-code
description: "Clean code guidelines(within change radius)"
---
<!-- codex-migrate:owned source=.cursor/skills/clean-code/SKILL.md -->
# Clean Code Guidelines

## Scope guard
- Apply these guidelines **only within the agreed change radius**.
- Do not do drive-by refactors; if a refactor is needed beyond the radius, ask first.

## Readability & structure
- Use meaningful names; avoid unclear abbreviations.
- Keep functions small and single-purpose.
- Prefer clear interfaces; hide implementation details.

## Avoid duplication (DRY)
- Extract repeated logic into helpers when it improves clarity and testability.
...
```

### `skill:database-migration`

- Source: `.cursor/skills/database-migration/SKILL.md`
- Status: `conflict`
- Targets: `.codex/skills/database-migration/SKILL.md`
- Conflicts:
  - `.codex/skills/database-migration/SKILL.md`: Target skill already exists and is unmanaged
- Proposed outputs:
  - `.codex/skills/database-migration/SKILL.md`

```text
---
name: database-migration
description: "Database Migration"
---
<!-- codex-migrate:owned source=.cursor/skills/database-migration/SKILL.md -->
# Database Migration

## Overview

Help create and manage database migrations, generating complete migration files following the project's database framework conventions.

## Steps

1. **Migration Analysis**
    - Review current database schema changes needed
    - Identify data transformation requirements
    - Check for potential data loss or corruption risks
    - Analyze performance impact of schema changes
...
```

### `skill:design-rest-api`

- Source: `.cursor/skills/design-rest-api/SKILL.md`
- Status: `conflict`
- Targets: `.codex/skills/design-rest-api/SKILL.md`
- Conflicts:
  - `.codex/skills/design-rest-api/SKILL.md`: Target skill already exists and is unmanaged
- Proposed outputs:
  - `.codex/skills/design-rest-api/SKILL.md`

```text
---
name: design-rest-api
description: "Design REST API"
---
<!-- codex-migrate:owned source=.cursor/skills/design-rest-api/SKILL.md -->
# Design REST API

## Overview

Design RESTful API endpoints following REST principles and best practices. Create well-structured, intuitive, and maintainable APIs that follow industry standards for resource naming, HTTP methods, status codes, and error handling.

## Steps

1. **Resource Identification**
    - Identify core resources/entities using nouns (e.g., `/users`, not `/getUsers`)
    - Define relationships and hierarchies between resources
    - List all data attributes for each resource
    - Keep nesting to 2-3 levels maximum
...
```

### `skill:docker-logs`

- Source: `.cursor/skills/docker-logs/SKILL.md`
- Status: `conflict`
- Targets: `.codex/skills/docker-logs/SKILL.md`
- Conflicts:
  - `.codex/skills/docker-logs/SKILL.md`: Target skill already exists and is unmanaged
- Proposed outputs:
  - `.codex/skills/docker-logs/SKILL.md`

```text
---
name: docker-logs
description: "Docker Logs Tail"
---
<!-- codex-migrate:owned source=.cursor/skills/docker-logs/SKILL.md -->
# Docker Logs Tail

Tail logs from Docker containers to check for errors and monitor application behavior.

## Instructions

When user requests to check container logs:

1. **Discover running containers**: First, list all running containers to see what's available:

   ```bash
   docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Image}}"
   ```
...
```

### `skill:generate-api-docs`

- Source: `.cursor/skills/generate-api-docs/SKILL.md`
- Status: `conflict`
- Targets: `.codex/skills/generate-api-docs/SKILL.md`
- Conflicts:
  - `.codex/skills/generate-api-docs/SKILL.md`: Target skill already exists and is unmanaged
- Proposed outputs:
  - `.codex/skills/generate-api-docs/SKILL.md`

```text
---
name: generate-api-docs
description: "Generate MQTT/Device Protocol Documentation"
---
<!-- codex-migrate:owned source=.cursor/skills/generate-api-docs/SKILL.md -->
# Generate MQTT/Device Protocol Documentation

## Overview

Create comprehensive documentation for MQTT topics, message formats, and device communication protocols (Modbus, TCP, Serial) following the project's documentation standards.

## Steps

1. **MQTT Protocol Documentation**
    - Document MQTT broker configuration and connection details
    - List all MQTT topics used for data upload
    - Document message formats (Protobuf, JSON, Custom Frame)
    - Include QoS levels and retention policies
...
```

### `skill:generate-crud-operations`

- Source: `.cursor/skills/generate-crud-operations/SKILL.md`
- Status: `conflict`
- Targets: `.codex/skills/generate-crud-operations/SKILL.md`
- Conflicts:
  - `.codex/skills/generate-crud-operations/SKILL.md`: Target skill already exists and is unmanaged
- Proposed outputs:
  - `.codex/skills/generate-crud-operations/SKILL.md`

```text
---
name: generate-crud-operations
description: "Generate CRUD Operations"
---
<!-- codex-migrate:owned source=.cursor/skills/generate-crud-operations/SKILL.md -->
# Generate CRUD Operations

## Overview

Generate complete CRUD (Create, Read, Update, Delete) operations for a data model including database schema, API endpoints, business logic, validation, and tests. Accelerates development by scaffolding boilerplate code while following best practices.

## Steps

1. **Model Definition**
    - Define model name and purpose
    - List fields with types, constraints, and defaults
    - Identify required vs optional fields
    - Define relationships (foreign keys, associations)
...
```

### `skill:git-commit`

- Source: `.cursor/skills/git-commit/SKILL.md`
- Status: `conflict`
- Targets: `.codex/skills/git-commit/SKILL.md`
- Conflicts:
  - `.codex/skills/git-commit/SKILL.md`: Target skill already exists and is unmanaged
- Proposed outputs:
  - `.codex/skills/git-commit/SKILL.md`

```text
---
name: git-commit
description: "Git Create Commit"
---
<!-- codex-migrate:owned source=.cursor/skills/git-commit/SKILL.md -->
# Git Create Commit

## Overview

Create a short, focused commit message and commit staged changes.

## Steps

1. **Review changes**
    - Check the diff: `git diff --cached` (if changes are staged) or `git diff` (if unstaged)
    - Understand what changed and why
2. **Ask for issue key (optional)**
    - Check the branch name for an issue key (Linear, Jira, GitHub issue, etc.)
...
```

### `skill:git-squash-merge-branch`

- Source: `.cursor/skills/git-squash-merge-branch/SKILL.md`
- Status: `conflict`
- Targets: `.codex/skills/git-squash-merge-branch/SKILL.md`
- Conflicts:
  - `.codex/skills/git-squash-merge-branch/SKILL.md`: Target skill already exists and is unmanaged
- Proposed outputs:
  - `.codex/skills/git-squash-merge-branch/SKILL.md`

```text
---
name: git-squash-merge-branch
description: "Merge Branch"
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
...
```

### `skill:onboard-new-developer`

- Source: `.cursor/skills/onboard-new-developer/SKILL.md`
- Status: `conflict`
- Targets: `.codex/skills/onboard-new-developer/SKILL.md`
- Conflicts:
  - `.codex/skills/onboard-new-developer/SKILL.md`: Target skill already exists and is unmanaged
- Proposed outputs:
  - `.codex/skills/onboard-new-developer/SKILL.md`

```text
---
name: onboard-new-developer
description: "Onboard New Developer"
---
<!-- codex-migrate:owned source=.cursor/skills/onboard-new-developer/SKILL.md -->
# Onboard New Developer

## Overview

Comprehensive onboarding process to get a new developer up and running quickly with the project.

## Steps

1. **Environment setup**
    - Install Go 1.24+
    - Set up development environment
    - Configure IDE and extensions (VS Code/Cursor recommended)
    - Set up git and SSH keys
...
```

### `skill:optimize-database-queries`

- Source: `.cursor/skills/optimize-database-queries/SKILL.md`
- Status: `conflict`
- Targets: `.codex/skills/optimize-database-queries/SKILL.md`
- Conflicts:
  - `.codex/skills/optimize-database-queries/SKILL.md`: Target skill already exists and is unmanaged
- Proposed outputs:
  - `.codex/skills/optimize-database-queries/SKILL.md`

```text
---
name: optimize-database-queries
description: "Optimize Database Queries"
---
<!-- codex-migrate:owned source=.cursor/skills/optimize-database-queries/SKILL.md -->
# Optimize Database Queries

## Overview

Analyze and optimize database queries to improve performance, reduce load times, and eliminate bottlenecks. Provides systematic approaches to identify slow queries, understand execution plans, and apply optimization techniques.

## Steps

1. **Query Performance Analysis**
    - Identify slow-running queries in application
    - Review logs for query execution times
    - Use database profiling tools
    - Check for N+1 query problems
...
```

### `skill:write-integration-tests`

- Source: `.cursor/skills/write-integration-tests/SKILL.md`
- Status: `conflict`
- Targets: `.codex/skills/write-integration-tests/SKILL.md`
- Conflicts:
  - `.codex/skills/write-integration-tests/SKILL.md`: Target skill already exists and is unmanaged
- Proposed outputs:
  - `.codex/skills/write-integration-tests/SKILL.md`

```text
---
name: write-integration-tests
description: "Write Integration Tests"
---
<!-- codex-migrate:owned source=.cursor/skills/write-integration-tests/SKILL.md -->
# Write Integration Tests

## Overview

Create comprehensive integration tests that verify multiple components work correctly together. Unlike unit tests, integration tests validate interactions between modules, API endpoints with databases, external services, and complete workflows.

## Steps

1. **Test Scope Definition**
    - Identify components being integrated (API + Database, Service + External API)
    - Define integration boundaries and contracts
    - List all integration points
    - Determine test data requirements
...
```

### `agent:debugger`

- Source: `.cursor/agents/debugger.md`
- Status: `planned`
- Targets: `.codex/config.toml, .codex/agents/debugger.toml`
- Proposed outputs:
  - `.codex/config.toml`

```text
# codex-migrate:start:agents
[agents.debugger]
description = "Go debugging expert. Use when you see panic, test failures, 500 responses, concurrency issues, log anomalies, or race detector reports. Outputs root-cause analysis and minimal fix suggestions."
config_file = "agents/debugger.toml"

[agents.test_runner]
description = "Go test expert. After code changes, new features, or bug fixes, proactively run go test, analyze failures, attempt minimal fixes (without changing test intent), and loop until tests pass or produce a clear \"cannot fix\" report. Suitable for all Go projects."
config_file = "agents/test_runner.toml"

[agents.verifier]
description = "Strict verifier. Use when a task or feature is claimed \"done\" or \"implemented\" — check that it actually works, edge cases are covered, and error handling is sound. Prevents false completion."
config_file = "agents/verifier.toml"

# codex-migrate:end:agents
```
  - `.codex/agents/debugger.toml`

```text
# codex-migrate:owned source=.cursor/agents/debugger.md
model = "inherit"
developer_instructions = """
You are a senior debugging engineer focused on Go runtime and concurrency issues.

## Workflow

1. **Gather** all available clues: panic stack, test failure output, logs, race report, user description.
2. **Locate** the most likely failing file, line number, and goroutine.
3. **Analyze** common Go failure patterns:
   - nil pointer dereference
   - context deadline exceeded / canceled not handled
   - errors swallowed or error wrapping lost
   - data race (especially maps/slices shared across goroutines)
   - defer order bugs, resource leaks
   - json unmarshal / struct tag issues
4. **Provide** a minimal reproducible example when possible.
5. **Propose** a fix as a diff (prefer one-line or minimal-scope changes).
...
```

### `agent:test-runner`

- Source: `.cursor/agents/test-runner.md`
- Status: `planned`
- Targets: `.codex/config.toml, .codex/agents/test_runner.toml`
- Proposed outputs:
  - `.codex/config.toml`

```text
# codex-migrate:start:agents
[agents.debugger]
description = "Go debugging expert. Use when you see panic, test failures, 500 responses, concurrency issues, log anomalies, or race detector reports. Outputs root-cause analysis and minimal fix suggestions."
config_file = "agents/debugger.toml"

[agents.test_runner]
description = "Go test expert. After code changes, new features, or bug fixes, proactively run go test, analyze failures, attempt minimal fixes (without changing test intent), and loop until tests pass or produce a clear \"cannot fix\" report. Suitable for all Go projects."
config_file = "agents/test_runner.toml"

[agents.verifier]
description = "Strict verifier. Use when a task or feature is claimed \"done\" or \"implemented\" — check that it actually works, edge cases are covered, and error handling is sound. Prevents false completion."
config_file = "agents/verifier.toml"

# codex-migrate:end:agents
```
  - `.codex/agents/test_runner.toml`

```text
# codex-migrate:owned source=.cursor/agents/test-runner.md
model = "fast"
developer_instructions = """
You are an experienced Go test automation expert, strictly following Go testing best practices.

## Core responsibilities

- When you detect code changes or modifications to handlers, services, or repositories, **proactively** run tests.
- Default command: `go test -v -race -count=1 ./...`
- If a targeted test path exists (e.g. for the changed area), run that first (e.g. `go test ./internal/handler/...`).
- On test failure: analyze output → locate file, line number, and exact assertion failure reason.
- Propose a **minimal fix diff** (preserve existing test logic; fix only the implementation).
- Re-run tests to verify.
- Loop at most 3 times; if still failing, stop and report root cause.

## Output format (strict)

1. **Test command:** `...`
...
```

### `agent:verifier`

- Source: `.cursor/agents/verifier.md`
- Status: `planned`
- Targets: `.codex/config.toml, .codex/agents/verifier.toml`
- Proposed outputs:
  - `.codex/config.toml`

```text
# codex-migrate:start:agents
[agents.debugger]
description = "Go debugging expert. Use when you see panic, test failures, 500 responses, concurrency issues, log anomalies, or race detector reports. Outputs root-cause analysis and minimal fix suggestions."
config_file = "agents/debugger.toml"

[agents.test_runner]
description = "Go test expert. After code changes, new features, or bug fixes, proactively run go test, analyze failures, attempt minimal fixes (without changing test intent), and loop until tests pass or produce a clear \"cannot fix\" report. Suitable for all Go projects."
config_file = "agents/test_runner.toml"

[agents.verifier]
description = "Strict verifier. Use when a task or feature is claimed \"done\" or \"implemented\" — check that it actually works, edge cases are covered, and error handling is sound. Prevents false completion."
config_file = "agents/verifier.toml"

# codex-migrate:end:agents
```
  - `.codex/agents/verifier.toml`

```text
# codex-migrate:owned source=.cursor/agents/verifier.md
model = "inherit"
developer_instructions = """
You are an extremely rigorous Go backend feature verification expert.

## Workflow when invoked

1. **Clarify** what the user or main agent claims is complete (feature, handler, service, etc.).
2. **Inspect** that the corresponding code exists and is well-structured (layering, interfaces, error wrapping).
3. **Run** relevant tests (`go test ...`); if tests are missing or coverage is low, call it out.
4. **Design and simulate** 3–5 key scenarios (happy path, edge, failure, concurrency):
   - Pay special attention: context cancellation, timeout, error chaining, nil checks, race conditions.
5. If the project has integration/e2e tests, **run them first**.
6. **Reason manually** about possible gaps: input validation, authorization, idempotency, transactions, resource cleanup.

## Output format (required)

### Verification summary
...
```

## Orphans

- None
