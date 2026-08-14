---
name: subagent-driven-reporting
description: Use when a new Evidencecraft Run explicitly selects Subagent-Driven execution or an incomplete Run already freezes `subagent-driven-reporting`.
---

# Subagent-Driven Reporting

Execute one confirmed Report Plan through fresh, isolated workers while the Main Agent remains the sole controller and integrator. Dispatch one research worker at a time by default; context isolation, not parallel speed, is the reason to use this Executor.

## Admit only a Subagent-Driven Run

Start only when a current confirmed Plan exists and:

- the current execution handoff explicitly selected Subagent-Driven for a new Run, or existing progress freezes `subagent-driven-reporting`;
- the exact user selection statement and any explicit parallel request are available for a new Run;
- names Work Packages, dependencies, inputs, unique outputs, checks, review inputs, and final destination;
- supplies current confirmed Brief, Source Profiles when needed, and Metric Definitions when needed;
- defines the standalone reader-report, governance-separation, citation, figure/asset, export, distinct draft/final, and real Review Package manifest interfaces required by `writing-report-plans`;
- every delegated Package can be bounded by an exact Task Brief and checked from its declared output, even when it depends on accepted upstream Packages.

Every required research/production Package must be delegation-safe. Main-Agent integration remains outside worker delegation, but a Plan containing another delegation-unsafe required Package is not executable here; return that interface to `writing-report-plans` before dispatch.

Do not run both Executors for the same active Run ID. Before any Package starts, an explicit reselection may replace the mode in that otherwise empty Run. After work starts, a mode change requires a new Run ID. If this Run selected Inline, route to `executing-report-plans`. If no Run selection exists, return to `using-evidencecraft` for the two-option execution handoff. If a Package cannot be bounded or reviewed from a frozen brief, return that interface defect to `writing-report-plans`; sequential dependencies alone are not defects.

The Main Agent may inspect source availability before dispatch. It must not silently change audience, scope, source meaning, metric meaning, Plan checks, or the Run-selected Executor.

Read and apply [the shared language contract](../using-evidencecraft/references/language-and-localization-contract.md) before creating or resuming a Run. Recover an existing Run from progress first and pass the frozen fields to every worker and reviewer; they cannot change them.

Read and apply [the common Executor output contract](../executing-report-plans/references/executor-output-contract.md). This Skill adds isolated dispatch, task review, and integration; it must return the same core Run and review-handoff interface as sequential execution.

If only `interaction_language` changes, continue the current lifecycle state and use it for subsequent user interaction. If `artifact_language` differs from the confirmed Plan, stop and return to `writing-report-plans` for report-interface revision and reconfirmation; do not dispatch workers or repeat unaffected semantic/analysis work under an unconfirmed language. A same-period rerender preserves the prior report, records the existing replacement relationship, creates a new version under the reconfirmed Plan, and sends the new bytes through task and whole-report review.

## Establish the control plane

Create or resume a Plan-scoped run namespace. Keep all worker briefs, reports, task reviews, corrections, progress, evidence, draft, and Review Package paths inside that run. Use the Plan's exact paths when it specifies them.

Instantiate [the Subagent-Driven progress ledger](assets/subagent-progress-template.md) in `artifact_language`, localizing its headings, labels, table headers, placeholders, narrative, and artifact-type phrases and removing all template comments, with:

- Plan identity and Run ID;
- Run-selected Executor, exact user selection/time, explicit parallel authorization or `none`, frozen language contract, and semantic dependency identities;
- one row per Work Package, including dependencies, owner, unique write paths, dispatch/review state, and accepted output identity;
- integration, draft, and independent-review state.
- evidence-log, staged-asset, Review Package manifest, planned-final, and reader-contract state.

On recovery, read the Plan once, then reconcile the ledger with actual files. A `DONE` status without the required output and checks is not complete. A verified accepted output with a matching identity is not redispatched merely because conversational history is missing. If a legacy parallel wave is already in flight, do not cancel or duplicate it: reconcile each actual worker and file, allow active work to return, preserve successful claims, and process every result through this Executor's verification and task review. Apply the new serial-default and explicit-authorization rules to subsequent dispatches. Never borrow another run's ledger or worker artifacts.

## Schedule from accepted dependencies

Build the dependency graph from the Plan. Select the next dependency-ready Package whose upstream outputs have been accepted. Create its brief, dispatch one fresh worker, verify and review its result, then accept it before selecting another Package.

Never dispatch multiple research workers directly or concurrently from this Skill. Packages with dependencies remain eligible for isolation; pass only accepted upstream artifacts named by the current brief.

If and only if progress records the user's explicit request for parallel execution and at least two Packages appear dependency-ready, identify the complete proposed batch. Instantiate and freeze a separate Task Brief, unique output path, and Task Report path for every candidate before invoking the required subordinate Skill `dispatching-parallel-research`. That Skill independently proves concurrency safety and returns worker claims. After it returns, this Executor still verifies and task-reviews each Package separately before accepting any result. If the subordinate Skill refuses the batch, continue here serially without treating the refusal as a Run blocker.

## Give each worker one frozen brief

Create one [Task Brief](assets/task-brief-template.md) per Work Package. Make it the single source of task requirements. Include exact:

- Plan, Run ID, Work Package ID, goal, and decision use;
- input paths, semantic identities, periods/as-of values, and dependencies;
- source and metric rules that bind the task;
- allowed reads and the worker's unique allowed writes;
- required output, evidence locators, checks, and [Task Report](assets/task-report-template.md) path;
- frozen `interaction_language`, `artifact_language`, and terminology/source-title handling, which the worker may not change;
- explicit prohibitions and Return Routes.

Do not paste unrelated run history. Workers do not dispatch subagents, interact with the user, redefine sources or metrics, edit shared artifacts, integrate other workers, or save the final report.

Task Briefs, worker outputs, Task Reports, and task reviews are governance-layer artifacts. They should retain exact evidence paths, locators, identities, Work Package IDs, and Evidence IDs when those are needed for verification. Do not ask workers to make these artifacts audience-ready or to remove governance detail; the Main Agent owns the separate reader-facing synthesis boundary.

Instantiate each Task Brief and Task Report template in `artifact_language`, treating every English heading, label, and artifact-type phrase—including “Work Package Task Brief” and “Work Package Task Report”—as a semantic slot and removing all template comments. Dispatch a fresh-context worker with [the worker prompt](prompts/report-worker.md), passing `artifact_language` and terminology/source-title handling explicitly. Give access to the brief and its declared inputs, not an informal summary in place of available artifacts. Record the worker identity and dispatch state in progress. A normal dispatch must begin only after the preceding worker has returned and its Package is accepted.

## Treat worker reports as claims

Workers return one of four states:

- `DONE`: claimed output and checks are complete;
- `DONE_WITH_CONCERNS`: output exists, but a named concern needs Main Agent disposition;
- `NEEDS_CONTEXT`: a precise missing input or decision prevents safe work;
- `BLOCKED`: access, capability, or governed requirements prevent completion.

For `NEEDS_CONTEXT` or `BLOCKED`, inspect the actual condition. Supply already-governed context when available. Route source access or fitness to `profiling-evidence`, metric meaning to `defining-metrics`, Plan defects to `writing-report-plans`, and changed use/scope to `framing-analysis`. Do not tell a worker to guess.

For `DONE` or `DONE_WITH_CONCERNS`, the Main Agent must inspect the actual output and report, rerun or independently spot-check the Plan's highest-risk task checks, confirm precise evidence locators, and verify the worker stayed inside its write scope. Status prose is never proof.

## Require independent task review

After Main Agent verification, dispatch a fresh read-only reviewer using [the task-reviewer prompt](prompts/task-reviewer.md). Give it the Task Brief, Task Report, exact output and identity, binding semantic artifacts, required checks, `artifact_language`, and terminology/source-title handling. The worker cannot review its own work or change the language contract.

The task reviewer returns:

- `ACCEPT`: requirements, evidence, checks, and scope all pass;
- `REVISE`: one or more blocking findings name exact evidence, impact, and correction;
- `BLOCKED`: required review evidence or a governing decision is unavailable;
- advisory observations that do not change acceptance.

The Main Agent verifies every blocking finding against the actual artifacts. Unsupported reviewer feedback is rejected only with counter-evidence recorded in progress.

For a valid `REVISE`, send the exact open findings to the original worker when possible. The worker appends a correction record to its Task Report and writes a new output identity. Then dispatch [the task-reviewer prompt](prompts/task-reviewer.md) in scoped re-review mode with the prior findings, prior identity, correction record, and current output identity. The re-review must verdict every prior finding and inspect the changed output for new consequential defects. Never accept a correction without re-review.

Follow the Plan's risk-proportionate correction stop rule rather than importing a fixed review-round count from code workflows. Continue only while a round has a concrete, verifiable correction path; when the same blocking condition repeats without new evidence, capability, or authority, route semantic or planning defects to their owning stage and mark the package blocked. Do not normalize repeated failure into acceptance.

## Accept, then integrate

Accept a Work Package only after actual-output verification and `ACCEPT`, or after all blocking findings are `CLOSED` by re-review. Record its exact output identity, evidence locators, review path/verdict, and accepted state in progress. Downstream Packages may consume only accepted outputs; then choose the next Package and dispatch a new worker with no inherited conversation history.

The Main Agent alone then:

1. reconciles cross-package grain, period, population, denominators, categories, and semantic identities;
2. rejects contradictions or incompatible outputs instead of averaging, choosing silently, or smoothing them in prose;
3. instantiates the common [Evidence log template](../executing-report-plans/assets/evidence-log-template.md) and applies the shared evidence interface;
4. performs the Plan's integration and cross-section checks;
5. synthesizes one reader-facing draft whose consequential statements are supported by accepted evidence without exposing the internal traceability mechanism;
6. verifies required sections, comparisons, limitations, and save language;
7. applies the common reader-boundary, asset, final-destination, and fresh-verification checks.

The Main Agent also verifies that accepted worker outputs and task reviews use `artifact_language` except for the frozen canonical/source-exact exceptions. Language-contract violations are task defects, not harmless stylistic differences.

If an integration defect is execution-only under unchanged semantics, reopen the first affected Work Package with this Executor. If the packages or checks cannot compose as planned, return to `writing-report-plans`. Semantic defects take their earlier Return Routes.

## Seal the common Executor interface

Apply the common Executor contract's seal sequence, including the common [Review Package template](../executing-report-plans/assets/review-package-template.md). Add every accepted worker output, Task Brief, Task Report, and task review to the verified handoff. Freeze them in dependency order before integrated outputs and shared artifacts.

Route the sealed package to `reviewing-analysis` only after every Package is accepted and every integration check passes. Task reviews verify individual handoffs; they never replace independent whole-report review.

## Result

Return the common Executor handoff result plus accepted/blocked Work Packages and worker/task-review identities. Include any parallel-dispatch batch record, but do not treat dispatch status as acceptance. Name `reviewing-analysis` only when sealed; otherwise return one exact blocker. Use `interaction_language` for the user-facing result and `artifact_language` for persistent artifacts.
