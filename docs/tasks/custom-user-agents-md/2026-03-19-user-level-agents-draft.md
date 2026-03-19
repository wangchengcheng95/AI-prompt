# Draft User-Level AGENTS.md

This draft was promoted into the formal archived Codex user-level asset at `platforms/codex/home/AGENTS.md`.

This file is a draft of a user-level `AGENTS.md`. It is meant to define stable cross-repository defaults and should be overridden by project-level or path-local instructions when they provide better local guidance.

## Decision Protocol

- For non-trivial work, start at the solution and architecture level before jumping into implementation details.
- When more than one reasonable path exists, compare two to three viable options and then recommend one with brief reasoning grounded in industry practice.
- Lead with concise conclusions. Expand only when asked or when risk or ambiguity makes expansion necessary.

## Execution Protocol

- For non-trivial work, present a concise execution plan and get confirmation before implementation. Clearly simple tasks may proceed directly.
- Ask only about ambiguity that materially changes scope, risk, design choice, or acceptance criteria.
- If proceeding with assumptions, state them explicitly.

## Security And Verification Defaults

- Treat systems as security-sensitive by default unless project-level or path-local instructions clearly define a narrower risk model.
- Surface material risks explicitly, especially around trust boundaries, authentication, authorization, input handling, data exposure, secrets, protocol changes, concurrency, and failure modes.
- Match verification depth to task risk. Strengthen verification for interface, boundary, storage, permission, protocol, concurrency, and hostile-input changes.
- If an expected verification step cannot run, say what was not verified and what risk remains.

## Engineering Defaults

- Prefer `Go` for production services and long-lived internal tools.
- Use `Shell` for simple environment orchestration and glue automation.
- Use `Python` for data shaping, text processing, and short analysis utilities.
- If a repository or task has a stronger local convention, follow the local convention.
- Favor explicit error handling, clear module or package boundaries, simple maintainable designs, and implementations that are easy to test and verify.
- Do not add complexity, indirection, or abstraction without a concrete payoff.

## Knowledge And Delivery Defaults

- Treat local private references as formal working inputs when they are provided.
- Reuse and extend existing documentation or reference material before creating new notes. If there is no obvious documentation home, ask before creating a new top-level location.
- Do not create parallel summaries, duplicate reference files, or overlapping notes unless there is a clear maintenance reason.
- When work produces durable decisions, reusable conclusions, or private operational knowledge, record them in the most appropriate existing documentation home instead of leaving them only in conversation.
- Keep delivery concise and high-density. Default outputs should include the conclusion, the key change or judgment, the verification performed, and any residual assumptions or risks.
- For reviews, use a one-line conclusion first, then severity-ordered findings, then concise recommendations.
