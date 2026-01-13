# Implementation Phase

---

**Implement the approved design.**

## Pre-Implementation Checklist

Before writing code, verify:

- [ ] All design constraints are understood
- [ ] Invariants are clearly defined
- [ ] Failure modes have mitigation strategies
- [ ] Critique phase issues are addressed
- [ ] API contracts are finalized

## Implementation Requirements

### 1. Code Structure
- Follow the approved design architecture
- Maintain clear separation of concerns
- Use appropriate design patterns

### 2. Constraint Enforcement
- Implement all invariant checks
- Enforce transaction boundaries as designed
- Add validation at system boundaries

### 3. Error Handling
- Handle all identified failure modes
- Implement proper error propagation
- Add context to errors for debugging
- Ensure no silent failures

### 4. Testing Considerations
- Write testable code
- Consider how to test failure scenarios
- Ensure observability hooks are present

## Output

Implement the code following all design constraints. Include inline comments explaining critical sections, especially invariant enforcement and failure handling.
