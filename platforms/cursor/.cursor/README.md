[English](README.md) | [中文](README.zh.md)

# Archived Cursor Asset

This directory stores the archived Cursor-facing asset layout maintained by this repository.

It contains the archived external Cursor asset set that can be copied into other repositories or workspaces. Repo-maintenance-only Cursor entrypoints remain in the root `.cursor/` directory and are intentionally not duplicated here.

## Contents

- `agents/`
- `skills/`
- `commands/`
- `rules/`
- `archived/`

## Carrier Definitions

- `agents/`: Cursor role-style agent assets.
- `skills/`: reusable skill directories that remain platform-native for Cursor.
- `commands/`: Cursor command prompts grouped by domain under one carrier.
- `rules/`: Cursor rule packs grouped by ruleset family.
- `archived/`: no-longer-primary content kept for reference only.

## Notes

- Treat this directory as archived external content under maintenance.
- If a change is meant only for maintaining this repository, put it in the root `.cursor/` directory instead.
- Do not add new peer directories such as `xxx-commands` or `yyy-rules`; place new assets under one of the carriers above.
