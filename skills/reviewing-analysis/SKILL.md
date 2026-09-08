---
name: reviewing-analysis
description: Independently review a sealed Review Package when it is ready for whole-report review or re-review before final save.
---

# Reviewing Analysis

Independently judge whether a completed analysis is fit for its confirmed use. Own the review verdict, finding severity, and Return Routes; never own execution corrections or semantic redesign.

## Admit a review, not unfinished work

Review only a sealed Review Package from `executing-report-plans` or `subagent-driven-reporting`, or a revised package submitted for re-review. Start with the manifest, Run readiness, and any prior review/correction record. Verify the complete required membership and identities; open analytical content according to the review scope rather than loading every artifact into the coordinator context.

Before dispatch, open the Review Package manifest and verify that it is a real, sealed file; every required member and staged reader asset exists; every recorded identity matches the current bytes (use the common contract's local identity helper or an equivalent check); the draft and planned final paths are distinct; and the Executor marked the run ready for independent review. A status phrase, virtual package directory, missing member, placeholder identity, or coordinator summary is not an admissible Review Package. Do not infer readiness from a draft alone.

Required evidence includes preparation actually relied upon, its supporting records/extracts, and versioned calculation implementations/settings. Check membership through the common contract; unused background reading does not belong in the sealed package. Review existing evidence rather than starting another planning investigation.

Read and apply [the shared language contract](../using-evidencecraft/references/language-and-localization-contract.md), recovering the frozen fields from Run progress, then Plan and Brief. Pass them explicitly to the reviewer and record any legacy inference in the current Run.

| Observed state | Action |
|---|---|
| A Work Package output, evidence log, draft, staged reader asset, or manifest is missing/incomplete or has an identity mismatch | Return to the Run-selected Executor. |
| The Plan has no usable review inputs, checks, or final-save rule | Return to `writing-report-plans`. |
| The request is to calculate, research, draft, or fix findings | Use the Run-selected Executor; do not turn review into execution. |
| The user changed intended use, audience, question, or scope | Return to `framing-analysis`. |
| A source or reusable metric semantic change is already known | Return to `profiling-evidence` or `defining-metrics` before review. |
| A requested language change is not yet reflected in the sealed Run delivery contract | Return to the producer to apply the explicit delivery change and reseal new bytes; return to planning only if a binding interface changes. |

Review can discover a semantic defect, but it cannot repair one.

## Require an independent reviewer

The Main Agent assembles context and handles the result. A fresh-context reviewer performs the judgment. Do not let the authoring Executor review its own package.

1. Instantiate [the reviewer prompt](prompts/analysis-reviewer.md) in an independent reviewer call.
2. Supply the sealed manifest path/identity, confirmed use and risk, Plan check/save-rule references, frozen language fields, and prior review/correction references. Let the manifest carry member identities; do not duplicate its full table in the dispatch prompt.
3. Give read access to all required files. The reviewer first reads the reader draft, then follows consequential claims to evidence and governing sections; a complete accessible package does not require every file to be pasted or read in full. Summaries cannot replace source evidence.
4. Require read-only work. The reviewer must not edit the draft, evidence, Plan, progress, or final destination.
5. Require a verdict-first record using [the Review Report template](assets/review-report-template.md) and the language contract. Omit empty finding sections; record checks and evidence references without duplicating the manifest.

If an independent context is unavailable, stop as `BLOCKED`: review independence is a missing capability, not a reason for self-approval.

## Review against the confirmed use

The independent reviewer applies [the reviewer prompt](prompts/analysis-reviewer.md) as the normative rubric. It covers package identity, scope and semantic fidelity, reproducibility and traceability, reasoning and limitations, reader usability, governance separation, localization, and save safety. Findings must cite actual artifact locators and evidence.

## Classify findings by consequence

Use the prompt's `BLOCKING | QUALIFICATION | ADVISORY` definitions and required finding fields exactly. The Main Agent verifies consequence and responsibility against the actual package; style preferences do not become blockers.

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
| Access, calculation, evidence capture, reader self-containment, governance leakage, asset mapping, draft/final handling, package assembly, or verification error under unchanged semantics | The Run-selected Executor—`executing-report-plans` or `subagent-driven-reporting`—at the first affected Work Package. |
| Work Package, dependency, output, check, review input, or save-rule defect | `writing-report-plans`. |
| Source grain, keys, time, authority, lineage, transformation, mapping, or fitness defect | `profiling-evidence`, then planning. |
| Metric meaning, population, formula, time, deduplication, aggregation, missing rule, or source mapping defect | `defining-metrics`, then planning. |
| Audience, intended use, question, scope, risk, or success criterion defect | `framing-analysis`, then planning. |

Group findings by Return Route and identify every downstream Package that must be reverified. `BLOCKED` reports must not authorize final save.

## Re-review corrections

For re-review, supply the preserved prior manifest/review, correction record, revised manifest, and actual member/content delta. The reviewer must:

1. Verify the new manifest and programmatically compare identities to establish changed, added, removed, and unchanged members. The author's claimed scope is not proof.
2. Verdict every prior material finding from actual correction evidence; inspect affected claims and dependencies and rerun invalidated checks.
3. Carry forward prior checks only when their evidence identities, checker, use, and freshness remain valid. Cite the prior review and state this narrower scope explicitly.
4. Expand to a full review when semantic changes are broad, impact cannot be bounded, prior review evidence is inadequate, or a new material error undermines confidence. A serious defect discovered outside the diff still requires action.
5. Save a superseding review without erasing earlier evidence or output versions.

Do not automatically repeat the entire high-impact review for a local wording, precision, or table-layout fix. Such a fix still requires independent review of changed bytes and affected meaning. If a blocking condition repeats without new evidence, capability, or a concrete correction path, stop and route it; no fixed review-round quota and no acceptance by exhaustion.

## Save only the reviewed bytes

After `PASS`, or `QUALIFIED` when explicitly permitted:

1. freshly verify the manifest identity and all reviewed stable members, including draft, assets/companions, evidence and semantic dependencies, using the common identity check;
2. preserve the Review Report at the Plan's risk-proportionate review path;
3. copy the exact reviewed draft bytes to the Plan's final destination without editorial changes, and copy exactly the reviewed staged assets and reader companions to their declared final mappings without regeneration or substitution;
4. verify the final Markdown identity equals the reviewed draft identity and every final asset/companion identity equals its reviewed staged identity;
5. record `draft identity -> final path / final identity`, the reviewed-to-final asset/companion mappings and identities, the verdict, and the Review Report path in the Review Report and progress—not in the final report.

The final report must not gain a backlink to the Brief, Plan, Evidence log, Review Package, Review Report, or progress during save. If any reviewed input changed, do not save; create a new Review Package and re-review. If saving would require adding a missing qualification, editing wording, repairing a URI, or regenerating an asset, return to the Run-selected `executing-report-plans` or `subagent-driven-reporting` Executor and re-review the revised draft and asset set.

Low-risk clean review may use a compact record; high-risk, qualified, or blocked review requires enough finding and verification detail for its consequence. Neither case needs empty sections or a second copy of the manifest. External publication remains outside this Skill.

## Result

Tell the user the verdict and practical consequence, material findings or limitations, and the review/final artifact links. Keep exact identities, detailed Return Routes, and re-review evidence in the governance record. Name a saved final only after the passing save gate. The user-facing result uses `interaction_language`; the saved Review Report uses `artifact_language` while preserving canonical codes and recorded source-exact exceptions.
