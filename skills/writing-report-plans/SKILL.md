---
name: writing-report-plans
description: Use when a confirmed Analysis Brief needs a new or revised executable Report Plan, or its structure, dependencies, Work Packages, outputs, verification, review, or save interfaces changed.
---

# Writing Report Plans

Translate confirmed analysis meaning into an executable, reviewable Report Plan. Own work decomposition, interfaces, dependencies, verification, stop conditions, and a non-binding execution recommendation; do not perform downstream analysis or choose an Executor for a Run.

## Establish plan state

Inspect the exact Analysis Brief, Source Profiles, Metric Definitions, existing Plan, prior run progress, and project capabilities before drafting.

Read and apply [the shared language contract](../using-evidencecraft/references/language-and-localization-contract.md), even if no router ran. Freeze all three fields in the Plan; a current Run repeats them in progress for recovery.

| State | Action |
|---|---|
| No confirmed Brief or the intended use changed | Return to `framing-analysis`. |
| A source semantic gap blocks a required use | Route that exact gap to `profiling-evidence`. |
| A reusable metric meaning or mapping is unresolved | Route it to `defining-metrics`. |
| A sealed Run is ready for independent whole-report review | Route to `reviewing-analysis`; do not resume an Executor. |
| Current Plan covers the same Brief, definitions, sections, interfaces, capabilities, verification, and execution recommendation | Reuse it; a new Run still needs an execution handoff. |
| Legacy Plan records a selected Executor and an existing Run froze it in progress | Preserve it for that Run only. |
| Legacy Plan records a selected Executor but no Run exists | Treat it as a recommendation; do not revise the Plan solely for execution choice. |
| Only period records or values changed | Do not rewrite or reconfirm the Plan. |
| Only `interaction_language` changed | Keep the current Plan and lifecycle state; use the new language for user interaction. |
| `artifact_language` changed while audience and intended use remain the same | Revise and reconfirm only the Plan's report/presentation interface; do not reframe, reprofile, redefine metrics, or repeat language-independent analysis. |
| Sections, comparisons, dependencies, Work Packages, capabilities, outputs, verification, or save/review rules changed | Revise the affected Plan and reconfirm it. |
| A prior run failed because execution violated an unchanged Plan | Return to the Run-selected Executor; do not redesign around an implementation error. |

Do not call a definition current merely because a file exists. Verify its status, source qualifications, and confirmation relationship.

## Inputs and planning authority

Consume exact paths and current contents for:

- one confirmed Analysis Brief;
- every required Source Profile and its use-specific fitness decision;
- every reusable Metric Definition;
- relevant prior Plan/run files when revising or recovering;
- available capabilities and output constraints.

Decide report structure, data/evidence dependencies, Work Package boundaries, execution order, intermediate/final output locations, completion checks, review package, stop/recovery rules, and one recommended execution mode with rationale and feasible alternatives.

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
- task briefs/reports only when a Run selects Subagent-Driven execution;
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

Draw the dependency order explicitly. Decide delegation fitness separately from parallel safety: a Package may be safe for a fresh worker even when it depends on accepted upstream outputs. Mark a Package as parallel-candidate only when it has disjoint reads/writes/resources and no dependency on another candidate. This marker is informational and never authorizes concurrency. The final synthesis Package consumes verified Package outputs; it does not rely on worker summaries alone.

Require important statements to trace internally to evidence-log records, verified task results, or explicit limitations. Keep those internal references in governance artifacts; synthesize the supported substance and reader-facing citations into the report. Specify how conflicting evidence, missing coverage, and cross-Package inconsistencies stop or qualify synthesis.

### 5. Recommend an execution mode

Recommend `subagent-driven-reporting` when every research/production Package intended for worker execution can be bounded by an exact Task Brief and fresh contexts reduce long-run context load. Sequential dependencies do not disqualify it: downstream workers receive only accepted upstream artifacts declared by their briefs. Executor-owned final integration is not a delegated Package. If any required non-integration Package is delegation-unsafe, Subagent-Driven is unavailable unless the Plan is revised; recommend Inline instead.

Recommend `executing-report-plans` when the work is short, small enough for one context, requires sustained whole-run judgment, cannot be bounded safely for delegation, or subagents are unavailable. List every technically available alternative and explain context load, task length, coupling, delegation fitness, and capabilities. Record parallel candidates separately; do not present parallel dispatch as a third normal mode.

The recommendation is advisory. The user chooses Subagent-Driven or Inline at the execution handoff for each new Run, and `progress.md` freezes that Run selection. Changing modes does not revise or reconfirm an otherwise current Plan.

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
- both Executors can consume the core interface, and the Plan does not bind either one to a future Run;
- delegation fitness is not confused with parallel safety;
- stop, recovery, review, and save paths are usable;
- draft and final are distinct, and the synthesis Package writes only the draft;
- the Plan contains an executable reader self-containment, governance-leakage, reference, and asset-resolution check;
- the Review Package is a real manifest rather than a claimed directory or status sentence;
- independent whole-report review is mandatory and no self-review shortcut remains;
- no placeholder or vague completion claim remains.
- the language contract is frozen and all Plan headings, labels, tables, and narrative follow `artifact_language` without template-language leakage.

For a high-impact, multi-source, heavily delegated, or substantially revised Plan, dispatch a fresh-context reviewer using [prompts/report-plan-reviewer.md](prompts/report-plan-reviewer.md), passing the frozen `artifact_language` and terminology/source-title handling explicitly. A `REVISE` finding stops confirmation until repaired; a `BLOCKED` finding returns to the named authority or semantic stage. The reviewer reports defects in `artifact_language` and never silently edits the Plan.

## Confirmation gate

Present the full Plan, including its execution recommendation and feasible alternatives, for explicit user confirmation. Use `interaction_language` for the confirmation request while leaving the Plan itself in `artifact_language`. When the Plan introduces a Metric Definition in `Ready for Plan Confirmation`, present and confirm them together, then update the Plan and Definition confirmation records to `Current` without creating a separate Approval object.

Declare a Plan `Current` only when:

- the Brief is confirmed and all required semantic dependencies are usable;
- every Work Package and interface passes self-review;
- blocking plan-review findings are resolved;
- the user explicitly confirms the written Plan and any bundled Definitions;
- confirmation records the exact paths and accepted qualifications.

Only a user response received after the full Plan was presented can confirm it. An earlier request to continue authorizes at most the transition into planning; it cannot confirm an unseen Plan. If confirmation is unavailable, leave the Plan `Draft` or `Ready for Confirmation` and stop before execution.

After valid confirmation, record it, declare the Plan `Current`, and present the execution handoff. Put the recommended feasible option first, then the other feasible option. Describe Subagent-Driven as `subagent-driven-reporting`, with one fresh worker per Package and task verification/review between Packages. Describe Inline Execution as `executing-report-plans`, with the Main Agent executing Packages in its current context. Mark only the actual first option as recommended.

Ask which approach to use. Generic authorization such as “execute,” “continue,” or “follow the Plan” does not select a mode. An explicit current-Run choice of Inline, Subagent-Driven, or “use the recommendation” does. If only Inline is feasible, state why and still obtain confirmation before execution. Do not create a Run or perform analysis until one mode is selected.

## Recovery and completion

On resumption, read the Plan, confirmation, run progress, evidence log, and actual outputs. Apply the shared language contract. Route a sealed `READY FOR INDEPENDENT REVIEW` Run to `reviewing-analysis`. Route an incomplete Run's progress-frozen Executor to its earliest incomplete Package. If no Run exists, present the execution handoff; planning does not choose on the user's behalf. If a semantic dependency changed, stop affected work, return to its owner, and revise only dependent Packages after the semantic artifact is current again.

Return the Plan path, status, execution recommendation, dependency/qualification summary, and either the execution-choice request or an exact upstream blocker. Planning completes at a confirmed current Plan—not at report execution.

## Return Routes

| Finding | Route and stop |
|---|---|
| Confirmed current Plan, no Run selection | Present the two-option execution handoff and stop. |
| Sealed Run is ready for independent whole-report review | `reviewing-analysis`. |
| Incomplete Run has a frozen Executor | Route that Executor. |
| Brief meaning or authority changed | `framing-analysis` |
| Source semantics or use fitness unresolved | `profiling-evidence` |
| Reusable metric semantics or source mapping unresolved | `defining-metrics` |
| Execution failed under an unchanged Plan | Return to the Run-selected Executor. |

Do not execute, synthesize findings, or review the report inside this Skill.
