# Go code-simplifier subagent — implementation plan

> **For agentic workers:** Use `superpowers:executing-plans` (or implement inline with checkpoints). Steps use checkbox (`- [ ]`) syntax.

**Goal:** Add `platforms/cursor/.cursor/agents/go-code-simplifier.md`, a self-contained Cursor subagent for Go simplification under behavior preservation, per [design spec](../specs/2026-03-22-go-code-simplifier-agent-design.md).

**Architecture:** Single new markdown agent file; no changes to `clean-code` or other agents; prompt synthesized from spec + source prompts at authoring time.

**Tech stack:** Markdown, YAML front matter; consumer verification with `go test` / `go vet` in real Go repos (manual).

---

### Task 1: Confirm inputs

**Files:**

- Read: `docs/superpowers/specs/2026-03-22-go-code-simplifier-agent-design.md`
- Read: `platforms/cursor/.cursor/skills/clean-code/SKILL.md`
- Read: `references/external/claude-plugins-official/plugins/code-simplifier/agents/code-simplifier.md` (run `bash scripts/sync-references.sh --only claude-plugins-official` if missing)

- [ ] **Step 1:** Open the three paths above and confirm the spec “Prompt sources” table matches what you will merge.

- [ ] **Step 2:** Skim Cursor [Subagents](https://cursor.com/docs/context/subagents) and follow bundled **`create-subagent`** skill for front matter fields.

---

### Task 2: Add subagent file

**Files:**

- Create: `platforms/cursor/.cursor/agents/go-code-simplifier.md`

- [ ] **Step 1:** Create file with valid YAML front matter:
  - `name: go-code-simplifier`
  - `description:` specific trigger (bounded Go edits, clarity without behavior change); optional “use proactively” only if product noise is acceptable
  - `model: inherit` (or `fast` if team prefers; document in commit message if changed)

- [ ] **Step 2:** Write system prompt body (markdown after `---`) that is **self-contained** and covers spec sections: role, behavior preservation, scope guard / no drive-by, `AGENTS.md`/`CLAUDE.md`, Effective Go + Code Review Comments themes, clarity vs brevity + balance, comments/constants, default recent-files scope, process with `go test`, output summary. **Do not** reference or require the `clean-code` skill at runtime. **Do not** copy TS/React bullets from Anthropic; map to Go.

- [ ] **Step 3:** Keep prompt focused (avoid multi-thousand-word essays per `create-subagent` best practices).

---

### Task 3: Sanity check

**Files:**

- None (commands only)

- [ ] **Step 1:** Verify front matter parses (no tab-indent in YAML; `---` pairs closed).

- [ ] **Step 2:** Optional manual test: copy `platforms/cursor/.cursor/agents/go-code-simplifier.md` into a sample Go repo’s `.cursor/agents/`, invoke subagent on a small change, confirm `go test` on touched packages passes.

---

### Task 4: Commit (task branch)

- [ ] **Step 1:** `git status` — expect new/changed: `platforms/cursor/.cursor/agents/go-code-simplifier.md`, this plan file, optionally spec updates already committed separately.

- [ ] **Step 2:** Commit on a **task branch** (not `main` unless user allowed), English subject, e.g. `feat(platforms/cursor): add go-code-simplifier subagent`.

---

## Plan review

- Reviewer: human or plan-document-reviewer subagent with paths: this plan + design spec.
- After approval: choose **inline** vs **subagent-driven** execution per superpowers `writing-plans` handoff.
