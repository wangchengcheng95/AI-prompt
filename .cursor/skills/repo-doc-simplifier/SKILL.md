---
name: repo-doc-simplifier
description: Aggressively simplify one repository-maintained Markdown document while preserving true constraints, commands, paths, scope, and stable facts. Use when a root maintenance doc, a docs/ maintenance doc, or a Markdown asset under platforms/ has become repetitive, bloated, or harder to maintain, and you need a shorter rewrite without changing repo-local governance or downstream platform semantics.
---

# Repo Doc Simplifier

Simplify one repository-maintained Markdown document without changing its real meaning.

## Choose The Mode

- Use `repo-maintenance` mode for root maintenance files and `docs/` maintenance files that govern this repository itself.
- Use `platform-asset` mode for Markdown assets under `platforms/` that are consumed by other repositories or tools.

Do not use it for:

- `templates/` assets
- cross-document consolidation
- adding new policy or new scope

## Run The Simplification

1. Identify the document's single job.
2. Identify the audience: repo maintainer or downstream platform consumer.
3. Choose the correct mode and keep only content that directly supports the document's job for that audience.
4. Remove repetition, filler, soft framing, and low-value background.
5. Merge overlapping sections and rewrite in shorter, more direct language.
6. Output the rewritten full document in Markdown.

## Quick Keep Table

| Mode | Must keep | Why |
| --- | --- | --- |
| `repo-maintenance` | active constraints and repository boundaries | they define how this repository is maintained |
| `repo-maintenance` | confirmed decisions and stable facts | they anchor future maintenance choices |
| `repo-maintenance` | phase scope, sequencing, and minimum necessary structure | they preserve the intended maintenance flow |
| `platform-asset` | exact commands, paths, config keys, trigger phrases, and invocation semantics | downstream tools or repos may rely on them as an execution contract |
| `platform-asset` | platform-specific behavior that downstream consumers rely on | generalizing it can change how the asset is used |
| `platform-asset` | stable constraints, caveats, and execution order | they affect correct downstream execution and interpretation |
| `platform-asset` | distinctions between repo-local entrypoints and archived external assets when the document depends on them | removing them can blur asset ownership and usage boundaries |

## Remove

- repeated explanations of the same point
- obvious restatements implied by nearby text
- long background that does not change action or interpretation
- decorative framing and filler words
- low-value examples
- bloated sectioning with many tiny headings

## Merge Carefully

- adjacent sections with the same practical purpose
- repeated scope statements
- closely related bullets or short paragraphs that read better as one point

## Guardrails

- Do not change facts, commitments, dates, or repository boundaries.
- Do not invent new requirements just to improve flow.
- Do not move content into other files by default.
- Do not expand the document with extra examples, rationale, or commentary.
- Do not simplify away executable details such as commands, paths, config keys, or trigger words.
- Do not simplify away distinctions between repo-local maintenance assets and archived platform assets.
- Do not generalize platform-specific instructions just to make the wording shorter.
- If a detail seems important but verbose, keep the meaning and compress the wording.

## Output

Return the rewritten full document directly.

Do not default to a plan, critique, or long explanation unless the user asks for one.
