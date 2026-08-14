---
name: using-evidencecraft
description: Use when an Evidencecraft analysis or recurring report starts or resumes and no isolated Task Brief or review package already fixes the role.
---

# Using Evidencecraft

Choose the next Evidencecraft responsibility before calculating, drafting, or asking broad discovery questions. This Skill owns routing only; the routed Skill owns the work.

If you were dispatched as an isolated report worker or reviewer, stop using this router. Follow the supplied Task Brief or review package instead and do not reopen the full lifecycle.

## Check actual state

Inspect the request and the relevant workspace for current:

- confirmed Analysis Brief;
- Source Profiles and Metric Definitions when the Plan depends on them;
- confirmed Report Plan and its execution recommendation, including any legacy Plan selection;
- current Run progress and its frozen Executor choice, user selection record, and explicit parallel authorization when present;
- Plan-scoped progress, evidence log, draft, and Review Package;
- latest Review Report, correction record, and final report identity when present;
- language fields in the Brief, Plan, and current Run progress when present;
- stated change in audience, intended use, question, scope, source semantics, metric semantics, or Plan structure.

Read status fields, but verify that named artifacts and required files actually exist. Do not infer a current lifecycle from a polished draft or a stale ledger alone.

## Resolve the language contract before routing

Read and apply [the shared language contract](references/language-and-localization-contract.md). This router owns the initial resolution and passes all three fields to the next Skill; it does not rewrite semantic artifacts. If explicit current requirements conflict, ask the contract's one focused question and stop routing until resolved.

## Classify once

Use the first matching state:

| Observed state | Next responsibility |
|---|---|
| No confirmed Brief for this decision use | `framing-analysis` |
| The request explicitly asks for source profiling, or a Return Route, progress record, or review finding identifies an exact changed/unresolved source semantic or fitness gap | `profiling-evidence`, then planning |
| The request explicitly asks for metric definition, or a Return Route, progress record, or review finding identifies an exact changed/unresolved reusable metric gap | `defining-metrics`, then planning |
| No confirmed usable Plan exists, semantic dependencies still need first preflight, or package/check/save interfaces changed | `writing-report-plans` |
| Only `interaction_language` changed | Keep the current lifecycle state; use the new interaction language and route by the underlying work state. |
| `artifact_language` changed while audience and intended use remain the same | `writing-report-plans` to revise and reconfirm the report interface; reuse current Profiles/Definitions and language-independent analysis. |
| A sealed Run is `READY FOR INDEPENDENT REVIEW`, or corrected artifacts were resealed | `reviewing-analysis` |
| A Review Report is `BLOCKED` | Follow its earliest exact Return Route and affected Package; do not restart everything. |
| Confirmed current Plan and an incomplete non-sealed Run freezes `executing-report-plans` or legacy `sequential` | `executing-report-plans` |
| Confirmed current Plan and an incomplete non-sealed Run freezes `subagent-driven-reporting` | `subagent-driven-reporting` |
| Confirmed current Plan, no Run selection, and the current request explicitly chooses Inline | `executing-report-plans` with that selection record |
| Confirmed current Plan, no Run selection, and the current request explicitly chooses Subagent-Driven or parallel execution | `subagent-driven-reporting`; preserve explicit parallel wording as authorization only when present |
| Confirmed current Plan, no Run selection, and the current request says to use the recommendation | Route the Plan-recommended mode only when it remains feasible; otherwise present the feasible handoff. |
| Confirmed current Plan, no Run selection, and no explicit mode choice | Present the execution handoff and stop before creating a Run. |

A first-time, merely suspected, or unclassified source/metric gap is planning input, not a router investigation. `writing-report-plans` owns the first dependency preflight and invokes a specialist only with an exact intended use and gap. The router recognizes a direct semantic backjump only from explicit or already-recorded evidence.

A normal recurring cycle with the same confirmed use, source semantics, metric semantics, and Plan does not repeat framing or planning. Resume an existing Run with its frozen Executor. For a new Run, obtain one execution-mode choice before an Executor creates progress. New source bytes or a new reporting period alone are execution inputs, not semantic change.

For a legacy Plan with `Selected Executor`, preserve that value only for an existing Run whose progress froze it. With no Run, treat the legacy value as the Plan recommendation and present the normal handoff; do not revise the Plan solely to move execution choice into Run state.

Treat legacy progress value `Executor: sequential` as `executing-report-plans`. Preserve the Run without reprompting and append a compatibility record: selection source `legacy progress`, selection time `unavailable (legacy)`, and parallel authorization `none` unless an exact prior user statement or already-active legacy parallel wave proves otherwise. Do not invent a selection quote or timestamp.

A language change is a delivery constraint, not a new analysis responsibility. Do not return to framing merely because interaction language changed. An artifact-language-only change revises the Plan's report interface and requires confirmation, but does not reopen profiling, metric definition, or unaffected execution. Return to framing only when audience or intended use also changed. For a same-period rerender, preserve the prior report, create a replacement version under the Plan's existing supersession rules, and review the new bytes.

## Route recovery from evidence

For an incomplete run, reconcile progress claims with actual files and identities before choosing the resume point:

- execution or verification defect under unchanged semantics → the Run-selected Executor at the first affected Work Package;
- Work Package, dependency, output, check, execution recommendation, review input, or save-rule defect → `writing-report-plans`;
- source grain, keys, time, authority, lineage, transformation, mapping, access, or fitness defect → `profiling-evidence`, then planning;
- metric meaning, population, formula, time, deduplication, aggregation, missing rule, or source mapping defect → `defining-metrics`, then planning;
- audience, intended use, question, scope, risk, or success criterion change → `framing-analysis`, then planning.

Redo only work that depends on the changed semantic or corrected output. Preserve accepted, current artifacts and prior reports as history.

## Hand off a new Run

When a current Plan has no Run selection, inspect actual subagent capability and present feasible choices in `interaction_language`. Put the Plan-recommended option first when it remains feasible, then the other feasible option, and mark only that Plan-recommended option as recommended. If the stored recommendation is no longer feasible, state why and present the remaining option without relabeling it as the Plan recommendation. Describe Subagent-Driven as `subagent-driven-reporting`, with one fresh worker per Work Package and verification/review between Packages. Describe Inline Execution as `executing-report-plans`, with the Main Agent executing Packages in its current context.

Ask which approach to use and stop. Do not treat “execute,” “continue,” or “follow the Plan” as a choice. Treat an explicit Inline, Subagent-Driven, or “use the recommendation” statement for this Run as a choice. An explicit request for parallel execution selects Subagent-Driven and also supplies parallel authorization; parallel dispatch remains a subordinate, eligibility-gated mechanism rather than a third top-level mode.

If subagents are unavailable, present only Inline with the reason and still obtain confirmation. Do not create progress, inspect execution inputs, or invoke an Executor while waiting.

## Enforce one Run-selected Executor

The chosen Executor creates `progress.md` and records the exact user selection, selection time, and explicit parallel authorization or `none`. Before the first Package starts, an explicit reselection may replace the mode in that otherwise empty Run. Once any Work Package starts, never run the other Executor against that Run. A later mode change stops current writes and starts a new Run ID while preserving the old Run as history; it does not revise an otherwise current Plan. A resumed Run never repeats the handoff.

## Announce and stop

For an ordinary route, return a compact user-visible route record in `interaction_language`. Localize its labels and use at most four bullet lines:

- **State** — always include the canonical state `first setup | current cycle | recovery | review | semantic backjump` and one sentence naming the decisive evidence or change.
- **Next** — always include exactly one next Skill and the exact Work Package or artifact when applicable.
- **Evidence and reuse** — include one combined line only when inspected identities or reusable artifacts are needed to justify the route, backjump, or recovery.
- **Contract or blocker** — include one combined line only when language or terminology handling is non-default, changed, conflicting, or affects delivery, or when an actual blocker or decision is required.

The execution handoff above replaces this route shape while a new Run lacks a choice. Default language handling, identity detail that does not affect the route, and the absence of blockers stay out of the user-visible record. Regardless of what is displayed, pass the complete resolved language contract, governing identities, reusable artifacts and rationale, the exact selection statement, parallel authorization, and any blocking evidence to the routed Skill.

Preserve canonical state values, exact Skill names, identifiers, and paths. If the request asks only for classification, routing, or a handoff recommendation, stop after the route record. Otherwise invoke the routed Skill and continue under its instructions. Do not calculate, profile, define, plan, execute, review, or save while acting as this router.
