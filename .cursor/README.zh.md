[English](README.md) | [中文](README.zh.md)

# 后端 AI 提示工程仓库

本仓库包含专门为**后端开发**设计的 AI 命令和规则集合。

## 仓库目的

**重点：** 面向后端开发工作流的 AI 辅助提示工程

**范围：** 
- 后端 API 开发（REST、GraphQL）
- 数据库设计和优化
- 服务器架构和微服务
- 认证和安全
- 性能优化
- DevOps 和基础设施

---

## 后端开发命令

这些目录包含用于**实际后端开发项目**的命令：

### `backend-commands/` (6 个命令)
**范围：** 语言无关的后端开发命令

适用于不同编程语言的通用后端命令：

**API 开发：**
- `design-rest-api.md` - 遵循最佳实践设计 RESTful API 端点
- `generate-api-docs.md` - 生成全面的 API 文档
- `generate-crud-operations.md` - 为数据模型生成完整的 CRUD 操作

**数据库：**
- `database-migration.md` - 创建和管理数据库迁移
- `optimize-database-queries.md` - 分析和优化数据库查询性能

**测试：**
- `write-integration-tests.md` - 为多组件系统创建集成测试

### `go-backend-commands/` (1 个命令)
**范围：** Go 特定的后端开发

为 Go 后端项目定制的命令：

- `add-error-handling.md` - 实现 Go 错误处理模式（显式 `if err != nil`、错误包装、context 使用）

### `user-commands/` (36 个命令)
**范围：** 项目无关，可在后端项目中复用

适用于任何后端项目或技术栈的通用编程命令：

**开发工作流：**
- `clarify-task.md` - 编码前询问澄清问题
- `setup-new-feature.md` - 系统化设置新功能
- `debug-issue.md` - 系统化调试代码
- `refactor-code.md` - 提高代码质量
- `optimize-performance.md` - 性能分析和优化
- `fix-compile-errors.md` - 分析和修复编译错误

**代码质量：**
- `code-review.md` - 全面的代码审查
- `light-review-existing-diffs.md` - 对差异进行快速质量检查
- `lint-fix.md` - 修复 lint 问题
- `lint-suite.md` - 运行 linter 并自动修复
- `deslop.md` - 移除 AI 生成的代码冗余
- `add-documentation.md` - 添加全面的文档
- `simplify-doc.md` - 简化和整合文档

**测试：**
- `write-unit-tests.md` - 创建全面的单元测试
- `run-all-tests-and-fix.md` - 执行并修复测试失败

**安全：**
- `security-audit.md` - 全面的安全审计
- `security-review.md` - 安全审查和修复

**Git 和 PR 管理：**
- `git-commit.md` - 创建聚焦的提交消息
- `git-push.md` - 推送并与远程同步
- `git-squash-merge-branch.md` - 压缩合并分支并生成提交摘要
- `fix-git-issues.md` - 解决 Git 问题
- `create-pr.md` - 创建结构良好的 PR
- `generate-pr-description.md` - 生成 PR 描述
- `address-github-pr-comments.md` - 处理 PR 反馈

**可视化和规划：**
- `diagrams.md` - 生成 Mermaid 图表
- `visualize.md` - 可视化数据血缘
- `overview.md` - 生成架构图
- `roadmap.md` - 生成功能路线图

**工作流阶段：**
- `design-phase.md` - 设计阶段工作流
- `implementation-phase.md` - 实现阶段工作流
- `critique-phase.md` - 评审阶段工作流
- `verification-phase.md` - 验证阶段工作流

**Go 后端标准：**
- `go-backend-standards.md` - Go 后端编码标准
- `go-refactor-conventions.md` - Go 重构约定
- `go-refactor-design.md` - Go 重构设计模式

### `devops-commands/` (1 个命令)
**范围：** DevOps 和基础设施管理

- `docker-logs.md` - 跟踪 Docker 容器日志

### `project-specific-archived/` (4 个命令)
**范围：** 项目特定命令（归档供参考）

与特定项目紧密耦合且不易复用的命令：
- `generate-device-protocol-docs.md` - 设备协议文档
- `generate-mqtt-docs.md` - MQTT 文档
- `onboard-new-developer.md` - 项目特定入职
- `run-regression-tests-and-fix.md` - 项目特定回归测试

---

## 后端开发规则

### `go-backend-rules/` (9 个规则)
Go 后端开发的规则和标准：

- `00-overview.mdc` - Go 后端标准概述
- `ai-boundary.mdc` - AI 交互边界
- `ai-interaction.mdc` - AI 交互指南
- `architecture.mdc` - 架构原则
- `clean-code.mdc` - 代码整洁标准
- `engineering-doctrine.mdc` - 工程原则
- `english-prompt.mdc` - 英文提示要求
- `go-backend.mdc` - Go 后端特定规则
- `testing.mdc` - 测试标准

---

## 使用指南

### 对于使用本仓库的后端开发者

在后端项目中使用以下命令类别：

**Go 后端项目：**
```
user-commands/ + go-backend-commands/ + backend-commands/ + go-backend-rules/
```

**通用后端项目（任何语言）：**
```
user-commands/ + backend-commands/
```

**DevOps 任务：**
```
user-commands/ + devops-commands/
```

---

## 添加新命令

添加新命令时遵循以下分类：

### 对于后端开发命令：
1. **是否 Go 特定？** → `go-backend-commands/`
2. **是否后端但语言无关？** → `backend-commands/`
3. **是否 DevOps/基础设施？** → `devops-commands/`
4. **是否项目无关且可复用？** → `user-commands/`
5. **是否与特定项目紧密耦合？** → `project-specific-archived/`

---

## 仓库原则

### 后端优先
- 所有命令和规则都针对后端开发工作流优化
- 排除前端相关命令
- 不包含全栈命令（仅后端）

### 质量标准
- 命令包含清晰的步骤、检查清单和最佳实践
- 每个命令都是可操作且具体的
- 提供常见用例示例
- 包含安全和性能考虑

### 语言支持
- 主要：Go 后端开发
- 通用：语言无关的后端模式
- 文档：英文，技术精确

---

## 命令格式

所有命令遵循此标准结构：

```markdown
# 命令标题

## 概述
简要描述目的和使用时机

## 步骤
1. **步骤名称**
    - 详细子步骤
    - 具体操作
    
2. **下一步**
    - 更多细节

## 检查清单
- [ ] 可验证项
- [ ] 另一个检查点
```

---

## 注意事项

- 命令设计用于 Cursor AI 助手和 Claude
- 每个命令包含清晰的步骤、检查清单和最佳实践
- 后端特定命令优先考虑安全性、性能和可扩展性
- 除非在语言特定目录中，否则命令应该是语言无关的
- 定期更新确保与当前后端最佳实践一致

---

## 仓库统计

- **后端命令：** 6 个（语言无关）
- **Go 特定命令：** 1 个
- **用户命令：** 36 个（项目无关）
- **DevOps 命令：** 1 个
- **活跃命令总数：** 44 个
- **后端规则：** 9 个（Go 重点）

---

## 贡献

向本仓库贡献时：

1. 确保命令符合后端开发重点
2. 遵循目录分类指南
3. 添加新命令或类别时更新本 README
