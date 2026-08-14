<!-- Template use: render every heading, label, table header, placeholder replacement, and narrative passage in the confirmed artifact language. The sample title's “Subagent-Driven Progress” phrase is a translatable artifact-type label, not a canonical identifier. Preserve canonical codes and IDs, exact Skill names, paths, hashes, citations, code, formulas, and original source titles. Remove this and every Template instruction comment from the instantiated artifact. -->

# Evidencecraft Subagent-Driven Progress

## Run identity

- Report Plan path / identity:
- Run ID:
- Executor: `subagent-driven-reporting`
- Execution mode: `Subagent-Driven`
- User selection statement:
- Selected at:
- Explicit parallel authorization: `none | exact current-Run user statement`
- Status: `INITIALIZING | RUNNING | BLOCKED | INTEGRATING | READY FOR INDEPENDENT REVIEW`
- Analysis Brief identity:
- Source Profile identities:
- Metric Definition identities:
- Interaction language:
- Artifact language:
- Terminology and source-title handling:
- Delivery profile: `standalone reader report` unless the confirmed Plan says otherwise
- Planned final report path (must differ from draft):
- Reader-report governance exclusions:
- Started / last reconciled:
- Work started: `no | yes — first Package and timestamp`
- Prior Run reference, if this Run replaces a different mode: `none | exact Run ID and reason`

## Work Package ledger

| Package | Dependencies | Worker | Output / report / review paths | Dispatch state | Verification / review | Accepted output identity |
|---|---|---|---|---|---|---|
|  |  |  |  | pending | pending |  |

<!-- Template instruction: allowed dispatch states are `pending | active | reported | correction | blocked | accepted`. Only one normal research worker may be `active`. -->

## Dispatch record

| Dispatch | Packages | Mode | Dependency-ready evidence | Parallel authorization / safety result | Result |
|---|---|---|---|---|---|
|  |  | `serial | dispatching-parallel-research` |  |  |  |

## Verification and correction log

| Package / round | Actual output inspected | Fresh checks / observed result | Reviewer verdict / path | Main Agent disposition |
|---|---|---|---|---|
|  |  |  |  |  |

## Accepted evidence and integration

- Accepted output identities:
- Cross-package grain/period/population checks:
- Contradictions and resolutions:
- Evidence log path / identity:
- Integrated outputs:
- Report draft path / identity:
- Staged reader assets path(s) / identity / final relative URI mapping: `none` or exact rows
- Required sections/comparisons/limitations freshly checked:
- Reader self-containment and key values in prose/tables checked:
- Governance leakage, internal IDs, engineering traceability, `...`, glob/brace, and path-only references checked:
- Formal external citations and substantive code/file identifiers preserved correctly:
- Every Markdown image resolves through the declared asset mapping:
- Planned final Markdown/assets are still unwritten:

## Review Package and route

- Review Package manifest path:
- Manifest members actually opened and identities verified:
- Missing members / placeholder identities / unresolved assets: `none` or exact blockers
- Sealed manifest identity (record only after seal):
- Manifest identity recorded at:
- Route: `reviewing-analysis` only when ready
- Final report saved here: `no — outside this Executor`

## Recovery record

- Ledger state compared with actual files:
- Legacy in-flight parallel workers reconciled without cancellation or redispatch:
- Status claims downgraded or restored:
- First incomplete or blocked Package:
- Exact Return Route and required evidence:

## Independent review and final-save record

<!-- Template instruction: append only after `reviewing-analysis` acts; this mutable section is not a frozen manifest member identity. -->

- Review Report path / identity or compact independent-review record:
- Verdict: `PASS | QUALIFIED | BLOCKED`
- Reviewed draft identity -> final report path / verified identity:
- Reviewed staged assets -> final asset paths / verified identities: `none` or exact mappings
- Final saved at: [timestamp or not authorized]
- Governance backlinks added to final report: `no` or blocking defect
