# Source Profiling Methods

Planning and Executors read **Planning and Run health checks** for routine readiness; profiling also reads the relevant diagnostic sections for a real semantic gap. Cover only dimensions that can change the intended-use decision.

## Planning and Run health checks

Bound the check by the analysis question, candidate sources, required fields, period, and known rules. Inspect relevant warehouse metadata, files or documents; do not scan a whole warehouse or launch deep governance. Prefer existing valid checks, dictionaries and metadata, then the smallest read-only probe needed for a decision.

| Check | Applicable evidence and boundary |
|---|---|
| Access and structure | Required objects/fields exist and can be inspected; distinguish unavailable access, cached previews and full source state. |
| Time coverage and freshness | Required partitions/periods, snapshot or watermark, and declared update/cutoff expectations. |
| Required values | Nulls, types, units and domain constraints only for fields required by this use, against an explicit rule or documented expectation. |
| Declared keys | Uniqueness at the declared grain, including scope and composite keys; repeated IDs alone are not a defect. |
| Candidate relationships | Expected cardinality and match coverage for the proposed source slices; a successful join alone proves neither correct meaning nor complete coverage. |

Establish query cost bounds from project limits, provider estimates/enforced budgets, or demonstrably bounded local input. A row-output LIMIT or read-only flag alone does not bound warehouse scanning cost. With no reliable boundary, use metadata or existing observations and record the necessary query as not checked. Do not silently exceed a budget or substitute invented thresholds.

Record the decision served, exact inputs/snapshot and parameters, check method/implementation identity, full versus sampled coverage, cost boundary, time, observed result and limits. Known rules supply expectations; missing rule authority is an unresolved question, not an automatic failure or pass. Nulls and negative values can be valid. Sampled success cannot prove full coverage; unperformed checks remain explicitly unverified.

Planning stores relevant observations in its preparation record; execution links valid preparation evidence into its evidence log and renews only invalid checks using the common Executor reuse contract. A new period does not inherit last period's health result. Passing these checks does not establish source semantics or authority. Route real semantic gaps to profiling; ordinary access or period-specific issues stay with the caller, which handles the blocker and any required user decision. Do not repair source data or infer a governance mandate.

## Source dimensions

| Dimension | Questions to resolve | Useful observations |
|---|---|---|
| Identity and provenance | What logical source is this? Is the locator stable? Who produced it? | System/file/view name, owner, version/extract, access time, citation/hash |
| Entity and grain | What does one row, record, event, document, or cell range represent? | Entity examples, uniqueness counts, repeated keys, nested or multi-valued fields |
| Keys and relationships | Which identifiers are stable, scoped, composite, reused, or nullable? | Uniqueness, nulls, orphan keys, match rates, one-to-many/many-to-many paths |
| Field meaning | What business state does each required field encode? | Dictionary definitions, observed values, units, enums, blanks, conflicting labels |
| Time semantics | Is time an event, effective, snapshot, receipt, extraction, publication, or correction time? | Timezone, inclusivity, boundary records, multiple timestamps, period assignment |
| Update and correction | Append, overwrite, snapshot, late arrival, deletion, restatement, or manual repair? | Refresh cadence, watermark, change history, receipt lag, replacement rules |
| Authority and precedence | Which source or role decides truth when values conflict? | Named steward, policy, source-of-record declaration, override and reconciliation rules |
| Transformation and lineage | What filtering, joins, formulas, aggregation, normalization, or manual edits occurred? | Upstream chain, query/view logic, workbook formulas, export settings, edit history |
| Coverage and quality | Which population, periods, fields, and exceptions are present or absent? | Counts, null/duplicate rates, date span, category distribution, missing cohorts |
| Access and observability | Can the relevant state be inspected and reproduced? | Permissions, truncation, pagination, row limits, hidden sheets, unavailable history |
| Intended use | Which downstream decision, metric input, comparison, or claim will consume it? | Required grain, population, cutoff, authority, precision, and risk tolerance |

Native grain and intended analysis grain are separate facts. Aggregation may bridge them only after the aggregation rule is defined by the responsible metric or plan stage.

## Diagnostic probes

### Structural probe

Inspect schema or headings, record counts, types, units, representative values, nulls, duplicates, and nested structures. Confirm that the inspection covers the real source rather than a preview, cached subset, or rendered export.

Use structural probes to discover candidate meanings. Do not infer authority, completeness, or stability from structure alone.

### Relationship probe

Measure uniqueness at each candidate key and match coverage in both directions. Inspect unmatched and multiply matched examples. Test composite keys and time-scoped identifiers when a simple identifier appears reusable.

Record the observed cardinality. “The join ran” does not establish that the join represents the intended entity or period.

### Temporal boundary probe

Inspect records immediately before, at, and after period/cutoff boundaries. Distinguish business-event time from receipt or extraction time. Check timezones, inclusive/exclusive rules, late arrivals, corrections, and snapshot effective dates.

If receipt time is required but absent, event time cannot silently substitute for it.

### Lineage probe

Trace only transformations needed to resolve the named meaning or fitness question, using existing documentation, queries and known upstream references. At an inspected boundary, record relevant inputs, outputs and transformations. Stop when sufficient authoritative evidence resolves the question, or at an explicit unavailable/cost boundary; preserve any material uncertainty. Do not reconstruct enterprise-wide lineage or repair source systems.

When two paths disagree, preserve both observations until precedence is documented or decided by the responsible authority.

### Coverage probe

Compare the intended population and period to the observed population and date span. Check missing cohorts, source-specific exclusions, delayed regions, truncated histories, and categories that exist only in one source.

Small samples can reveal counterexamples but cannot prove full coverage. Record query limits, sampling rules, and unobserved partitions.

### Change probe

Compare the current source with the last Profile using meaning-bearing features, not only bytes or modification time. Look for renamed/retyped fields, grain shifts, key reuse, changed status definitions, update cadence, new corrections, authority changes, transformation edits, and intended-use changes.

## Change classification

| Observed change | Profile action |
|---|---|
| New period rows/documents or ordinary values under unchanged semantics | Keep the Profile current; record the period instance in the evidence log. |
| Same-period corrected content under the established correction rule | Keep semantics unless the correction reveals a meaning change; preserve replacement evidence. |
| Format-only export change with verified equivalent meaning | Record if useful; do not reopen unrelated decisions. |
| Field meaning, type, unit, enum, grain, or key behavior changed | Reopen affected dimensions and use decisions. |
| Event/effective/receipt/cutoff or update behavior changed | Reopen temporal and downstream use decisions. |
| Authority, precedence, lineage, transformation, or population mapping changed | Reopen affected decisions and return to planning. |
| Intended use changed | Assess the new use even if the source itself did not change. |
| Access temporarily unavailable | Mark the relevant decision `BLOCKED`; retain but do not overextend prior observations. |

## Fitness calibration

- Use `FIT` only when required semantics and authority are sufficiently observed for the stated risk.
- Use `QUALIFIED` when a narrower population, period, field subset, reconciliation, or explicit limitation makes the use supportable.
- Use `UNFIT` when a known mismatch cannot be repaired without changing the source, use, metric, or plan.
- Use `BLOCKED` when the decision depends on inaccessible data, missing lineage, or unresolved authority.

The same source may be `FIT` for descriptive counts, `QUALIFIED` for trend comparison, and `UNFIT` for causal attribution. Name the use precisely enough that another Agent can apply the decision without guessing.

## Evidence quality in a Profile

Prefer reproducible observations:

- exact source locator and access/as-of context;
- concise method or query description;
- counts, boundary examples, or citations supporting the conclusion;
- limits on what was inspected;
- a clear distinction between documentation and observed behavior.

Do not paste large raw logs or extracts into the Profile. Preserve stable citations, hashes, compact examples, and the method needed to reproduce material observations.
