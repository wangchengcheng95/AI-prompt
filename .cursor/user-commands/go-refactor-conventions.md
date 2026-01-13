# Go Refactor: Coding Conventions

## Overview

Refactor selected Go code to conform to Go coding conventions and engineering best practices. Produce idiomatic, production-ready Go code.

> **Portability:** Project-agnostic. Follows [Effective Go](https://go.dev/doc/effective_go) and [Go Code Review Comments](https://github.com/golang/go/wiki/CodeReviewComments).

## Target

- `$SELECTION` — Selected code, file(s), or folder to refactor

## Naming Conventions

| Element | Convention | Good | Bad |
|---------|------------|------|-----|
| Package | lowercase, short, no `_` | `repository` | `user_repository` |
| Interface | noun or `-er` suffix | `Reader`, `UserRepository` | `IReader` |
| Struct | CamelCase noun | `TemplateService` | `template_service` |
| Constructor | `New` + type | `NewUserService()` | `CreateUserService()` |
| Boolean | `is/has/can/should` | `IsValid`, `HasPermission` | `Valid` |
| Errors | `Err` prefix (sentinel) | `ErrNotFound` | `NotFoundError` |
| Context | `ctx` | `ctx context.Context` | `c`, `context` |

## File Organization

```
package → imports (stdlib / third-party / internal) → const → var → types → New* → exported methods → unexported methods → helpers
```

## Error Handling Rules

1. **Never ignore errors** — No `_ = doSomething()`
2. **Wrap with context** — `fmt.Errorf("operation: %w", err)`
3. **Guard clauses** — Return early on error, avoid deep nesting
4. **Use `errors.Is()` / `errors.As()`** — Not string matching

## Context Rules

1. First parameter: `ctx context.Context`
2. Pass to all I/O operations
3. **Never store in structs**
4. Use for cancellation and deadlines

## Function Design

| Rule | Target |
|------|--------|
| Function length | ≤50 lines |
| Nesting depth | ≤3 levels |
| Parameters | Use parameter object if >4 params |

## Go Idioms

- **Accept interfaces, return structs**
- **Use `defer` for cleanup** (file.Close, mutex.Unlock)
- **Use zero values** — Don't initialize to `0`, `""`, `nil`
- **Use `make()` with size hints** when capacity is known

## Layer Conventions

> Adapt to your project's architecture.

| Layer | Responsibility | Rules |
|-------|----------------|-------|
| Handler | HTTP/transport | Parse → validate → call service → format response. **No business logic.** |
| Service | Business logic | All business rules. First param `ctx`. Return errors, don't log. |
| Repository | Data access | Pure data operations. **No business rules.** Wrap DB errors. |

## Refactoring Checklist

### Naming
- [ ] Package names: lowercase, no underscores
- [ ] Interfaces: `-er` suffix or noun
- [ ] Constructors: `New*` prefix
- [ ] Booleans: `is/has/can/should` prefix
- [ ] Errors: `Err` prefix

### Structure
- [ ] File elements in correct order
- [ ] Imports grouped: stdlib → third-party → internal
- [ ] Functions ≤50 lines
- [ ] Nesting ≤3 levels

### Error Handling
- [ ] No ignored errors
- [ ] Errors wrapped with context
- [ ] Guard clauses (early returns)
- [ ] `errors.Is()` / `errors.As()` for checking

### Context
- [ ] First param is `ctx context.Context`
- [ ] Context passed to all I/O
- [ ] No context stored in structs

### Idioms
- [ ] Accept interfaces, return structs
- [ ] `defer` for cleanup
- [ ] Zero values used appropriately

## Output Format

1. **Violations found** — List of convention violations
2. **Refactored code** — Complete, compilable Go code
3. **Changes summary** — Brief description of each fix
