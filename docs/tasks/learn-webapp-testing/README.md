---
task_id: learn-webapp-testing
title: Learn web application testing (practical stack)
status: proposed
priority: high
kind: research
branch: null
issue: null
last_updated: 2026-03-21
next_step: "Pick one stack (for example Playwright or Cypress + your framework); complete the official getting-started tutorial and run one smoke test against a local dev server."
promotion_targets:
  - templates/
  - platforms/
---

# Learn web application testing

## Status

- State: proposed (owner learning track)
- Branch: none unless you add templates or platform assets to this repository
- Last updated: 2026-03-21

## Original Goal

Build hands-on competence in **webapp testing**: local E2E or integration tests, stable selectors, CI-friendly runs, and clear failure signals—not tied to any single vendor tutorial.

## Current Slice

- Choose baseline tooling (browser automation + test runner) for a project you actually run.
- Complete upstream getting-started documentation once.
- Add or extend one smoke test that starts the app (or hits a fixed URL), performs one critical user path, and exits non-zero on failure.

## Current Status

- Task registered; no stack choice or commands recorded here yet.

## Confirmed Findings

- None yet; this repository does not mandate a single web stack—learning notes stay task-local until you promote a template.

## Open Questions

- Target project: greenfield, this repo’s future web surface, or an external codebase?
- Headless CI only versus local headed debugging workflow?

## Promotion Targets

- Reusable, tool-neutral starter patterns → `templates/` if you decide they belong in this archive.
- Tool-specific maintained snippets → `platforms/<tool>/` per asset-boundary rules.

## Next Session Entrypoint

1. Write your chosen stack and version constraints under **Confirmed Findings**.
2. Link the official quickstart you followed (URL in plain text).
3. Record the exact command you run for a green local test pass.
