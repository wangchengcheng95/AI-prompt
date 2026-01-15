[English](README.md) | [中文](README.zh.md)

# Backend AI Prompt Engineering Repository

This repository contains organized AI commands and rules specifically designed for **backend development**.

## Repository Purpose

**Focus:** AI-assisted prompt engineering for backend development workflows

**Scope:**
- Backend API development (REST, GraphQL)
- Database design and optimization
- Server architecture and microservices
- Authentication and security
- Performance optimization
- DevOps and infrastructure

---

## Backend Development Commands

These directories contain commands that are used **in actual backend development projects**:

### `backend-commands/` (6 commands)
**Scope:** Language-agnostic backend development commands

General backend commands that work across different programming languages:

**API Development:**
- `design-rest-api.md` - Design RESTful API endpoints following best practices
- `generate-api-docs.md` - Generate comprehensive API documentation
- `generate-crud-operations.md` - Generate complete CRUD operations for data models

**Database:**
- `database-migration.md` - Create and manage database migrations
- `optimize-database-queries.md` - Analyze and optimize database query performance

**Testing:**
- `write-integration-tests.md` - Create integration tests for multi-component systems

### `go-backend-commands/` (1 command)
**Scope:** Go-specific backend development

Commands tailored for Go backend projects:

- `add-error-handling.md` - Implement Go error handling patterns (explicit `if err != nil`, error wrapping, context usage)

### `user-commands/` (36 commands)
**Scope:** Project-agnostic, reusable across backend projects

Generic programming commands that work with any backend project or tech stack:

**Development Workflow:**
- `clarify-task.md` - Ask clarifying questions before coding
- `setup-new-feature.md` - Systematically set up new features
- `debug-issue.md` - Debug code systematically
- `refactor-code.md` - Improve code quality
- `optimize-performance.md` - Performance analysis and optimization
- `fix-compile-errors.md` - Analyze and fix compilation errors

**Code Quality:**
- `code-review.md` - Comprehensive code review
- `light-review-existing-diffs.md` - Quick quality pass on diffs
- `lint-fix.md` - Fix lint issues
- `lint-suite.md` - Run linters with autofix
- `deslop.md` - Remove AI-generated code slop
- `add-documentation.md` - Add comprehensive documentation
- `simplify-doc.md` - Simplify and consolidate documentation

**Testing:**
- `write-unit-tests.md` - Create comprehensive unit tests
- `run-all-tests-and-fix.md` - Execute and fix test failures

**Security:**
- `security-audit.md` - Comprehensive security audit
- `security-review.md` - Security review with remediation

**Git & PR Management:**
- `git-commit.md` - Create focused commit messages
- `git-push.md` - Push and sync with remote
- `git-squash-merge-branch.md` - Squash merge branches with commit summary
- `fix-git-issues.md` - Resolve Git problems
- `create-pr.md` - Create well-structured PRs
- `generate-pr-description.md` - Generate PR descriptions
- `address-github-pr-comments.md` - Process PR feedback

**Visualization & Planning:**
- `diagrams.md` - Generate Mermaid diagrams
- `visualize.md` - Visualize data lineage
- `overview.md` - Generate architecture diagrams
- `roadmap.md` - Generate feature roadmap

**Workflow Phases:**
- `design-phase.md` - Design phase workflow
- `implementation-phase.md` - Implementation phase workflow
- `critique-phase.md` - Critique phase workflow
- `verification-phase.md` - Verification phase workflow

**Go Backend Standards:**
- `go-backend-standards.md` - Go backend coding standards
- `go-refactor-conventions.md` - Go refactoring conventions
- `go-refactor-design.md` - Go refactoring design patterns

### `devops-commands/` (1 command)
**Scope:** DevOps and infrastructure management

- `docker-logs.md` - Tail Docker container logs

### `project-specific-archived/` (4 commands)
**Scope:** Project-specific commands (archived for reference)

Commands that are tightly coupled to specific projects and not easily reusable:
- `generate-device-protocol-docs.md` - Device protocol documentation
- `generate-mqtt-docs.md` - MQTT documentation
- `onboard-new-developer.md` - Project-specific onboarding
- `run-regression-tests-and-fix.md` - Project-specific regression tests

---

## Backend Development Rules

### `go-backend-rules/` (9 rules)
Rules and standards for Go backend development:

- `00-overview.mdc` - Overview of Go backend standards
- `ai-boundary.mdc` - AI interaction boundaries
- `ai-interaction.mdc` - AI interaction guidelines
- `architecture.mdc` - Architecture principles
- `clean-code.mdc` - Clean code standards
- `engineering-doctrine.mdc` - Engineering principles
- `english-prompt.mdc` - English prompt requirements
- `go-backend.mdc` - Go backend specific rules
- `testing.mdc` - Testing standards

---

## Usage Guide

### For Backend Developers Using This Repository

When working on backend projects, use these command categories:

**For Go Backend Projects:**
```
user-commands/ + go-backend-commands/ + backend-commands/ + go-backend-rules/
```

**For General Backend Projects (any language):**
```
user-commands/ + backend-commands/
```

**For DevOps Tasks:**
```
user-commands/ + devops-commands/
```

---

## Adding New Commands

Follow this classification when adding new commands:

### For Backend Development Commands:
1. **Is it Go-specific?** → `go-backend-commands/`
2. **Is it backend but language-agnostic?** → `backend-commands/`
3. **Is it DevOps/infrastructure?** → `devops-commands/`
4. **Is it project-agnostic and reusable?** → `user-commands/`
5. **Is it tightly coupled to a specific project?** → `project-specific-archived/`

---

## Repository Principles

### Backend-First Focus
- All commands and rules are optimized for backend development workflows
- Frontend-related commands are excluded
- Full-stack commands are not included (backend-only focus)

### Quality Standards
- Commands include clear steps, checklists, and best practices
- Each command is actionable and specific
- Examples provided for common use cases
- Security and performance considerations included

### Language Support
- Primary: Go backend development
- General: Language-agnostic backend patterns
- Documentation: English with technical precision

---

## Command Format

All commands follow this standard structure:

```markdown
# Command Title

## Overview
Brief description of purpose and when to use

## Steps
1. **Step Name**
    - Detailed sub-step
    - Specific actions
    
2. **Next Step**
    - More details

## Checklist
- [ ] Verifiable item
- [ ] Another checkpoint
```

---

## Notes

- Commands are designed for use with Cursor AI assistant and Claude
- Each command includes clear steps, checklists, and best practices
- Backend-specific commands prioritize security, performance, and scalability
- Commands should be language-agnostic unless in language-specific directories
- Regular updates ensure alignment with current backend best practices

---

## Repository Statistics

- **Backend Commands:** 6 (language-agnostic)
- **Go-Specific Commands:** 1
- **User Commands:** 36 (project-agnostic)
- **DevOps Commands:** 1
- **Total Active Commands:** 44
- **Backend Rules:** 9 (Go-focused)

---

## Contributing

When contributing to this repository:

1. Ensure commands align with backend development focus
2. Follow the directory classification guidelines
3. Update this README when adding new commands or categories
