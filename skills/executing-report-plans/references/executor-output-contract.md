# Common Executor Output Contract

Both Executors apply this contract when initializing or recovering a Run and sealing its handoff. Reuse the loaded contract within a context. Orchestration differs; evidence, acceptance, and final-save boundaries do not.

Other callers read only the named sections needed by their role: planning for handoff design, workers for computation, and reviewers for evidence/identity checks. A cross-reference does not require loading unrelated orchestration or save instructions.

## Core outputs and ownership

Use the shared [progress template](../assets/progress-template.md) for both modes. Record Run/Plan/semantic identities, period/as-of, language contract, Executor and selection basis/source/time, explicit parallel authorization or `none`, Package state and verification references. Legacy records retain their actual history; never invent a selection quote or timestamp.

The Run also contains the [evidence log](../assets/evidence-log-template.md), verified Package outputs, reader draft, declared staged assets or companions, and [Review Package manifest](../assets/review-package-template.md). Delegated work adds Task Briefs, Task Reports, and independent task reviews. Keep one authoritative record for each fact; other records link to it rather than repeat complete tables.

The Executor owns Run writes and draft synthesis. Workers own only their declared outputs. Independent reviewers are read-only. Final destinations remain unwritten until `reviewing-analysis` passes the save gate. Preserve prior reports when producing a new period or correction.

## Consume preparation before repeating work

Before affected computation, inspect the Plan's preparation references and already-completed work. Bind reusable observations to their exact source snapshot/identity, parameters, fields/period and full or sampled coverage, check method/implementation, result identity, and freshness. Apply **Verify once per valid evidence boundary** below. A snapshot match permits reuse only within that checked scope; sampling never satisfies a full-coverage requirement, and not checked never means passed.

Link valid preparation sections from the Run evidence log as upstream evidence, with the reuse decision and remaining checks. Do not copy their full tables or fabricate a pre-existing Run. Renew only invalid checks and affected dependents. New periods may reuse methods and code but require current data-readiness evidence. Read **Planning and Run health checks** in [source-profiling-methods.md](../../profiling-evidence/references/source-profiling-methods.md) when new or missing checks are needed. Critical inaccessible or unbounded-cost checks block affected work; ordinary access failures stay with this Executor, semantic defects go to their owner.

Legacy Plans need no bulk rewrite merely because they lack preparation fields. Establish missing readiness evidence during Run preflight; return to planning only for an actual strategy/interface or material scope defect. If planning produced conversation-only artifacts, have their producer persist the exact authorized content and references when permitted before admitting the Run. Never claim an unsaved artifact has a file identity. Preserve preparation versions already relied upon; later observations belong to new records.

## Compute stable results, then write from evidence

For each calculation, reuse an applicable project SQL/model/script or the implementation from the last accepted Run with the same semantic contract. Verify compatibility and exact code identity before reuse. If none exists, create it at the Package's declared output location and validate it against the metric's independently derived examples and applicable invariants. For a fully specified one-off measure, use the Plan's rule. Do not regenerate accepted computation logic from prose each period or require a separate global implementation registry.

Record a calculation reference binding:

- data snapshots/extracts, source identities, resolved parameters and metric/one-off rule identity;
- exact SQL/script/model version, relevant dependencies and result-affecting engine, numeric, time and tie-breaking settings;
- result location/identity, entity-period-dimension keys, unit and calculation/display precision;
- validation evidence, qualifications and any correction/supersession relationship.

Identical complete inputs must yield identical normalized business values, not identical report prose or file bytes. Use deterministic operations and numeric representation appropriate to the metric; unstable floating-point aggregation, unfixed current-time functions or unspecified ties cannot support an exact-repeatability claim. A new or changed implementation must pass independent expected cases and a repeated calculation on the same small fixed inputs; repeatability alone cannot prove correctness. Preserve code and prior results when fixing a bug, invalidate affected downstream evidence, and disclose required restatements. Legacy work without a verified implementation establishes its baseline at execution; do not claim retrospective guarantees.

Synthesis starts from accepted results, the coverage/evidence index, and relevant Plan sections. Organize and explain those facts; do not rediscover project context, requery sources or silently recompute canonical metrics merely to write prose. Every numerical derivation, including a newly requested percentage or growth rate, needs calculation evidence. Return it to the owned calculation step under existing semantics, then resume writing; change the Plan only when scope, meaning or work interfaces actually change. Authorized result-triggered drilldowns follow the blueprint's bounds. This does not create a mandatory separate Package, agent or review stage.

## Evidence and reader boundary

Use a coverage index and compact evidence cards to bind consequential claims to exact locators, semantic definitions, period/as-of, grain/population, durable identity, observation/derivation, verification, support status, and limitations. Group claims with a common derivation; do not make a separate verbose card for every cell. Missing or conflicting evidence remains explicit.

At synthesis, read [the reader and decision contract](../../using-evidencecraft/references/reader-and-decision-contract.md). Write the answer, interpretation, key values, and material limits for the audience. Full calculation tables stay in evidence unless required as reader content. Prose, compact comparisons, figures, and allowed citations should make the report usable without repository access. Internal IDs, hashes, audit navigation, and review state stay in governance.

## Verify once per valid evidence boundary

The producing owner performs each required check against actual output and inspects its result, including failures and coverage. Record a check reference containing:

- command or method and checker/script identity or version;
- exact input and output identities, source snapshot/as-of and freshness basis;
- expected result or independent derivation, observed result, execution time, and disposition;
- result file or locator sufficient to inspect the check without pasting full logs into progress.

The Main Agent verifies the output/interface, check binding, evidence locators, and declared write scope. Reuse a successful deterministic check only if these bindings and freshness still hold. Rerun when data/check code changes, identity or freshness is unknown, results are incomplete, or a discrepancy requires investigation. Read-only access to a live source does not establish an immutable snapshot.

Independent task review still checks consequential semantics and computations. Whole-report review still checks the complete claim/evidence coverage and reader use. Reusing mechanical checks never substitutes for either judgment. The Main Agent need not repeat the same calculation before an independent reviewer repeats it; it must investigate concrete concerns rather than trust a status label.

## Seal and hand off

After required work passes:

1. Reconcile claims, required coverage, cross-Package consistency, and qualifications against verified outputs.
2. Check reader usability, governance separation, permitted citations, and staged-to-final asset/companion mappings. Confirm current final destinations remain unwritten.
3. Freeze outputs in dependency order, then evidence, draft, and assets. Preserve earlier reviewed versions and correction evidence.
4. Create the complete manifest with governing Brief/Plan/Profiles/Definitions, preparation actually relied upon and its supporting records/extracts, versioned calculation implementations/settings, evidence, outputs, required verification records/checker sources, delegated task records, draft/assets, final mappings, and known limits. Reference unused background documents only as context; do not freeze a whole project library. Reference mutable progress by Run ID/status. Exclude the manifest's own hash and mutable progress hash; store seal/admission/save identity-check results outside the frozen member set to avoid circular identities.
5. Inspect member coverage against the Plan and compute/verify every stable identity. Hashing proves bytes, not completeness or meaning; every member must be accessible for review, but it need not be pasted or fully reread by every agent.
6. Record the sealed manifest identity and verification result in progress, then set `READY FOR INDEPENDENT REVIEW`, never `APPROVED` or `FINAL`.

For local files, use [manifest_identity.py](../scripts/manifest_identity.py) to avoid repeated manual hash tables. From the project root, invoke it by its installed absolute path:

```text
python3 <skill-root>/executing-report-plans/scripts/manifest_identity.py hash --root <project-root> <member-path> ...
python3 <skill-root>/executing-report-plans/scripts/manifest_identity.py verify --root <project-root> <manifest-path>
```

The `hash` command prints the marked three-column table for the manifest; replace generic roles with actual roles. `verify` fails on malformed rows, missing/changed files, duplicate paths, or self-reference. Keep the marker pair and column order; headings and roles may be localized. Paths resolve against the recorded project root. This read-only helper does not select members, seal files, judge evidence, or authorize saving. It requires Python 3; if unavailable, use an equivalent local hashing tool and record the method. Legacy manifests need no migration solely to use this helper.

Provider-native identities or live-source freshness need provider-appropriate verification recorded separately. Freeze local evidence extracts where reproducibility requires them; never silently treat the local-file check as verification of an external source.

If a sealed member changes, invalidate the affected checks, preserve the prior review basis, repair through its owner, and reseal. Return a compact handoff with manifest/progress references, meaningful verification results, limitations, and the next responsibility; avoid listing every member again in chat.
