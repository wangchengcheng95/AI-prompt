# `platforms/codex` 现有 `verifier` 演化清单

这是一份临时设计清单，用于指导 `platforms/codex/.codex/skills/verifier/SKILL.md` 后续如何演化，以吸收可复现的 `verification-loop` 参考和本轮已摘要的 `verification-phase` 风格检查模式的长处，同时保持与当前 `platforms/codex` 资产的一致性。

## 目标

不是新增一个新的 verification skill，而是扩展现有 `verifier`，让它更适合：

- Go 后端仓库
- Shell 脚本仓库
- Python 执行脚本仓库

## 现有 `verifier` 应保留的内容

以下内容已经有价值，不应在改写时丢掉：

- 严格、怀疑式验证立场，不轻信“已完成”声明
- 先澄清“具体声称完成了什么”
- 先看代码是否真的存在、结构是否合理
- 必须要求证据，而不是只接受口头判断
- 场景驱动检查：happy path、edge、failure、concurrency
- 人工补充推理：validation、authorization、idempotency、transactions、cleanup

这些内容是当前 `verifier` 的骨架，应继续保留。

## 与目标形态相比，当前 `verifier` 缺少什么

### 1. 缺少显式的命令化验证阶段

当前只强调跑 `go test`，但缺少更完整的阶段划分，例如：

- build
- typecheck 或编译级检查
- lint 或静态检查
- tests
- security hygiene
- diff review

结果是：

- 验证步骤不够标准化
- 输出不够结构化
- 不同 agent 执行时波动可能较大

### 2. 缺少风险预检查层

当前已经提到幂等性、事务、cleanup 等问题，但没有明确触发条件，也没有“出现哪些问题必须中止”的规则。

建议补充：

- 哪些类型的改动必须进入高风险检查
- 哪些风险一旦成立必须直接判定为不通过

### 3. 缺少跨语言执行分支

当前明显只面向 Go 后端。

如果要用于其他仓库，还需要至少定义：

- Go 分支
- Shell 分支
- Python 脚本分支

否则这个 skill 的平台复用价值会受限。

### 4. 缺少结构化输出层

当前输出偏结论式：

- Passed
- Partial pass with risk
- Failed / not implemented

这很好，但还不够细。未来需要补出：

- 命令执行层结果
- 风险评估层结果

这样用户能快速分辨是“工具没过”还是“原则有风险”。

## 未来版本建议新增的内容

### A. 新增统一的验证阶段骨架

建议最少有以下阶段：

1. 风险预检查
2. 构建与静态检查
3. 测试与覆盖率
4. 安全与回归检查
5. 差异审查
6. 最终汇总

### B. 新增按语言切换的命令建议

#### Go

- `go test ./...`
- `go test -race -count=1 ./...`
- `go vet ./...`
- 按仓库情况运行覆盖率或目标包测试

#### Shell

- `shellcheck`
- `shfmt -d`
- `bash -n` 或 `sh -n`
- 关键脚本 dry-run 或最小样例执行

#### Python

- `pytest`
- `ruff check`
- `python -m compileall`
- `mypy` 或 `pyright`，二选一，由仓库决定

### C. 新增风险触发条件

建议把下列情况作为高风险检查触发器：

- 涉及写操作、副作用或重复执行
- 涉及并发、异步任务、后台处理
- 涉及事务、状态迁移、重试、去重
- 涉及删除、迁移、覆盖、远程调用

### D. 新增强中止条件

建议明确以下问题一旦成立，应直接判定为不通过：

- 核心不变量可能被破坏
- 关键失败模式未处理
- 存在竞态、死锁或数据损坏风险
- 写路径不具备幂等性且业务要求幂等
- 清理逻辑缺失，可能导致资源或文件残留

## 未来版本建议避免的内容

以下内容不建议直接照搬进 `platforms/codex` 的正式 skill：

- 过多前端导向示例
- 过多 Node.js 专属命令
- 对所有仓库都强制要求同一种测试覆盖率门槛
- 把高风险原则检查强制施加到所有简单改动

原因是这些内容会让 skill 变得更像“特定技术栈模板”，而不是“跨仓库复用的 Codex 平台资产”。

## 推荐的演化方式

更合理的演化路径应是：

1. 保留现有 `verifier` 的怀疑式验证语气与场景推理骨架
2. 引入 `verification-loop` 的阶段化执行框架
3. 引入 `verification-phase` 的高风险检查项和中止条件
4. 为 Go、Shell、Python 增加最小可执行分支
5. 保持输出格式简洁，但区分“执行结果”和“设计风险”

## 如果下一步要正式改 `verifier`

正式改写前，建议先回答以下问题：

- 这个 skill 是否默认覆盖所有仓库，还是只在检测到 Go、Shell、Python 时启用对应分支？
- `shellcheck`、`shfmt`、`ruff`、`mypy` 等工具缺失时，是跳过、降级提示，还是判定不通过？
- `go vet`、`go test -race` 是否默认执行，还是按仓库规模与耗时策略降级？

## 本轮已确认的取舍

基于当前讨论，先采用以下约束：

- 假设不存在 `test-runner` 这个 skill
- 本轮只聚焦 `verifier` 自身该如何演化
- 与测试执行相关的职责直接并入 `verifier`

## 当前结论

最合适的方向不是“新增 verification skill”，而是“扩展 `platforms/codex` 现有 `verifier`，把它从 Go-only 验证 skill 演化成面向 Go 后端、Shell、Python 脚本仓库的统一 verification 入口”。
