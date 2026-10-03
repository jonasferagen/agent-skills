# Choose an integration

Start from a workflow step and the capability it requires. Select a service or
mechanism only after identifying the required input, result, side effects and
consumer acceptance. A selected provider name is not yet an operation contract.
Use [workflow design](workflows.md) when that contract is still unclear.

## Compare the choices that matter

Record the decision, alternatives, constraints, recommendation, reason and evidence
still needed. Include continuing a manual procedure or using an existing local
tool when either can satisfy the need. Compare only dimensions that affect this
workflow: quality, supported artifacts, reproducibility, human review, data exposure,
execution authority, failure visibility, recovery, cost and operating effort.
Verify provider-specific capabilities and terms from current authoritative sources
when they influence selection; a target named in project notes is not that evidence.

Keep a capability's contract independent of its transport where useful. Distinguish
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
calls have external effects, submit data or incur cost. Existing user authorization
sets the permitted scope; writing this design grants no new access or spending.
Use project-policy when a proposed integration changes exposure, retained state,
recovery, compatibility or authority, and preserve unresolved prerequisites.

Use [project-contracts](../../project-contracts/SKILL.md) to specify the exchange
between requesting and executing owners. For a provider integration, establish
request and attempt identity, provider job lookup when available, unknown
outcome handling, retry/resume, cancellation and partial-output behavior for the
chosen operation. Do not assume a provider supports idempotency or cancellation.
A retry policy needs evidence about the provider's actual behavior and how local
records survive interruption. State which results and records are durable before
scratch or credentials are cleaned up.

## Hand off to implementation

Name the smallest operation that can test the choice, its owner, prerequisites
and acceptance evidence. Implementation belongs to the capability owner;
creative acceptance and consumer adoption retain their own owners. Provider-specific
setup and commands belong in its procedures, linked from the design.

Keep decisions scoped: a proposed mechanism, a selected design, implemented
behavior and verified operation are separate [states](../../../references/status-and-evidence.md#states). Preserve unselected alternatives only when
they explain a meaningful tradeoff. A successful local experiment does not establish
paid-provider retry safety or production readiness. Broaden reusable integration
guidance after a concrete operation exposes a repeated need.
