---
name: reviewing-analysis
description: Use when a completed report draft and Review Package need independent evidence review or re-review before final save; verify scope, source and metric fidelity, calculations, traceability, claims, and limitations, then return PASS, QUALIFIED, or BLOCKED with exact responsibility routes without silently editing the analysis.
---

# Reviewing Analysis

Independently judge whether a completed analysis is fit for its confirmed use. Own the review verdict, finding severity, and Return Routes; never own execution corrections or semantic redesign.

## Admit a review, not unfinished work

Review only a sealed Review Package from `executing-report-plans` or `subagent-driven-reporting`, or a revised package submitted for re-review. Inspect exact paths and current contents for:

- confirmed Analysis Brief;
- all governing Source Profiles and Metric Definitions;
- confirmed Report Plan and its final-save rule;
- progress, evidence log, and verified Work Package outputs;
- report draft and Review Package manifest;
- prior Review Report and correction evidence for re-review.

Before dispatch, open the Review Package manifest and verify that it is a real, sealed file; every required member and staged reader asset exists; every recorded identity matches the current bytes; the draft and planned final paths are distinct; and the Executor marked the run ready for independent review. A status phrase, virtual package directory, missing member, placeholder identity, or coordinator summary is not an admissible Review Package. Do not infer readiness from a draft alone.

Recover the language contract independently from Run progress, then the confirmed Plan and Brief. For legacy packages without language fields, use the user's current explicit requirement or the primary language of the current substantive request and record the inferred contract in the current Run rather than rewriting old artifacts. Use `interaction_language` for questions, status, Return Routes, and the user-facing verdict message. Use `artifact_language` for the Review Report and all persistent review text. Pass `artifact_language` and terminology/source-title handling to the reviewer explicitly; English sources, templates, prompts, Profiles, or Definitions do not change them.

| Observed state | Action |
|---|---|
| A Work Package output, evidence log, draft, staged reader asset, or manifest is missing/incomplete or has an identity mismatch | Return to the selected Executor. |
| The Plan has no usable review inputs, checks, or final-save rule | Return to `writing-report-plans`. |
| The request is to calculate, research, draft, or fix findings | Use the selected Executor; do not turn review into execution. |
| The user changed intended use, audience, question, or scope | Return to `framing-analysis`. |
| A source or reusable metric semantic change is already known | Return to `profiling-evidence` or `defining-metrics` before review. |
| The requested `artifact_language` differs from the confirmed Plan/Run | Return to `writing-report-plans` for report-interface revision and reconfirmation before reviewing a new version. |

Review can discover a semantic defect, but it cannot repair one.

## Require an independent reviewer

The Main Agent assembles context and handles the result. A fresh-context reviewer performs the judgment. Do not let the authoring Executor review its own package.

1. Instantiate [the reviewer prompt](prompts/analysis-reviewer.md) in an independent reviewer call.
2. Replace every placeholder with exact paths, identities, confirmed use, risk, Plan checks, save rule, `artifact_language`, terminology/source-title handling, and any prior review/correction records.
3. Give the reviewer the files or access needed to inspect them; do not substitute a summary for available evidence.
4. Require read-only work. The reviewer must not edit the draft, evidence, Plan, progress, or final destination.
5. Require output conforming semantically to [the Review Report template](assets/review-report-template.md), with every heading, label, table header, narrative passage, and artifact-type phrase—including the top-level “Analysis Review Report” label—rendered in `artifact_language` and all template comments removed.

If an independent context is unavailable, stop as `BLOCKED`: review independence is a missing capability, not a reason for self-approval.

## Review against the confirmed use

The reviewer must inspect the actual package and report only findings supported by locators and evidence.

### 1. Package and semantic identity

Check that every Brief, Profile, Definition, Plan, run output, evidence entry, and draft identity is current and mutually consistent. Treat a stale or mixed-semantic package as blocking even if its prose is polished.

### 2. Coverage and fidelity

Map each Brief question, Plan-required section, comparison, and success criterion to draft content and evidence. Verify that:

- scope, audience, intended use, period/as-of, and exclusions match the confirmed Brief;
- source grain, keys, time, authority, lineage, fitness qualifications, and transformations are respected;
- metric population, numerator/denominator, time, deduplication, aggregation, missing-data behavior, and source mapping are respected;
- Work Package completion evidence supports the consumed outputs.

### 3. Reproducibility and traceability

Reperform or spot-check the Plan's highest-impact calculations from source locators when feasible. Trace every consequential number and claim through the evidence log to a qualified source or verified upstream output. Status labels and agent reports are not evidence.

### 4. Reasoning and limitations

Check for unsupported inference, causal language without design, denominator or grain shifts, cherry-picking, contradictory sections, false precision, missing uncertainty, and qualifications that failed to propagate. A disclosed limitation may constrain use without invalidating the analysis; an undisclosed limitation affecting a decision is blocking.

### 5. Report usability and save safety

Check required sections, clear distinction between observation and interpretation, decision-relevant caveats, and absence of unreviewed final/approved claims. Treat reader self-containment and governance separation as formal review dimensions:

- the reader report must contain the context, evidence explanation, key values, qualifications, and interpretation needed to understand its conclusions without opening repository governance files;
- current-run Brief, Plan, Evidence log, Review Package, progress, Run/WP/Evidence IDs, review status, identities, hashes, and engineering traceability must stay outside the reader report;
- an internal or engineering path cannot be the only support for a consequential claim;
- every Markdown image must resolve through the Plan-declared staging-to-final asset mapping, and a path-only figure reference is not a figure;
- the reviewed draft path must differ from the planned final path, and the final report and final asset set must still be unwritten before authorization.

Formal external citations, paper links, reader-accessible URLs, and code or file names that are themselves report subject matter are allowed. They become defects only when the report requires repository access, uses them as internal navigation, or makes them carry the evidence chain instead of explaining the claim.

Check the draft and all audience-facing artifacts against the confirmed `artifact_language`: untranslated English template headings, labels, table headers, placeholders, or unexplained narrative mixing in a Chinese report are usability defects. Exact governance paths, hashes, and internal IDs remain legitimate inside the Review Package and Review Report, but their presence there does not authorize them in the reader report. Confirm the Plan's final destination and whether qualified reports may be saved.

## Classify findings by consequence

Use exactly these levels:

- `BLOCKING`: a wrong or unsupported consequential result; stale/mixed semantics; missing required evidence or section; hidden material limitation; unreconciled contradiction; internal governance path or run identity leaked into the reader report; engineering path used as sole support; path-only or unmapped key figure; mixed draft/final identity; missing Review Package manifest/member or identity mismatch; unsafe final-save condition; or an untranslated template heading/field that violates the confirmed artifact language and report interface.
- `QUALIFICATION`: the analysis is technically supported only for a narrower or explicitly caveated use, and that limitation is already prominent everywhere it matters.
- `ADVISORY`: a non-consequential clarity or presentation improvement that does not change fitness for the confirmed use.

For every finding record an ID, level, exact artifact and locator, observed evidence, expected requirement, why it matters for the confirmed use, affected claims, responsible stage, and required action. Do not inflate preferences into blockers.

## Return a verdict

The independent reviewer proposes a verdict; the Main Agent verifies every material finding against the package before accepting it. Reject or reclassify unsupported feedback with specific counter-evidence. Never respond to feedback by silently editing the report.

- `PASS`: no valid BLOCKING or QUALIFICATION findings remain; the draft is supported for the confirmed use.
- `QUALIFIED`: no valid BLOCKING finding remains; one or more material constraints are fully and prominently disclosed, and the Plan or user explicitly permits a qualified report.
- `BLOCKED`: any valid BLOCKING finding remains, required review evidence is unavailable, or a needed qualification is absent from the reviewed draft.

When reviewer and Main Agent disagree on a material finding and evidence does not resolve it, use `BLOCKED` and request the narrow decision or evidence needed. The Main Agent may downgrade a proposed PASS based on verified defects; it may not waive a verified blocker for convenience.

## Route findings to the owner

Choose the earliest stage that owns the defect, not the easiest place to patch prose:

| Defect | Return Route |
|---|---|
| Access, calculation, evidence capture, reader self-containment, governance leakage, asset mapping, draft/final handling, package assembly, or verification error under unchanged semantics | The Plan-selected Executor—`executing-report-plans` or `subagent-driven-reporting`—at the first affected Work Package. |
| Work Package, dependency, output, check, review input, or save-rule defect | `writing-report-plans`. |
| Source grain, keys, time, authority, lineage, transformation, mapping, or fitness defect | `profiling-evidence`, then planning. |
| Metric meaning, population, formula, time, deduplication, aggregation, missing rule, or source mapping defect | `defining-metrics`, then planning. |
| Audience, intended use, question, scope, risk, or success criterion defect | `framing-analysis`, then planning. |

Group findings by Return Route and identify every downstream Package that must be reverified. `BLOCKED` reports must not authorize final save.

## Re-review corrections

For re-review, supply the prior Review Report, the responsible stage's correction report, revised artifacts, and new identities. The reviewer must:

1. verify each prior BLOCKING and QUALIFICATION finding against actual changes;
2. confirm unchanged findings were not merely relabeled;
3. inspect affected dependents for regressions;
4. rerun the full high-impact coverage, traceability, and reasoning checks;
5. issue a new Review Report that supersedes, but does not erase, the prior one.

The author or Main Agent saying an issue is fixed is not closure evidence.

## Save only the reviewed bytes

After `PASS`, or `QUALIFIED` when explicitly permitted:

1. verify freshly that the draft, reviewed staged asset set, evidence log, semantic dependencies, and Review Package still match the identities the reviewer inspected;
2. preserve the Review Report at the Plan's risk-proportionate review path;
3. copy the exact reviewed draft bytes to the Plan's final destination without editorial changes, and copy exactly the reviewed staged assets to their declared final asset mappings without regeneration or substitution;
4. verify the final Markdown identity equals the reviewed draft identity and every final asset identity equals its reviewed staged identity;
5. record `draft identity -> final path / final identity`, the reviewed-to-final asset mapping and identities, the verdict, and the Review Report path in the Review Report and progress—not in the final report.

The final report must not gain a backlink to the Brief, Plan, Evidence log, Review Package, Review Report, or progress during save. If any reviewed input changed, do not save; create a new Review Package and re-review. If saving would require adding a missing qualification, editing wording, repairing a URI, or regenerating an asset, return to the Plan-selected `executing-report-plans` or `subagent-driven-reporting` Executor and re-review the revised draft and asset set.

Low-risk clean review may be recorded compactly when the Plan allows it; high-risk, qualified, or blocked review requires the full Review Report. External publication remains outside this Skill.

## Result

Return the verdict, Review Report path or complete compact record, all material findings with evidence, exact Return Routes, re-review requirements, and—only after a passing save gate—the final report path and verified identity. The user-facing result uses `interaction_language`; the saved Review Report uses `artifact_language` while preserving canonical codes and recorded source-exact exceptions.
