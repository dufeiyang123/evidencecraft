---
name: writing-report-plans
description: Research relevant project context and data readiness to create or revise a Report Plan from an authorized Analysis Brief, including strategy, report blueprint, work interfaces, and verification; not full report analysis or writing.
---

# Writing Report Plans

Turn authorized analysis intent into a researched, readable Plan. Own strategy, bounded preparation, dependencies, work interfaces, and recovery. A decision-complete Plan resolves business and method choices; empirical results may remain unknown. Business scope belongs to framing, source-fitness diagnosis to profiling, metric meaning to definition, findings to execution, and independent verdicts to review.

## Establish state

Read the Brief and relevant existing Plan. Inspect referenced semantic dependencies for the uses this Plan requires; open prior progress or review findings when revising or recovering. Verify status and authority, not merely file existence.

Apply the resolved [language contract](../using-evidencecraft/references/language-and-localization-contract.md). When defining delivery or presenting decisions, read [the reader and decision contract](../using-evidencecraft/references/reader-and-decision-contract.md).

| State | Action |
|---|---|
| No authorized Brief or changed business meaning | Return to `framing-analysis`. |
| Exact source fitness or reusable metric gap | Route that gap to its specialist, then resume planning. |
| Current Plan still covers meaning and execution interfaces | Reuse it; new period values alone do not reopen planning. |
| Sealed Run ready for independent review | `reviewing-analysis`. |
| Execution violated an unchanged Plan | Return to the Run's Executor. |
| Dependency, output, check, capability, or save interface changed | Revise affected interfaces and dependent work only. |

Language or layout adjustments within the authorized delivery contract stay with the producer. A binding delivery-interface change belongs here; the explicit request itself may authorize it. Do not reconfirm unchanged business meaning.

## Build the executable contract

### 1. Research only decisions that shape the Plan

Map Brief questions to candidate sources and metrics. Search project indexes and relevant passages before reading whole documents. Distinguish authoritative business/metric rules, existing SQL/models, and historical analysis examples. Check authority, date, scope, and applicability; a polished historical report may suggest methods or structure, but cannot authorize its old formula or transfer its numbers and conclusions. Record the adopted approach and relevant exceptions, not a literature review.

Before establishing a Current Plan, assess the task's data readiness using the **Planning and Run health checks** section of [source-profiling-methods.md](../profiling-evidence/references/source-profiling-methods.md). Reuse valid observations first. Each additional read-only probe must resolve a named strategy or feasibility question within a known cost boundary. Stop once the questions, metrics, methods, usable sources, and material limits are clear. Do not compute full business metrics, perform attribution, or build report figures here.

Keep one preparation record when persistence supports handoff, recovery, or audit. Use [assets/preparation-notes-template.md](assets/preparation-notes-template.md) under `docs/evidencecraft/preparations/<id>/preparation.md`, or the project's analysis workspace. It records exact references, bounded observations, strategy choices, reusable work and remaining conditions; it is not a second report or a Run. Preserve versions already referenced by a Run. If host planning restrictions prohibit writes, return the Plan and preparation content in the conversation with exact references; persist when permitted, without claiming files already exist.

Explain data readiness to the user as achievable analysis, material impact, and a recommended adjustment. A passing check adds no confirmation gate. If a critical observation or capability is unavailable, provide a useful **Draft** with affected work and release conditions, not an executable Current Plan. Non-critical gaps may remain explicit qualifications. Negotiate only material changes to scope, source, period, meaning, or delivery; an authorized narrower scope can become Current after its own requirements are satisfied.

### 2. Resolve semantic dependencies and capability

Record exact semantic artifact references, intended use, usable status, qualifications, and invalidation triggers. A missing Profile or Definition is not automatically a gap: invoke specialists only when source meaning/fitness or reusable metric meaning actually needs investigation. Pass relevant preparation evidence to the specialist instead of restarting discovery. A generic health check does not establish business meaning or source authority.

Do not conceal `UNFIT`, `BLOCKED`, or a material unresolved choice inside a Package. Obtain the responsible semantic or business decision before affected execution. Definitions `Ready for Plan Confirmation` may be incorporated once their material choices have an authoritative basis.

Check that execution and independent whole-report review are feasible before costly work. Inline does not remove the independent-review requirement. Record an unavailable capability as a blocker; an explicit change to an unreviewed draft leaves this audited-final workflow and cannot satisfy its review/save gate.

### 3. Separate reusable meaning from observations

The Plan contains period parameters, source-selection/freshness rules, semantic versions, output interfaces, and verification methods. Reference preparation observations as dated decision evidence; do not copy them into recurring requirements. Current file identities, counts, and snapshots stay in preparation before a Run, then in or referenced from Run evidence. Never freeze a sample period's values as future expected results.

A check may require a true invariant, such as conservation across transfer legs, or an independently derived reconciliation total. Explain why it must hold and how the expected result is obtained. A date-specific assertion belongs to that Run unless the task explicitly concerns a fixed historical snapshot.

### 4. Define delivery and remaining work

Put the user-facing analysis proposal first: task understanding, data readiness, recommended strategy and rationale, report blueprint, and material limits or choices. Keep execution detail below it. The blueprint maps reader questions to required metrics/evidence and presentation intent, without predicted findings. Bound any result-triggered drilldown by its trigger, allowed dimensions, and stop condition; analysis structure may adapt within these authorized bounds.

Default to a standalone reader report. Specify the questions and consequential information readers must find, necessary method explanations, qualifications, language, and external citations. Use the shared reader contract to choose prose, compact tables, or figures. Full intermediate tables need not be copied into the report. Declare any required companion deliverable and its review/save interface.

Define these exact Run interfaces:

- Plan-scoped workspace, progress, evidence log, verified Package outputs, and draft path;
- staged reader assets, final asset root, and relative-URI mappings when used;
- final report path distinct from the draft; the Executor never writes final destinations;
- a real manifest containing identities of stable review inputs, with mutable progress referenced by Run ID/status rather than its hash;
- independent whole-report review and its saved record, followed by exact reviewed-byte/asset saving only through `reviewing-analysis`.

Downstream rendering consumes the reviewed reader Markdown and declared reader assets. Governance points to the report from outside; internal IDs, hashes, workflow logs, and audit navigation stay in governance. If audit materials are requested, use a separate dossier unless the user asks for a combined deliverable.

Create a Work Package when its output can be checked and rejected independently. Fold setup, access, and formatting into the deliverable they support. A short analysis may need only one Package plus integration; do not split work to create more agent or review stages.

Each Package needs:

1. purpose and linked question;
2. exact input selectors/references, semantic qualifications, accepted dependencies, reusable preparation and its validity conditions;
3. remaining procedure sufficient for a capable Executor, with formulas owned by Definitions or an explicit one-off Plan rule; identify existing computation implementations or where execution will establish them;
4. owned output path/interface and evidence requirements;
5. observable completion checks, expected-result derivation, and check owner;
6. stop conditions and exact Return Routes;
7. delegation fitness and the minimum context a worker needs.

Use parameterized paths for recurring data, resolving exact current identities in the Run. A worker's Task Brief pins its actual inputs before dispatch. Do not use vague instructions such as “validate the result.”

### 5. Order work and allocate verification

Make dependencies explicit and acyclic. Delegation safety is separate from parallel safety. Parallel candidates need accepted prerequisites and no conflicting write, mutable resource, or source-session ownership; candidate status never authorizes concurrency.

Assign each deterministic check to one producing owner and define its method and expected-result derivation; the producer records actual observations when it runs. Main-Agent acceptance verifies outputs and check bindings rather than automatically repeating calculations. Independent task review still examines consequential correctness; whole-report review checks reader usefulness, coverage, cross-Package consistency, and claim support.

Read **Consume preparation before repeating work** and **Verify once per valid evidence boundary** in the [common Executor contract](../executing-report-plans/references/executor-output-contract.md) when designing reuse. Its computation section governs numerical handoffs: execution produces verified results and versioned SQL/scripts; writing consumes accepted results and evidence. New derived numbers return to their calculation owner. These are responsibilities within the chosen Executor, not mandatory separate Packages, agents, or approval stages.

### 6. Recommend execution

Recommend Inline for short work, sustained whole-run judgment, unavailable delegation, or work that cannot be bounded safely. Recommend Subagent-Driven when exact Task Briefs and fresh contexts are likely to reduce context load enough to justify worker and review overhead. Every non-integration Package in that mode must be delegation-safe; final integration remains Main-Agent-owned.

State the rationale and any material cost/capability trade-off. Do not list infeasible alternatives or force a menu when no decision is needed. The router resolves a new Run using explicit choices, applicable preferences, and feasible authorized defaults; progress freezes that resolution. Parallel execution still needs explicit authorization for the Run.

Do not hardcode models, reasoning effort, connectors, or Harnesses in the reusable Skill. Plans may name actual capabilities. Respect user and environment settings; any optional resource allocation must remain within their authority.

## Write, review, and establish readiness

When writes are permitted, instantiate [assets/report-plan-template.md](assets/report-plan-template.md) at `docs/evidencecraft/plans/YYYY-MM-DD-<topic>-report-plan.md`. Apply the shared language contract and omit unused optional slots. Use the same structure in the conversation when persistence is unavailable.

Self-review coverage, exact interfaces, dependencies, semantic authority, qualifications, check ownership, delegation boundaries, recovery, reader usability, draft/final separation, and executable review/save gates. Resolve placeholders and hidden choices.

Use [prompts/report-plan-reviewer.md](prompts/report-plan-reviewer.md) for an independent readiness review when new or changed interfaces create unresolved high-consequence semantic, ownership, or verification risk after self-review. Multiple sources or many Packages alone do not trigger another reviewer. If this review is required but unavailable, record the blocker. The initial review covers the complete Plan; subsequent review focuses on prior findings, actual changes, and affected dependencies, widening when impact is uncertain.

A Plan becomes `Current` when the Brief and required semantic dependencies are usable, critical planning checks are satisfied, required reviews have no blocking findings, and material choices have authority. Full report calculations and execution checks need not have run. Record each new business/metric choice and its real authorization source. Update bundled Definitions to `Current` only for meaning covered by that authority.

Present the proposal, including data readiness and material choices, with the saved Plan link or conversation artifact. Ask only unresolved material choices, or honor an explicitly requested Plan approval checkpoint. Existing instructions authorize routine execution design; never claim that they confirm an unseen file. If authority is missing, leave `Draft` or `Ready for Confirmation` and stop dependent execution.

## Completion and recovery

Return the saved Plan path or conversation artifact, readiness, material qualifications, and next action. Route a persisted Current Plan through `using-evidencecraft` to resolve a new Run, resume the frozen Executor, or review a sealed package. A Draft never admits formal execution; continue useful planning while blocking dependent work. Only the bounded preparation above belongs here, not full report analysis or writing.

On change, preserve earlier records, identify affected dependencies, and redo only invalidated work. Business changes return to framing; source changes to profiling; metric changes to definition; execution mistakes to the current Executor. A presentation-only correction does not reopen semantic work.
