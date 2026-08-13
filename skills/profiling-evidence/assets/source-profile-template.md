<!-- Template use: render every heading, label, table header, placeholder replacement, and narrative passage in the confirmed artifact language. The sample title's “Source Profile” phrase is a translatable artifact-type label, not a canonical identifier. Preserve canonical decisions, IDs, exact Skill names, paths, citations, code, and source-language titles. Remove this and every Template instruction comment from the instantiated artifact. -->

# Source Profile: [logical source]

## Profile context

- Logical source: [stable human-readable name]
- Locator: [path, query/view, document, or connector-neutral locator]
- Intended analysis use: [specific downstream use]
- Analysis Brief: [exact path]
- Requested by: [planning, recovery, or Return Route]
- Observed at: [timestamp/date]
- Extraction/as-of context: [version, period, cutoff, or snapshot]
- Stable citation/hash: [value or unavailable with reason]
- Artifact language: [language for this durable Profile]
- Terminology and source-title handling: [translation, first-use explanation, or preserve-original rules]

## Fitness summary

| Intended use | Decision | Rationale | Required qualification or resolution |
|---|---|---|---|
| [use] | FIT / QUALIFIED / UNFIT / BLOCKED | [evidence-backed reason] | [none or exact condition] |

## Observed semantics

### Identity, entity, and grain

- Producer/owner: [observed or documented authority]
- Native entity: [entity represented]
- Native grain: [one record/document represents]
- Analysis-grain relationship: [same, one-to-many, many-to-one, many-to-many, unknown]

### Keys and relationships

- Candidate primary key: [fields and observed uniqueness]
- Foreign/composite keys: [fields, scope, nullability]
- Match coverage/cardinality: [observations]
- Unresolved key risks: [none or details]

### Required field meaning

| Field or concept | Meaning | Basis | State |
|---|---|---|---|
| [name] | [business meaning/unit/status] | observed / documented / inferred / unknown | [usable limitation] |

### Time, update, and correction

- Event/effective time: [meaning and timezone]
- Receipt/extraction/publication time: [meaning or absent]
- Period and cutoff behavior: [inclusion rule]
- Refresh/update mode: [append, overwrite, snapshot, other]
- Late arrival/correction/deletion/restatement: [behavior and evidence]

### Authority, lineage, and transformation

- Source of record and precedence: [authority or unknown]
- Upstream origin: [lineage]
- Transformations: [filter, join, formula, aggregation, normalization, manual edit]
- Unobservable boundary: [none or exact boundary]

### Coverage and observable quality

- Population and date span inspected: [coverage]
- Missing cohorts/partitions: [none or details]
- Nulls, duplicates, conflicts, or anomalies: [material observations]
- Inspection limits: [sampling, row caps, permissions, hidden history]

## Hypotheses and probes

| Question or hypothesis | Input/locator | Method | Observed result | Interpretation |
|---|---|---|---|---|
| [falsifiable claim] | [exact scope] | [probe summary] | [result] | [supported/refuted/unknown] |

## Allowed and prohibited uses

### Allowed

- [use and required qualification]

### Prohibited

- [use the evidence cannot support and why]

## Limitations and unknowns

- [material limitation, owner, and resolution condition]

## Currentness and change triggers

- This Profile remains current while: [source identity, semantics, and use conditions]
- Reopen when: [grain/key/time/update/authority/lineage/mapping/use change]
- Ordinary new-period content that does not reopen this Profile: [examples]

## Return Route

- Decision: [FIT / QUALIFIED / UNFIT / BLOCKED by intended use]
- Return to: `writing-report-plans` | `framing-analysis` | `defining-metrics` | chosen Executor
- Next condition: [what the receiving stage must do or resolve]
