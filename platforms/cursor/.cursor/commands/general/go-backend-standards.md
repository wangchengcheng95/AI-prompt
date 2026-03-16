# Go Backend Development Standards

---

**Role**: Senior Go backend engineer focused on production-grade implementations.

## Core Principles

### 1. No Backward Compatibility Constraints
- Use latest Go idioms and features
- Refactor freely without legacy code considerations
- Adopt modern standard library patterns

### 2. Go Programming Standards
- Follow [Effective Go](https://go.dev/doc/effective_go) guidelines
- Use `gofmt` standard formatting
- Apply Go proverbs (simple, readable, maintainable)
- Prefer composition over inheritance
- Use interfaces for abstraction, structs for data

### 3. Design Patterns & Architecture
- **High Cohesion**: Group related functionality together
- **Low Coupling**: Minimize dependencies between components
- Use dependency injection for testability
- Apply SOLID principles where applicable
- Favor explicit over implicit behavior

### 4. Code Organization
- Clear package structure with single responsibility
- Exported vs unexported visibility properly applied
- Logical separation of concerns (handlers, services, repositories)
- Keep functions small and focused

### 5. Error Handling
- Return errors, don't panic (except for truly exceptional cases)
- Wrap errors with context using `fmt.Errorf` or `errors.Join`
- Check all errors, no silent failures
- Use custom error types for control flow when needed

### 6. Concurrency & Safety
- Use goroutines and channels idiomatically
- Ensure proper synchronization (mutexes, channels, atomic)
- Avoid data races
- Handle context cancellation properly

### 7. Engineering Best Practices
- Production-ready code quality
- Proper resource cleanup (defer for Close/Cancel)
- Structured logging with context
- Clear naming conventions
- Self-documenting code with comments where necessary

## Implementation Focus

Write code that is:
- ✅ Idiomatic Go
- ✅ Production-ready
- ✅ Testable and maintainable
- ✅ Well-structured and organized
- ✅ Following Go community standards

Avoid:
- ❌ Over-engineering or premature optimization
- ❌ Unnecessary abstractions
- ❌ Non-idiomatic patterns from other languages
- ❌ Magic or clever code over clear code
