# Data-flow diagrams

Use this view for information entering, moving through, being retained in or leaving
a system. Select the task before loading authoring rules.

- Read, explain, apply or outline the view in prose: [reading notes](read.md).
- Assess its accuracy: [semantic review](../review.md) with the reading notes.
- Create or change diagram source: [construction](design.md).
- Review only rendered readability: [verification](../verification.md).

Use [form selection](../select.md) when the question may instead require ordering,
control flow, stored relationships or ownership. Examples are conditional on
construction needs; reading a diagram does not require generating another one.

## External guidance

[OWASP's system-modeling guidance](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html#system-modeling)
identifies processes, stores, flows, external entities and trust boundaries as useful
parts of a security model. Its scope is threat modeling, not a universal DFD notation
standard. [Mermaid's flowchart documentation](https://mermaid.js.org/syntax/flowchart.html)
owns the syntax used by the illustrative diagrams here. Their shape choices,
routing and document decomposition are this skill's conventions. Verify target-renderer support
when using features beyond those already established in the project.
