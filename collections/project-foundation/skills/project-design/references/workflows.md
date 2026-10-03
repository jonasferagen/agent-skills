# Design a workflow

Start with an actual request or a clearly labelled example. Reuse the project's
owners and artifact definitions. Trace a request to an accepted result before
choosing orchestration, storage or service boundaries. Repository output may be
briefs, reviews, procedures and decisions; do not require a runtime for each owner.

## Trigger, actors and completion

Identify the trigger, required inputs and the observable result that completes
the workflow. Distinguish completion of an operation, acceptance of its output
and adoption by its consumer. A tool success status cannot establish creative
approval, delivery correctness or consumer suitability by itself.

Name the responsible role at each step and who may make its decision. Separate
human judgment, agent preparation and tool execution where that affects authority
or evidence. Use existing delegation; do not invent mandatory human approvals or
infer execution permission from a proposed procedure. Leave consequential unknown
actors or criteria visible and state which step depends on resolving them.

Identify consequential handoffs and their producing and accepting owners. Use
[project-contracts](../../project-contracts/SKILL.md) when input/result identity,
acceptance conditions or failure obligations need definition. Keep the overall
workflow focused on how work moves through those exchanges.

## Artifacts and state changes

Give each original, candidate, review, accepted revision and consumer selection
one authoritative owner. Link identities and revisions instead of copying the
underlying decisions into every record. Link the accepted output to the exact
brief and inputs it satisfies. A changed brief or input invalidates that match
until assessed; do not silently reuse an earlier approval for a different result.

Describe the important states and who may move work between them. State what is
preserved on rejection and which event makes outputs eligible for cleanup.
Distinguish intended transitions from mechanisms already implemented. Choose
storage paths and serialization only when the workflow needs them.

## Interruptions and recovery

Exercise the failures most likely to change the design: incomplete input, a
rejected result, interrupted execution, a duplicate request, a late output or a
consumer's conflicting edit. For each, identify the diagnosing owner, retained
state, next allowed action and evidence needed to resume.

Use the contract for the affected exchange to determine repeat, interruption and
cancellation behavior. Missing terms are contract-design work; do not infer safe
retry from a workflow arrow or treat withdrawal as confirmed cancellation.

## Record and exercise the design

Keep workflow and handoff contracts in their architecture owner, performing steps
in the responsible repository's procedures, and actual runs/reviews in work records.
Foundation tables hold concise adopted facts; they do not become workflow manuals.
Design options and reasons belong beside the choice or in an existing decision
record when the explanation warrants one. Keep unresolved tasks in one active queue.

Walk the normal case and a consequential exception using linked example records
or an existing artifact. Show what each owner receives and decides, and what
remains unchanged. Label synthetic identities, simulated approvals and proposed
mechanisms. A walkthrough establishes design consistency only; real execution,
recovery and acceptance require separate evidence.
