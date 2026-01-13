# Cursor Commands

This directory contains organized Cursor AI commands categorized by scope and tech stack.

## Directory Structure

### `user-commands/` (35 commands)
**Scope:** Project-agnostic, reusable across most AI-assisted coding projects

Generic programming commands that work with any project or tech stack:

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

**Testing:**
- `write-unit-tests.md` - Create comprehensive unit tests
- `run-all-tests-and-fix.md` - Execute and fix test failures

**Security:**
- `security-audit.md` - Comprehensive security audit
- `security-review.md` - Security review with remediation

**Git & PR Management:**
- `git-commit.md` - Create focused commit messages
- `git-push.md` - Push and sync with remote
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

**Go Refactoring:**
- `go-backend-standards.md` - Go backend coding standards
- `go-refactor-conventions.md` - Go refactoring conventions
- `go-refactor-design.md` - Go refactoring design patterns

**Utilities:**
- `english-prompt-enforcement.md` - English prompt enforcement rules
- `refactor-cursor-commands.md` - Refactor cursor commands

### `go-backend-commands/` (1 command)
**Scope:** Go-specific backend development

- `add-error-handling.md` - Implement Go error handling patterns (explicit `if err != nil`, error wrapping, context usage)

### `backend-commands/` (2 commands)
**Scope:** General backend development (language-agnostic)

- `database-migration.md` - Create and manage database migrations
- `generate-api-docs.md` - Generate API documentation

### `devops-commands/` (1 command)
**Scope:** DevOps and infrastructure management

- `docker-logs.md` - Tail Docker container logs

### `frontend-commands/` (1 command)
**Scope:** Frontend/UI development

- `accessibility-audit.md` - Comprehensive WCAG accessibility audit

### `project-specific-archived/` (4 commands)
**Scope:** Project-specific commands (archived for reference)

Commands that are tightly coupled to a specific project and not easily reusable:
- `generate-device-protocol-docs.md` - Device protocol documentation
- `generate-mqtt-docs.md` - MQTT documentation
- `onboard-new-developer.md` - Project-specific onboarding
- `run-regression-tests-and-fix.md` - Project-specific regression tests

## Usage Recommendations

### For Most Projects
Start with `user-commands/` - these work across any project and tech stack.

### For Go Backend Projects
Use `user-commands/` + `go-backend-commands/` + `backend-commands/`

### For Frontend Projects
Use `user-commands/` + `frontend-commands/`

### For Full-Stack Projects
Use all relevant directories based on your tech stack.

## Adding New Commands

When adding new commands, follow this classification:

1. **Is it project-agnostic?** → `user-commands/`
2. **Is it Go-specific?** → `go-backend-commands/`
3. **Is it backend but language-agnostic?** → `backend-commands/`
4. **Is it frontend-specific?** → `frontend-commands/`
5. **Is it DevOps/infrastructure?** → `devops-commands/`
6. **Is it tightly coupled to your specific project?** → Keep in project root or archive

## Notes

- Commands are designed to be used with Cursor AI assistant
- Each command includes clear steps, checklists, and best practices
- Generic commands are preferred over project-specific ones for better reusability
- Tech-stack specific commands should be clearly documented with their dependencies
