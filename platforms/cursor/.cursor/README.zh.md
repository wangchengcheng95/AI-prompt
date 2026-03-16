[English](README.md) | [中文](README.zh.md)

# 归档的 Cursor 资产

该目录存放本仓库维护的 Cursor 外部资产布局。

这里保留的是可分发到其他仓库或工作环境中的 Cursor 外部资产。仅用于维护本仓库自身的 Cursor 入口仍然位于根目录 `.cursor/`，不再与这些外部资产混放。

## 当前内容

- `agents/`
- `skills/`
- `commands/`
- `rules/`

## 载体定义

- `agents/`：Cursor 的角色型 agent 资产。
- `skills/`：可复用的 skill 目录，保持 Cursor 原生形态。
- `commands/`：Cursor 命令提示词，统一按领域分组放在一个载体下。
- `rules/`：Cursor 规则包，采用 `common/` 共享基线加语言覆盖层的组织方式。

## 说明

- 将该目录视为“被维护的外部资产”。
- 如果某项变更只服务于维护本仓库，请改根目录 `.cursor/`，不要改这里。
- 不要再新增 `xxx-commands`、`yyy-rules` 或 `archived/` 这类新的平级目录；新增资产必须落在上述载体之一。
