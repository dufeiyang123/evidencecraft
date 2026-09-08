---
name: framing-analysis
description: Create or revise an Analysis Brief when an evidence-first analysis lacks one, or its audience, intended use, questions, scope, period semantics, risk, or success criteria changed.
---

# Framing Analysis

Turn an analysis request into a confirmed, durable boundary for planning. Own the meaning of the requested analysis, not the evidence semantics, metric definitions, execution design, findings, or final review.

## Establish the state

Inspect the request, project instructions, nearby documentation, and any existing Brief before asking questions. Do not ask for facts available in the workspace.

Use project indexes and relevant passages to identify candidate data, business rules, existing implementations and historical method examples. Record exact useful references for planning; do not read every project document or start health queries here. Historical reports inform framing but do not authorize their old metrics or conclusions.

Classify the state:

| State | Action |
|---|---|
| No Brief | Frame from the request and project context. |
| Draft Brief | Resume from its unresolved material choices. |
| Confirmed Brief, no semantic change | Report that it remains current, route to `writing-report-plans`, and stop. |
| Confirmed Brief with changed audience, use, questions, scope, period rule, risk, or success criteria | Reopen only affected sections, then resolve only changed material choices. |
| Downstream work returned a framing defect | Resolve the cited defect without absorbing the downstream role. |

Treat new period contents, new values, source refreshes, and execution errors as non-framing changes. Route them to the current Plan, a conditional specialist, or the Executor as appropriate.

## Inputs and authority

Start with whatever is available:

- the user's request and the decision or communication it should support;
- relevant project context and prior reports;
- an existing Analysis Brief and its confirmation record, if any;
- a downstream Return Route that identifies a framing defect.

Decide and record the analysis object, audience, use, reader-artifact expectation, questions, non-goals, scope, period semantics, constraints, risks, and success criteria. The reader-artifact expectation says whether the report must stand alone and which delivery formats or distribution context matter; it does not design paths, Work Packages, evidence structures, or rendering mechanics. The user retains authority over choices that change the intended decision, audience, commitments, or acceptable risk. Make conservative, reversible assumptions only for non-material details and label them tentative.

Do not decide source fitness, joins, transformations, metric formulas, Work Packages, execution recommendations, Run choices, findings, or review verdicts here.

## Resolve the language contract

Read and apply [the shared language contract](../using-evidencecraft/references/language-and-localization-contract.md) before the first question or artifact, especially when no router ran or a field changed. Record all three fields in the Brief. Missing fields in a current legacy Brief are presentation metadata, not a reason to reopen its analysis meaning.

## Frame the analysis

### 1. Bound the request

Summarize the apparent object, audience, intended use, and requested outcome in a few sentences. If the request contains several independent analyses with different audiences, decisions, or timelines, propose a decomposition and frame only the first agreed unit.

Identify likely non-goals early. A Brief that attempts to serve unrelated decisions is not ready for planning.

### 2. Resolve material choices

Apply [the reader and decision contract](../using-evidencecraft/references/reader-and-decision-contract.md). Ask only choices not settled by the request or authoritative context. Prefer one focused question; bundle tightly related choices when this avoids repeated interruptions.

Prioritize questions that can change:

1. who will use the report and what they will do with it;
2. which decision questions the analysis must answer;
3. included and excluded populations, periods, regions, products, or cases;
4. comparison and cutoff semantics that belong to the business question rather than a metric formula;
5. acceptable uncertainty, sensitivity, confidentiality, and consequence of error;
6. whether the audience artifact must stand alone and which delivery formats materially constrain its use;
7. what observable result would make the analysis useful.

Keep three explicit buckets while clarifying:

- **Confirmed:** the user or authoritative context fixed the choice.
- **Tentative:** a reversible assumption is adequate for drafting.
- **Open:** a material choice still requires authority or investigation.

Do not disguise an Open choice as an assumption. If the user cannot resolve it, preserve it and stop before confirmation.

### 3. Compare framing approaches when they matter

When two or more plausible frames would materially change scope, usefulness, or risk, present 2–3 approaches with trade-offs and a recommendation. Typical differences include decision-first versus exploratory coverage, narrow high-confidence scope versus broad qualified scope, and a single Brief versus decomposed analyses.

Skip artificial alternatives when only one responsible frame fits the request. Never create options merely to satisfy a count.

### 4. Write a decision overview and durable scope

Instantiate [assets/analysis-brief-template.md](assets/analysis-brief-template.md) at `docs/evidencecraft/specs/YYYY-MM-DD-<topic>-analysis-brief.md`, applying the language contract. Start with the intended decision, scope, result, and material limits in plain language. Scale detail to the work; omit empty optional sections.

Keep source names and candidate metrics as context. Hand off relevant project references and any known access/query-cost constraints; planning owns strategy research and bounded health checks. Name semantic gaps without answering them here. Link the durable Brief when presenting a choice; do not require the user to inspect technical fields to understand the decision. If host planning restrictions prohibit writes, provide the Brief in the conversation and state that persistence remains pending.

### 5. Review readiness

Before declaring the scope ready, check the written Brief with fresh eyes:

- no placeholder, contradiction, or unresolved material choice is hidden;
- every question supports the stated use and fits the scope;
- the reader-artifact expectation is explicit without absorbing planning or rendering decisions;
- non-goals prevent plausible scope creep;
- period and cutoff language is unambiguous enough to plan;
- risks and success criteria can be checked later;
- tentative assumptions are visible and have an owner or resolution point;
- downstream semantic gaps are named without being prematurely solved.
- headings, labels, and narrative use the artifact language, apart from recorded terminology exceptions and canonical identifiers.

When unresolved framing ambiguity could materially affect a high-impact decision or conflicting stakeholder commitments, dispatch an independent fresh-context reviewer using [prompts/analysis-brief-reviewer.md](prompts/analysis-brief-reviewer.md). Give the reviewer only the specified review package, including `{{ARTIFACT_LANGUAGE}}` and `{{TERMINOLOGY_AND_SOURCE_TITLE_HANDLING}}`. Treat `REVISE` as a stop before confirmation; treat `BLOCKED` as a return to the user or responsible authority. The reviewer may identify defects but may not make product choices or silently rewrite the Brief.

### 6. Record authorization without repeating it

Declare the Brief `Confirmed` when its material scope and risk choices have an authoritative basis, readiness checks pass, and blocking findings are resolved. Explicit instructions in the current request or applicable standing decisions may supply that basis. Record the source and exactly which choices it covers; this is confirmation of business scope, not a claim that the user reviewed the generated file.

If material choices remain, present a short decision overview, the recommendation and its consequences, and the Brief link. Ask for those choices only. If the user requested approval of the complete Brief, present it and wait for that approval. Never treat silence as acceptance or turn an Open material choice into a default.

Leave a `Draft` with an exact Open choice when authority is missing; stop dependent planning and execution. Otherwise route to `writing-report-plans` and continue when the request authorizes the work. New material decisions discovered in planning still need authority; routine implementation details do not create another automatic confirmation gate.

## Observable result

Return:

1. the path and status of the Analysis Brief;
2. a short list of confirmed, tentative, and open choices;
3. any semantic gap routed to a conditional specialist;
4. the next responsible Skill or the authority currently blocking progress.

The durable result is a readable Markdown Brief, not a JSON lifecycle object or approval schema.

## Recovery

On resumption, read the Brief and actual project files before relying on conversation memory.

- If the Brief is Draft, verify that its Open Choices still match reality and resume at the earliest unresolved choice.
- If the Brief is Confirmed, verify the confirmation record and compare only meaning-bearing changes since confirmation.
- If business meaning changes, mark the affected scope unresolved, record the change, revise it, rerun readiness checks, and obtain authority only for material choices not already covered by the new request. Preserve earlier decision records.
- If nothing material changed, do not reconfirm it merely because a new reporting period began.
- If only the interaction language changed, use it immediately without reopening the Brief. If only the requested artifact language changed, apply the shared language contract; return to framing only when audience or intended use also changed.

Never infer completion from a filename, old chat statement, or status label alone.

## Return Routes

| Condition | Route and stop |
|---|---|
| Confirmed Brief is current | `writing-report-plans` |
| Source structure, grain, authority, update, mapping, or use is unknown | Record the gap for `profiling-evidence`; planning decides when to invoke it. |
| Reusable metric population, formula, time basis, or source mapping is unknown | Record the gap for `defining-metrics`; planning decides when to invoke it. |
| User intent or risk authority is unavailable | Return to the user or named owner with the exact Open choice. |
| Downstream work exposes a changed question, audience, scope, or use | Remain in `framing-analysis` until the revised Brief is confirmed. |

The normal terminal state is a confirmed Brief routed to `writing-report-plans`. Do not perform that Skill's work here.
