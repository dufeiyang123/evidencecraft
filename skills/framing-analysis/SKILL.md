---
name: framing-analysis
description: Use when a new recurring evidence report or analysis lacks a confirmed Analysis Brief, or when its audience, decision use, questions, scope, period, risk, or success criteria have materially changed; do not use merely to inspect sources, define a metric, write an execution plan, run analysis, or review a draft.
---

# Framing Analysis

Turn an analysis request into a confirmed, durable boundary for planning. Own the meaning of the requested analysis, not the evidence semantics, metric definitions, execution design, findings, or final review.

## Establish the state

Inspect the request, project instructions, nearby documentation, and any existing Brief before asking questions. Do not ask for facts available in the workspace.

Classify the state:

| State | Action |
|---|---|
| No Brief | Frame from the request and project context. |
| Draft Brief | Resume from its unresolved material choices. |
| Confirmed Brief, no semantic change | Report that it remains current, route to `writing-report-plans`, and stop. |
| Confirmed Brief with changed audience, use, questions, scope, period rule, risk, or success criteria | Reopen only affected sections, then confirm the revised Brief as a whole. |
| Downstream work returned a framing defect | Resolve the cited defect without absorbing the downstream role. |

Treat new period contents, new values, source refreshes, and execution errors as non-framing changes. Route them to the current Plan, a conditional specialist, or the Executor as appropriate.

## Inputs and authority

Start with whatever is available:

- the user's request and the decision or communication it should support;
- relevant project context and prior reports;
- an existing Analysis Brief and its confirmation record, if any;
- a downstream Return Route that identifies a framing defect.

Decide and record the analysis object, audience, use, reader-artifact expectation, questions, non-goals, scope, period semantics, constraints, risks, and success criteria. The reader-artifact expectation says whether the report must stand alone and which delivery formats or distribution context matter; it does not design paths, Work Packages, evidence structures, or rendering mechanics. The user retains authority over choices that change the intended decision, audience, commitments, or acceptable risk. Make conservative, reversible assumptions only for non-material details and label them tentative.

Do not decide source fitness, joins, transformations, metric formulas, Work Packages, Executor choice, findings, or review verdicts here.

## Resolve the language contract

Resolve two presentation fields before the first user-visible question or artifact. Scope each requirement to the field it actually governs: an instruction to deliver the report in English does not by itself change the language used to question a Chinese-speaking user.

- **Interaction language:** use an explicit interaction preference; otherwise use the primary language of the current substantive request.
- **Artifact language:** use an explicit deliverable language, then a confirmed audience delivery requirement; otherwise inherit the interaction language.
- **Terminology handling:** record how to treat source titles, proper nouns, quotations, and specialized terms.

Use the interaction language for questions, options, summaries, confirmation requests, and other user-facing messages. Use the artifact language for every heading, label, table header, placeholder replacement, and narrative passage in durable Markdown artifacts. User-visible artifact-type phrases such as “Analysis Brief” are translatable labels, including in the document title and prose; they are not canonical identifiers. Preserve canonical status codes, Work Package IDs, exact Skill names, paths, hashes, citations, code, formulas, and source-language titles unless the user requests a translation.

An English Skill, prompt, template, source, or identifier never changes either field. Infer both fields without asking when the precedence is clear. If explicit requirements conflict, ask one focused question in the interaction language. Record the resolved contract in the Brief. Missing language fields in an otherwise current legacy Brief are presentation metadata, not a reason to reopen its analysis meaning; establish the current-run contract and add the fields when the Brief is next revised.

## Frame the analysis

### 1. Bound the request

Summarize the apparent object, audience, intended use, and requested outcome in a few sentences. If the request contains several independent analyses with different audiences, decisions, or timelines, propose a decomposition and frame only the first agreed unit.

Identify likely non-goals early. A Brief that attempts to serve unrelated decisions is not ready for planning.

### 2. Resolve material choices

Ask one focused question at a time in the interaction language. Prefer a small set of concrete choices when the trade-off is clear; use an open question when the user must supply meaning.

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

### 4. Draft and confirm in sections

Instantiate [assets/analysis-brief-template.md](assets/analysis-brief-template.md) at `docs/evidencecraft/specs/YYYY-MM-DD-<topic>-analysis-brief.md`. Treat its English headings and labels, including the top-level “Analysis Brief” document-type label, as semantic slots: render every user-visible part in the artifact language and remove all template comments before saving. Do not edit the template in place.

Present the draft in coherent sections scaled to complexity. Confirm meaning as sections stabilize instead of withholding the whole design until the end. Revise when the user's response changes the intended frame.

Keep source names and candidate metrics only as known context. Mark semantic questions for `profiling-evidence` or `defining-metrics`; do not answer those questions inside the Brief.

### 5. Review readiness

Before requesting final confirmation, check the written Brief with fresh eyes:

- no placeholder, contradiction, or unresolved material choice is hidden;
- every question supports the stated use and fits the scope;
- the reader-artifact expectation is explicit without absorbing planning or rendering decisions;
- non-goals prevent plausible scope creep;
- period and cutoff language is unambiguous enough to plan;
- risks and success criteria can be checked later;
- tentative assumptions are visible and have an owner or resolution point;
- downstream semantic gaps are named without being prematurely solved.
- headings, labels, and narrative use the artifact language, apart from recorded terminology exceptions and canonical identifiers.

For a high-impact, multi-stakeholder, unusually ambiguous, or substantially revised Brief, dispatch an independent fresh-context reviewer using [prompts/analysis-brief-reviewer.md](prompts/analysis-brief-reviewer.md). Give the reviewer only the specified review package, including `{{ARTIFACT_LANGUAGE}}` and `{{TERMINOLOGY_AND_SOURCE_TITLE_HANDLING}}`. Treat `REVISE` as a stop before confirmation; treat `BLOCKED` as a return to the user or responsible authority. The reviewer may identify defects but may not make product choices or silently rewrite the Brief.

### 6. Apply the confirmation gate

Ask the user in the interaction language to confirm the complete written Brief. Capture the exact confirmation, confirmer, and date in the Confirmation Record. A vague acknowledgment of the conversation is not confirmation of the file; name the path and material tentative choices in the request.

Declare the Brief confirmed only when:

- all required sections are complete;
- no material Open choice remains;
- any blocking review finding is resolved;
- tentative choices are explicitly accepted as tentative;
- the user explicitly confirms the written Brief.

If confirmation is unavailable, save a Draft with Open Choices and stop. Do not write a Report Plan, profile evidence, define metrics, or begin execution while waiting.

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
- If a confirmed section changed, mark the Brief Draft, record the reason, revise the affected sections, rerun readiness checks, and reconfirm the whole Brief.
- If nothing material changed, do not reconfirm it merely because a new reporting period began.
- If only the interaction language changed, use it immediately without reopening the Brief. If only the requested artifact language changed, record the presentation change and route to planning to revise the report contract; return to framing only when audience or intended use also changed.

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
