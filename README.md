# Backend AI Prompt Engineering

A curated collection of AI commands and rules specifically designed for **backend development workflows** using AI assistants (Cursor, Claude Code, etc.).

---

## What is This Repository?

This repository provides:
- **AI Commands**: Structured prompts for specific backend development tasks
- **AI Rules**: Guidelines that govern how AI assistants should behave in backend contexts
- **Quality Standards**: Best practices for backend development across languages and frameworks

### Backend-Only Focus

✅ **In Scope:**
- Backend API development (REST, GraphQL, gRPC)
- Database design, migrations, and optimization
- Server architecture and microservices
- Authentication, authorization, and security
- Performance optimization and monitoring
- DevOps and infrastructure management
- Testing strategies (unit, integration, e2e for backend)

❌ **Out of Scope:**
- Frontend development (React, Vue, Angular, etc.)
- Full-stack features mixing frontend and backend
- UI/UX design and client-side concerns

---

## Repository Structure

This repository uses a **two-level separation**:

### Level 1: Meta-Level (Managing This Repository)
**Directory**: `.cursor/commands/`

Commands for creating, testing, and optimizing the prompts in **this repository itself**:
- Creating new AI commands
- Testing command effectiveness
- Optimizing prompt quality
- Refactoring repository structure

**Use these when**: Working ON this repository (prompt engineering)

### Level 2: Application-Level (Backend Development)
**Directories**: `backend-commands/`, `go-backend-commands/`, `user-commands/`, `devops-commands/`, `go-backend-rules/`

Commands and rules for **actual backend development projects**:
- Language-agnostic backend commands (API design, database operations, CRUD, testing)
- Go-specific commands and rules
- Project-agnostic workflow commands (git, code review, security, testing)
- DevOps commands (Docker, deployment, monitoring)

**Use these when**: Working IN backend projects (software development)

📚 **See [.cursor/README.md](.cursor/README.md) for complete command inventory and detailed usage guide**

---

## Quick Start

### For Backend Developers

**Working on a Go backend project?**
```
Use: user-commands/ + backend-commands/ + go-backend-commands/ + go-backend-rules/
```

**Working on any backend project?**
```
Use: user-commands/ + backend-commands/
```

**DevOps tasks?**
```
Use: user-commands/ + devops-commands/
```

### For Contributors (Managing This Repository)

**Creating new commands:**
```
Use: .cursor/commands/create-ai-command.md
```

**Testing commands:**
```
Use: .cursor/commands/test-ai-command.md
```

**Optimizing prompts:**
```
Use: .cursor/commands/optimize-ai-prompt.md
```

---

## Repository Statistics

- **Total Active Commands**: 45
  - Meta-Commands: 4 (repository management)
  - Backend Commands: 6 (language-agnostic)
  - Go-Specific Commands: 1
  - User Commands: 34 (project-agnostic workflows)
  - DevOps Commands: 1
- **Backend Rules**: 9 (Go-focused)
- **Primary Language Support**: Go
- **General Support**: Language-agnostic backend patterns

---

## Key Principles

### Backend-First
All commands and rules are optimized for backend development workflows. No frontend or full-stack content.

### Clear Separation
- **Meta-level** (`.cursor/commands/`): Tools for managing this repository
- **Application-level** (other directories): Tools for backend development

### Quality Standards
- Commands include clear steps, checklists, and best practices
- Each command is actionable and specific
- Security and performance considerations included
- Examples provided for common use cases

### Precision Over Verbosity
- Concise, actionable instructions
- No unnecessary documentation
- Focus on what developers need

---

## Documentation

- **[.cursor/README.md](.cursor/README.md)** - Complete command inventory, detailed usage guide, and directory structure
- **[docs/REPOSITORY-GOALS.md](docs/REPOSITORY-GOALS.md)** - Detailed repository objectives, scope, and success criteria

---

## Command Format

All commands follow a standard structure:

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

## Language Support

- **Primary**: Go backend development (most detailed rules and commands)
- **General**: Language-agnostic backend patterns (applicable to any language)
- **Future**: Additional language-specific collections (Python, Java, Node.js)

---

## Contributing

When contributing to this repository:

1. Use `.cursor/commands/create-ai-command.md` to create new commands with proper structure
2. Use `.cursor/commands/test-ai-command.md` to validate commands before committing
3. Ensure commands align with backend development focus
4. Follow the directory classification guidelines in `.cursor/README.md`
5. Update `.cursor/README.md` when adding new commands or categories

---

## License

See [LICENSE](LICENSE) for details.
