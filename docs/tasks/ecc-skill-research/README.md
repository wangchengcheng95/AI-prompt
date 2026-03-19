---
task_id: ecc-skill-research
title: ECC Skill 研究任务
status: active
priority: high
kind: research
branch: docs-ecc-agent-skills-notes
issue: null
pr: https://github.com/wangchengcheng95/AI-prompt/pull/12
last_updated: 2026-03-19
next_step: 继续第二轮高优先级 skill 研究，优先 deep-research、market-research、api-design、dmux-workflows，并明确筛选标准与归属边界。
promotion_targets:
  - platforms/codex/
  - docs/EVOLUTION-GOALS.md
---

# ECC Skill 研究任务

这个任务目录用于记录围绕 `references/external/everything-claude-code/.agents/skills/` 展开的研究背景、中间结论与后续入口。

## 原始目标

本轮最初目标不是改造 `verifier`，而是先研究以下目录中的 skill 都是做什么的，并判断哪些值得后续复用：

- `references/external/everything-claude-code/.agents/skills/`

希望回答的问题包括：

- 这些 skill 在上游项目里承担什么角色
- 哪些 skill 更适合继续只作为归档参考
- 哪些 skill 值得演化为本仓库后续可复用的资产
- 如果要复用，应放在 repo-local 维护入口，还是 `platforms/codex/`

## 本轮实际完成的范围

本轮工作先做了全量归类和优先级判断，然后沿着 `verification-loop` 深挖，最终落到 `platforms/codex` 现有 `verifier` 的演化上。

因此，本轮 PR 只能视为：

- 对原始研究目标的一次中间收敛
- 把讨论过程中形成的关键判断和中间资产落盘
- 顺手完成了与该讨论直接相关的少量平台资产和 repo-local 维护资产调整

它不能视为“已经完成对 `.agents/skills` 全量研究”的最终结果。

## 本轮已落盘的材料

### 1. 全量技能归类与复用优先级

- [skill-summary.md](./skill-summary.md)

当前结论：

- `.agents/skills` 在这个归档快照中实际有 24 个技能目录，不是上游 README 中写的 16 个
- 它更像上游项目为 Codex 或 agent 平台准备的技能打包层
- 高优先级继续深挖的方向包括：
  - `verification-loop`
  - `security-review`
  - `api-design`
  - `backend-patterns`
  - `deep-research`
  - `market-research`

### 2. `verification-loop` 与 `verification-phase` 的对比

- [verification-skill-comparison.md](./verification-skill-comparison.md)

当前结论：

- `verification-loop` 更像命令驱动的交付验收流水线
- `verification-phase` 更像原则驱动的设计风险检查表
- 更合理的方向不是二选一，而是组合成两层验证结构

### 3. `platforms/codex` 现有 `verifier` 的演化清单

- [verifier-evolution-checklist.md](./verifier-evolution-checklist.md)

当前结论：

- 不建议新增一个平行的 verification skill
- 更合理的方向是扩展 `platforms/codex` 现有 `verifier`
- 目标使用场景聚焦：
  - Go 后端仓库
  - Shell 脚本仓库
  - Python 执行脚本仓库

## 本轮已确认的重要判断

### 1. 研究对象属于外部归档参考资产

`references/external/everything-claude-code/.agents/skills/` 是外部归档参考资产，不是本仓库当前维护入口。

因此，对它的研究结果如果要沉淀为长期可复用资产，更可能进入：

- `platforms/codex/`

而不是直接进入根级 repo-local 维护入口。

### 2. `verifier` 的演化是研究副产物，不是原始目标本身

本轮之所以进入 `verifier`，是因为：

- `verification-loop` 是高优先级候选 skill
- 它和本轮已摘要的 `verification-phase` 风格检查模式有明显互补关系
- `platforms/codex` 里已经存在同类资产 `verifier`

所以才收敛出“扩展现有 `verifier`，而不是新增平行 skill”的判断。

### 3. `repo-doc-simplifier` 不应再把 `platforms/` 一刀切排除

本轮已确认：

- Markdown 是否可被简化，不取决于文件格式，而取决于文档承载的契约
- repo-local 文档主要保护“仓库治理语义”
- `platforms/` 文档主要保护“下游消费语义”
- 更合理的设计是一个 skill，两种模式，而不是完全相同地处理这两类文档

### 4. 修改 skill 时应强制参考官方 `skill-creator`

本轮已经把这条约束写入根级 [AGENTS.md](../../../AGENTS.md)：

- 修改或创建任何 `SKILL.md` 时，先使用 `$skill-creator`
- 再参考 [skill-writing-guides.md](../../../references/skill-writing-guides.md)

## 本轮顺手完成的代码与文档变更

以下变更是讨论过程中的直接产物：

- 更新根级 [AGENTS.md](../../../AGENTS.md)，把 `skill-creator` 提升为强约束
- 重写 [repo-doc-simplifier/SKILL.md](../../../.codex/skills/repo-doc-simplifier/SKILL.md)，支持 `repo-maintenance` 与 `platform-asset` 双模式
- 生成 [repo-doc-simplifier/openai.yaml](../../../.codex/skills/repo-doc-simplifier/agents/openai.yaml)
- 演化 [verifier/SKILL.md](../../../platforms/codex/.codex/skills/verifier/SKILL.md)
- 同步 [verifier.toml](../../../platforms/codex/.codex/agents/verifier.toml)
- 生成 [verifier/openai.yaml](../../../platforms/codex/.codex/skills/verifier/agents/openai.yaml)

这些变更已经被整理进当前 PR，但它们只是本轮研究过程中的已确认输出，不代表原始研究目标已经结束。

## 当前 PR 与分支信息

用于保存本轮中间结果的分支和 PR：

- 分支：`docs-ecc-agent-skills-notes`
- PR：`feat(codex): evolve verifier and doc simplifier skills`
- 链接：<https://github.com/wangchengcheng95/AI-prompt/pull/12>

这个 PR 的作用更像“保存已确认中间结论和配套改动”，而不是宣称对 `.agents/skills` 的研究已经完成。

## Todo List

- Follow-up is now tracked in [docs/tasks/codex-home-agents-path-constraint/README.md](../codex-home-agents-path-constraint/README.md).

## 尚未完成的原始目标

以下事项仍然没有完成：

- 还没有系统梳理 24 个 skill 中哪些只应继续作为参考，哪些值得转成长期维护资产
- 还没有对高优先级 skill 做逐个深入分析
- 还没有收敛一套面向后续复用的筛选标准
- 还没有形成“下一批要引入或改造哪些 skill”的明确清单

换句话说，本轮完成的是：

- 初筛
- 一个重点样本的深挖
- 与该样本相关的资产调整

但没有完成“整个目录研究完毕并形成系统决策”。

## 下一轮建议从哪里继续

新会话、新分支继续时，建议按以下顺序推进：

1. 先读这个任务目录下的 4 份文档：
   - [README.md](./README.md)
   - [skill-summary.md](./skill-summary.md)
   - [verification-skill-comparison.md](./verification-skill-comparison.md)
   - [verifier-evolution-checklist.md](./verifier-evolution-checklist.md)
2. 明确下一轮是否继续研究 `verification-loop` 之外的高优先级 skill。
3. 如果继续全局研究，优先从以下 4 个方向继续：
   - `deep-research`
   - `market-research`
   - `api-design`
   - `dmux-workflows`
4. 对每个候选 skill 明确回答三件事：
   - 它解决什么问题
   - 是否值得沉淀为本仓库长期维护资产
   - 如果值得，归属应是 `platforms/codex/` 还是仅保留为外部参考

## 对下一轮的建议约束

下一轮最好保持范围收敛，避免再像本轮一样从“研究全量技能”自然滑入某一个 skill 的实现细节。

更稳妥的做法是：

- 先完成“研究与筛选”
- 再单独开实现型任务去改造具体 skill

这样能避免研究任务和实现任务混在一个分支里。
