---
name: subagent-driven-reporting
description: Use when a confirmed Report Plan explicitly selects the multi-agent Executor and contains genuinely independent Work Packages; coordinate isolated workers, verify and review each handoff, integrate accepted evidence, and produce the same draft and Review Package interface as sequential execution.
---

# Subagent-Driven Reporting

Execute one confirmed Report Plan through isolated workers while the Main Agent remains the sole integrator. Parallelism changes who performs independent Work Packages; it never weakens semantic control, evidence verification, or review.

## Admit only a multi-agent run

Start only when the current confirmed Plan:

- explicitly selects `subagent-driven-reporting` as its one Executor;
- names Work Packages, dependencies, inputs, unique outputs, checks, review inputs, and final destination;
- supplies current confirmed Brief, Source Profiles when needed, and Metric Definitions when needed;
- contains at least two packages that can be understood and completed without jointly mutating shared state.

Do not run both Executors for the same Run ID. If the Plan selects `executing-report-plans`, route there. If packages are coupled, write the same output, require unresolved results from one another, or cannot be reviewed independently, return to `writing-report-plans` or use the Plan-selected sequential Executor after the Plan is revised.

The Main Agent may inspect source availability before dispatch. It must not silently change audience, scope, source meaning, metric meaning, Plan checks, or Executor selection.

## Establish the control plane

Create or resume a Plan-scoped run namespace. Keep all worker briefs, reports, task reviews, corrections, progress, evidence, draft, and Review Package paths inside that run. Use the Plan's exact paths when it specifies them.

Initialize [the multi-agent progress ledger](assets/multi-agent-progress-template.md) with:

- Plan identity and Run ID;
- selected Executor and semantic dependency identities;
- one row per Work Package, including dependencies, owner, unique write paths, dispatch/review state, and accepted output identity;
- integration, draft, and independent-review state.

On recovery, read the Plan once, then reconcile the ledger with actual files. A `DONE` status without the required output and checks is not complete. A verified accepted output with a matching identity is not redispatched merely because conversational history is missing. Never borrow another run's ledger or worker artifacts.

## Prove independence before dispatch

Build the dependency graph from the Plan. A group is parallel-safe only when every package in it:

- depends only on accepted upstream artifacts already present;
- has a distinct owner and distinct output/report/review paths;
- does not edit the shared evidence log, progress ledger, report draft, Review Package, or final report;
- does not compete for a source session, mutable extract, rate limit, temporary table, or other shared resource in a way that can change results;
- can be verified against its own required evidence and acceptance checks.

Dispatch all dependency-ready, parallel-safe packages together. Serialize packages that share mutable state or a constrained source even if their topics differ. Parallelism is optional; isolation and correct dependencies are mandatory.

## Give each worker one frozen brief

Create one [Task Brief](assets/task-brief-template.md) per Work Package. Make it the single source of task requirements. Include exact:

- Plan, Run ID, Work Package ID, goal, and decision use;
- input paths, semantic identities, periods/as-of values, and dependencies;
- source and metric rules that bind the task;
- allowed reads and the worker's unique allowed writes;
- required output, evidence locators, checks, and [Task Report](assets/task-report-template.md) path;
- explicit prohibitions and Return Routes.

Do not paste unrelated run history. Workers do not interact with the user, redefine sources or metrics, edit shared artifacts, integrate other workers, or save the final report.

Dispatch a fresh-context worker with [the worker prompt](prompts/report-worker.md). Give access to the brief and its declared inputs, not an informal summary in place of available artifacts. Record the worker identity and dispatch state in progress.

## Treat worker reports as claims

Workers return one of four states:

- `DONE`: claimed output and checks are complete;
- `DONE_WITH_CONCERNS`: output exists, but a named concern needs Main Agent disposition;
- `NEEDS_CONTEXT`: a precise missing input or decision prevents safe work;
- `BLOCKED`: access, capability, or governed requirements prevent completion.

For `NEEDS_CONTEXT` or `BLOCKED`, inspect the actual condition. Supply already-governed context when available. Route source access or fitness to `profiling-evidence`, metric meaning to `defining-metrics`, Plan defects to `writing-report-plans`, and changed use/scope to `framing-analysis`. Do not tell a worker to guess.

For `DONE` or `DONE_WITH_CONCERNS`, the Main Agent must inspect the actual output and report, rerun or independently spot-check the Plan's highest-risk task checks, confirm precise evidence locators, and verify the worker stayed inside its write scope. Status prose is never proof.

## Require independent task review

After Main Agent verification, dispatch a fresh read-only reviewer using [the task-reviewer prompt](prompts/task-reviewer.md). Give it the Task Brief, Task Report, exact output and identity, binding semantic artifacts, and required checks. The worker cannot review its own work.

The task reviewer returns:

- `ACCEPT`: requirements, evidence, checks, and scope all pass;
- `REVISE`: one or more blocking findings name exact evidence, impact, and correction;
- `BLOCKED`: required review evidence or a governing decision is unavailable;
- advisory observations that do not change acceptance.

The Main Agent verifies every blocking finding against the actual artifacts. Unsupported reviewer feedback is rejected only with counter-evidence recorded in progress.

For a valid `REVISE`, send the exact open findings to the original worker when possible. The worker appends a correction record to its Task Report and writes a new output identity. Then dispatch [the task-reviewer prompt](prompts/task-reviewer.md) in scoped re-review mode with the prior findings, prior identity, correction record, and current output identity. The re-review must verdict every prior finding and inspect the changed output for new consequential defects. Never accept a correction without re-review.

Use at most three correction rounds per package unless the Plan sets a lower cap. After the cap, route unresolved semantic or planning defects to their owning stage and mark the run blocked; do not normalize repeated failure into acceptance.

## Accept, then integrate

Accept a Work Package only after actual-output verification and `ACCEPT`, or after all blocking findings are `CLOSED` by re-review. Record its exact output identity, evidence locators, review path/verdict, and accepted state in progress. Downstream packages may consume only accepted outputs.

The Main Agent alone then:

1. reconciles cross-package grain, period, population, denominators, categories, and semantic identities;
2. rejects contradictions or incompatible outputs instead of averaging, choosing silently, or smoothing them in prose;
3. writes the shared evidence log with claim IDs, precise locators, support status, and propagated qualifications;
4. performs the Plan's integration and cross-section checks;
5. synthesizes one report draft with every consequential statement traceable to accepted evidence;
6. verifies required sections, comparisons, limitations, and save language.

If an integration defect is execution-only under unchanged semantics, reopen the first affected Work Package with this Executor. If the packages or checks cannot compose as planned, return to `writing-report-plans`. Semantic defects take their earlier Return Routes.

## Seal the common Executor interface

Produce the same core handoff as `executing-report-plans`:

- Plan-scoped progress;
- evidence log;
- verified Work Package outputs, plus worker Task Briefs, Reports, and task reviews;
- one report draft;
- one Review Package manifest.

Freeze stable artifacts in dependency order: accepted worker outputs and task reviews, integrated outputs, evidence log, then report draft. Build the Review Package from those stable identities. Record its identity once in progress, whose status may continue changing under the same Run ID. Do not put a mutable progress hash inside the stable manifest or create a self-referential hash cycle.

Mark the run `READY FOR INDEPENDENT REVIEW` only after all packages are accepted and all integration checks freshly pass. Route the sealed package to `reviewing-analysis`. Task reviews verify individual handoffs; they never replace independent whole-report review. This Skill does not approve or save the final report.

## Result

Return Run ID, accepted and blocked Work Packages, worker and task-review identities, checks performed, progress/evidence/draft/Review Package paths, unresolved concerns and exact Return Routes, and—only when sealed—the route to `reviewing-analysis`.
