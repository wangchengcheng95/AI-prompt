# Verification Phase

---

**Verify implementation against engineering principles.**

## Instructions

Review the implementation and check compliance:

### 1. Design Adherence
- [ ] All design constraints are implemented
- [ ] Invariants are properly enforced
- [ ] Transaction boundaries match the design
- [ ] Failure modes are handled as specified

### 2. Engineering Principles
- [ ] **Correctness**: Logic is sound and handles edge cases
- [ ] **Safety**: No data loss or corruption possible
- [ ] **Consistency**: Invariants cannot be violated
- [ ] **Idempotency**: Retry-safe where required
- [ ] **Atomicity**: Operations are properly bounded
- [ ] **Error Handling**: All errors are caught and handled
- [ ] **Observability**: Sufficient logging and metrics

### 3. Code Quality
- [ ] Clear naming and structure
- [ ] No unnecessary complexity
- [ ] Proper resource cleanup
- [ ] Thread-safety where required

### 4. Risk Analysis
- [ ] No unhandled concurrency issues
- [ ] No single points of failure introduced
- [ ] Performance bottlenecks identified
- [ ] Security considerations addressed

## Abort Conditions

**If ANY of the following are violated, ABORT and explain:**
- Critical invariants can be broken
- Unhandled failure modes exist
- Race conditions or deadlocks are possible
- Data corruption scenarios are unaddressed
- Design constraints are not met

## Output Format

Provide a checklist of verification results. For any violations, explain the issue clearly and suggest fixes.
