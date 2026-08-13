# Evidencecraft 项目计划

状态：`CLEAN_SKILL_REBUILD_START`

当前实现：无生产 Skills；无活动 Schema；无仓库内历史评测套件。

目标：从干净上下文创建六个主流程 Skills 和两个条件专业 Skills，形成适度完整、可移植、
可组合的周期证据报告方法。

## 1. 产品目标

Evidencecraft 帮助 Agent 从多来源证据生成可追溯的单项目周期报告。核心根据来源的结构、
实体、粒度、键、时间、更新、权威、变换和用途理解证据，不绑定具体平台、文件名或业务系统。

MVP 负责澄清目标、写计划、执行、记录证据、审查和保存报告。连接、认证、定时触发、工具
映射和外部发布属于 Harness，不写进核心 Skills。

## 2. 主流程

```text
using-evidencecraft
→ framing-analysis
→ writing-report-plans
→ executing-report-plans 或 subagent-driven-reporting
→ reviewing-analysis
→ 保存报告
```

计划阶段只有在发现独立语义缺口时才调用：

```text
writing-report-plans
  ↳ profiling-evidence → 返回 planning
  ↳ defining-metrics   → 返回 planning
```

首次默认确认 Brief 和 Plan 两次；需要新指标时与 Plan 一起确认。正常周期复用 Plan，只执行、
审查和保存新报告。普通内容或数值变化不触发重新 Profiling/定义 Metric。

## 3. 八个目标 Skills

| Skill | 主要判断权 | 默认结果 | 对应 Superpowers 结构模式 |
|---|---|---|---|
| `using-evidencecraft` | 识别首次、周期、恢复或回跳 | 下一责任和简短路由记录 | 类似 `using-superpowers`：高频、短小、自包含，不接管下游工作 |
| `framing-analysis` | 冻结对象、读者、用途、范围和风险 | `analysis-brief.md` | 类似 `brainstorming`：完整澄清与确认流程；可带 Brief 模板或独立 fresh-context reviewer prompt |
| `writing-report-plans` | 把 Brief 变成可执行计划 | `report-plan.md` | 类似 `writing-plans`：精确输入、依赖、任务和验证；可带 Plan 模板及按需 plan-reviewer prompt |
| `executing-report-plans` | 顺序执行并综合报告 | progress、evidence log、报告草稿 | 类似 `executing-plans` + verification：正文可紧凑，但必须覆盖预检、忠实执行、阻断、恢复和新鲜验证 |
| `subagent-driven-reporting` | 委派真正独立的任务并验收交接 | task briefs/reports、同一核心输出 | 类似 `subagent-driven-development`：可拆 worker、task-reviewer、re-review prompt 和 ledger；格式稳定后再加 brief/review-package/workspace 脚本 |
| `reviewing-analysis` | 独立核对证据、限制和结论 | pass/qualified/blocked 与 Return Routes | 类似 code-review Skills：允许独立 reviewer prompt、输入包契约、反馈分级和责任阶段 Return Routes |
| `profiling-evidence` | 判断来源语义和用途适用性 | 按需 `source-profile.md` | 类似 `systematic-debugging`：正文承载调查阶段；稳定来源维度和诊断技术可拆 References，重复探查稳定后才脚本化 |
| `defining-metrics` | 冻结可复用定量口径 | 按需 `metric-definition.md` | 结合 brainstorming、planning 与 TDD 不变量；可带 Metric Definition 模板和详细口径 Reference |

每个 Skill 创建前必须实际阅读表中对应的 Superpowers `SKILL.md`；表格摘要不能替代原文研究。
表中结构是创建时的设计起点，不是必须生成的文件清单。应比较对应 Skill 的正文和配套文件，
再按 Evidencecraft 的职责保留、改造或省略；每个附加 prompt、Reference、template、script 或
metadata 都必须有明确调用方，不追求文件或行数一一相同。

## 4. Markdown 交接

默认布局：

```text
docs/evidencecraft/
  specs/YYYY-MM-DD-<topic>-analysis-brief.md
  plans/YYYY-MM-DD-<topic>-report-plan.md
  sources/<logical-source>-profile.md       # 仅在需要时
  metrics/<metric>-definition.md            # 仅在需要时
.evidencecraft/runs/<plan>-<as-of>/
  progress.md
  evidence-log.md
  task-N-brief.md                            # 仅委派时
  task-N-report.md                           # 仅委派时
  review.md                                  # 按风险
reports/YYYY-MM-DD-<topic>.md
```

路径是约定，不是文件清单：

- Brief 和 Plan 是长期语义基线；
- Source Profile 只用于实际使用、含混、变化或跨周期复用的来源；
- Metric Definition 只用于跨周期复用、影响多个结果或高风险的口径；
- progress、evidence log、任务交接和草稿默认是临时运行文件；
- 低风险 clean review 可以只记一行，高风险/阻断才保存完整 `review.md`；
- 不为没有真实机器消费者的交接创建 JSON Schema。

### Analysis Brief 最小内容

- 对象、读者和用途；
- 目标、非目标和问题；
- 范围、周期和风险；
- 成功标准；
- 已确认、暂定和开放选择；
- 精确确认记录。

### Report Plan 最小内容

- Brief 精确引用；
- 周期、`as-of` 和时效规则；
- 来源与按需 Source Profiles；
- 指标与按需 Metric Definitions；
- 报告章节；
- Work Packages、依赖、输出位置和完成检查；
- 一个推荐 Executor；
- 停止条件、Return Routes、review 输入和保存位置。

### Task brief/report

工作 Agent 只接收任务目的、冻结输入、约束、唯一输出位置、完成检查和停止条件。返回实际
输入、方法、输出、验证、限制，以及 `COMPLETE | QUALIFIED | NEEDS_CONTEXT | BLOCKED`。
状态不是证据，主 Agent 必须检查真实产物。

### Evidence log

每期只记录来源、period/`as-of`、locator、访问时间、hash/citation、覆盖、时效、状态和限制。
同周期修正增加新记录并说明替代关系，不创建 Snapshot 对象图。

## 5. 周期变化规则

| 变化 | 返回阶段 |
|---|---|
| 正常新周期内容、数值变化 | 直接执行当前 Plan |
| 同周期迟到修正，语义不变 | 新运行和替代报告；保留旧报告 |
| 来源结构、粒度、权威、更新、对象映射或用途变化 | `profiling-evidence`，再回 planning |
| 指标含义、人口、时间或来源映射变化 | `defining-metrics`，再回 planning |
| 章节、比较规则、Work Package 或能力边界变化 | `writing-report-plans` |
| 任务执行或验证错误 | 当前 Executor 调查与修复 |
| 证据不足、过度结论或跨任务不一致 | Reviewer 指定责任阶段 |

只重做真正依赖变化语义的工作，不因来源字节变化重做全链。

## 6. 建设顺序

一次创建、验证并审阅一个 Skill：

1. `framing-analysis`
2. `profiling-evidence`
3. `defining-metrics`
4. `writing-report-plans`
5. `executing-report-plans`
6. `reviewing-analysis`
7. `subagent-driven-reporting`
8. `using-evidencecraft`

入口最后创建，因为它必须路由到已经可靠的下游；多智能体 Skill 在顺序闭环可靠后创建。

创建每个 Skill 前：研究对应 Superpowers 原文和配套结构，写简短研究记录，确定职责匹配的
结构包、实际调用方和有意省略项，再开始实现。

## 7. 完成标准

单个 Skill：

- Trigger、主要判断权、结果、停止门和 Return Route 清楚；
- 复杂度、正文深度和配套结构与对应职责相称；
- 重要决策门、角色边界、恢复或验证机制没有因追求短小而丢失；
- 正文、prompt、Reference、template、script 和 metadata 的边界清楚，使用渐进披露且各有调用方；
- 对对应 Superpowers 结构的保留、改造和省略都有 Evidencecraft 语义理由；
- 静态校验通过；
- 自然正例和最近邻负例通过；
- 高风险职责按验收政策完成所需 baseline 或组合场景；
- 没有把旧 Schema、旧 fixture 或 Harness 细节带回生产正文。

流程级：

- 首次 Brief → Plan → 一个 Executor → Review → Report 可运行；
- 正常周期复用 Plan，不重复确认；
- 两个 Executor 对同一次运行互斥，输出接口一致；
- 条件专业 Skills 能正确触发，也能在 current 定义存在时正确跳过；
- 会话可从 progress 和实际文件恢复；
- 重要陈述可追溯到 evidence log、任务结果或明确限制。

验收强度和测试停止规则见 `docs/skill-evaluation-policy.md`。
