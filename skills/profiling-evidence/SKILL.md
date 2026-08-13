---
name: profiling-evidence
description: Use when planning or recovery exposes uncertainty or change in a source's entity, grain, keys, field meaning, time, update/correction behavior, authority, lineage, transformation, coverage, or fitness for a stated analysis use; do not use for ordinary new-period values when current source definitions remain valid.
---

# Profiling Evidence

Determine whether a logical source is fit for a specific, already framed analysis use. Investigate semantics before allowing downstream work to rely on accessibility, familiar column names, or a successful join.

## Own the source-fitness decision

Own these judgments:

- what the source represents and at what grain;
- how records identify and relate to analysis entities;
- which time, update, correction, authority, and transformation semantics apply;
- what coverage and limitations were actually observed;
- whether the source is `FIT`, `QUALIFIED`, `UNFIT`, or `BLOCKED` for each intended use.

Do not change the analysis audience, questions, or scope; define metric populations or formulas; design Work Packages; execute the report; or issue the final analysis review verdict.

## Admit only a real semantic gap

Start from a confirmed Analysis Brief or an exact downstream Return Route, the intended use, the candidate source locator, and any current Source Profile. Inspect actual project files before asking for information already present.

Recover the interaction language, artifact language, and terminology handling independently. A current explicit requirement takes priority; for an existing Run, use its progress record next, then the confirmed Plan and Brief. If legacy artifacts omit the fields, use the primary language of the current substantive request and record the resolved contract in the current Run rather than rewriting historical artifacts. Use the interaction language for any user-facing question or status. Use the artifact language for a new or materially revised Source Profile, including every heading, label, table header, and narrative passage. Preserve canonical decisions, identifiers, paths, citations, code, and source-language titles.

| Condition | Action |
|---|---|
| No named source or no stated intended use | Return to `writing-report-plans`; return to `framing-analysis` if the use itself is undecided. |
| Current Profile covers the same logical source, semantics, and intended use | Record that profiling is skipped and return to planning. |
| Only rows, values, documents, or reporting period contents changed under the same semantics | Do not reopen the Profile; let the Executor record period evidence. |
| Only the interaction or artifact language changed | Do not reopen source semantics; reuse the Profile and let planning apply the current presentation contract. |
| Structure, grain, keys, time, update, authority, lineage, transformation, mapping, or use may differ | Open or revise a Source Profile and investigate. |
| The source cannot be observed or authoritative context is unavailable | Record exactly what is inaccessible and use `BLOCKED`; do not guess. |

A source can be current for one use and unassessed for another. Match both source identity and intended use before skipping.

## Investigate in phases

Read [references/source-profiling-methods.md](references/source-profiling-methods.md) before choosing probes or making a fitness decision. Use only the sections relevant to the source form and risk.

### 1. Observe and reproduce the semantic gap

Preserve the source. Record the logical name, locator, access time, extraction/as-of context, and any available stable citation or hash. Inspect metadata, dictionaries, owner notes, schemas, representative records, and existing transformations without silently cleaning or normalizing them.

State the reported gap in observable terms. Reproduce it with the smallest representative inspection that can distinguish meanings—for example, duplicate entity keys, one-to-many records, boundary timestamps, conflicting status fields, missing receipt time, or an undocumented transformation.

For each source boundary, record:

- what enters and leaves;
- entity and row/document grain;
- candidate primary and foreign keys;
- event, effective, receipt, extraction, and cutoff times that exist or are absent;
- update, correction, deletion, and restatement behavior;
- owning authority, precedence, and lineage;
- transformations already applied;
- coverage and observable limitations.

Separate **observed**, **documented**, **inferred**, and **unknown** statements. A sample demonstrates what was seen, not what must be true for the entire source.

### 2. Localize the meaning boundary

Trace an ambiguous or conflicting field backward through views, exports, formulas, manual edits, joins, and upstream systems until reaching the earliest observable source or an authority boundary. Do not repair the downstream symptom and call the meaning known.

Compare:

- a working versus failing record or period;
- declared documentation versus actual values;
- candidate sources that claim the same authority;
- current behavior versus the last confirmed Profile;
- the intended analysis grain versus native source grain.

List material differences before selecting a cause. A technically valid relationship can still be semantically wrong, many-to-many, temporally misaligned, or non-authoritative.

### 3. Form and test one fitness hypothesis at a time

Write each hypothesis as: “This source is [fit/not fit] for [use] because [specific semantic claim], which would produce [observable result].”

Choose the smallest probe that can falsify it. Change one assumption at a time and record:

- the question;
- exact input or locator;
- method or query summary;
- observed result;
- interpretation and remaining alternatives.

When a probe fails, update the hypothesis; do not layer transformations until the data appears to work. If the source is too large or remote for exhaustive inspection, state the sampling or query boundary and preserve uncertainty.

### 4. Decide fitness by intended use

Use the evidence gathered, not source reputation or convenience:

| Decision | Meaning |
|---|---|
| `FIT` | Observed and authoritative semantics support the intended use without a material unresolved limitation. |
| `QUALIFIED` | The use is supportable only with explicit restrictions, coverage limits, reconciliation, or visible qualifications. |
| `UNFIT` | Known semantics contradict a requirement of the intended use. |
| `BLOCKED` | Required observation or authority is unavailable, so fitness cannot yet be decided. |

Decide separately for each use. State allowed uses, prohibited uses, limitations, and the evidence behind the decision. Never convert `BLOCKED` into `QUALIFIED` simply to keep planning moving.

### 5. Write the Source Profile

Instantiate [assets/source-profile-template.md](assets/source-profile-template.md) at `docs/evidencecraft/sources/<logical-source>-profile.md`. Treat its English headings and labels, including the top-level “Source Profile” document-type label, as semantic slots: render every user-visible part in the artifact language and remove all template comments before saving. Artifact-type phrases in prose are also translatable unless they are exact Skill names, paths, or recorded source-exact terms. Do not edit the template in place. One Profile may cover a tightly coupled logical source group only when its joint semantics cannot be understood separately; otherwise keep profiles source-specific and cross-reference the relationship.

Complete the Profile with actual observations, tests, use-specific decisions, and change triggers. Do not create a Source Contract, EvidenceSnapshot, JSON Schema, lifecycle object, or invented evidence ID.

## Completion gate

Profiling is complete only when:

- the source and intended use are exact;
- relevant dimensions have an observed, documented, inferred, or unknown state;
- material hypotheses have recorded probes and results;
- every intended use has a fitness decision and rationale;
- limitations, prohibited uses, and change triggers are explicit;
- unresolved authority or access gaps are `BLOCKED`, not hidden;
- headings, labels, and narrative use the artifact language apart from recorded terminology exceptions and canonical identifiers;
- the Profile is saved or the response truthfully says persistence was unavailable.

Do not compute the report metric, create the execution plan, or continue downstream work inside this Skill.

## Recovery

On resumption, read the current Profile and inspect the actual source before trusting chat history or a status label.

1. Verify the logical source, locator, intended use, and last observation still match.
2. Recheck the earliest unresolved hypothesis or unavailable boundary.
3. Preserve successful prior observations unless a meaning-bearing change invalidates them.
4. Add new observations and explain which earlier conclusion they revise.
5. Reissue only the affected use decisions; do not re-profile unrelated sources or dimensions.

A corrected same-period file may require new evidence logging without a semantic Profile change. Reopen the Profile only when its meaning, authority, update behavior, or intended use changed.

Do not translate or rewrite an otherwise current Profile merely because a later report uses a different artifact language. Downstream work may consume semantic artifacts in another language while rendering its own outputs under the current contract.

## Return Routes

| Finding | Route and stop |
|---|---|
| Use-specific Profile is complete | Return the Profile path and decision to `writing-report-plans`. |
| Audience, decision, question, scope, or acceptable risk is unresolved | `framing-analysis` |
| Metric population, formula, time basis, aggregation, or cross-source mapping is the unresolved meaning | `defining-metrics` |
| Source should be replaced, added, or used differently in the work design | `writing-report-plans` |
| A query, extraction, calculation, or period-specific data handling failed under already confirmed semantics | Return to the chosen Executor. |
| Evidence is insufficient for a downstream claim | Preserve the limitation and let `reviewing-analysis` route the claim or plan defect. |

The normal Return Route is planning. Report the exact remaining condition for `QUALIFIED`, `UNFIT`, or `BLOCKED` decisions so planning can narrow, replace, or stop the affected work.
