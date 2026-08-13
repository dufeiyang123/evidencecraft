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
- language fields in the Brief, Plan, and current Run progress when present;
- stated change in audience, intended use, question, scope, source semantics, metric semantics, or Plan structure.

Read status fields, but verify that named artifacts and required files actually exist. Do not infer a current lifecycle from a polished draft or a stale ledger alone.

## Resolve the language contract before routing

Determine two independent fields. Scope each requirement to the field it governs, then apply this evidence order:

1. the user's explicit current requirement for interaction or delivery language;
2. a confirmed audience delivery requirement in the current Brief, Plan, or Run;
3. the primary language of the current substantive user request.

Set `interaction_language` from an explicit interaction preference, otherwise from the primary language of the current substantive request. Set `artifact_language` from an explicit deliverable requirement, then a confirmed audience delivery requirement; if neither applies, inherit it from `interaction_language`. An artifact-only instruction such as “deliver the report in English” does not switch questions or confirmations away from the user's Chinese request. Ignore incidental foreign terms, links, citations, code, and quoted source titles when detecting the request's primary language; a Simplified Chinese request defaults to Simplified Chinese.

Record terminology and source-title handling with the contract. Translate user-visible headings, labels, table headers, placeholders, narrative, and artifact-type phrases such as “Analysis Brief,” “Report Plan,” and “Review Report”; those phrases are not canonical identifiers even when they appear in a top-level title. Preserve canonical status/verdict codes, Work Package IDs, exact Skill names, paths, hashes, citations, code, formulas, original source titles, and recorded proper-name exceptions. English Skill text, templates, prompts, sources, Profiles, or Definitions never override the contract.

Infer without asking when these rules produce one answer. If two explicit current requirements conflict, ask exactly one confirmation question in the primary language of the current request, then stop routing until resolved. For a legacy Brief or Plan without language fields, pass the inferred contract to the responsible Skill and, when a current Run exists, record it in progress; localize the newly appended section, labels, and narrative in `artifact_language` even when the preserved surrounding history is in another language. Literal field keys such as `interaction_language` may appear in backticks for recovery clarity. Do not rewrite historical content merely to add or localize the fields.

## Classify once

Use the first matching state:

| Observed state | Next responsibility |
|---|---|
| No confirmed Brief for this decision use | `framing-analysis` |
| Confirmed Brief exists, but source fitness/meaning needed by the report is unknown or changed | `profiling-evidence`, then planning |
| Confirmed Brief exists, but a reusable metric meaning, population, time rule, or source mapping is unknown or changed | `defining-metrics`, then planning |
| Governing semantics are current, but no confirmed usable Plan exists or package/check/save interfaces changed | `writing-report-plans` |
| Only `interaction_language` changed | Keep the current lifecycle state; use the new interaction language and route by the underlying work state. |
| `artifact_language` changed while audience and intended use remain the same | `writing-report-plans` to revise and reconfirm the report interface; reuse current Profiles/Definitions and language-independent analysis. |
| Confirmed current Plan selects sequential execution and the run is new or incomplete | `executing-report-plans` |
| Confirmed current Plan selects multi-agent execution and the run is new or incomplete | `subagent-driven-reporting` |
| A sealed package is ready, or corrected artifacts were resealed after review findings | `reviewing-analysis` |
| A review is BLOCKED | Follow its earliest exact Return Route and affected Package; do not restart everything. |

A normal recurring cycle with the same confirmed use, source semantics, metric semantics, and Plan does not repeat framing or planning. Create or resume the period's Run ID and use the Plan-selected Executor. New source bytes or a new reporting period alone are execution inputs, not semantic change.

A language change is a delivery constraint, not a new analysis responsibility. Do not return to framing merely because interaction language changed. An artifact-language-only change revises the Plan's report interface and requires confirmation, but does not reopen profiling, metric definition, or unaffected execution. Return to framing only when audience or intended use also changed. For a same-period rerender, preserve the prior report, create a replacement version under the Plan's existing supersession rules, and review the new bytes.

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
- resolved interaction language, artifact language, and terminology/source-title handling;
- evidence inspected and governing identities, when available;
- one next Skill and exact Work Package or artifact, when applicable;
- artifacts reused and reason they remain current;
- blocking evidence or decision required, if any.

Write the route record in `interaction_language`, preserving the canonical state values, Skill names, identifiers, and paths. If the request asks only for classification, routing, or a handoff recommendation, stop after the route record. Otherwise invoke the routed Skill and pass the resolved contract explicitly before continuing under that Skill's instructions. Do not calculate, profile, define, plan, execute, review, or save while acting as this router.
