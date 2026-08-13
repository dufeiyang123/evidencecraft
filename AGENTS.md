# Evidencecraft Agent 工作规范

本仓库已回到干净的 Skill 创建起点。开始设计、创建或修改任何 Skill 前，完整阅读：

1. 本文件；
2. `PLAN.md`；
3. `docs/skill-evaluation-policy.md`。

当前工作树没有可复用的旧 Skill、Schema 或历史评测模板。不要主动从 Git 历史恢复旧实现，
也不要把历史 commit 当成当前设计依据；只有用户明确要求历史审计或迁移时才读取它们。

## 1. 创建 Skill 前先研究 Superpowers

新建或实质修改 Skill 时，必须先使用当前 Codex 的 `skill-creator`，再研究该职责对应的
Superpowers 主流程 Skill 的当前正文：

| Evidencecraft 职责 | 先研究的 Superpowers Skill |
|---|---|
| `using-evidencecraft` | `using-superpowers` |
| `framing-analysis` | `brainstorming` |
| `writing-report-plans` | `writing-plans` |
| `executing-report-plans` | `executing-plans`、`verification-before-completion` |
| `subagent-driven-reporting` | `subagent-driven-development`、按需 `dispatching-parallel-agents` |
| `reviewing-analysis` | `requesting-code-review`、`receiving-code-review`、`verification-before-completion` |
| `profiling-evidence` | `brainstorming`、`systematic-debugging`、`writing-plans` |
| `defining-metrics` | `brainstorming`、`writing-plans`、按需 `test-driven-development` |

所有 Skill 还要研究 `../superpowers/skills/writing-skills/SKILL.md`。

在当前任务计划或 commentary 中先记录：

- 研究了哪些文件和 Superpowers commit；
- 对应 Skill 的正文规模、职责深度、配套文件清单及每个配套文件的用途；
- 借鉴的 2–5 个机制精髓；
- 决策门、角色分离、恢复机制和验证方式如何工作；
- 明确不照搬的 Git、代码提交、固定任务粒度、固定 subagent/review 轮数；
- Evidencecraft 的 Trigger、判断权、Markdown 产物和 Return Route；
- 选择怎样的 Skill 结构，以及为什么保留或省略对应 Superpowers 的配套文件；
- 为什么需要独立 Skill，而不是普通 prompt、Reference、模板、脚本或 Harness 规则。

完成这段研究记录后才编辑生产 `SKILL.md`。研究记录不要求写入新的永久文档。

## 2. 职责匹配的 Skill 包

不以文件数、行数或“单文件”作为质量目标，也不逐文件复制 Superpowers。根据职责复杂度、
交接风险、恢复需要和复用价值选择结构；对应 Superpowers Skill 的规模和模式是设计基准，
不是配额。

- 高频入口或简单顺序流程优先短小、自包含，避免每次触发都加载低价值细节；
- `SKILL.md` 写 Trigger、输入、核心流程、主要判断权、停止/完成门、结果和 Return Route；
- 复杂流程可用一层 `references/` 渐进披露稳定知识、详细技术或变体，正文必须说明何时读取；
- 稳定且会被复制为交付物的 Markdown 格式可以放入 `assets/` 作为模板；
- implementer、reviewer、re-reviewer 等角色若有不同输入和输出契约，可使用正文直接引用的
  独立 prompt 文件，避免把角色细节挤进主流程；
- 重复、确定、容易手工出错的提取、检查或 workspace 操作才进入 `scripts/`，新增脚本必须实跑；
- 按当前 `skill-creator` 生成并保留实际发现、界面或分发需要的 `agents/openai.yaml`；
- 不创建 README、安装指南、变更日志、测试说明、空目录、重复 Reference 或无人调用的配套。

“精简”只表示没有无消费者和重复的产物，不表示压缩必要流程。复杂 Skill 可以像对应的
Superpowers Skill 一样拥有完整正文和配套资源，只要每个部分都有独立职责和实际调用方。

核心 Skill 不依赖具体模型、Harness、连接器、用户机器路径或项目测试夹具。

## 3. 产物原则

主流程默认使用人和 Agent 都能直接读取的 Markdown：Brief、Plan、任务 brief/report、进度
ledger、证据日志、最终报告和按风险需要的 review。

每个职责必须有可观察结果，但不要求每个结果成为永久文件。运行内交接默认临时；只有跨会话
恢复、下游复用、阻断/异常、高影响决定或正式审计需要时才保存。

不要默认创建 JSON Schema、Approval 对象、生命周期对象图、兼容桥或成套正负例。只有同时
存在稳定的跨运行语义、真实机器消费者、已被实际流程证明稳定的字段，以及明确的 validator/
迁移负责人时，才另行提议机器契约。

## 4. 目标流程

首次流程：

```text
using → framing → writing plan → 一个 Executor → review → report
```

`profiling-evidence` 和 `defining-metrics` 是条件专业 Skill，只在计划或恢复发现来源/指标语义
缺口时插入，完成后返回计划或发起调查的阶段。正常周期复用已确认 Plan。

同一次运行只能选择顺序或多智能体 Executor 之一。工作 Agent 只收到一个任务 brief，不与
用户交互、不修改共享报告、不重新定义来源或指标；主 Agent 验证实际输出后再综合。

## 5. 验收纪律

测试遵守 `docs/skill-evaluation-policy.md`：

- 文档、拼写、链接和非行为 Reference：只做静态检查；
- 新 Skill 或行为变化：默认一个自然正例和一个最近邻负例；
- 状态、路由、停止纪律、审查、委派或高影响判断按风险增加一个 baseline 或组合场景；
- 只有归因和交接风险都需独立决策时才同时增加两者，单 Skill 最多四个模型场景；
- baseline 已表现正确时停止针对该行为扩写，不为制造 RED 重复 prompt；
- 不采用固定 5+ 次 micro-test，不为每个字段单独运行模型；
- 候选出现关键失败时立即停止、修复并只重跑失败边界；
- 一组相邻 Skills 完成后才做一次首次流程和一次周期复用集成测试。

行为验证使用 Codex；不可用时记录 `BLOCKED`，不改用 Claude Code、GLM 或其他模型替代。
测试输出默认放临时目录，不在仓库重建 `evals/`。完成记录写在任务结果或 commit message；
只有用户明确授权发布级研究时才持久化正式评测证据。

## 6. 工作区纪律

- 一次只创建或修改一个主要 Skill；相邻 Skill 未稳定前不扩张范围。
- 不从已删除的历史实现复制结构、术语、测试数量或产物清单。
- 保存用户已有改动，不使用破坏性 Git 操作，不修改 `../superpowers`。
- 完成前运行受影响的 `quick_validate.py`、链接/路径检查、必要脚本测试和
  `git diff --check`，再审阅完整 Diff。
- 未经明确要求，不推送远端、不创建 PR、不安装连接器或发布配置。

具体职责、建设顺序和 Markdown 交接见 `PLAN.md`。
