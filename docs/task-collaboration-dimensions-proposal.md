# Task collaboration dimensions (archived reference)

## Status

This document **archives a proposed classification** for human–AI collaboration. It is **reference material only**: it does not, by itself, change agent behavior until linked from an operative contract or skill.

## 1. Exploration (uncertainty / discovery) — must we establish facts first?

- **Meaning**: Whether the task path is already known and whether external truth depends on retrieval or experimentation.
- **Drives behavior**: Whether to consult documentation or online sources, whether to run a small spike, and whether conclusions should cite sources.
- **Relation to “complexity”**: A task can be complex with a known path → exploration can stay low; a task can be simple but depend on external facts → exploration should be high. A single “complexity” label therefore blurs with this dimension. If only one label is kept, **exploration plus scope** is a clearer replacement for vague “complexity.”

## 2. Scope / decomposition — how much work and how many steps

- **Meaning**: Size of change, number of subtasks, and whether milestones are needed—not “how hard” it is intellectually.
- **Drives behavior**: Whether to produce a plan before editing, whether to split across PRs or phases, and single-turn versus multi-turn delivery.
- **Industry intuition**: Close to structural workflow complexity; related to how deep the model must reason, but **not identical** to reasoning depth.

## 3. Urgency — how fast a result is needed and how long discussion can run

- **Meaning**: Deadlines, whether other work is preempted, and whether “stop the bleeding first, refine later” is acceptable.
- **Drives behavior**: Time boxes, caps on discussion rounds, and whether **assumptions-first** work is allowed with **explicitly listed risks**.
- **Suggestion**: Prefer **P0 / P1 / P2** or **today / this week / backlog** over a vague “high priority,” which is often conflated with **importance**.

## 4. Blast radius / safety — cost if something goes wrong (recommended as its own axis)

- **Meaning**: Production impact, security, privacy, money, compliance, irreversible migrations, and similar exposure.
- **Drives behavior**: Checklists, rollback or canary paths, least privilege, audit trails; at high risk, **no silent execution** or **mandatory confirmation** before irreversible steps.
- **Why separate**: The same “small change” in production versus a scratch repo should follow **different** processes; blast radius cannot be read from “complexity” alone.

## 5. Authority / sign-off — who may decide

- **Meaning**: Which choices require explicit human approval (architecture, product copy, external commitments, data deletion).
- **Drives behavior**: Default assumptions versus **pause and ask**; deliverable is a **recommendation** versus an **implementation ready to merge**.
- **Applicability**: Stronger when multiple people or external/legal sensitivity exists; for solo work, can fold into default rules.

## Read more

- Repository maintenance contract: `docs/agent-iteration-contract.md`.
