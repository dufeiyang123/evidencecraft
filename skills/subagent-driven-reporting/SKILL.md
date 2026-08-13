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
- defines the standalone reader-report, governance-separation, citation, figure/asset, export, distinct draft/final, and real Review Package manifest interfaces required by `writing-report-plans`;
- contains at least two packages that can be understood and completed without jointly mutating shared state.

Do not run both Executors for the same Run ID. If the Plan selects `executing-report-plans`, route there. If packages are coupled, write the same output, require unresolved results from one another, or cannot be reviewed independently, return to `writing-report-plans` or use the Plan-selected sequential Executor after the Plan is revised.

The Main Agent may inspect source availability before dispatch. It must not silently change audience, scope, source meaning, metric meaning, Plan checks, or Executor selection.

Recover the language contract independently before creating or resuming a Run. Apply a current explicit field-scoped requirement first; otherwise, for an existing Run, use the contract in progress, then the confirmed Plan and Brief, then the primary language of the current substantive request. If legacy artifacts lack language fields, record `interaction_language`, `artifact_language`, and terminology/source-title handling in the current progress ledger without rewriting old artifacts. The Main Agent uses `interaction_language` for user questions, status, routing, and confirmation. All persistent run artifacts—including progress, Task Briefs, worker outputs, Task Reports, task reviews, evidence, Review Package, and report draft—use `artifact_language`. Preserve canonical codes and identifiers, paths, hashes, citations, code, formulas, and original source titles. English sources, prompts, templates, Profiles, or Definitions cannot change the frozen contract.

If only `interaction_language` changes, continue the current lifecycle state and use it for subsequent user interaction. If `artifact_language` differs from the confirmed Plan, stop and return to `writing-report-plans` for report-interface revision and reconfirmation; do not dispatch workers or repeat unaffected semantic/analysis work under an unconfirmed language. A same-period rerender preserves the prior report, records the existing replacement relationship, creates a new version under the reconfirmed Plan, and sends the new bytes through task and whole-report review.

## Establish the control plane

Create or resume a Plan-scoped run namespace. Keep all worker briefs, reports, task reviews, corrections, progress, evidence, draft, and Review Package paths inside that run. Use the Plan's exact paths when it specifies them.

Instantiate [the multi-agent progress ledger](assets/multi-agent-progress-template.md) in `artifact_language`, localizing its headings, labels, table headers, placeholders, narrative, and artifact-type phrases and removing all template comments, with:

- Plan identity and Run ID;
- selected Executor, frozen language contract, and semantic dependency identities;
- one row per Work Package, including dependencies, owner, unique write paths, dispatch/review state, and accepted output identity;
- integration, draft, and independent-review state.
- evidence-log, staged-asset, Review Package manifest, planned-final, and reader-contract state.

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
- frozen `interaction_language`, `artifact_language`, and terminology/source-title handling, which the worker may not change;
- explicit prohibitions and Return Routes.

Do not paste unrelated run history. Workers do not interact with the user, redefine sources or metrics, edit shared artifacts, integrate other workers, or save the final report.

Task Briefs, worker outputs, Task Reports, and task reviews are governance-layer artifacts. They should retain exact evidence paths, locators, identities, Work Package IDs, and Evidence IDs when those are needed for verification. Do not ask workers to make these artifacts audience-ready or to remove governance detail; the Main Agent owns the separate reader-facing synthesis boundary.

Instantiate each Task Brief and Task Report template in `artifact_language`, treating every English heading, label, and artifact-type phrase—including “Work Package Task Brief” and “Work Package Task Report”—as a semantic slot and removing all template comments. Dispatch a fresh-context worker with [the worker prompt](prompts/report-worker.md), passing `artifact_language` and terminology/source-title handling explicitly. Give access to the brief and its declared inputs, not an informal summary in place of available artifacts. Record the worker identity and dispatch state in progress.

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

Accept a Work Package only after actual-output verification and `ACCEPT`, or after all blocking findings are `CLOSED` by re-review. Record its exact output identity, evidence locators, review path/verdict, and accepted state in progress. Downstream packages may consume only accepted outputs.

The Main Agent alone then:

1. reconciles cross-package grain, period, population, denominators, categories, and semantic identities;
2. rejects contradictions or incompatible outputs instead of averaging, choosing silently, or smoothing them in prose;
3. instantiates the common [Evidence log template](../executing-report-plans/assets/evidence-log-template.md), maintaining its coverage index and compact evidence cards with exact governance locators, support status, and propagated qualifications;
4. performs the Plan's integration and cross-section checks;
5. synthesizes one reader-facing draft whose consequential statements are supported by accepted evidence without exposing the internal traceability mechanism;
6. verifies required sections, comparisons, limitations, and save language;
7. applies the same reader-report checks as `executing-report-plans`: the draft is self-contained; key values are in prose or tables; current-run Brief/Plan/Evidence log/Review Package/progress paths, Run/WP/Evidence IDs, review states, identities, hashes, and engineering traceability are absent; `...`, globs, brace expansion, and path-only “see file” references are absent; every Markdown image has the Plan-declared staging-to-final mapping; and the final Markdown/assets remain unwritten.

Formal external citations, paper links, reader-accessible URLs, and code or file names that are substantive report subject matter remain allowed. They cannot make repository access a prerequisite, act as governance navigation, or substitute for reader-facing explanation.

The Main Agent also verifies that accepted worker outputs and task reviews use `artifact_language` except for the frozen canonical/source-exact exceptions. Language-contract violations are task defects, not harmless stylistic differences.

If an integration defect is execution-only under unchanged semantics, reopen the first affected Work Package with this Executor. If the packages or checks cannot compose as planned, return to `writing-report-plans`. Semantic defects take their earlier Return Routes.

## Seal the common Executor interface

Produce the same core handoff as `executing-report-plans`:

- Plan-scoped progress;
- evidence log;
- verified Work Package outputs, plus worker Task Briefs, Reports, and task reviews;
- one report draft;
- one real Review Package manifest instantiated from the common [Review Package template](../executing-report-plans/assets/review-package-template.md), repeating the frozen language and delivery contracts and enumerating current member paths and identities.

Freeze stable artifacts in dependency order: accepted worker outputs and task reviews, integrated outputs, evidence log, report draft, then staged reader assets. Build the Review Package manifest from those stable identities. The manifest does not record its own hash or a mutable progress hash. After sealing, record its actual identity once in progress, whose status may continue changing under the same Run ID.

Before marking the run `READY FOR INDEPENDENT REVIEW`, open and inspect every manifest member, verify every recorded identity against the actual current file, reject missing files and placeholder hashes, resolve every staged/final asset mapping, and freshly confirm that the final Markdown/assets do not exist. Record the actual files and identities checked in progress. Route the sealed package to `reviewing-analysis` only after all packages are accepted and every integration and package check passes. Task reviews verify individual handoffs; they never replace independent whole-report review. This Skill does not approve or save the final report.

## Result

Return Run ID, accepted and blocked Work Packages, worker and task-review identities, checks performed, progress/evidence/draft/Review Package paths, unresolved concerns and exact Return Routes, and—only when sealed—the route to `reviewing-analysis`. Use `interaction_language` for this user-facing result and `artifact_language` for the referenced persistent artifacts.
