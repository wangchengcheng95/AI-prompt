---
name: repo-doc-simplifier
description: Aggressively simplify one repo-maintenance document in this repository while preserving true constraints, decisions, scope, and stable facts. Use for root or docs/ maintenance files, not platform assets under platforms/.
---
# Repo Doc Simplifier

## Purpose

Aggressively simplify one repo-local maintenance document so it becomes shorter, clearer, and easier to maintain without changing its real meaning.

Use this skill only for maintaining this repository itself, typically in root docs or `docs/` maintenance files.

Do not use it for:

- `platforms/` assets
- `templates/` assets
- cross-document consolidation
- adding new policy or new scope

## Workflow

1. Identify the document's single job.
2. Keep only content that directly supports that job.
3. Remove repetition, filler, soft framing, and low-value background.
4. Merge overlapping sections and rewrite in shorter, more direct language.
5. Output the rewritten full document in Markdown.

## Keep

- active constraints and repository boundaries
- confirmed decisions and stable facts
- phase scope, sequencing, and minimum necessary structure

## Remove

- repeated explanations of the same point
- obvious restatements implied by nearby text
- long background that does not change action or interpretation
- decorative framing and filler words
- low-value examples
- bloated sectioning with many tiny headings

## Merge

- adjacent sections with the same practical purpose
- repeated scope statements
- closely related bullets or short paragraphs that read better as one point

## Guardrails

- Do not change facts, commitments, dates, or repository boundaries.
- Do not invent new requirements just to improve flow.
- Do not move content into other files by default.
- Do not expand the document with extra examples, rationale, or commentary.
- Do not simplify away distinctions between repo-local maintenance assets and archived platform assets.
- If a detail seems important but verbose, keep the meaning and compress the wording.

## Output

Return the rewritten full document directly.

Do not default to a plan, critique, or long explanation unless the user asks for one.
