---
name: writing-report-plans
description: Use when a confirmed Analysis Brief must become a new or revised executable report plan, or when report sections, comparisons, source/metric dependencies, Work Packages, capability boundaries, outputs, verification, or recovery rules have changed; do not use to frame, profile, define, execute, or review the analysis itself.
---

# Writing Report Plans

Translate confirmed analysis meaning into an executable, reviewable Report Plan. Own work decomposition, interfaces, dependencies, verification, stop conditions, and the recommended Executor; do not perform downstream analysis.

## Establish plan state

Inspect the exact Analysis Brief, Source Profiles, Metric Definitions, existing Plan, prior run progress, and project capabilities before drafting.

Resolve the language contract even if no router ran. Scope explicit requirements to the field they govern: an artifact-only delivery instruction does not change user interaction. A current explicit requirement takes priority; for an existing Run, recover its progress contract next, then current Plan/Brief fields. Otherwise use an explicit interaction preference or the primary language of the current substantive request for `interaction_language`, and an explicit deliverable requirement, confirmed audience delivery requirement, or inherited interaction language for `artifact_language`. Use `interaction_language` for questions, options, status, routes, and confirmation messages; use `artifact_language` for the Plan and all downstream persistent artifacts. Record terminology and source-title handling, preserving canonical codes and identifiers, paths, hashes, citations, code, formulas, and original source titles.

| State | Action |
|---|---|
| No confirmed Brief or the intended use changed | Return to `framing-analysis`. |
| A source semantic gap blocks a required use | Route that exact gap to `profiling-evidence`. |
| A reusable metric meaning or mapping is unresolved | Route it to `defining-metrics`. |
| Current Plan covers the same Brief, definitions, sections, interfaces, capabilities, and verification | Reuse it for the new period and proceed to Executor selection. |
| Only period records or values changed | Do not rewrite or reconfirm the Plan. |
| Only `interaction_language` changed | Keep the current Plan and lifecycle state; use the new language for user interaction. |
| `artifact_language` changed while audience and intended use remain the same | Revise and reconfirm only the Plan's report/presentation interface; do not reframe, reprofile, redefine metrics, or repeat language-independent analysis. |
| Sections, comparisons, dependencies, Work Packages, capabilities, outputs, verification, or save/review rules changed | Revise the affected Plan and reconfirm it. |
| A prior run failed because execution violated an unchanged Plan | Return to the chosen Executor; do not redesign around an implementation error. |

Do not call a definition current merely because a file exists. Verify its status, source qualifications, and confirmation relationship.

## Inputs and planning authority

Consume exact paths and current contents for:

- one confirmed Analysis Brief;
- every required Source Profile and its use-specific fitness decision;
- every reusable Metric Definition;
- relevant prior Plan/run files when revising or recovering;
- available capabilities and output constraints.

Decide report structure, data/evidence dependencies, Work Package boundaries, execution order, intermediate/final output locations, completion checks, review package, stop/recovery rules, and one recommended Executor.

Do not decide business scope, source authority, metric population/formula, findings, or review verdicts. Do not bind the reusable Skill to a particular connector, model, platform, or local fixture; a project Plan may name actual available tools and locators.

## Write the Plan

### 1. Preflight semantic dependencies

Map each Brief question and required report section to the exact source uses and Metric Definitions it needs. For each dependency record:

- path and intended use;
- `FIT`, `QUALIFIED`, `UNFIT`, `BLOCKED`, `Ready`, or `Current` state as applicable;
- qualification the Plan must enforce;
- semantic change that would invalidate downstream work.

If a required dependency is `UNFIT` or `BLOCKED`, do not hide it in a Work Package. Return to the responsible specialist or narrow the Plan only with user authority.

### 2. Lock the report and run interfaces

Define the report's required sections, comparison rules, evidence/limitation expectations, delivery profile, and final save path. The default delivery profile is a `standalone reader report`: the audience artifact contains the context needed to understand its conclusions, while governance artifacts point to the report from outside it.

For that profile, make the Plan state all of these interfaces explicitly:

- reader self-containment: which context, methods, key values, and limitations must appear in the report;
- governance separation: the exact Brief, Plan, Profiles/Definitions, evidence log, Run/Work Package/Evidence IDs, review records, statuses, paths, and hashes that stay outside the audience artifact;
- reader citations: formal external sources, URLs, papers, and reader-accessible references remain usable; internal paths never substitute for support;
- tables and figures: put key quantitative content in prose or tables first; use a figure only when it materially improves understanding, and declare its staging path, final asset root, and relative URI mapping;
- export interface: downstream renderers consume only the reviewed Markdown and its declared report-local assets;
- draft/final separation: the draft lives in the Run workspace, the final path is different, and only `reviewing-analysis` may save there after a passing gate.

Do not add an engineering traceability appendix to the reader report by default. If the user explicitly requests audit materials, plan a separate companion dossier. Combine governance material into the reader artifact only when the user explicitly asks for one combined deliverable.

Define the run workspace and common governance interface that either Executor must produce:

- `.evidencecraft/runs/<plan>-<as-of>/progress.md`;
- `evidence-log.md` with a coverage index plus compact evidence cards containing source/upstream locator, period/as-of, identity, observation or derivation, verification, status, reader handling, and limitations;
- report draft at the exact Plan path;
- task briefs/reports only when the multi-agent Executor is selected;
- one real Review Package manifest with exact members and identities;
- an independent whole-report review; a low-risk clean review may use a compact saved record, but may not be replaced by self-review;
- final report destination.

Freeze `interaction_language`, `artifact_language`, and terminology/source-title handling in the Report contract. Require `progress.md` to repeat them as recovery state. The Plan, progress, evidence log, task artifacts, Review Report, draft, and final report use `artifact_language`; user-facing execution updates use `interaction_language`. A worker, reviewer, English source, prompt, or template cannot silently change either field.

Both Executors must preserve these core semantics. Their orchestration artifacts may differ.

### 3. Define Work Packages

Create a Work Package only when its deliverable can be independently checked and a reviewer could reject it without necessarily rejecting its neighbors. Fold setup, access, and formatting into the Package whose deliverable needs them; do not split work into arbitrary tiny actions.

For every Package specify:

1. purpose and linked Brief question/report section;
2. exact frozen inputs and semantic qualifications;
3. upstream dependencies and start condition;
4. procedure at sufficient detail for a capable Executor with no hidden context;
5. sole output path and interface consumed downstream;
6. evidence-log entries and traceability requirements;
7. completion checks with observable expected results;
8. stop conditions and precise Return Routes;
9. whether it is safe to delegate and what context a worker would receive.

Never use “analyze as appropriate,” “handle edge cases,” “validate the result,” or references to another Package without stating the actual interface and check.

### 4. Order dependencies and synthesis

Draw the dependency order explicitly. Parallel-ready Packages must have disjoint outputs and no need to redefine shared sources, metrics, or report text. The final synthesis Package consumes verified Package outputs; it does not rely on worker summaries alone.

Require important statements to trace internally to evidence-log records, verified task results, or explicit limitations. Keep those internal references in governance artifacts; synthesize the supported substance and reader-facing citations into the report. Specify how conflicting evidence, missing coverage, and cross-Package inconsistencies stop or qualify synthesis.

### 5. Recommend exactly one Executor

Recommend `executing-report-plans` when work is sequential, tightly coupled, small enough for one context, or unsafe to isolate. Recommend `subagent-driven-reporting` only when multiple Packages are genuinely independent, context isolation adds value, and the main Agent can verify all task outputs.

State why the recommendation fits this Plan. The run owner must select exactly one before execution and record it in `progress.md`; the two Executors must never operate on the same run concurrently.

### 6. Specify fresh verification and review

For each Package and the whole report, name the command, inspection, reconciliation, hand check, or evidence comparison that will demonstrate completion at execution time. Require fresh outputs from the actual run; prior-period success and worker status labels are not evidence.

Define the exact manifest path and package for `reviewing-analysis`: frozen delivery contract, confirmed Brief, current Plan/Profiles/Definitions, progress by Run ID/status, evidence log, verified Package outputs, draft report, staged assets and final URI mappings when any, and known limitations. Require identities for every stable member; the manifest does not record its own hash, and progress records that hash only after sealing. Define pass, qualified, and blocked handling without preselecting the reviewer verdict.

### 7. Write and self-review

Instantiate [assets/report-plan-template.md](assets/report-plan-template.md) at `docs/evidencecraft/plans/YYYY-MM-DD-<topic>-report-plan.md`. Treat its English headings and labels, including the top-level “Report Plan” document-type label, as semantic slots: render every user-visible heading, field, table header, placeholder replacement, and narrative passage in `artifact_language`, preserve only the recorded canonical or source-exact exceptions, and remove all template comments. Artifact-type phrases in prose are translatable unless they are exact Skill names, paths, or recorded source-exact terms. Do not edit the template in place.

Check:

- every Brief question and report section maps to Work and verification;
- every input/output path and cross-Package interface is exact;
- dependency order has no hidden or circular prerequisite;
- no specialist gap is disguised as execution work;
- both Executors can consume the core interface and remain mutually exclusive;
- stop, recovery, review, and save paths are usable;
- draft and final are distinct, and the synthesis Package writes only the draft;
- the Plan contains an executable reader self-containment, governance-leakage, reference, and asset-resolution check;
- the Review Package is a real manifest rather than a claimed directory or status sentence;
- independent whole-report review is mandatory and no self-review shortcut remains;
- no placeholder or vague completion claim remains.
- the language contract is frozen and all Plan headings, labels, tables, and narrative follow `artifact_language` without template-language leakage.

For a high-impact, multi-source, heavily delegated, or substantially revised Plan, dispatch a fresh-context reviewer using [prompts/report-plan-reviewer.md](prompts/report-plan-reviewer.md), passing the frozen `artifact_language` and terminology/source-title handling explicitly. A `REVISE` finding stops confirmation until repaired; a `BLOCKED` finding returns to the named authority or semantic stage. The reviewer reports defects in `artifact_language` and never silently edits the Plan.

## Confirmation gate

Present the full Plan and recommended Executor for explicit user confirmation, using `interaction_language` for the confirmation request while leaving the Plan itself in `artifact_language`. When the Plan introduces a Metric Definition in `Ready for Plan Confirmation`, present and confirm them together, then update the Plan and Definition confirmation records to `Current` without creating a separate Approval object.

Declare a Plan `Current` only when:

- the Brief is confirmed and all required semantic dependencies are usable;
- every Work Package and interface passes self-review;
- blocking plan-review findings are resolved;
- the user explicitly confirms the written Plan and any bundled Definitions;
- confirmation records the exact paths and accepted qualifications.

If confirmation is unavailable, leave the Plan `Draft` or `Ready for Confirmation` and stop before execution.

## Recovery and completion

On resumption, read the Plan, confirmation, run progress, evidence log, and actual outputs. Use the language contract recorded in progress for an existing Run; English templates, sources, prompts, Profiles, or Definitions do not switch it. If a legacy Brief or Plan lacks language fields, infer the contract from the current explicit requirement or substantive request and record it in progress without bulk-rewriting old artifacts. If the Plan remains current, resume at the earliest incomplete Package; do not replan completed verified work. If a semantic dependency changed, stop affected work, return to its owner, and revise only dependent Packages after the semantic artifact is current again.

Return the Plan path, status, recommended Executor, dependency/qualification summary, and next responsible Skill. Planning completes at a confirmed current Plan or an exact upstream blocker—not at report execution.

## Return Routes

| Finding | Route and stop |
|---|---|
| Confirmed current Plan, sequential Executor selected | `executing-report-plans` |
| Confirmed current Plan, multi-agent Executor selected | `subagent-driven-reporting` |
| Brief meaning or authority changed | `framing-analysis` |
| Source semantics or use fitness unresolved | `profiling-evidence` |
| Reusable metric semantics or source mapping unresolved | `defining-metrics` |
| Execution failed under an unchanged Plan | Return to the selected Executor |
| Draft report is ready for independent assessment | `reviewing-analysis` |

Do not execute, synthesize findings, or review the report inside this Skill.
