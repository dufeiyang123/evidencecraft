# Language and Localization Contract

Use this contract when routing begins, a language field is missing or changed, or a Skill creates or materially revises a persistent artifact. Once a Plan is current or a Run exists, its frozen contract remains authoritative unless the user explicitly changes the affected field.

## Resolve three fields

- `interaction_language`: questions, options, status, routes, confirmations, and user-facing results.
- `artifact_language`: Brief, Plan, Profiles, Definitions, run records, task artifacts, reviews, draft, and final report.
- terminology and source-title handling: translations, first-use explanations, proper-name exceptions, quotations, and original-title rules.

Scope every instruction to the field it governs. “Deliver the report in English” does not switch a Chinese conversation to English.

Apply this order:

1. A current explicit requirement for the affected field.
2. For an existing Run with no explicit field change: its progress record, then the current Plan, then the confirmed Brief.
3. For `interaction_language`: an explicit interaction preference, otherwise the primary language of the current substantive request.
4. For `artifact_language`: an explicit deliverable requirement, then a confirmed audience delivery requirement, then a current Plan or Brief field, otherwise `interaction_language`.

Ignore incidental foreign terms, links, citations, code, and quoted source titles when detecting the request's primary language. A Simplified Chinese request defaults to Simplified Chinese.

Infer without asking when the rules yield one answer. If two explicit current requirements conflict, ask one focused question in the primary language of the request and stop the affected transition until resolved.

## Respect lifecycle ownership

- An interaction-language-only change takes effect immediately and does not reopen semantic artifacts or lifecycle state.
- An artifact-language-only change under the same audience and intended use returns to `writing-report-plans` to revise and reconfirm the report interface. Reuse current Profiles, Definitions, and language-independent analysis.
- A language request coupled with changed audience or intended use returns to `framing-analysis`.
- For legacy artifacts without language fields, infer the contract and record it in the current Run. Add the fields when that artifact is next revised; do not bulk-rewrite history.

## Localize artifacts

English templates and prompts are maintenance sources, not delivery defaults. When instantiating an artifact, translate headings, labels, table headers, placeholders, narrative, and artifact-type phrases such as “Analysis Brief,” “Report Plan,” and “Review Report.” Remove template comments.

Preserve these exact unless the confirmed contract says otherwise:

- canonical status and verdict codes;
- Work Package and Evidence IDs;
- exact Skill names, paths, hashes, and citations;
- code, formulas, and original source titles;
- recorded proper-name or source-exact exceptions.

English sources, templates, prompts, Profiles, Definitions, workers, or reviewers never switch the frozen contract. A language violation is an interface defect owned by the stage that produced the affected artifact.
