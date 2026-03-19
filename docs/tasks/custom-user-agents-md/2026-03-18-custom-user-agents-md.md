# Customized User-Level AGENTS.md Task

## Status

- State: promoted to formal asset
- Current phase: formal asset review and handoff
- Priority order: `solution and architecture analysis > independent execution > knowledge organization`
- Branch: `custom-user-agents-md`
- PR status: do not create yet
- Last updated: 2026-03-19

## Goal

Define the stable content for a personalized user-level `AGENTS.md` that matches the user's role, work habits, technical stack, and information constraints before choosing the final adaptation format.

## Current Draft Artifact

- Draft file: `docs/tasks/custom-user-agents-md/2026-03-19-user-level-agents-draft.md`
- Draft status: promoted into the formal Codex user-level asset at `platforms/codex/home/AGENTS.md`
- Next refinement focus: documentation and knowledge-handling defaults rather than boundary/failure-path rules

## Current Outcome

- A first actual user-level `AGENTS.md` draft now exists and has been promoted into the formal Codex user-level asset.
- The drafting direction has been corrected from profile-driven narration to constraint-driven engineering defaults.
- Public guidance links for future `AGENTS.md` work have been refreshed and the repository rule now requires checking them first and then re-searching for newer or more authoritative sources.
- The task has reached the formal-asset stage and is paused before commit or PR creation.

## Recommended Next Step

- Review `platforms/codex/home/AGENTS.md` as the primary artifact.
- Decide whether the next iteration should:
  - refine one or two remaining engineering defaults
  - simplify wording without changing the rule set
  - commit the current repository changes

## Accepted Slice

This kickoff slice is intentionally narrow:

- start the task on a dedicated branch
- record the current understanding, assumptions, and TODOs
- keep the work in discovery and documentation mode
- defer PR creation until the content direction is mature enough for review

## Drafting Correction

The current task has a confirmed drafting correction:

- the future document should not preserve raw user biography or role labels unless they imply a concrete engineering constraint
- inputs such as language, product domain, private-document workflow, and working style should be translated into general software-engineering rules
- the final user-level `AGENTS.md` should be constraint-driven, not profile-driven
- the target should be a thin but constrained engineering profile, not either an ultra-thin collaboration note or a full personal engineering handbook

## Derived Engineering Constraints

The currently known inputs imply these more general engineering constraints:

- primary work happens in backend and platform-style systems, so the document should favor service reliability, explicit interfaces, operational clarity, and maintainable change scope
- the problem domain is security-sensitive, so the document should favor defensive defaults, explicit risk surfacing, stronger verification on boundary changes, and careful handling of failure paths
- the main implementation language is `Go`, so production code rules should favor idiomatic Go simplicity, explicit error handling, clear package boundaries, and concurrency safety
- scripting exists to support engineering work, so the document should favor task-shaped language selection rather than forcing one scripting language for every job
- the work includes solution design and requirement breakdown, so the document should optimize for architectural reasoning and trade-off analysis, not only code generation
- important working material may exist only in local private references, so the document should treat local project references as first-class inputs when they are provided

## Collaboration Preferences

- lead with concise conclusions and expand only on request
- compare two to three viable options before recommending one
- confirm the plan before execution starts
- use a mixed review format: one-line conclusion, severity-ordered findings, concise recommendations
- when asking for a decision, provide an industry-best-practice recommendation and brief reasoning
- use limited questioning and ask only when uncertainty changes scope, risk, design choice, or acceptance criteria
- use concise high-density delivery rather than long process narration

## Working Assumptions

- The task should stay content-first for now and should not lock into a final file format too early.
- The eventual personalized `AGENTS.md` should optimize first for architecture and solution analysis, second for independent execution, and third for knowledge organization.
- Local private references should be treated as first-class sources when they exist.
- The future document should not over-specify conflict handling between private references and other sources because the user does not expect that scenario to occur in normal work.
- The future document should constrain durable collaboration behavior instead of acting like a one-off prompt.
- The future document should not preserve every balanced preference as a separate rule; it should keep only the stable defaults that reduce model drift, avoid rework, or capture user-specific working style.
- No PR operations should happen during this kickoff phase.

## Candidate Content Areas

- user role and decision scope
- default technical stack and tool preferences
- medium-strength code quality expectations
- scripting language decision rules by task type
- information source priority and medium-strength private reference handling
- default task decomposition behavior
- limited-question clarification rules
- architecture comparison and recommendation style
- reasoning and assumption disclosure requirements
- concise high-density reporting expectations
- iteration, review, and refinement expectations
- verification depth by task risk
- reporting style for plans, trade-offs, progress, and results
- stop conditions and when the agent must ask before proceeding

## Initial Language Recommendation Hypothesis

Use task-shaped defaults instead of a single script language rule:

- prefer `Go` for production services and long-lived internal tools
- prefer `Shell` for environment orchestration and simple glue automation
- prefer `Python` for data shaping, text processing, and short analysis utilities

This remains a hypothesis until the user confirms whether it matches actual practice and team expectations.

## Verification Baseline Hypothesis

Use a risk-tiered medium-to-high verification baseline:

- design and planning work is not complete without assumptions, boundaries, main risks, option comparison, and a recommendation
- normal code changes should at least pass the most relevant local implementation-level verification
- interface, storage, permission, protocol, or security-control changes should default to stronger integration-oriented verification
- Go changes involving concurrency or shared state should default to `go test -race` or an equivalent concurrency check
- input-heavy or security-sensitive changes should prefer boundary, adversarial, and when appropriate fuzz-style validation
- if an expected verification step cannot run in the current environment, the gap must be stated explicitly with the remaining risk

## External Research Findings

### 1. The strong sources agree on a small core

The strongest cross-tool sources converge on a small set of things that make instruction files useful:

- give executable commands, not only preferences
- encode concrete boundaries, not vague intentions
- keep instructions short, local, and directly actionable
- use nested or path-local instructions when context differs by subtree

This is consistent across:

- OpenAI Codex documentation
- the `agents.md` open format site
- GitHub Copilot documentation
- GitHub's analysis of more than 2,500 public `agents.md` files

### 2. This directly supports the user's correction

The external sources do not support filling a user-level `AGENTS.md` with narrative role description unless that description turns into concrete recurring constraints.

The useful transformation is:

- input: language, system type, security sensitivity, private-reference workflow
- output: code-quality rules, verification thresholds, decision protocol, file boundaries, and reusable commands

### 3. Public examples relevant to the user's scene

Two public Go and backend-oriented examples were especially useful:

- `temporalio/temporal` uses a root `AGENTS.md` to encode explicit commands, error-handling expectations, test workflow, regeneration rules, and review/communication constraints
- `BishopFox/sliver` uses a much shorter file that still encodes build commands, Go coding rules, architectural boundaries, and testing guidance

The contrast is useful:

- Temporal shows what a mature service backend repo tends to encode when the project wants a strong operating manual
- Sliver shows that even a concise file can still be useful when it focuses on commands, code constraints, and boundaries

### 4. Implications for the future user-level file

The future personalized user-level `AGENTS.md` should probably:

- avoid biography-style role description
- encode only stable software-engineering defaults that would apply across repositories
- bias toward constraints such as error handling, architecture-first decision flow, verification depth, boundary changes, and knowledge-source handling
- avoid turning into a generic writing-style or personality file

### 5. Open design consequence

The external evidence suggests the future user-level file should stay small and high-signal.

Detailed stack commands, repository structure, and path-specific boundaries are usually better placed in project-level or nested files, not in the user-level file.

The user's current preferred direction matches this:

- keep the user-level file thin
- preserve a small number of stable engineering constraints that apply across repositories
- treat security sensitivity as a user-level soft default that project-level or path-local instructions may tighten or relax when needed
- treat language and engineering style as user-level soft defaults that project-level or path-local instructions may override when needed
- treat local private references as a medium-strength formal input rule across repositories

## Constraint-Driven Skeleton

### 1. Engineering Context

The future user-level `AGENTS.md` should express only the constraints that matter repeatedly:

- backend and platform engineering context
- security-sensitive systems context as a soft default
- `Go` as the primary production language and task-shaped scripting defaults as soft defaults
- local private references as valid working inputs

### 2. Decision Protocol

The future document should encode:

- concise conclusion first
- two to three options before recommendation
- recommendation plus brief reasoning when a decision is needed
- architecture and solution analysis before premature implementation detail

### 3. Execution Protocol

The future document should encode:

- plan confirmation before non-trivial execution, while allowing direct handling of clearly simple tasks
- limited questioning for materially important ambiguity only
- explicit assumptions when continuing without asking

### 4. Quality Protocol

The future document should encode:

- concrete code-quality rules derived from backend, security, and `Go` constraints
- risk-tiered medium-to-high verification
- stronger checks for interface, storage, protocol, permission, concurrency, and hostile-input changes

### 5. Knowledge Protocol

The future document should encode:

- local private references as formal inputs when they are provided
- when to use or extend local references
- when to avoid duplicate note creation
- what belongs in the user-level file versus project-local or task-local documents

### 6. What Still Needs To Be Made Explicit

The current skeleton still needs concrete wording for:

- the smallest concrete code-quality rules worth enforcing repeatedly
- the smallest concrete `docs/references` rules worth enforcing repeatedly
- the boundary between user-level stable rules and project-level or task-level supporting documents
- the final adaptation format once the content is stable

## Pruning Pass

### Keep As Explicit Rules

These items are strong candidates to survive into the final user-level `AGENTS.md` because they meaningfully reduce behavioral drift:

- bias toward solution and architecture analysis before jumping into execution details
- treat systems as security-sensitive by default unless project-local instructions clearly narrow the risk model
- confirm the plan before non-trivial execution starts, while allowing direct handling of clearly simple tasks
- compare two to three viable options before recommending one
- when asking for a decision, provide the recommended option and brief industry-based reasoning
- use limited questioning and ask only when uncertainty changes scope, risk, design choice, or acceptance criteria
- use a mixed review format: one-line conclusion, severity-ordered findings, concise recommendations
- use concise high-density delivery rather than long process narration
- use risk-tiered medium-to-high verification and state unverified gaps explicitly
- treat local private references as first-class working inputs

### Compress Into Fewer Rules

These items should probably remain in the final direction, but only after being compressed into fewer and more concrete rules:

- backend, security, and `Go` inputs should be translated into a short set of concrete engineering rules
- `Go`, `Shell`, and `Python` preferences should become one task-shaped language selection rule with soft-default wording
- medium-strength `docs/references` expectations should become a short set of rules for reuse, extension, and avoiding duplicate notes
- concise-conclusion-first and high-density reporting should likely become one communication block

### Keep As Background, Not Final Rules

These items are useful during discovery but are weak candidates for the final user-level `AGENTS.md` as standalone instructions:

- the raw priority ordering `solution and architecture analysis > independent execution > knowledge organization`
- narrative role descriptions such as specific job title or product examples without derived engineering constraints
- the note that source-conflict handling is not worth over-specifying
- the current task branch, kickoff state, and no-PR-yet status
- placeholder phrases such as "medium-strength" without the concrete rules they are meant to summarize

## Candidate Core Rule Set

The current best candidate for the future user-level `AGENTS.md` is a five-rule core:

1. For non-trivial work, analyze the problem at the solution and architecture level first, compare two to three viable options, and give a recommended path with brief reasoning.
2. For non-trivial work, confirm the execution plan before implementation; ask only about ambiguity that materially changes scope, risk, design choice, or acceptance criteria, and otherwise continue with explicit assumptions.
3. Treat systems as security-sensitive by default unless project-level or path-local instructions clearly narrow the risk model; surface risks explicitly and strengthen verification for boundary, interface, permission, protocol, concurrency, and hostile-input changes.
4. Use language and engineering defaults as soft defaults: prefer `Go` for production and long-lived tooling, choose `Shell` or `Python` by task shape for scripting, and favor explicit error handling, clear boundaries, simple maintainable design, and verifiable implementations.
5. Treat local private references as formal working inputs when they are provided; prefer reuse and extension over duplicate notes, and keep delivery concise, high-density, and reviewable.

## Why This Core Is Small Enough

This candidate set is intentionally compact:

- decision protocol is merged into one rule
- execution and clarification are merged into one rule
- security posture and verification depth are merged into one rule
- language defaults and engineering-quality expectations are merged into one rule
- knowledge handling and delivery style are merged into one rule

This keeps the user-level file thin while still expressing the user's stable cross-repository defaults.

## TODO

- decide whether the five-rule core is the right final size or should be reduced further
- refine the wording of each rule so it reads like stable user-level instruction text rather than design notes
- decide what should stay in the user-level file versus move to project-level or nested instruction files
- draft the first actual user-level `AGENTS.md` text once the core rule set is accepted

## Open Questions

- Is the five-rule core the right size for the future user-level `AGENTS.md`, or should it be reduced to four rules?
- Does the current rule grouping preserve enough signal without hiding an important constraint that should remain separate?

## Progress Log

- 2026-03-18: reviewed the repo-local maintenance instructions, the repo self-iteration contract, the brainstorming skill, and the AGENTS writing guidance.
- 2026-03-18: classified the kickoff slice as accepted and bounded.
- 2026-03-18: created task branch `custom-user-agents-md`.
- 2026-03-18: created this task tracker under `docs/tasks/` to record scope, status, and TODOs before any PR work.
- 2026-03-18: captured the user's collaboration preference to lead with concise conclusions and expand only on request.
- 2026-03-18: captured the user's preference to compare two to three viable options before receiving a recommendation.
- 2026-03-18: captured the user's preference to confirm the plan before execution starts.
- 2026-03-18: captured the user's preferred review format as one-line conclusion, severity-ordered findings, and concise recommendations.
- 2026-03-18: confirmed that the future document should avoid heavy rules for source-conflict scenarios because the user does not expect them in normal work.
- 2026-03-18: captured the user's preference that future choice prompts should include an industry-best-practice recommendation first.
- 2026-03-18: selected a risk-tiered medium-to-high verification baseline as the default delivery standard.
- 2026-03-18: selected medium-strength code quality rules instead of either minimal or exhaustive style constraints.
- 2026-03-18: selected medium-strength `docs/references` guidance focused on usage rules and creation boundaries rather than a detailed taxonomy.
- 2026-03-18: selected limited questioning as the default clarification strategy.
- 2026-03-18: selected concise high-density reporting as the default delivery format.
- 2026-03-18: synthesized the confirmed preferences into a structured instruction skeleton for the future user-level `AGENTS.md`.
- 2026-03-18: added a pruning principle to avoid keeping every balanced preference as a separate rule in the final document.
- 2026-03-18: completed a first pruning pass to separate rules to keep, compress, and leave as background context.
- 2026-03-18: corrected the drafting direction to favor derived engineering constraints over raw user-profile narration.
- 2026-03-18: confirmed with the user that the constraint-driven drafting direction is closer to the intended outcome.
- 2026-03-19: completed a first round of external web research across OpenAI, AGENTS.md, GitHub Copilot, GitHub Blog, and public Go/security-oriented repositories.
- 2026-03-19: updated `references/agents-writing-guides.md` with current public guidance links and strengthened the repository rule to re-check for newer or more authoritative sources before future `AGENTS.md` drafting.
- 2026-03-19: confirmed the target shape as a thin but constrained engineering profile for the future user-level `AGENTS.md`.
- 2026-03-19: selected security-sensitive handling as a user-level soft default rather than either omitting it or making it an unoverrideable hard rule.
- 2026-03-19: selected language and engineering-style defaults as user-level soft defaults rather than project-only guidance.
- 2026-03-19: selected local private references as a medium-strength formal input rule for the future user-level `AGENTS.md`.
- 2026-03-19: selected explicit plan confirmation for non-trivial tasks as a user-level default execution rule.
- 2026-03-19: condensed the current decisions into a five-rule candidate core for the future user-level `AGENTS.md`.
- 2026-03-19: drafted the first actual user-level `AGENTS.md` text under `docs/tasks/2026-03-19-user-level-agents-draft.md`.
- 2026-03-19: user confirmed that the current draft direction is right and already close to usable.
- 2026-03-19: user chose to improve the draft by adding a small number of more concrete engineering constraints rather than compressing it further.
- 2026-03-19: user selected documentation and knowledge handling as the next area for adding a more concrete cross-repository constraint.
- 2026-03-19: selected "reuse before creating new documentation" as the next concrete knowledge-handling rule to fold into the draft.
- 2026-03-19: added a second concrete knowledge-handling rule to the draft: durable decisions and reusable conclusions should be recorded in an appropriate documentation home instead of remaining only in conversation.
- 2026-03-19: promoted the reviewed draft into `platforms/codex/home/AGENTS.md` as the formal archived Codex user-level asset.
