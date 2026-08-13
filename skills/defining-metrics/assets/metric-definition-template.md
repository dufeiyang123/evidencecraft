# Metric Definition: [metric name]

## Status and ownership

- Status: Draft | Ready for Plan Confirmation | Current
- Metric owner: [person or role]
- Intended use: [decision/comparison this supports]
- Analysis Brief: [exact path]
- Report Plan: [candidate/current path or not yet written]
- Current since: [Plan confirmation date or not current]
- Supersedes: [prior Definition path or none]

## Metric interface

- Name: [stable human-readable name]
- Output grain: [one value per entity/period/dimension]
- Unit: [count, ratio, percent, currency, duration, score]
- Direction: [how higher/lower values may be interpreted]
- Allowed dimensions: [segments/cohorts or none]
- Prohibited interpretations: [claims this metric cannot support]

## Population

- Canonical entity: [entity and key]
- Admission rule: [who/what enters and at what effective moment]
- Inclusions: [rules]
- Exclusions: [rules]
- Population source: [Source Profile path and mapped fields]

## Computation

### Numerator

[Membership rule, unit, qualifying state, once-per-entity behavior]

### Denominator

[Eligibility/exposure rule, unit, zero-denominator behavior]

### Formula

```text
[literal formula or pseudocode]
```

### Identity, deduplication, and corrections

- Canonical keys: [fields]
- Deduplication/version order: [rule]
- Cross-source mapping/cardinality: [rule]
- Correction/restatement treatment: [rule]

### Time and cutoff

- Event/effective time: [field, meaning, timezone]
- Period boundaries: [inclusive/exclusive rule]
- Receipt/extraction cutoff: [field and rule]
- Late data: [next cycle, restatement, exclusion, or escalation]

### Missing, zero, unknown, and suppressed

- Missing input: [treatment]
- Zero activity/value: [treatment]
- Unknown classification: [treatment]
- No denominator: [NULL/not reported/other]
- Suppression: [threshold or none]

### Aggregation, comparison, and precision

- Aggregation: [ratio of sums, weighted average, sum, other]
- Weights: [source/rule or none]
- Comparison basis: [prior period/cohort/target and comparability]
- Calculation precision: [rule]
- Display rounding: [stage and rule]

## Source mapping

| Concept | Source Profile | Field/transformation | Fitness/qualification |
|---|---|---|---|
| [population/numerator/time/etc.] | [path] | [exact mapping] | [FIT/QUALIFIED condition] |

## Invariants

- [property] — catches: [specific wrong implementation]
- [property] — catches: [specific wrong implementation]

## Hand-derived examples

### Fixture

| Row | Literal inputs | Expected membership/treatment | Reason |
|---|---|---|---|
| A | [values] | [numerator/denominator/excluded/etc.] | [hand-derived reason] |

### Expected result

- Numerator: [literal]
- Denominator: [literal]
- Metric result: [literal]
- Boundary/counterexample result: [literal]

## Decisions and limitations

### Confirmed

- [choice — authority]

### Tentative

- [choice — owner and resolution point]

### Open

- [material choice — deciding authority and why readiness stops]

### Limitations

- [coverage, comparability, interpretation, or source qualification]

## Currentness and Return Route

- Reuse while: [population/formula/grain/time/mapping conditions]
- Reopen when: [semantic change triggers]
- Ordinary new-period changes that do not reopen: [examples]
- Return to: `writing-report-plans` | `framing-analysis` | `profiling-evidence`
- Next condition: [combined Plan confirmation or exact blocker]
