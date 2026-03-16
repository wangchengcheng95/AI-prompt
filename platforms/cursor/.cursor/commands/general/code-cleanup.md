# Code Cleanup

## Overview

Clean up generated code by removing redundant/intermediate code, ensuring engineering doctrine compliance, and applying clean code principles. This command should be used after code generation to ensure production-ready Go code.

## Steps

1. **Remove Redundant Code**
   - Remove unused variables/functions/types/imports
   - Remove commented-out code (unless documenting important alternatives)
   - Remove debug prints/temporary logging
   - Consolidate duplicate logic
   - Remove dead code paths
   - Remove development scaffolding

2. **Verify Engineering Doctrine Compliance**
   - **Errors**: Capture all errors, wrap with `fmt.Errorf("op: %w", err)`, use typed errors
   - **Context**: All I/O accept `context.Context` as first param, propagate end-to-end, goroutines handle cancellation
   - **Concurrency**: Managed goroutines only (use `errgroup.WithContext`), no `time.Sleep` for sync (tests only)
   - **Layers**: Service=logic only (no SQL/HTTP/logging), Repository=data only (no business logic), Handler=transport only

3. **Apply Clean Code Principles**
   - Use meaningful English names
   - Keep functions small and single-purpose
   - Remove redundant comments (keep comments explaining "why")
   - Replace magic values with named constants
   - Remove unused imports, group stdlib/external/internal, no dot imports

4. **Final Verification**
   - Ensure no error checks or validation were removed
   - Ensure clarity wasn't sacrificed for brevity
   - Ensure behavior wasn't changed

## Checklist

- [ ] Removed all unused code and imports
- [ ] Removed debug/temporary code
- [ ] All errors captured and wrapped with context
- [ ] All I/O functions accept `context.Context`
- [ ] No unmanaged goroutines
- [ ] Layer boundaries respected (Service/Repository/Handler)
- [ ] Code follows clean code principles
- [ ] Imports optimized and grouped
- [ ] No behavior changes introduced

## Keep

- All error handling paths
- Defensive checks
- Edge case code
- Intentional validation
