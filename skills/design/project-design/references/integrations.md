# Choose an integration

Start from a workflow step and the capability it requires. Select a service or
mechanism only after identifying the required input, result, side effects and
consumer acceptance. A selected provider name is not yet a **handoff
agreement** (the written terms of one exchange: what is handed over and how it
is identified, what the receiver checks before accepting it, and what each side
does on failure). Use [workflow design](workflows.md) when the operation itself
is still unclear.

## Compare the choices that matter

Record the decision, alternatives, constraints, recommendation, reason and evidence
still needed. Include continuing a manual procedure or using an existing local
tool when either can satisfy the need. Compare only dimensions that affect this
workflow: quality, supported inputs and outputs, reproducibility, human review, data exposure,
execution authority, failure visibility, recovery, cost and operating effort.
Verify provider-specific capabilities and terms from current authoritative sources
when they influence selection; a target named in project notes is not that evidence.

Keep what a capability promises independent of its transport where useful. Distinguish
manual use, local command execution, direct provider calls and a persistent service.
Do not introduce a queue, broker, shared adapter framework or network service solely
because more than one integration may eventually exist. Identify the concrete
coordination or reliability requirement that would justify it.

## Establish the operation boundary

Before implementation, identify who requests work, which actor may execute it,
what may be read or written, where credentials are supplied and where outputs
remain candidates. Record required version/model/configuration and how the result
will identify them. Keep secrets out of records and Git.

Separate setup and preflight from execution. Determine which supposedly validating
calls have external effects, submit data or incur cost. What the user has already authorized
sets the permitted scope; writing this design grants no new access or spending.
When an integration changes data exposure, retained state, recovery,
compatibility or who may act, raise it with the user before proceeding, and
keep unresolved prerequisites visible.

Write the handoff agreement between the requesting and executing sides. For a
call to an external service that may have side effects or cost, also establish
how a request and each attempt are identified, how an unknown outcome is
resolved (can the service be asked what happened?), and what retry, cancellation
and a partial result mean for the chosen operation. Do not assume the service
supports idempotency or cancellation; a retry policy needs evidence of its
actual behavior and of how local records survive interruption. State which
results and records are durable before scratch or credentials are cleaned up.

## Hand off to implementation

Name the smallest operation that can test the choice, its owner, prerequisites
and acceptance evidence. Implementation belongs to whoever owns the capability;
accepting the output and adopting it downstream are separate decisions by the
people responsible for those steps. Provider-specific
setup and commands belong in its procedures, linked from the design.

Keep decisions scoped: proposed, decided, implemented and verified are separate
states. Preserve unselected alternatives only when they explain a meaningful
tradeoff. A successful local experiment does not establish retry safety against
an external service or production readiness. Broaden reusable integration
guidance after a concrete operation exposes a repeated need.
