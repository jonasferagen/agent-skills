# External operation boundaries

Use this reference when an application operation submits an external effect,
recovers an uncertain attempt or promises custody of external output. Start with
the selected dependency, exact input and required result. If they are missing,
label any design example as synthetic and identify which implementation decisions
need the real requirements. Provider selection is a separate decision; retain an
unsettled choice when it changes the operation's design.

## Preserve the actual contract

Verify the selected operation against current official documentation before
relying on its behavior. Record the source and observation date beside the
design, so a later reader can tell when the behavior was checked. Distinguish
direct responses, streamed bytes and durable provider jobs. Check only the capabilities needed by the trace, such as lookup, output retrieval,
idempotency, cancellation and retention. An unavailable capability constrains the
design; it must not be invented to satisfy a shared interface.
If current evidence cannot be obtained, label the uncertain contract as an
assumption and retain verification as an implementation prerequisite. Continue
design work that does not depend on resolving it.

Keep common bookkeeping separate from capability-specific inputs and outcomes.
Share a request identity or output manifest when their meanings agree. Give a
provider-specific operation its own contract when a generic operation would hide
required inputs, stages or recovery behavior. Additional providers alone do not
justify a plugin registry, worker queue or persistent service.

## Establish the execution boundary

Separate preparation from submission. Preparation validates local input,
configuration and destinations without initiating the external effect. Identify
any remote check that transmits input or incurs cost. Keep credentials scoped to
the adapter that needs them and out of request records and logs. Make the effect
boundary visible to callers. Apply the project's existing authorization and
data-handling rules to actual execution.

For an operation whose repetition can cause a second charge or durable effect,
retain intent and an attempt identity before the external effect. Persist the
provider identity as soon as it becomes available. Explain the gap between those
two writes: local bookkeeping cannot prove that a submission never reached the
provider. A timeout or lost response may leave the attempt's outcome unknown.

Reconcile an uncertain outcome using the supported provider lookup or idempotency
mechanism. A known job identifier does not solve a submission whose response was
lost before that identifier was retained. If supported reconciliation cannot
resolve the attempt, expose the unknown outcome and the consequence of
resubmission to the actor responsible for deciding whether another effect is
acceptable. Do not treat uncertainty as confirmed failure. Do not hide
automatic submission retries in the HTTP client or SDK.

Distinguish safe repetition of a status read or output download from repeating
the effect itself (a charge, a render, a sent message). Choose timeouts and retry
limits for each operation's effects. A new attempt preserves the earlier record
and cannot overwrite the earlier attempt's outputs.
Request withdrawal, attempted cancellation and confirmed termination are separate
facts; a late output still needs an owner.

## Secure the result

When the operation promises a retained deliverable, retain its output bytes and
required companion files before claiming completion. A provider URL with an
expiry is a retrieval mechanism, not durable custody. Record output identities
and completeness, the actual operation and parameters the provider reports where
available, and enough provider evidence to diagnose failure. Keep unavailable
facts explicit and remove secrets from retained responses. An ordinary lookup or status read
needs only the result and retention the operation's agreement requires.

For a retained result, choose a completion boundary for publication of the result
and its record. Downloads and partial writes must not appear as complete outputs.
Describe recovery after the provider finishes but local capture fails, using
only retrieval behavior the provider supports. Retention and receiver acknowledgement follow the agreement
between sender and receiver; successful execution does not decide whether the
receiver accepts the output.

Trace the most consequential uncertainty window during design. Name which checks
are local, which need an authenticated provider, and which incur a new effect.
A design trace is not runtime evidence. Local doubles establish application
decisions only. Checks against the real dependency need their own evidence and
must stay within the task's authorized effects; an extra submission is another
effect, even when called a retry.
