# Evidencecraft 项目计划

状态：`ACTIVE — CROSS-HARNESS SKILLS PLUGIN`

当前生产源已扩展为九 Skill 流程集，继续由 Claude Code、Codex 与 OpenClaw 共用同一
skills-only/bundle plugin，并作为 `v0.5.0` 发布。无活动 Schema；无仓库内历史评测套件。

目标：维护并扩展适度完整、可移植、可组合的周期证据报告方法；只有职责达到独立 Skill 门槛时
才扩展当前流程集，并持续保持 Claude Code、Codex 与 OpenClaw 插件可发布。

## 1. 产品目标

Evidencecraft 主要服务中初级数据分析师的口径翻译、多表关联、临时分析和周期报告维护，优先
处理跨部门对账、零散分析和周期复用。数仓是主要分析对象，项目规则、已有实现和优质历史
报告帮助选择研究策略；核心不绑定具体平台、连接器或业务系统，不承担深度数据治理。

口径、计算和证据要求稳定，分析视角与表达允许按场景调整。“覆盖日常 60% 以上工作”仍需
定义统计口径并验证；工作流约束的实现不代表已验证覆盖率、数值稳定性、可读性或 token 降幅。

MVP 负责澄清目标、写计划、执行、记录证据、审查和保存报告。连接、认证、定时触发、工具
映射和外部发布属于 Harness，不写进核心 Skills。

## 2. 主流程

```text
using-evidencecraft
→ framing-analysis
→ writing-report-plans（相关资料、有限健康检查、策略与报告蓝图）
→ 新 Run 执行 handoff
→ executing-report-plans 或 subagent-driven-reporting（计算验证 → 写作）
→ reviewing-analysis
→ 保存报告
```

计划阶段只有在发现独立语义缺口时才调用：

```text
writing-report-plans
  ↳ profiling-evidence → 返回 planning
  ↳ defining-metrics   → 返回 planning
```

Brief 和 Plan 记录业务范围及口径的实际授权依据；已有明确指令不重复询问，不声称用户已审阅
未展示的文件。只确认未解决的实质选择，并遵守用户要求的审批点。Plan 保存执行建议；新 Run
沿用明确选择、适用偏好或授权范围内的可行默认，在 progress 中冻结依据。正常周期复用 Plan；
本期数值、行数、快照身份和校验结果留在 Run；计划前观察保存在 preparation 中并由 Run 引用，
不把它们变成长期 Plan 的固定预期，也不因普通周期变化重新 Profiling/定义 Metric。

Plan 决策完整指问题、口径、方法和交接明确，不要求提前得到报告结论。先检索相关项目资料，
区分权威规则、可复用实现和历史方法样例；历史数值、结论与口径不能自动继承。通用健康检查
只覆盖任务所需来源、字段和周期，优先有效已有检查与元数据，查询必须有可信成本边界。
抽样不证明全量，未检查不是通过，检查通过不代表业务含义已知。关键检查受限时先交付清楚
标注影响与解除条件的 Draft，阻断正式执行；非关键缺口可带限制继续，不新增固定确认环节。

## 3. 首个九 Skill 流程集

| Skill | 主要判断权 | 默认结果 | 对应 Superpowers 结构模式 |
|---|---|---|---|
| `using-evidencecraft` | 识别首次、周期、恢复、回跳或新 Run handoff | 下一责任、执行选择或简短路由记录 | 类似 `using-superpowers`：高频、短小、自包含，不接管下游工作 |
| `framing-analysis` | 冻结对象、读者、用途、范围和风险 | `analysis-brief.md` | 类似 `brainstorming`：完整澄清与确认流程；可带 Brief 模板或独立 fresh-context reviewer prompt |
| `writing-report-plans` | 方案级调研、数据准备度、研究策略与执行接口 | 两层 `report-plan.md`、按需 preparation 与非绑定推荐 | 类似 `writing-plans`：精确输入、依赖、任务、验证与执行 handoff |
| `executing-report-plans` | 执行 Run 已选择的 Inline 模式 | progress、evidence log、报告草稿 | 类似 `executing-plans` + verification：覆盖预检、忠实执行、阻断、恢复和新鲜验证 |
| `subagent-driven-reporting` | 逐个委派 fresh worker 并验收交接 | task briefs/reports、同一核心输出 | 类似 `subagent-driven-development`：上下文隔离、文件化交接、任务审查和 ledger；不等同并行 |
| `dispatching-parallel-research` | 判断显式授权的 ready Packages 是否可并发 | 并发 worker claims，返回父 Executor | 类似 `dispatching-parallel-agents`：独立问题域才并发，不拥有整合或 review |
| `reviewing-analysis` | 独立核对证据、限制和结论 | pass/qualified/blocked 与 Return Routes | 类似 code-review Skills：允许独立 reviewer prompt、输入包契约、反馈分级和责任阶段 Return Routes |
| `profiling-evidence` | 判断来源语义和用途适用性 | 按需 `source-profile.md` | 类似 `systematic-debugging`：正文承载调查阶段；稳定来源维度和诊断技术可拆 References，重复探查稳定后才脚本化 |
| `defining-metrics` | 冻结可复用定量口径 | 按需 `metric-definition.md` | 结合 brainstorming、planning 与 TDD 不变量；可带 Metric Definition 模板和详细口径 Reference |

每个 Skill 创建前必须实际阅读表中对应的 Superpowers `SKILL.md`；表格摘要不能替代原文研究。
表中结构是创建时的设计起点，不是必须生成的文件清单。应比较对应 Skill 的正文和配套文件，
再按 Evidencecraft 的职责保留、改造或省略；每个附加 prompt、Reference、template、script 或
metadata 都必须有明确调用方，不追求文件或行数一一相同。

未来新增的表外 Skill 先研究职责最近邻的一个或多个 Superpowers 流程模式；若没有直接对应项，
仍需完成 `writing-skills` 研究并说明独立 Skill 的必要性、借鉴机制和有意省略项。

## 4. Markdown 交接

默认布局：

```text
docs/evidencecraft/
  specs/YYYY-MM-DD-<topic>-analysis-brief.md
  plans/YYYY-MM-DD-<topic>-report-plan.md
  preparations/<id>/preparation.md          # 仅需保存调研交接时；不创建 Run
  sources/<logical-source>-profile.md       # 仅在需要时
  metrics/<metric>-definition.md            # 仅在需要时
.evidencecraft/runs/<plan>-<as-of>/
  progress.md
  evidence-log.md
  outputs/...                               # 经验证结果、计算实现与设置；也可引用项目已有版本
  task-N-brief.md                            # 仅委派时
  task-N-report.md                           # 仅委派时
  draft.md
  assets/                                    # 仅有读者图像时；发布前 staging
  review-package.md                          # 真实、封存的 manifest
  review.md                                  # 必需独立审查；记录详略按风险
reports/YYYY-MM-DD-<topic>.md
reports/assets/<topic>/...                   # 仅有已审查的报告本地 assets 时
```

路径是约定，不是文件清单：

- Brief 和 Plan 是长期语义基线；
- preparation 是一份有下游消费者的调研记录，供 Plan、Executor 与 review 引用；被 Run 使用
  的版本保留，后续观察另存。不是新健康报告、审批对象或计划阶段的 Run；
- Source Profile 只用于实际使用、含混、变化或跨周期复用的来源；
- Metric Definition 只用于跨周期复用、影响多个结果或高风险的口径；
- progress、evidence log、任务交接和草稿默认是临时运行文件；
- 最终 Markdown 是可独立阅读的纯读者产物；默认不包含 Brief、Plan、Evidence log、Review
  Package、Run/WP/Evidence ID、审查状态、hash 或工程型追溯附录；
- 正式外部引用和作为报告主题本身的代码/文件名可以保留，但不能要求读者访问仓库才能理解结论；
- 正文先回答读者问题，以简短解释、紧凑表格或适当图形呈现关键数值；逐行计算明细保留在证据中，
  用户明确要求的读者明细附件应声明并审查；报告核心结论无需仓库访问即可理解；
- Review Package 是包含真实成员路径与 identity 的封存 manifest，不是状态文字或虚拟目录；
- 治理产物单向记录已审查报告及其 identity，最终报告不反向引用治理链；
- 下游 PDF 转换只消费通过审查的最终 Markdown 与已声明 assets，不需要理解 Evidencecraft；
- 低风险 clean review 可以用紧凑记录，高风险/阻断才保存完整 `review.md`；两者都必须实际执行
  独立整报告审查，并在保存后记录 draft → final identity 映射；
- 不为没有真实机器消费者的交接创建 JSON Schema。

宿主计划模式禁止写文件时，在会话中使用相同内容结构交付，明确尚未保存；允许写入后保存
授权内容与引用，再进入执行，不重复完整调研。

### Analysis Brief 最小内容

- 对象、读者和用途；
- 目标、非目标和问题；
- 范围、周期和风险；
- 成功标准；
- 读者产物是否需要独立阅读及预期交付格式；
- 已确认、暂定和开放选择；
- 语义缺口、精确确认记录和 Return Route；
- 相关项目资料、候选数据、已有实现/历史样例的精确引用，以及已知访问和查询成本限制；
- 不在 Brief 中设计路径、Work Package、证据卡或渲染细节。

### Report Plan 最小内容

- 面向用户的任务理解、数据现状、策略与依据、报告蓝图、重要限制和真正需要决定的问题；
- 蓝图映射问题、指标/维度、证据要求与表达方式，不预填结论；条件下钻需有触发和停止边界；
- 执行部分引用 preparation，区分已完成且可复用的工作与剩余任务；
- Brief 精确引用；
- 周期、`as-of` 和时效规则；
- 来源与按需 Source Profiles；
- 指标与按需 Metric Definitions；
- 报告章节与默认 `standalone reader report` 交付契约；
- reader self-containment、governance separation 和正式外部引用政策；
- 按读者问题组织的表达、数值精度、表格/图形选择，以及 assets/附件的 staging、最终路径和 URI 映射；
- 最终 Markdown 加声明 assets 作为下游转换器的完整输入；
- Work Packages、依赖、输出位置和完成检查；
- 一个非绑定执行建议、可行替代、delegation boundary 和仅供判断的 parallel candidates；
- 新 Run handoff 在授权范围内解析 Executor，Run progress 冻结方式、实际依据/来源、时间和并行授权；
- Run draft 与不同 final path、Executor 不提前写 final 的规则；
- 停止条件、Return Routes、真实 Review Package manifest、独立整报告 review 输入和保存位置；
- 默认不生成工程型追溯附录；明确需要审计材料时生成独立 companion dossier，除非用户要求合并。

### Task brief/report

工作 Agent 只接收任务目的、冻结输入、可复用准备工作及条件、剩余任务、约束、唯一输出位置、
完成检查和停止条件。返回实际输入、方法、输出、验证、限制，以及
`DONE | DONE_WITH_CONCERNS | NEEDS_CONTEXT | BLOCKED`。
Task Brief、Task Report 与 worker output 属于治理层，应保留精确路径、locator 和 Evidence ID。
状态不是证据，主 Agent 必须检查真实产物；task review 只验收 Work Package，不能替代整报告
独立审查。

### Evidence log

每期采用“覆盖索引＋紧凑证据卡片”：索引把报告要求/结论映射到 Evidence ID、支持状态和报告
处理；卡片记录支持对象、精确来源与 locator、period/`as-of`、identity、观察或计算、验证、
状态与限制。unsupported、blocked 和 conflict 单独保留，不为缺失信息制造大量空字段。同周期
修正增加新记录并说明替代关系，不创建 Snapshot 对象图。

有效 preparation 以引用接入证据日志，记录复用依据，不再复制完整检查表。匹配快照、参数、
覆盖、方法、结果身份和时效后才复用；新周期复用方法与代码，不能继承旧健康结论。

### 计算与写作

Executor 复用合适的项目 SQL/模型/脚本或同语义的已接受运行实现；没有时在工作包约定位置
建立并验证。绑定完整输入、语义与代码版本、影响结果的设置，以及带实体/周期/维度、单位和
精度的结果。新建或修改实现用独立预期案例和相同固定输入重复计算验证；修复保留旧版本和
更正关系。验收针对规范化业务数值，不要求报告文字或文件字节每次一致。

写作读取已接受的结果、证据索引及相关 Plan 部分。新增占比、增幅等数值返回计算责任者，
在语义不变时不重开全套规划。计算、写作是同一 Executor 内的职责，不强制拆工作包或 Agent。
manifest 纳入实际依赖的 preparation、支持记录/提取、计算实现及设置，不封存未使用的资料库。

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

只重做真正依赖变化语义的工作，不因来源字节变化重做全链。纯表达调整由产出阶段完成，审查新字节，
不重新确认未改变的业务语义。修复复审检查历史问题、真实差异和受影响依赖；语义变化广或影响不明
时扩大为完整审查。机械检查仅在输入/输出/校验程序身份和时效仍有效时复用，不能替代独立判断。

既有 Plan 不批量迁移。缺少 preparation 字段时，在下次 Run 预检中补足必要证据；只有真实
策略、接口或范围缺陷返回 planning。缺少可验证历史实现的计算，在首次执行建立基线，不追认
过去的确定性。

## 6. 建设顺序

一次创建、验证并审阅一个 Skill：

1. `framing-analysis`
2. `profiling-evidence`
3. `defining-metrics`
4. `writing-report-plans`
5. `executing-report-plans`
6. `reviewing-analysis`
7. `subagent-driven-reporting`
8. `dispatching-parallel-research`
9. `using-evidencecraft`

入口最后创建，因为它必须路由到已经可靠的下游；Subagent-Driven 在顺序闭环可靠后创建，
Parallel Skill 在其父 Executor 稳定后创建。

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

- 首次 Brief → Plan → execution handoff → 一个 Executor → Review → Report 可运行；
- 正常周期复用 Plan；新 Run 在已有授权范围内解析执行方式，仅询问实质分歧，恢复时不重复询问；
- 两个顶层 Executor 对同一次运行互斥，输出接口一致；Parallel Skill 只在显式授权后从
  Subagent-Driven 临时调用；
- 条件专业 Skills 能正确触发，也能在 current 定义存在时正确跳过；
- 会话可从 progress 和实际文件恢复；
- 重要陈述可追溯到 evidence log、任务结果或明确限制。
- 最终 Markdown 可脱离 `.evidencecraft` 与 `docs/evidencecraft` 独立阅读，并只把自身及已声明
  assets 交给 PDF 等下游转换器；
- Review Package manifest 的每个成员真实存在且 identity 匹配，draft/final 分离，保存后
  `draft identity → final path / identity` 只记录在治理产物中。

验收强度和测试停止规则见 `docs/skill-evaluation-policy.md`。

## 8. 后续 Skill 与插件分发

第 3 节列出的九个 Skills 是首个可运行流程集，不是产品上限。未来只有候选满足独立自然
Trigger、主要判断权、可观察结果、停止门和 Return Route 时，才按 `AGENTS.md` 与验收政策
增加新的生产 Skill；普通知识、固定格式和确定性操作仍优先使用 Reference、模板或脚本。

所有未来 Skill 都进入同一根 `skills/`，由 Claude Code、Codex 与 OpenClaw 插件共享，不为
Harness 复制实现。每次 Skill 更新必须保持三平台插件可发布，但版本同步、Git tag、GitHub
Release、ClawHub release 和远端 push 只在用户明确授权后执行。具体门、双历史同步方式和远端
tag 验收见
`docs/plugin-release-workflow.md`。
