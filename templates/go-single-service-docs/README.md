# Go 后端服务文档模板使用说明

## 适用范围

这套模板面向单仓库单服务的 Go 后端项目。
设计目标不是产出大而全的系统手册，而是让新会话或仓库 Agent 在较短时间内建立正确心智模型，并能继续补齐长期有效的项目文档。

## 模板组成

- `system-overview.md`：服务是什么，负责什么，不负责什么，与谁交互。
- `architecture.md`：服务内部怎么组织，模块如何分层，关键调用链如何流转。
- `operations.md`：服务怎么启动、配置、依赖什么、去哪里观测和排障。
- `current-status.md`：当前阶段做到哪里、卡在哪里、下一步接什么。
- `decisions.md`：已经确认的重要设计决策、原因和影响。
- `known-risks.md`：已经验证的风险、脆弱点、触发条件和规避方式。

## 建议阅读顺序

按下面顺序阅读和补齐，通常最稳定：

1. `system-overview.md`
2. `architecture.md`
3. `operations.md`
4. `current-status.md`
5. `known-risks.md`
6. `decisions.md`

## 给仓库 Agent 的使用规则

- 先完整阅读本目录下的 `README.md`，再逐个阅读 6 份模板。
- 严格按照每份模板里的“补齐指引”“优先信息来源”“完成标准”“缺失信息写法”执行。
- 只补齐已验证事实，不根据经验、命名习惯或常见项目结构臆测内容。
- 信息不足时使用 `待确认`，明确不存在时使用 `不适用`，存在矛盾时使用 `存在冲突，待核实`。
- 不要把一类信息写到错误文档中：
  - 服务身份和边界写入 `system-overview.md`
  - 内部结构和调用链写入 `architecture.md`
  - 运行方式和观测入口写入 `operations.md`
  - 当前进展和阻塞写入 `current-status.md`
  - 已确认设计取舍写入 `decisions.md`
  - 已验证风险写入 `known-risks.md`
- 如发现某项内容更适合落到其他文档，应移动到正确位置，而不是重复记录。

## 建议优先查找的信息源

- 仓库根目录 `README`、设计文档和已有 `docs/`
- `cmd/`、`main.go`、路由注册、服务初始化和核心 package
- `Makefile`、启动脚本、`Dockerfile`、部署目录和 CI/CD 配置
- 配置样例、环境变量定义、配置加载代码
- 测试、历史提交、PR 描述、issue 和事故复盘

## 什么时候算补齐完成

满足下面条件即可认为完成首轮补齐：

- 新会话能在几分钟内看懂服务边界、架构和运行方式。
- 新会话能判断当前接什么工作、哪些地方有风险、哪些设计是有意为之。
- 文档之间边界清晰，没有明显重复或互相矛盾。
- 对无法确认的信息做了显式标记，而不是用猜测补空。

## 建议复制到目标仓库 `AGENTS.md` 的指令

可将下面这段说明复制到目标仓库的 `AGENTS.md` 或等效 Agent 入口文件中：

```md
## Project Documentation Memory

The repository uses the documentation templates under `docs/` as the authoritative project memory.

When you need to initialize or update project documentation:

1. Read `docs/README.md` first if present.
2. Then read these files in order:
   - `docs/system-overview.md`
   - `docs/architecture.md`
   - `docs/operations.md`
   - `docs/current-status.md`
   - `docs/known-risks.md`
   - `docs/decisions.md`
3. Follow each document's local instructions, especially:
   - fill only verified facts
   - do not guess missing information
   - use `待确认` for unknown items
   - use `不适用` when a section truly does not apply
   - use `存在冲突，待核实` when sources disagree
4. Keep information in the correct document:
   - service identity and scope -> `system-overview.md`
   - internal structure and module boundaries -> `architecture.md`
   - runtime, configuration, dependencies, observability -> `operations.md`
   - active progress, blockers, next steps -> `current-status.md`
   - confirmed design choices and rationale -> `decisions.md`
   - verified risks and mitigations -> `known-risks.md`
```

## 维护建议

- 如果项目长期采用这套模板，建议将本文件一并复制到目标仓库中，并命名为 `docs/README.md`。
- 如果后续扩展到多服务仓库，优先保持这 6 类信息边界不变，再讨论目录层级是否需要按服务拆分。
- 如果 `decisions.md` 记录越来越多，可进一步演进为 `docs/adr/` 目录。
