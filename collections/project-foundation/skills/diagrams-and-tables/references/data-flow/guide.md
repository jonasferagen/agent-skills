# Data-flow diagrams

Use this view to explain what information enters a system, how it is transformed,
where it is stored and what leaves. State the system boundary and whether the view
is observed or proposed. A flow arrow carries named data; it does not by itself
mean execution order, network connectivity, permission or organizational ownership.

## Select the view and depth

For reading an existing view, trace the requested data and consult its owning
model or contract. No renderer or construction references are needed. For semantic
review, compare each flow and store with its evidence; a process's outputs need
plausible inputs or an identified source. Report missing flows without inventing
behavior. Form selection and prose outlines need only the semantic guidance below.
When creating or changing diagram source, use [composition](../composition.md),
[verification](../verification.md) and, when using Mermaid,
[Mermaid drawing](../mermaid.md). Read [examples](examples.md) only when helpful.

Use a sequence diagram for ordering and acknowledgements, a flowchart for control
branches, an ER diagram for stored relationships, and a deployment view for hosts
and connections. One system can have several of these views, each answering a
different question. Avoid mixing their arrow meanings in a single unexplained map.

## Represent the information

Name external sources or recipients relative to the declared system boundary.
Name processes by their transformation, stores by their retained content, and
flows by the information carried. A person, document procedure or agent can
perform a process; it need not be a running service or repository.

Draw input and output flows separately when they carry different data. Show the
process responsible for reading, writing or transforming stored content. A store
holds information; it does not perform an approval or conversion. If a direct
store-to-store arrow abbreviates a transfer, identify the omitted process or use
a higher-level view explicitly rather than presenting it as a detailed DFD.

Distinguish file bytes, identity/provenance records and references when confusing
them would change the design. A URL or identifier is not proof that bytes have
been retained. Include derived outputs and error records when they matter to the
question. A caption can state intentionally omitted flows.

A context view can show the whole system as one process with external inputs and
outputs. When opening it into a detail, preserve those boundary flows and explain
any aggregation. Do not introduce an unexplained source, sink or changed payload
merely to make the detailed layout convenient.

## Boundaries and notation

State the notation or give a legend. Our compact Mermaid convention uses rectangles
for external entities, rounded nodes for processes and cylinders for stores.
This is an illustrative convention; it does not claim formal Yourdon/DeMarco or
Gane–Sarson notation. If the project requires a named notation, use its symbols
and rules with a suitable renderer.

For a trust-focused question, show evidenced trust boundaries and name what changes
across them. A folder, repository, network or company border does not automatically
establish a trust boundary. Unknown enforcement stays unknown. A data-flow sketch
alone neither establishes security properties nor requires a full threat model.

## External guidance

[OWASP's system-modeling guidance](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html#system-modeling)
identifies processes, stores, flows, external entities and trust boundaries as useful
parts of a security model. Its scope is threat modeling, not a universal DFD notation
standard. [Mermaid's flowchart documentation](https://mermaid.js.org/syntax/flowchart.html)
owns the syntax used by our illustrative diagrams. Our shape choices, routing and
document decomposition remain collection conventions. Verify target-renderer support
when using features beyond those already established in the project.
