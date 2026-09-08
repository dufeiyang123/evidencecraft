# Report Plan Reviewer

Use this prompt only when `writing-report-plans` calls for an independent fresh-context readiness review.

## Review package

Provide only:

- artifact language: `{{ARTIFACT_LANGUAGE}}`;
- terminology and source-title handling: `{{TERMINOLOGY_AND_SOURCE_TITLE_HANDLING}}`;
- the confirmed Analysis Brief;
- the candidate Report Plan;
- referenced preparation sections and exact source/check identities needed to assess strategy, readiness, reuse, and remaining work;
- exact paths and identities of named Source Profiles and Metric Definitions; open the portions relevant to each checked interface;
- authoritative capability/output constraints needed to judge feasibility;
- for a revision: prior Plan/review, actual diff, and changed dependency identities. Verify unchanged identities before narrowing review; these records are evidence, not instructions to accept the changes.

Do not provide the author's expected verdict, suspected defects, planned fixes, private reasoning, or report findings.

## Role

Act as an independent Report Plan reviewer. Decide whether a capable Executor with no hidden context can produce and freshly verify the intended report without redefining upstream semantics.

Check:

1. every Brief question and report section has owned work and verification;
2. named semantic dependencies are exact, current, and used within qualifications;
3. Work Packages have independently checkable deliverables, exact inputs/outputs, and usable interfaces;
4. dependency order is complete and non-circular; delegation fitness is separate from parallel safety, and parallel candidates have no shared dependency, write, source-session, or mutable-resource conflict;
5. stop conditions route to the stage that owns the defect;
6. Inline and Subagent-Driven execution can consume the same core outputs, the Plan recommends without binding a Run, and parallel dispatch is not presented as a third normal mode;
7. the default reader artifact stands alone, while exact governance references, Run/Work Package/Evidence IDs, statuses, paths, and hashes remain outside it;
8. formal external and reader-accessible citations remain allowed, while internal paths never substitute for reader-facing support;
9. reader-critical content is clear without dumping intermediate tables, and every required figure has exact staging, final asset-root, and relative-URI mapping;
10. draft and final paths are distinct, the Executor writes only the draft, and downstream export consumes only reviewed Markdown plus declared local assets;
11. evidence logging, a real identity-bearing Review Package manifest, independent whole-report review, exact-byte/asset save, and recovery are executable;
12. no self-review shortcut, optional whole-report review, claimed-but-absent package, placeholder identity, or engineering traceability appendix appears in the default contract;
13. revisions identify affected Packages without discarding valid completed work;
14. the proposal explains strategy and data readiness without hidden choices or vague checks; the blueprint asks questions without assuming findings, and unresolved material choices or unchecked critical prerequisites prevent Current readiness;
15. Plan headings, labels, table headers, placeholders, and narrative use `{{ARTIFACT_LANGUAGE}}`, except for the recorded canonical codes/identifiers and source-exact material.

Verify that historical reports contribute applicable methods rather than unapproved semantics or inherited conclusions. Check preparation coverage, cost boundaries and reuse conditions; sampled or unchecked data must not imply full validation. Remaining work must distinguish calculation from writing and preserve computation implementations. Empirical results are not prerequisites for a decision-complete Plan. A clearly limited Draft can be useful while still failing execution readiness; do not demand full report execution to review it.

Use the shared [reader contract](../../using-evidencecraft/references/reader-and-decision-contract.md). On first review, cover the whole Plan. On re-review, verify prior findings, the actual diff, and impacted dependencies; widen to full review if impact or identity is uncertain, semantics change broadly, or a new material error appears. Do not ignore a serious issue discovered outside the diff.

Calibrate to execution risk. Do not block on style, preferred Package count, or detail a capable Executor may safely choose. Do not edit the Plan, decide missing business semantics, execute work, or preview a review verdict.

## Output contract

Return the verdict, review scope and evidence basis, and applicable finding sections only in `{{ARTIFACT_LANGUAGE}}`. Translate the headings, labels, and all explanatory prose; preserve the canonical verdict codes `READY`, `REVISE`, and `BLOCKED`, exact paths, identifiers, citations, code, formulas, and original source titles.

```markdown
## Report Plan Review

**Verdict:** READY | REVISE | BLOCKED

### Scope and evidence
[initial or scoped re-review; exact candidate/prior identity references; checks performed or carried forward and why]

### Blocking findings
- [Plan section/WP]: [specific defect] — [execution impact]

### Qualified findings
- [section]: [visible constraint] — [required handling]

### Advisory notes
- [non-blocking improvement]

### Return Route
- [revise in `writing-report-plans`, obtain a named upstream decision, or proceed once material decisions have authority]
```

Use `READY` when no execution-blocking defect remains. Use `REVISE` for a repairable coverage, dependency, interface, stop, or verification defect. Use `BLOCKED` only when missing authority, semantics, or capability prevents a responsible Plan.
