---
name: defining-metrics
description: Use when planning or recovery exposes an unresolved or changed reusable quantitative definition—population, numerator, denominator, unit, grain, time basis, deduplication, aggregation, missing-value behavior, comparison, or source mapping; do not use for source-fitness investigation or ordinary new-period values under a current definition.
---

# Defining Metrics

Turn a decision-relevant quantitative concept into a reusable Markdown definition whose meaning can be implemented and checked without inventing business rules. Own metric semantics, not source fitness, work planning, period execution, or report review.

## Admit the metric decision

Start with a confirmed Analysis Brief, the exact intended use, current Source Profiles, any existing Metric Definition, and the planning or review gap that invoked this Skill.

| State | Action |
|---|---|
| No confirmed use or the business question itself is unresolved | Return to `framing-analysis`. |
| Required source grain, authority, time, update, or mapping is unknown | Return the exact gap to `profiling-evidence`. |
| A current Definition covers the same concept, use, population, time, and source mapping | Record that definition work is skipped and return to planning. |
| Only period values or ordinary source contents changed | Reuse the current Definition; do not reapprove it. |
| Population, formula, grain, time, mapping, aggregation, comparison, or interpretation changed | Revise the affected Definition and revalidate it. |
| The measure is a one-off calculation fully specified in the Plan and has no cross-period or cross-result reuse | Keep it in the Plan rather than creating a durable Definition. |

A familiar metric name is not a definition. Treat “retention,” “active,” “conversion,” “average,” and similar labels as unresolved until their operational meaning is explicit.

## Authority and boundaries

Decide and record:

- metric purpose, unit, reporting grain, and allowed dimensions;
- eligible population and exclusions;
- numerator, denominator, formula, weights, and aggregation path;
- entity identity, deduplication, and cross-source mapping;
- event/effective/receipt time, period boundaries, and cutoff handling;
- missing, zero, unknown, late, corrected, and conflicting inputs;
- comparisons, rounding/display rules, limitations, and change triggers;
- invariants and hand-derived examples that can catch a wrong implementation.

The user or named metric owner retains authority over choices that change the business population, success meaning, risk, or official reporting treatment. Do not resolve those choices from convenient data. Do not repair an unfit source here, design Work Packages, run the period calculation, or judge the final claim.

## Define the metric

Read [references/metric-definition-methods.md](references/metric-definition-methods.md) before selecting invariants or examples. Apply only the dimensions that can alter this metric's result or interpretation.

### 1. State the decision interface

Write one sentence each for:

- the decision or comparison this metric supports;
- the entity and reporting grain of one output value;
- the unit and direction of interpretation;
- the consumers that may reuse it.

If two plausible meanings support different decisions, keep them separate. Do not create one overloaded metric with conditional meanings hidden in prose.

### 2. Resolve material choices

Ask one direction-changing question at a time. When multiple responsible definitions exist, present 2–3 approaches with trade-offs and a recommendation. Useful contrasts include snapshot versus period-flow population, account versus contract unit, simple versus weighted rate, event versus receipt time, and strict exclusion versus visible `Unknown`.

Keep each choice **Confirmed**, **Tentative**, or **Open**. A material Open choice stops readiness. Tentative choices must name the owner and the point at which planning will confirm or replace them.

### 3. Specify the computation contract

Define in plain language before pseudocode:

1. population admission and exclusion;
2. canonical entity key and reporting grain;
3. numerator and denominator membership;
4. event correction and deduplication order;
5. source-to-concept mapping and precedence;
6. period assignment, timezone, cutoff, and late data;
7. null, zero, unknown, suppressed, and no-denominator results;
8. aggregation, weighting, comparison, segmentation, and reconciliation;
9. raw precision versus display rounding.

Reference exact current Source Profiles for source semantics. If implementation would need an undefined join, eligibility source, mapping table, status precedence, or time field, return that gap rather than embedding an assumption.

### 4. Write invariants before implementation

State properties that every correct implementation must preserve. Examples include numerator membership being a subset of denominator membership, one contribution per canonical entity-period, compatible units, explicit zero-denominator behavior, partition totals reconciling to the overall result, and corrections never changing event-period assignment unless the definition says so.

Name the realistic error each invariant would catch. Do not assert wording or merely restate a formula.

### 5. Hand-check representative examples

Create a compact fixture inside the Definition containing literal input rows or cases and independently derived expected outputs. Include:

- one ordinary case;
- one boundary case most likely to be implemented incorrectly;
- one exclusion, missingness, correction, or multi-record case relevant to the metric.

Derive expected values by hand. Do not use the proposed implementation, its query, or the same helper logic to generate expectations. If the expected result is disputed, the semantic choice is still Open.

### 6. Write and self-review the Definition

Copy [assets/metric-definition-template.md](assets/metric-definition-template.md) to `docs/evidencecraft/metrics/<metric>-definition.md`. Do not edit the template in place.

Check that:

- purpose, formula, population, grain, time, and source mapping agree;
- numerator and denominator use compatible entities and periods;
- every required field maps to a fit or qualified source use;
- examples exercise the stated invariants with literal expectations;
- limitations and prohibited interpretations are prominent;
- there are no placeholders or hidden Open choices;
- change triggers distinguish semantic changes from ordinary values.

Do not turn the Definition into JSON Schema, executable lifecycle state, or an Approval object.

## Completion and confirmation gate

Return a Definition as `Ready for Plan Confirmation` only when:

- no material Open choice remains;
- source dependencies are exact and sufficiently profiled;
- computation and edge behavior admit one responsible implementation;
- invariants name the breaks they catch;
- hand-derived examples are internally consistent;
- the file states limitations and change triggers.

New or materially revised Definitions become `Current` only when the user confirms them together with the Report Plan that names them. Record that confirmation in the Plan and Definition; do not create a separate machine approval record. Until then, stop before execution.

## Recovery

On resumption, read the Definition, its named Brief/Plan/Profiles, and actual source semantics.

- If it is Draft, resume from the earliest Open or unvalidated choice.
- If it is Ready, verify the candidate Plan still uses the same interface before requesting combined confirmation.
- If it is Current, compare meaning-bearing changes only; new values and periods do not reopen it.
- When a semantic change occurs, preserve the prior Definition for reports that used it, write what changed, and revalidate only affected invariants/examples and consumers.

Never infer currentness from a filename or a formula copied into a report.

## Return Routes

| Finding | Route and stop |
|---|---|
| Definition is Ready for Plan Confirmation | `writing-report-plans` with the Definition path and unresolved tentative conditions |
| Business use, population choice, or acceptable risk is unresolved | `framing-analysis` |
| Source grain, authority, time, update, lineage, or fitness is unresolved | `profiling-evidence` |
| Current Definition is unchanged for a new period | `writing-report-plans`; planning may select the Executor |
| Execution disagrees with the Definition while semantics remain current | Return to the chosen Executor with the violated invariant/example |
| Review finds an ambiguous or unsupported metric meaning | Return to `defining-metrics`, or to the upstream stage named by the actual defect |

The normal terminal state is a readable Definition returned to planning, not a computed metric value.
