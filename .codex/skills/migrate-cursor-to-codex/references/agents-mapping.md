# Agents Mapping

This migration converts Cursor agents into Codex multi-agent outputs.

## Fixed mappings

- `.cursor/agents/<name>.md` maps to `.codex/config.toml` and `.codex/agents/<role_id>.toml`.
- Role IDs use underscores, so `test-runner` maps to `test_runner`.
- The generated `.codex/config.toml` block uses `[agents.<role_id>]` with `description` and `config_file`.
- The generated `.codex/agents/<role_id>.toml` file contains `model` and `developer_instructions`.

## Classification rules

- An agent is `direct` only when it is a true delegated role with role-style instructions and a workflow.
- An agent is `transform` when its content is better represented as a skill.
- An agent is `discard` when it is purely Cursor-specific.

## Ownership

- `.codex/config.toml` uses `# codex-migrate:start:agents` and `# codex-migrate:end:agents`.
- `.codex/agents/<role_id>.toml` uses `# codex-migrate:owned source=...`.
- If `.codex/config.toml` exists without the managed agents block, the plan must report a conflict and apply mode must not write to it.
