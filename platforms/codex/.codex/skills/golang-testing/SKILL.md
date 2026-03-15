---
name: golang-testing
description: Go backend testing patterns for table-driven tests, race-safe verification, and pragmatic test-first development.
---

# Go Testing Patterns

## When To Use

- Adding or changing Go backend behavior
- Backfilling tests around bug fixes
- Verifying concurrency, retries, or error handling
- Reviewing whether a change is truly done

## Default Workflow

1. Prefer test-first when the expected behavior is clear.
2. Start with the narrowest relevant package or test target.
3. Add success, failure, and edge-case coverage before broad refactors.
4. Run broader verification after the targeted test passes.

## Test Structure

- Use table-driven tests for behavior with multiple input cases.
- Use subtests to keep scenarios readable and independently runnable.
- Keep assertions specific enough to show which behavior failed.
- Use `t.Helper()` in reusable test helpers.
- Keep unit tests deterministic and free of network or shared external state.

## Backend-Specific Checks

- Assert error wrapping and sentinel/type matching when errors matter.
- Verify context cancellation, timeout handling, and cleanup behavior.
- Test idempotency and retry-sensitive paths for write operations.
- Add race coverage for concurrent code and shared-state access.

## Useful Commands

- Targeted package: `go test ./path/to/package`
- Full backend verification: `go test -race -count=1 ./...`
- Coverage pass: `go test -cover ./...`
- Focused benchmark: `go test -bench=. ./...`

## Additional Guidance

- Add fuzz tests for parsers, decoders, and validation-heavy inputs when risk is high.
- Prefer fixing implementation bugs over weakening tests.
- If a test is integration-heavy, document the boundary and setup cost.
