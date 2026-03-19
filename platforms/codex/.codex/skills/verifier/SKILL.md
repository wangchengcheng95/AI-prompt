---
name: verifier
description: Verify implementation claims with evidence-first staged checks for Go backends, shell scripts, and Python execution scripts. Use when deciding whether a feature, fix, refactor, migration, or operational script change is truly done, especially before PRs or after touching write paths, retries, concurrency, cleanup, or remote side effects.
---

# Verifier

Verify the claimed change before sign-off. Prefer evidence over confidence.

## Core Stance

- Require evidence before marking anything as passed.
- Distinguish tool execution failures from design-risk failures.
- Start with the narrowest relevant verification, then broaden when risk justifies it.
- If a critical invariant or failure mode is broken, stop and report `NOT READY`.

## Run The Verification

1. Clarify what is claimed complete and which files or behaviors changed.
2. Inspect the implementation and determine verification mode: Go backend, shell script, Python script, or mixed.
3. Run the high-risk precheck when the change touches writes, concurrency, retries, migrations, cleanup, or destructive operations.
4. Run build or static checks for the relevant mode.
5. Run targeted tests first, then broaden when scope or risk justifies it.
6. Review security, regression, and diff risk.
7. Produce an evidence-backed report with pass, risk, or fail status.

## Run The High-Risk Precheck

Run this precheck before relying on test results when the change involves:

- Write operations or repeated execution with side effects
- Transactions, state transitions, retries, deduplication, or queue consumers
- Concurrency, background work, or shared mutable state
- Deletion, overwrite, migration, or remote system interaction

Check explicitly:

- Are the intended invariants still enforced?
- Are important failure modes handled rather than ignored?
- Does the write path remain idempotent when retries or duplicate requests are possible?
- Could concurrency introduce races, deadlocks, or partial writes?
- Is cleanup defined for temporary files, goroutines, locks, or external resources?

Abort and report `NOT READY` if any of the following are true:

- A critical invariant can be broken
- A key failure mode is unhandled
- Race, deadlock, or data corruption risk is plausible
- A write path needs idempotency but does not provide it
- Cleanup is missing and can leave resources or state behind

## Choose The Verification Mode

Choose the narrowest branch that matches the changed files or claimed behavior. In mixed repositories, do not run every language branch by default. Run additional branches only when the diff spans them or shared interfaces and risk make them relevant.

### Go Backend

Prefer repository-native commands when they exist. Otherwise use:

- Targeted package: `go test ./path/to/package`
- Broader suite: `go test ./...`
- Race coverage: `go test -race -count=1 ./...`
- Static analysis: `go vet ./...`
- Optional compile pass when useful: `go build ./...`

Check:

- Handler, service, and repository layering
- Context propagation, timeout handling, and cancellation
- Error wrapping and error classification
- Idempotency, retries, and transaction boundaries
- Goroutine ownership, shutdown, and shared-state safety

### Shell Scripts

Use:

- Syntax check: `bash -n path/to/script.sh` or `sh -n path/to/script.sh`
- Format drift: `shfmt -d path/to/script.sh`
- Lint: `shellcheck path/to/script.sh`
- Safe execution proof: run a dry-run path or minimal sample invocation when available

Check:

- Quoting, word splitting, and glob expansion hazards
- Explicit error handling discipline
- `trap` coverage and temporary file cleanup
- Dangerous `rm`, `mv`, `cp`, or redirect paths
- Clear exit codes and failure messaging

### Python Scripts

Use:

- Targeted tests first: `pytest path/to/tests_or_module`
- Broader suite: `pytest`
- Lint: `ruff check path/to/module_or_dir`
- Compile smoke test: `python -m compileall path/to/module_or_dir`
- Type check if the repository already uses one: `mypy path/to/module_or_dir` or `pyright path/to/module_or_dir`

Check:

- Argument and input validation
- Exception paths and non-zero exit behavior
- Timeout, retry, and cleanup behavior around file or network I/O
- Repeat-run safety for scripts with side effects

## Test Strategy

- Start with the narrowest tests that exercise the changed behavior.
- Run integration or end-to-end tests for the changed area when they exist.
- Expand to broader suites when the change crosses packages, boundaries, or risk domains.
- Call out missing tests, weak coverage, or unverified paths explicitly.
- Do not weaken tests just to produce a passing report.

## Review Security And Regression Risk

- Hardcoded secrets, credentials, or unsafe defaults
- Debug leftovers, temporary bypasses, or verbose output that should not ship
- Missing validation or authorization on externally reachable paths
- Dangerous filesystem or network operations without guardrails
- Configuration or script changes that alter behavior outside the claimed scope
- Unintended behavior changes
- Missing error handling or cleanup
- Design drift from the claimed implementation
- Silent contract changes, especially around writes, retries, and outputs

## Report Results

### Verification summary

**Passed:**
- ...

**Partial pass with risk:**
- ...

**Failed / not ready:**
- ...

### Evidence

- Mode: Go backend / shell / Python / mixed
- Commands run: ...
- Key results: ...

### Risk review

- Invariants: pass / risk / n/a
- Failure modes: pass / risk / n/a
- Concurrency: pass / risk / n/a
- Idempotency: pass / risk / n/a
- Cleanup: pass / risk / n/a

### Gaps and recommendations

- Missing edge cases: ...
- Insufficient error handling: ...
- Missing verification commands: ...
- Suggested additional tests: ...

## Rules

- Never mark work as passed without concrete evidence.
- If a required tool is missing, say exactly which tool is unavailable and how confidence is reduced.
- Prefer an explicit uncertainty note over guessing.
