# Critique Phase

---

**Critically analyze the proposed design.**

## Instructions

Challenge the design by considering worst-case scenarios:

### 1. Concurrency Analysis
- Assume maximum concurrent operations
- Identify race conditions and deadlock potential
- Check for lost updates, dirty reads, phantom reads
- Verify locking strategies and isolation levels

### 2. Partial Failure Scenarios
- Assume operations can fail at any point
- Consider: network partitions, process crashes, timeouts
- Verify idempotency where required
- Check for orphaned resources or inconsistent states

### 3. Violated Assumptions
- List any implicit assumptions in the design
- Identify assumptions that may not hold under load
- Check for single points of failure
- Verify error handling completeness

### 4. Risk Assessment
- Rate risks by likelihood and impact
- Identify unhandled edge cases
- Check scalability bottlenecks
- Verify observability and debugging capabilities

## Output Format

List identified issues categorized by severity. For each issue, explain the scenario and potential impact. Suggest mitigations where applicable.
