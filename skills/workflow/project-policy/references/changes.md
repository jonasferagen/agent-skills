# Review changed circumstances and obligations

Assess the affected change, using existing policy and evidence. A proposed scope
expansion, an adopted rule and an already-observed operating condition have
different status. Finding real data in an experiment is a fact to address; it is
neither permission to process that data nor proof of readiness.

## Bound the change

Identify the old and new fact or obligation, its reason and affected owners.
Use the [policy axes](establish.md#discover-consequential-facts) when relevant.
Changes in users, exposure, data, lifetime, compatibility or recovery can require
review before any policy text changes. So can an adopted design that moves
responsibility, state or external authority.

Classify the effect as tighter requirements, relaxed requirements, a mixture or
a clarification. A wording-only correction needs a focused comparison; it does
not require reconstructing the policy or creating a worklog. An unchanged
obligation can still need implementation or evidence work.

Trace only affected consequences: responsibilities and boundaries, retained state
and migrations, interfaces, access and authority, checks, operation and recovery,
and reader or agent guidance. Bring in the project's engineering guidance for the
affected capability. No universal audit or automation framework is required.

When a change moves service responsibility or shared behavior across interfaces,
use service-boundaries if available, or the project's equivalent design guidance.
For new retained data or shared environments, follow the project's database,
migration and recovery routes. Policy establishes the required guarantees; those
owners establish the design and the evidence that supports them.

## Carry out authorized consequences

For tighter requirements, identify prerequisites and the evidence needed before
claiming readiness or enabling a proposed expansion. When the condition already
exists, distinguish current exposure from the authorized containment and repair
work. Continue unrelated work under known constraints.

For relaxed requirements, identify the guarantee being removed and consumers
that still depend on it. Assess simplification as well as added work, but retain
mechanisms that protect remaining commitments. A changed label does not authorize
deleting state, tests or compatibility support or starting a broad refactor.

Implement and verify consequences within the task's scope. Leave out-of-scope
work as concrete follow-ups with the affected guarantee, owner and needed check.
Use the project's existing authority for decisions; assessment alone grants no
permission to deploy, contact users or change external systems.

## Update owners and retain evidence

Keep policy current for operating facts and adopted constraints. Update affected
requirement owners, implementation guides, instructions and checks together as
their meaning changes. Current-state documentation describes what is implemented;
an adopted but unimplemented requirement remains in policy and its implementation
work remains in the plan. Link those owners instead of claiming the capability
already exists.

When a durable assessment is useful, record the date, assessed revisions, change,
consequences, checks and unresolved work in the project's work-record home.
Distinguish proposed, adopted, implemented and verified status. Preserve earlier
evidence as evidence of the conditions actually assessed. A passing package check
or updated policy text does not establish adoption or compliance by every consumer.
