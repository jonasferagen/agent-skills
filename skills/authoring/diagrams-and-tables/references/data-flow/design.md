# Construct a data-flow diagram

Use [reading notes](read.md) for the view's meanings; reuse a current reading.
State scope and observed/proposed status. For diagram construction, use
[composition](../composition.md), [verification](../verification.md) and, when
implementing in Mermaid, [Mermaid drawing](../mermaid.md). Use
[examples](examples.md) only when helpful. Prose outlines use reading notes alone.

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

## Declare the notation

Give a legend or name the required notation. Our compact Mermaid convention is
explained in the reading notes. If the project requires a formal notation, use its
symbols and rules with a suitable renderer.

For a trust-focused question, show evidenced trust boundaries and name what changes
across them. A folder, repository, network or company border does not automatically
establish a trust boundary. Unknown enforcement stays unknown. A data-flow sketch
alone neither establishes security properties nor requires a full threat model.

Source links and their scope live in the [family guide](guide.md#external-guidance).
