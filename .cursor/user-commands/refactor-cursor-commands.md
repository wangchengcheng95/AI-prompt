# Refactor Cursor Commands

## Task Objective

Refactor command files in the `.cursor/commands` directory to adapt them to the current project. These commands may have been copied from other projects and contain a large amount of content that doesn't match the current project.

## Prerequisites

1. **Read Design Documentation** (`docs/design/`)
   - Understand the functionality and architecture of the entire codebase
   - Understand the project's tech stack, directory structure, and development standards
   - Master the project's core concepts and business logic

2. **Read Existing Commands** (`.cursor/commands/`)
   - Understand the content and structure of current command files
   - Identify which commands are generic and which are specific to other projects
   - Find commands that need to be deleted, modified, or added

## Refactoring Steps

### 1. Analyze Project Characteristics
- Determine project type (frontend/backend/full-stack)
- Identify tech stack (language, framework, tools)
- Understand project architecture (layers, modules, dependencies)
- Understand project-specific concepts and workflows

### 2. Categorize and Process Commands

**Delete Category**:
- Commands that don't match the project type (e.g., backend commands in frontend projects, or vice versa)
- Commands referencing tools/services specific to other projects
- Completely irrelevant commands

**Modify Category**:
- Generic commands but referencing wrong tech stack → Update to current tech stack
- Commands with correct content but wrong examples/paths → Update to current project structure
- Commands with correct logic but inaccurate naming/descriptions → Fix descriptions

**Add Category**:
- Project-specific features requiring dedicated commands
- Missing generic development workflow commands

### 3. Execute Refactoring

**Execute directly without confirmation**:
- Delete irrelevant command files
- Modify existing command file content
- Create new command files
- Ensure all commands are finally adapted to the current project

**Refactoring Principles**:
- Maintain command generality and reusability
- Ensure command descriptions accurately reflect the current project
- Update all examples, paths, and tool references
- Maintain consistent command file format

## Acceptance Criteria

After refactoring, all commands under `.cursor/commands/` should:
- ✅ Match the current project type and tech stack
- ✅ Reference tools, paths, and examples relevant to the current project
- ✅ Not reference specific concepts or services from other projects
- ✅ Have clear and accurate command descriptions
- ✅ Cover the main workflows required for project development

## Output Requirements

After refactoring is complete, briefly explain:
1. Which commands were deleted and why
2. Which commands were modified and what the main changes were
3. Which commands were added and why
4. Overview of the final command list
