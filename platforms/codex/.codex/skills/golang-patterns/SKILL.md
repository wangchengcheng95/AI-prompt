---
name: golang-patterns
description: Idiomatic Go backend patterns for package design, error handling, context propagation, and concurrency safety.
---

# Go Backend Patterns

## When To Use

- Designing or refactoring Go backend code
- Reviewing handlers, services, and repositories
- Introducing concurrency, background work, or request-scoped I/O
- Tightening Go package boundaries before code review

## Package And API Shape

- Keep packages small, cohesive, and English-named.
- Accept interfaces at the boundary where they are consumed.
- Return concrete structs unless an interface return is truly required.
- Keep interfaces small and focused on one responsibility.
- Prefer constructors for wiring dependencies and operational config.

## Error Handling

- Never ignore returned errors.
- Wrap errors with operation context so callers know which step failed.
- Use `errors.Is` and `errors.As` when branching on wrapped errors.
- Keep error messages lowercase and without trailing punctuation.
- Use returned errors for recoverable failures; do not `panic`.

## Context And I/O

- Put `context.Context` first on request-scoped or I/O-heavy operations.
- Propagate context end-to-end through handler, service, and repository calls.
- Put explicit timeouts around network, database, and filesystem boundaries.
- Avoid `context.Background()` inside business logic.

## Concurrency

- Every goroutine needs an owner, cancellation path, and shutdown behavior.
- Prefer `errgroup.WithContext` for fan-out work that should cancel together.
- Protect shared maps and slices explicitly.
- Avoid sleep-based synchronization outside narrowly justified tests.

## Backend Layering

- Handlers handle transport and response shaping only.
- Services own business rules and orchestration.
- Repositories own persistence and query details.
- Keep SQL and storage-specific concerns out of handlers and services.

## Quick Review Prompts

- Are interfaces local and smaller than the concrete type they abstract?
- Are all error paths wrapped and still testable?
- Can every goroutine stop when the context is canceled?
- Would `go test -race` and `go vet` support the current design?
