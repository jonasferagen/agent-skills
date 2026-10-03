# External operation boundaries

Use this reference when a selected application operation depends on an external
service. Capability selection and cross-owner obligations remain with the
project's architecture. Start with the exact input and required result. If those
are missing, use an explicitly synthetic design case and retain the missing real
brief as an implementation prerequisite.

## Preserve the actual contract

Verify the selected operation against current official documentation before
relying on its behavior. Record the source and observation date in project
evidence. Distinguish direct responses, streamed bytes and durable provider jobs.
Check only the capabilities needed by the trace, such as lookup, output retrieval,
idempotency, cancellation and retention. An unavailable capability constrains the
design; it must not be invented to satisfy a shared interface.

Keep common bookkeeping separate from capability-specific inputs and outcomes.
Share a request identity or output manifest when their meanings agree. Give a
provider-specific operation its own contract when a generic operation would hide
required inputs, stages or recovery behavior. Additional providers alone do not
justify a plugin registry, worker queue or persistent service.

## Establish the execution boundary

Separate preparation from submission. Preparation validates local input,
configuration and destinations without initiating the external effect. Identify
any remote check that transmits input or incurs cost. Keep credentials scoped to
the adapter that needs them and out of request records and logs. Apply existing
input-data and spending authority; unresolved scope remains a prerequisite for
execution, not a reason to stop unrelated design work.

For an operation whose repetition can cause a second charge or durable effect,
retain intent and an attempt identity before the external effect. Persist the
provider identity as soon as it becomes available. Explain the gap between those
two writes: local bookkeeping cannot prove that a submission never reached the
provider. A timeout or lost response may leave the attempt's outcome unknown.

Reconcile an uncertain outcome using the supported provider lookup or idempotency
mechanism. A known job identifier does not solve a submission whose response was
lost before that identifier was retained. If supported reconciliation cannot
resolve the attempt, report uncertainty and require an explicit disposition
within the existing execution authority before another submission. Do not hide
automatic submission retries in the HTTP client or SDK.

Distinguish safe repetition of a status read or output download from repeating
generation. Choose timeouts and retry limits for each operation's effects. A new
attempt preserves the earlier record and cannot overwrite its candidate outputs.
Request withdrawal, attempted cancellation and confirmed termination are separate
facts; a late output still needs an owner.

## Secure the result

Retain the output bytes and required companion files before claiming a complete
deliverable. A provider URL with an expiry is a retrieval mechanism, not durable
custody. Record output identities and completeness, actual operation/model and
parameters where available, and enough provider evidence to diagnose failure.
Keep unavailable facts explicit and remove secrets from retained responses.

Choose a completion boundary for publication of the result and its record.
Downloads and partial writes must not appear as complete outputs. Describe recovery
after the provider finishes but local capture fails, using only retrieval behavior
the provider supports. Retention and receiver acknowledgement follow the project's
handoff agreement; successful execution does not make a creative acceptance decision.

Exercise the most consequential uncertainty window before implementation. Name
which checks are local, which need an authenticated provider, and which incur a
new effect. Local doubles establish application decisions only; live execution
and paid retries need their own authorized scope and evidence.
