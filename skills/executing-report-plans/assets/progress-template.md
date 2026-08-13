<!-- Template use: render every heading, label, table header, placeholder replacement, and narrative passage in the confirmed artifact language. The sample title's “Report Run Progress” phrase is a translatable artifact-type label, not a canonical identifier. Preserve canonical codes and IDs, exact Skill names, paths, hashes, citations, code, formulas, and original source titles. Remove this and every Template instruction comment from the instantiated artifact. -->

# Report Run Progress

<!-- Template instruction: instantiate this ledger in the Plan's run workspace and add entries without erasing prior run history. -->

## Run identity

- Run ID:
- Status: `NOT STARTED | IN PROGRESS | BLOCKED | READY FOR INDEPENDENT REVIEW`
- Executor: `sequential`
- Report Plan path:
- Plan identity/version/hash:
- Analysis Brief path:
- Source Profile paths and identities:
- Metric Definition paths and identities:
- Period/as-of:
- Interaction language:
- Artifact language:
- Terminology and source-title handling:
- Run workspace:
- Draft path:
- Planned final report path:
- Delivery profile:
- Governance references excluded from the reader report:
- Staged/final asset mapping: [none or exact mapping]
- Review Package manifest path:
- Review Package manifest identity/hash (record only after the manifest is frozen):
- Started at:
- Last reconciled at:

## Executor ownership

- Current owner: Main Agent
- Other active writer checked: `none | describe conflict`
- Prior Executor handoff, if any:

## Work Package ledger

<!-- Template instruction: repeat in Plan dependency order. -->

### WP-<id>: <name>

- Status: `NOT STARTED | BLOCKED BY <id> | IN PROGRESS | COMPLETE | BLOCKED`
- Linked question/section:
- Frozen inputs actually used:
- Started at:
- Output path:
- Output identity/hash:
- Completion checks:
  - Method or command:
  - Checked at:
  - Complete observed result:
  - Expected result:
  - Outcome: `PASS | FAIL`
- Evidence-log entries:
- Direct dependents unblocked:
- Limitations:

## Recovery reconciliation

<!-- Template instruction: append one entry for each resume or discrepancy. -->

### <timestamp>: <new run | resume | reconciliation>

- Progress claims inspected:
- Actual files inspected:
- Fresh checks rerun:
- Discrepancies:
- Preserved verified work:
- Downgraded or invalidated work:
- Earliest Package to run:
- Reason:

## Blocking record

<!-- Template instruction: complete only when blocked. -->

- First failing Package:
- Observed evidence:
- Blocker class: `execution | plan | source semantics | metric semantics | framing`
- Affected downstream Packages:
- Valid work preserved:
- Partial files quarantined or marked:
- Requested input or decision:
- Exact Return Route:

## Final execution gate

- Review Package members actually opened and identities verified:
- Final destinations absence check (method / checked at / result):
- Missing members, placeholder identities, or unresolved asset mappings: `none` or exact blocker

- [ ] Every Package output exists at the planned path.
- [ ] Every Package has fresh passing completion evidence.
- [ ] Evidence log covers every consequential result.
- [ ] Draft contains all Plan-required sections.
- [ ] Claims, calculations, and limitations reconcile to evidence entries.
- [ ] Reader draft stands alone and contains no current-run governance paths/IDs/statuses, engineering traceability appendix, path-only figures, shorthand paths, globs, or brace expansions.
- [ ] Formal reader citations and substantive source/code identifiers were preserved where needed without making repository access a prerequisite.
- [ ] Every Markdown image resolves through the declared staged/final asset mapping, or the asset contract is `none`.
- [ ] Planned final report and final asset destinations are still unwritten.
- [ ] Every Review Package manifest member exists and has the recorded real identity; no placeholder identity remains.
- [ ] Frozen draft/assets and Review Package manifest identities are recorded without self-referential or mutable-progress hashes.
- [ ] Status is `READY FOR INDEPENDENT REVIEW`, not approved or final.

## Handoff

- Next skill: `reviewing-analysis`
- Exact paths supplied:
- Execution-only corrections that may resume here:
- Open limitations for reviewer judgment:

## Independent review and final-save record

<!-- Template instruction: append only after `reviewing-analysis` acts; this mutable section is not a frozen manifest member identity. -->

- Review Report path / identity or compact independent-review record:
- Verdict: `PASS | QUALIFIED | BLOCKED`
- Reviewed draft identity -> final report path / verified identity:
- Reviewed staged assets -> final asset paths / verified identities: `none` or exact mappings
- Final saved at: [timestamp or not authorized]
- Governance backlinks added to final report: `no` or blocking defect
