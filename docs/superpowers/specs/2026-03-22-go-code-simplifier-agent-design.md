# Go code-simplifier Cursor subagent — design spec

> **Consumer assumption (A):** AI-prompt is source of truth. Authoritative paths live under `platforms/cursor/.cursor/`. Downstream Go repositories copy or sync that tree into their own `.cursor/`.

> **Chosen approach:** **Plan 1** — add **only** a new subagent markdown file. **No** edits to `platforms/cursor/.cursor/skills/clean-code/SKILL.md`. **Authoring-time only:** the subagent’s system prompt is **synthesized from** the existing `clean-code` skill text and Anthropic’s `code-simplifier` agent prompt (see below); the **shipped** `go-code-simplifier.md` must be **self-contained** (no runtime dependency on loading the `clean-code` skill). The maintainer may remove `clean-code` later in a separate change if subagent-only workflow is preferred.

## Goal

Provide a **Cursor custom subagent** (see [Cursor Subagents](https://cursor.com/docs/context/subagents)) that refactors **Go** code for clarity and maintainability **without changing behavior**, suitable for bundles copied from this repository’s archived Cursor layout.

## Authoring process (required)

**Follow Cursor’s official `create-subagent` skill** when drafting the file: scope → create `.md` under `.cursor/agents/` → YAML front matter (`name`, `description`, plus optional `model`, `readonly`, `is_background` per [Cursor Subagents](https://cursor.com/docs/context/subagents)) → body as system prompt → validate by invoking the subagent in Cursor. The skill is bundled as **Creating Custom Subagents** (`create-subagent`); use it for description-writing guidance, examples, and the step-by-step workflow.

In **this** repository, the maintained file path is **`platforms/cursor/.cursor/agents/go-code-simplifier.md`** (project-level subagent in the archived bundle), equivalent to consumer repo **`.cursor/agents/go-code-simplifier.md`** after copy.

## Prompt sources (authoring-time synthesis)

When writing the system prompt body, **merge and adapt** (do not copy verbatim where it conflicts with Go):

| Source | Path in AI-prompt | Use for |
|--------|-------------------|---------|
| **clean-code** (Cursor skill) | `platforms/cursor/.cursor/skills/clean-code/SKILL.md` | Change radius / no drive-by refactors; readability & structure; DRY; comments (why not what); magic numbers & config injection |
| **code-simplifier** (Anthropic plugin agent) | `references/external/claude-plugins-official/plugins/code-simplifier/agents/code-simplifier.md` | Explicit **preserve functionality**; clarity over brevity; anti–nested-ternary / anti–dense one-liners; **balance** (avoid harmful over-simplification); default focus on **recently modified** scope unless user widens it |

**Adaptation rules:**

- Replace any TypeScript/React/`CLAUDE.md` bullet examples from the Anthropic prompt with **Go** norms and pointers to the **consumer** repo’s `AGENTS.md` / `CLAUDE.md`.
- Fold in **clean-code** constraints so the subagent does not expand scope without user consent.
- **Final deliverable:** one self-contained markdown file; no instruction in that file to “also apply the clean-code skill” as a separate step.

## Non-goals

- Do not modify `platforms/cursor/.cursor/skills/clean-code/SKILL.md` in this change set.
- Do not add hooks, plugins, or root `.cursor/` repo-maintenance assets.
- Do not require Claude Code or Anthropic plugin runtime in the consumer; artifact is plain `.cursor/agents/*.md` for Cursor.

## Architecture

| Piece | Location | Responsibility |
|-------|----------|----------------|
| New subagent | `platforms/cursor/.cursor/agents/go-code-simplifier.md` | System prompt + front matter for Go simplification pass |
| Existing skills | Unchanged | `clean-code` remains as-is until optionally deleted later |

**Relationship to other agents in the same bundle:** Complementary to `verifier` and `test-runner`: this agent focuses on **style/structure simplification under behavior preservation**, not primary test execution or end-to-end “claimed done” auditing. No requirement to reference those agents by name inside `go-code-simplifier.md` (optional one-line “after edits run tests” is allowed without creating a hard dependency).

## Subagent file shape

### Front matter (required fields)

- `name`: `go-code-simplifier` (distinct from upstream Anthropic plugin name `code-simplifier`).
- `description`: When to delegate / invoke — e.g. after edits to a bounded set of Go files, user wants readability cleanup without semantic change; mention explicit path scope.
- `model`: `inherit` (default) or `fast` — prefer `inherit` if simplification needs heavier reasoning; document in implementation that org/plan may override per Cursor docs.

Optional: omit `readonly` so the agent can apply edits; if read-only review is desired later, fork a separate agent (YAGNI for v1).

### Prompt body (outline)

The outline below is the **target merge** of clean-code + code-simplifier themes (Go-specific):

1. **Role:** Expert Go simplification; preserve observable behavior.
2. **Invariants:** No API/behavior change; keep exported symbols compatible unless user explicitly widens scope (out of v1 default).
3. **Scope guard:** Apply only within **agreed change radius**; no drive-by refactors; ask before expanding (from clean-code).
4. **Project standards:** Follow consumer repo’s `AGENTS.md` / `CLAUDE.md` / team conventions when present.
5. **Go conventions:** Align with [Effective Go](https://go.dev/doc/effective_go) and [Go Code Review Comments](https://github.com/golang/go/wiki/CodeReviewComments) — errors, `context`, interfaces, naming, zero values, goroutine safety where relevant.
6. **Style principles:** Clarity over brevity; reduce nesting and duplication; avoid nested ternaries / overly dense expressions in favor of explicit branches (from code-simplifier, mapped to Go); do not remove useful abstractions solely to shrink line count (balance).
7. **Comments & constants:** Self-documenting code; comment **why**; replace magic numbers with named constants / config where appropriate (from clean-code).
8. **Default scope:** Prefer **recently modified** Go files in the session unless the user lists explicit paths (code-simplifier pattern, aligned with radius).
9. **Process:** Identify target → simplify → run `go test` (scoped) → fix only simplification-induced breaks → summarize changes.
10. **Output:** Short summary of what was simplified and tests run; flag remaining risks.

## Error handling & verification

- **Mandatory:** Run relevant `go test` paths after edits (at minimum the touched packages); if tests fail, revert or fix without changing intended behavior.
- **Optional:** `go vet` on touched packages when appropriate.
- **Stop:** If behavior change is required to “simplify,” stop and ask — do not silently change semantics.

## Data flow

N/A (stateless agent; no new data stores). Invocation: user or parent Agent delegates via Cursor subagent mechanism per product behavior.

## Testing (of the asset itself)

- Manual: copy bundle into a sample Go repo, invoke subagent on a small diff, confirm tests pass.
- No automated test harness required in AI-prompt for v1 (YAGNI).

## Distribution

Maintainers edit `platforms/cursor/.cursor/agents/go-code-simplifier.md` in AI-prompt. Consumers copy `platforms/cursor/.cursor/` (or subset including `agents/`) into their repository `.cursor/`.

## Follow-up (outside this spec)

- **Implementation:** Use `writing-plans` then `executing-plans` / direct PR when ready.
- **Removal of `clean-code`:** Separate decision; not part of this change set.
