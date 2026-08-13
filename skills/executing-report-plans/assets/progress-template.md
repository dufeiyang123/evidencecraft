# Report Run Progress

Copy this template into the Plan's run workspace. Add entries without erasing prior run history.

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
- Run workspace:
- Draft path:
- Review Package path:
- Review Package identity/hash (record only after the Package is frozen):
- Started at:
- Last reconciled at:

## Executor ownership

- Current owner: Main Agent
- Other active writer checked: `none | describe conflict`
- Prior Executor handoff, if any:

## Work Package ledger

Repeat in Plan dependency order.

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

Append one entry for each resume or discrepancy.

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

Complete only when blocked.

- First failing Package:
- Observed evidence:
- Blocker class: `execution | plan | source semantics | metric semantics | framing`
- Affected downstream Packages:
- Valid work preserved:
- Partial files quarantined or marked:
- Requested input or decision:
- Exact Return Route:

## Final execution gate

- [ ] Every Package output exists at the planned path.
- [ ] Every Package has fresh passing completion evidence.
- [ ] Evidence log covers every consequential result.
- [ ] Draft contains all Plan-required sections.
- [ ] Claims, calculations, and limitations reconcile to evidence entries.
- [ ] Review Package contains the exact current semantic dependencies.
- [ ] Frozen draft and Review Package identities are recorded without self-referential ledger hashes.
- [ ] Status is `READY FOR INDEPENDENT REVIEW`, not approved or final.

## Handoff

- Next skill: `reviewing-analysis`
- Exact paths supplied:
- Execution-only corrections that may resume here:
- Open limitations for reviewer judgment:
