---
name: using-evidencecraft
description: Use at the start of an evidence-analysis or recurring report request to inspect the actual Evidencecraft artifact state, classify the work as first setup, current cycle, recovery, review, or semantic backjump, and route to exactly one responsible skill before downstream work begins.
---

# Using Evidencecraft

Choose the next Evidencecraft responsibility before calculating, drafting, or asking broad discovery questions. This Skill owns routing only; the routed Skill owns the work.

If you were dispatched as an isolated report worker or reviewer, stop using this router. Follow the supplied Task Brief or review package instead and do not reopen the full lifecycle.

## Check actual state

Inspect the request and the relevant workspace for current:

- confirmed Analysis Brief;
- Source Profiles and Metric Definitions when the Plan depends on them;
- confirmed Report Plan and its one selected Executor;
- Plan-scoped progress, evidence log, draft, and Review Package;
- latest Review Report, correction record, and final report identity when present;
- stated change in audience, intended use, question, scope, source semantics, metric semantics, or Plan structure.

Read status fields, but verify that named artifacts and required files actually exist. Do not infer a current lifecycle from a polished draft or a stale ledger alone.

## Classify once

Use the first matching state:

| Observed state | Next responsibility |
|---|---|
| No confirmed Brief for this decision use | `framing-analysis` |
| Confirmed Brief exists, but source fitness/meaning needed by the report is unknown or changed | `profiling-evidence`, then planning |
| Confirmed Brief exists, but a reusable metric meaning, population, time rule, or source mapping is unknown or changed | `defining-metrics`, then planning |
| Governing semantics are current, but no confirmed usable Plan exists or package/check/save interfaces changed | `writing-report-plans` |
| Confirmed current Plan selects sequential execution and the run is new or incomplete | `executing-report-plans` |
| Confirmed current Plan selects multi-agent execution and the run is new or incomplete | `subagent-driven-reporting` |
| A sealed package is ready, or corrected artifacts were resealed after review findings | `reviewing-analysis` |
| A review is BLOCKED | Follow its earliest exact Return Route and affected Package; do not restart everything. |

A normal recurring cycle with the same confirmed use, source semantics, metric semantics, and Plan does not repeat framing or planning. Create or resume the period's Run ID and use the Plan-selected Executor. New source bytes or a new reporting period alone are execution inputs, not semantic change.

## Route recovery from evidence

For an incomplete run, reconcile progress claims with actual files and identities before choosing the resume point:

- execution or verification defect under unchanged semantics → the Plan-selected Executor at the first affected Work Package;
- Work Package, dependency, output, check, Executor selection, review input, or save-rule defect → `writing-report-plans`;
- source grain, keys, time, authority, lineage, transformation, mapping, access, or fitness defect → `profiling-evidence`, then planning;
- metric meaning, population, formula, time, deduplication, aggregation, missing rule, or source mapping defect → `defining-metrics`, then planning;
- audience, intended use, question, scope, risk, or success criterion change → `framing-analysis`, then planning.

Redo only work that depends on the changed semantic or corrected output. Preserve accepted, current artifacts and prior reports as history.

## Enforce one Executor

The confirmed Plan selects exactly one Executor for a Run ID. Never run `executing-report-plans` and `subagent-driven-reporting` against the same run. If the requested execution mode differs from the Plan, route to `writing-report-plans` to revise and reconfirm it before execution.

## Announce and stop

Return a compact route record:

- classified state: `first setup | current cycle | recovery | review | semantic backjump`;
- evidence inspected and governing identities, when available;
- one next Skill and exact Work Package or artifact, when applicable;
- artifacts reused and reason they remain current;
- blocking evidence or decision required, if any.

If the request asks only for classification, routing, or a handoff recommendation, stop after the route record. Otherwise invoke the routed Skill and continue under that Skill's instructions. Do not calculate, profile, define, plan, execute, review, or save while acting as this router.
