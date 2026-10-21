# Design a workflow

Start with an actual request or a clearly labelled example. Reuse the project's
owners and artifact definitions. Trace a request to an accepted result before
choosing orchestration, storage or service boundaries. A project's output may be
documents and decisions rather than running software; do not require a runtime
for each owner.

## Trigger, actors and completion

Identify the trigger, required inputs and the observable result that completes
the workflow. Distinguish completion of an operation, acceptance of its output
and adoption by its consumer. A tool success status cannot establish that the output
was approved, delivered correctly or suits its consumer.

Name the responsible role at each step and who may make its decision. Separate
human judgment, agent preparation and tool execution where that affects authority
or evidence. Use existing delegation; do not invent mandatory human approvals or
infer execution permission from a proposed procedure. Leave consequential unknown
actors or criteria visible and state which step depends on resolving them.

Identify consequential handoffs and their producing and accepting owners. Write
a **handoff agreement** (the written terms of one exchange: what is handed over
and how it is identified, what the receiver checks before accepting it, and what
each side does on failure) when identity, acceptance or failure obligations need
definition. Keep the overall workflow focused on how work moves
through those exchanges.

## Explain how the work is performed

For steps whose mechanism is unclear, name the performer, how they act, the result
and the next responsible owner. An agent following an instruction document is a
valid mechanism; link that procedure instead of inventing an API. Distinguish the
responsible owner from an executing agent, command or service when they differ.
A single step can combine methods, such as an agent invoking a CLI that calls a
provider. Keep detailed calls inside the owning procedure or interface explanation.

A swimlane view helps explain responsibility changes and execution methods.
Draw it in the format the project already uses for diagrams (Mermaid when it
has none). Show a small overview and link its procedures. Exact messages
may need a sequence detail; service boundaries and dependencies belong in their
architecture view. The diagram describes work, not a requirement to automate it.

Keep a concise mechanism explanation beside an unclear step. Use the process
the project already follows without adding a required method taxonomy or
migrating formats just to make agent-led work understandable.

## Artifacts and state changes

Give each artifact one authoritative owner: the original request, each
candidate output, the review of it, the accepted version and the record of
which version a consumer uses. Link identities and versions instead of copying
the underlying decisions into every record. Link the accepted output to the
exact request and inputs it satisfies. A changed request or input invalidates
that match until assessed; do not silently reuse an earlier approval for a
different result.

Describe the important states and who may move work between them. State what is
preserved on rejection and which event makes outputs eligible for cleanup.
Distinguish intended transitions from mechanisms already implemented. Choose
storage paths and serialization only when the workflow needs them.

## Interruptions and recovery

Exercise the failures most likely to change the design: incomplete input, a
rejected result, interrupted execution, a duplicate request, a late output or a
consumer's conflicting edit. For each, identify the diagnosing owner, retained
state, next allowed action and evidence needed to resume.

Use the handoff agreement for the affected exchange to determine repeat,
interruption and cancellation behavior. Missing terms are agreement work; do not
infer safe retry from a workflow arrow or treat withdrawal as confirmed
cancellation.

## Record and exercise the design

Keep workflow explanations and handoff agreements where the project keeps its
design documents, linked from the architecture overview. Performing steps belong
in the responsible repository's procedures, and records of actual runs and
reviews wherever the project logs them. Keep existing document locations until a
deliberate migration. Design options and reasons belong beside the choice, or in
a decision record if the project keeps them. Keep unresolved tasks in the
project's issue tracker rather than in a second list; if there is none, keep
them in the design note's open points and tell the user.

Walk the normal case and a consequential exception using linked example records
or an existing artifact. Show what each owner receives and decides, and what
remains unchanged. Label synthetic identities, simulated approvals and proposed
mechanisms. A walkthrough establishes design consistency only; real execution,
recovery and acceptance require separate evidence.
