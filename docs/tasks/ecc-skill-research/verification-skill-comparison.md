# `verification-loop` 与 `verification-phase` 对比及融合建议

这是一份临时讨论笔记，用于比较以下两类输入，并判断后续是否值得沉淀为本仓库可复用的技能资产：

- 可复现来源：`references/external/everything-claude-code/.agents/skills/verification-loop/SKILL.md`
- 本轮已摘要的 `verification-phase` 风格检查模式；当前仓库没有把它的原始来源纳入 `references/repos.manifest.tsv`，因此本文保留的是自包含结论，而不是对某个 repo-managed path 的逐段摘录

## 一句话判断

这两个 skill 看起来相似，但本质上不在同一层：

- `verification-loop` 偏“可执行的交付验收流水线”
- `verification-phase` 偏“设计一致性与工程原则检查表”

更合适的思路不是二选一，而是把它们组合成两层验证结构。

## 相同点

- 都发生在实现之后，属于收尾验证环节。
- 都试图降低错误实现、遗漏边界条件和隐含风险。
- 都适合放在 PR 前、重构后或大改动完成后执行。

## 关键差异

| 维度 | `verification-loop` | `verification-phase` |
|---|---|---|
| 核心定位 | 命令驱动的验收流水线 | 原则驱动的设计核对清单 |
| 主要手段 | build、typecheck、lint、test、security、diff review | 检查不变量、失败模式、原子性、幂等性、并发、安全 |
| 输出证据 | 强，容易给出命令结果和统一报告 | 弱，更多依赖审查者判断 |
| 泛化能力 | 中等，示例偏 Node/TS/Python | 高，技术栈无关 |
| 适合场景 | PR 前通用验收、日常工程交付 | 高风险逻辑、事务边界、并发、状态一致性审查 |
| 风险 | 容易停留在“命令都过了” | 容易停留在“原则都勾了” |

## `verification-loop` 的优点与不足

### 优点

- 可执行性很强，agent 或工程师都容易直接照做。
- 结构清楚，适合沉淀成统一的 PR 前验收动作。
- 输出格式明确，便于在交付时汇报状态。
- 包含 diff review，比单纯跑 CI 更接近真实交付流程。

### 不足

- 对工具链有明显预设，示例偏 JavaScript、TypeScript、Python。
- 安全检查比较浅，更多是卫生检查，不是系统性安全审查。
- 对事务边界、幂等性、并发、数据一致性等高风险问题覆盖不足。

## `verification-phase` 的优点与不足

### 优点

- 检查的是更本质的系统风险，而不是只看命令是否通过。
- 能覆盖不变量、失败模式、原子性、幂等性、并发等高风险主题。
- 更适合和设计阶段、批判阶段、实现阶段串成完整方法论。

### 不足

- 太抽象，不够操作化，执行质量依赖审查者水平。
- 没有命令级证据链，不能替代构建、测试、lint、类型检查。
- 对日常普通改动来说可能偏重，容易增加心智负担。

## 三种处理方案

### 方案 A：只保留 `verification-loop`

优点：

- 最容易落地
- 最适合 Codex 这类执行型 agent
- 最容易形成标准化收尾流程

缺点：

- 对高风险设计问题覆盖不够

适合：

- 日常 Web 应用和普通工程交付

### 方案 B：以 `verification-loop` 为骨架，吸收 `verification-phase` 的关键检查项

优点：

- 同时兼顾可执行性和设计正确性
- 更接近行业中的“自动化验证 + 工程审查”组合
- 更适合演化成仓库自己的复用 skill

缺点：

- 需要明确哪些原则检查必须做，哪些按风险触发

适合：

- 想沉淀长期可复用 skill，但又不希望技能过于抽象的场景

### 方案 C：两个 skill 保持独立，按场景串联调用

优点：

- 保留两个上游来源的原始语义
- 在高风险任务里可以先做原则审查，再跑命令验收

缺点：

- 使用门槛更高
- 容易出现职责重叠和触发混乱

适合：

- 已经有成熟分阶段工作流的团队

## 推荐方案

推荐 **方案 B**。

原因：

- 如果目标是做一个真正可复用的 skill，底座必须是可执行的。
- 只保留原则检查会太虚，难以转化为稳定交付动作。
- 只保留命令流水线又不够稳，尤其对后端、数据、并发、状态机类任务风险偏高。
- 因此最合理的做法是让 `verification-loop` 提供执行骨架，再把 `verification-phase` 中真正关键的高风险检查点嵌进去。

## 建议的融合版骨架

可以先按下面的结构理解未来的融合版 verification skill：

### Phase 0：风险预检查

只在满足以下任一条件时强制执行：

- 涉及事务、状态迁移、队列消费、并发访问
- 涉及支付、鉴权、数据写入、迁移、删除
- 涉及重构关键路径或跨模块变更

检查项可来自 `verification-phase`：

- 设计约束是否被实现
- 不变量是否被强制维护
- 失败模式是否被覆盖
- 是否存在并发、幂等性、原子性风险

### Phase 1：构建与静态检查

- build
- typecheck
- lint

这部分沿用 `verification-loop` 的执行风格。

### Phase 2：测试与覆盖率

- 单元测试
- 集成测试
- 必要时的 E2E
- 覆盖率门槛或至少说明未覆盖风险

### Phase 3：安全与回归检查

- 基础 secret 泄漏检查
- 调试输出与危险配置检查
- 与本次改动相关的安全边界回顾

### Phase 4：差异审查

除 diff review 外，增加两类问题：

- 是否偏离既定设计
- 是否引入了未声明的风险或行为变化

### Abort 条件

保留 `verification-phase` 的强中止语义：

- 核心不变量可被破坏
- 关键失败模式未处理
- 存在明显竞态、死锁、数据损坏风险
- 设计约束未落地

### 输出格式

输出不要只写 PASS 或 FAIL，应拆成两层：

- 执行结果层：build、typecheck、lint、tests、security、diff
- 设计风险层：invariants、failure modes、atomicity、idempotency、concurrency

这样最终报告既有命令证据，也有工程判断。

## 对本仓库的落地建议

如果后续真的要沉淀成仓库自有技能，我建议：

- 先不要直接复制任何一个上游版本到根级 `.codex/skills/`
- 先在讨论中收敛一个融合版最小骨架
- 若它面向外部平台复用，优先考虑放在 `platforms/codex/`
- 只有当它确实是“维护本仓库本身”会频繁使用的技能，才考虑进入根级 repo-local 维护入口

## 当前已确认的定位

基于本轮讨论，定位已经可以进一步收敛：

- 目标归属：`platforms/codex/`
- 目标用途：给其他仓库使用，而不是只服务本仓库维护
- 主要适用技术栈：Go 后端开发、Shell 脚本、Python 执行脚本

这意味着它应该被视为“外部平台资产”，而不是 repo-local 维护技能。

## 与现有 `platforms/codex` 资产的关系

当前 `platforms/codex/.codex/skills/` 下已经存在：

- `verifier`
- `golang-patterns`
- `golang-testing`

其中现有的 `verifier` 已经明确偏向 Go 后端验证，因此后续更合理的方向不是新增一个同类平行 skill，而是：

- 优先扩展现有 `verifier`
- 让它吸收 `verification-loop` 的命令化验收结构
- 再按风险吸收 `verification-phase` 的原则检查项

这样可以减少语义重叠，也更符合“先找现有归宿，再扩展”的维护原则。

## 对 Go、Shell、Python 场景的影响

既然目标仓库主要不是前端工程，而是 Go 后端、Shell、Python，那么未来的融合版 verification skill 应当调整重点。

### Go 后端

优先保留：

- `go test ./...`
- `go test -race -count=1 ./...`
- `go vet ./...`
- 覆盖率或关键包定向测试
- 并发、幂等性、事务边界、context 传播检查

重点风险：

- 写操作幂等性
- 并发访问与竞态
- goroutine 生命周期与取消
- repository 与 service 的层次边界
- 超时、重试、部分失败

### Shell 脚本

优先保留：

- `shellcheck`
- `shfmt -d`
- `bash -n` 或 `sh -n`
- 关键路径 dry-run 或最小样例执行

重点风险：

- 未引用变量或错误展开
- 临时文件和清理逻辑缺失
- `trap` 不完整
- 删除、覆盖、移动文件的危险路径
- exit code 不明确

### Python 执行脚本

优先保留：

- `pytest`
- `ruff check`
- `python -m compileall`
- `mypy` 或 `pyright`，按仓库实际情况启用一种

重点风险：

- 参数校验不足
- 临时文件和资源清理遗漏
- 异常路径未暴露明确退出码
- 幂等性不足，重复执行会造成副作用
- 文件系统或网络边界缺少超时与错误处理

## 因此带来的结构调整

如果未来要形成 `platforms/codex/` 下的正式 skill，我更倾向于：

- 保留统一的 verification 主框架
- 按语言或仓库类型定义不同的执行分支
- 避免保留过多前端导向示例
- 把“高风险原则检查”作为可按场景触发的附加层，而不是所有任务默认全量执行

换句话说，未来版本不应是“通用 Web skill”，而应更像：

- Go 后端优先
- Shell 与 Python 脚本可复用
- 对高风险写操作和并发场景更敏感

## 当前建议

短期内：

- 把 `verification-loop` 视为更强的默认参考
- 把 `verification-phase` 视为高风险任务的补充检查清单

中期如果要演化：

- 做一个融合版，而不是直接二选一
