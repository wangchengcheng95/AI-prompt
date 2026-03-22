# Task exploration levels (operative)

## Status

**Operative for phase 1.** When the user states how much discovery and alignment should precede execution, agents follow this playbook. Other collaboration dimensions (scope, urgency, blast radius, authority) are intentionally not adopted in phase 1 unless a later decision makes one operative.

## Purpose

Exploration here means **uncertainty reduction**: how much external research, user alignment, and up-front planning the agent should apply before and during edits. It is intentionally separate from raw change size or “complexity” labels.

## Recognizing a level

The user may use natural language or short tags, for example: `exploration low`, `explore high`, `low exploration`, or `L` / `M` / `H`. Map equivalent wording to the levels below.

## Levels

### Low

Use when the path is familiar, risk is low, and the user wants speed.

| Area | Expectation |
|------|-------------|
| External research | Repo-local reading first; hit authoritative sources only when a claim would be unsafe from memory (APIs, security, version-specific behavior). |
| User alignment | Prefer executing on the stated goal; at most one clarifying question if a material ambiguity blocks safe progress. |
| Planning | Keep internal; optional one-sentence intent—no standalone plan artifact unless the user asks. |
| Handoff | Standard `ready-to-merge` handoff; call out non-obvious assumptions briefly. |

### Medium (default when unstated)

Matches **Pre-Execution Due Diligence** and the default loop in `docs/agent-iteration-contract.md`.

| Area | Expectation |
|------|-------------|
| External research | For non-trivial work, consult authoritative sources before relying on memory or guesses. |
| User alignment | Spend interaction budget on decisions that materially change risk or scope; otherwise proceed with stated assumptions. |
| Planning | Produce a concise plan before editing when the task is non-trivial or multiple viable approaches exist. |
| Handoff | Standard contract handoff fields. |

### High

Use when facts are unclear, stakes are higher, or the user wants explicit alignment before large changes.

| Area | Expectation |
|------|-------------|
| External research | Start broad enough to reduce wrong-path risk; narrow iteratively. For facts about platform APIs, tool capabilities, or compatibility: (1) scan `references/repos.manifest.tsv` and read relevant local checkouts, (2) use WebSearch for authoritative online sources. Cite or link sources when conclusions affect behavior, security, compatibility, or migrations. |
| User alignment | Short structured check (goal, constraints, success criteria) before substantial edits unless the user clearly waived it. |
| Planning | Written plan before large or cross-cutting edits; incorporate user feedback if they engage. |
| Handoff | Explicit assumptions and residual unknowns; cite key sources where they drove decisions. |

## Default

If the user **does not** state an exploration level, treat the task as **medium** (existing contract behavior).

## Conflicts and shrinking

If a stated level is clearly disproportionate to the actual task (for example **high** exploration for a trivial typo), apply the contract’s **`shrink`**: use a proportional intensity, complete the slice, and state the adjustment in the handoff.

## See also

- Execution contract: `docs/agent-iteration-contract.md`
