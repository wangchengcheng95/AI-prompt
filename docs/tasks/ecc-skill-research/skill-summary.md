# ECC `.agents/skills` 归类与复用建议

这是一份临时笔记，用于评估归档外部资产 `references/external/everything-claude-code/.agents/skills` 中的技能是否值得在本仓库后续复用。

## 范围说明

- 分析对象：`references/external/everything-claude-code/.agents/skills`
- 在上游项目中的角色：面向 Codex 或 agent 平台的一组技能子集，每个技能由 `SKILL.md` 和 `agents/openai.yaml` 组成
- 在本仓库中的角色：外部归档参考资产，不是本仓库当前的维护入口

## 这个文件夹是做什么的

上游的 `.agents` 更像一个给 Codex 使用的“技能打包层”：

- `SKILL.md` 负责定义技能何时触发、要解决什么问题、采用什么流程、依赖什么工具。
- `agents/openai.yaml` 负责定义 agent 元数据，例如展示名、默认提示词、是否允许隐式调用。
- 它不是完整技能库，而是从更大的 `skills/` 目录中挑出来的一组 Codex 子集。

## 当前快照的实际情况

- 当前归档快照中，`.agents/skills` 实际有 24 个技能目录。
- 上游 `README.md` 在这一处仍然写的是 16 个自动加载技能，说明文档已经滞后。
- 因此，后续判断是否复用时，应优先以目录现状为准，而不是只看 README 中的数量描述。

## 建议的分类方式

### 1. 工程流程与质量控制

- `tdd-workflow`：测试先行开发流程与覆盖率要求
- `verification-loop`：构建、测试、lint、typecheck、安全检查等验证闭环
- `security-review`：鉴权、输入处理、密钥、敏感功能的安全检查清单
- `coding-standards`：通用编码规范，偏 TypeScript、JavaScript、React、Node.js
- `eval-harness`：评测驱动开发流程
- `strategic-compact`：上下文压缩时机与策略
- `dmux-workflows`：多 agent 并行协作与终端编排模式

这一组关注的是“如何做事”，价值主要体现在提高交付质量、验证完整性与协作效率。

### 2. 应用开发模式

- `api-design`：生产级 REST API 设计模式
- `backend-patterns`：后端架构、数据库、缓存、接口设计模式
- `frontend-patterns`：React 与 Next.js 前端开发模式
- `e2e-testing`：基于 Playwright 的端到端测试模式
- `claude-api`：Anthropic Claude API 集成模式
- `x-api`：X 或 Twitter API 集成模式

这一组关注的是“如何实现具体系统”，适合在明确技术方向后作为实现参考。

### 3. 研究与决策支持

- `deep-research`：多来源、带引用的深度研究流程
- `exa-search`：基于 Exa 的神经搜索工作流
- `market-research`：市场、竞品、尽调类研究

这一组关注的是“如何查证、归纳、支撑决策”，比较适合技术选型、竞品扫描、行业调研。

### 4. 内容、增长与融资

- `article-writing`：长文、教程、博客、通讯类写作
- `content-engine`：多平台内容系统与内容改写
- `crosspost`：针对不同平台做差异化分发
- `frontend-slides`：HTML 演示稿与幻灯片生成
- `investor-materials`：融资材料、deck、memo、one-pager
- `investor-outreach`：投资人触达邮件与相关沟通文案

这一组明显偏内容生产和融资协作，只有在仓库范围明确覆盖这类工作时才值得纳入活跃资产。

### 5. 媒体生产

- `fal-ai-media`：图像、音频、视频生成工作流
- `video-editing`：AI 辅助视频编辑工作流

这一组更偏媒体制作，与当前仓库的维护目标距离较远，优先级最低。

## 复用优先级建议

### 高优先级

- `verification-loop`
- `security-review`
- `api-design`
- `backend-patterns`
- `deep-research`
- `market-research`

原因：

- 复用面最广，不依赖特定内容生产场景。
- 对工程质量、验证质量、研究质量的提升最直接。
- 更容易提炼成跨项目可用的方法，而不是一次性素材。

### 中优先级

- `tdd-workflow`
- `e2e-testing`
- `frontend-patterns`
- `coding-standards`
- `dmux-workflows`
- `strategic-compact`

原因：

- 本身有价值，但是否适合要看团队工作方式。
- 例如严格 TDD、多 agent 编排、显式上下文压缩，并不是每个仓库都需要。

### 低优先级或强场景依赖

- `article-writing`
- `content-engine`
- `crosspost`
- `frontend-slides`
- `investor-materials`
- `investor-outreach`
- `fal-ai-media`
- `video-editing`
- `x-api`
- `claude-api`

原因：

- 这些能力都比较专项。
- 只有当仓库明确需要内容、融资、媒体、第三方平台集成能力时，才值得纳入长期维护范围。

## 对本仓库的建议

建议采用“窄引入”策略，而不是整包搬运：

- 大部分技能继续保留为归档外部参考，不急着转成仓库内活跃资产。
- 如果要复用，应优先挑选少数高价值技能，改造成仓库拥有、语义清晰、边界明确的资产。
- 不建议把内容营销、融资、媒体工作流引入根级维护入口，这会扩大仓库维护边界，不符合当前阶段目标。

## 最值得继续深挖的 5 个技能

如果下一步只挑少量技能深入分析，建议先看：

- `deep-research`
- `market-research`
- `verification-loop`
- `api-design`
- `dmux-workflows`

这 5 个覆盖了研究、验证、实现指导、多 agent 协作几个最有复用面的方向。

## 后续讨论可以围绕的问题

- 哪些技能应当继续只作为归档参考？
- 哪些技能值得演化为本仓库自己的 Codex 资产？
- 哪些内容如果要保留，应当进入 `platforms/codex/`，而不是根级维护入口？
