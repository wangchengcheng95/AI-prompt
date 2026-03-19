# AI-Friendly Repo Task

## Status

- State: active
- Branch: `docs-ai-friendly-repo-positioning`
- PR status: not created
- Last updated: 2026-03-19

## Original Goal

Acknowledge that this repository is not only an archive of cross-platform AI assets, but also the working repository for human-and-AI collaboration where the user provides goals and the AI is expected to organize information, index knowledge, drive execution, and ask for decisions at the right points.

## Current Slice

Use the smallest stable change first:

- update the repository positioning to say the repository is AI-friendly for human-and-AI collaboration
- avoid premature information-architecture refactors
- keep broader AI-friendly repository design work in this task workspace until the direction is validated

## Current Status

- The canonical positioning now explicitly includes the repository's human-and-AI collaboration role.
- The stable change is intentionally small and does not yet redefine the standard docs set or task workflow.
- This task workspace is the aggregation point for later AI-friendly repository improvements.

## Confirmed Findings

- The existing repository contract strongly emphasizes asset boundaries and archive structure.
- The current docs do not yet treat AI-oriented information organization as a first-class repository design principle.
- `docs/tasks/` is now the correct home for multi-session work that needs continuity before stable conclusions are promoted.

## Follow-Up Work To Land Later

- Define what "AI-friendly" means in repository terms:
  - retrievable
  - explicitly indexed
  - decision-oriented
  - easy for AI to resume across sessions
- Identify which stable docs should later absorb confirmed conclusions:
  - `docs/system-overview.md`
  - `docs/architecture.md`
  - `docs/agent-iteration-contract.md`
  - `docs/decisions.md`
- Evolve task organization so task workspaces become easier for AI to resume and maintain.
- Evaluate whether repository-level indexes, decision ledgers, or promotion rules should be added after repeated use proves they help.

## Open Questions

- Which repository information should become explicitly index-first rather than narrative-first?
- How much of the future AI-friendly structure belongs in stable governance docs versus task workspaces?
- Whether the repo-local collaboration contract should later require stronger task aggregation and promotion rules.

## Promotion Targets

- Promote only validated, repeated conclusions into the standard docs set.
- Keep exploratory structure ideas inside this task workspace until they prove useful across real tasks.

## Next Session Entrypoint

- Re-open this task workspace first when continuing the AI-friendly repository thread.
- Decide whether the next slice is:
  - task workspace structure refinement
  - repository indexing rules
  - promotion rules from task workspaces into stable docs
