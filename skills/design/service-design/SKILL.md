---
name: service-design
description: "Design or review service responsibilities, public interfaces, caller identity and storage custody across runtime boundaries. Use for HTTP/MCP behavior parity, retry and concurrency semantics, private-storage bypasses or service operational boundaries; not for container builds or protocol SDK setup alone."
metadata:
  version: "1.0.0"
---

# Service design

Give each service a clear responsibility and make its promises to callers
explicit. Preserve the project's chosen topology unless the task calls for
changing it. A new transport, repository or reusable package does not by itself
justify another running service.

## Establish the affected boundary

Start with the operation, resource or observed failure in the request. Read its
public contract, adapters, application operation and relevant ownership or
deployment evidence. Expand the review only when an affected dependency needs
it; a small interface change does not require a system-wide audit. Trace the
caller's preparation and result handling as well as execution. Runtime selection,
fixture setup and identity collection can depend on private provider files even
when the final execution command is public; transport questions must not hide
those dependencies in an integration review.

Identify who owns the behavior and state, how callers reach it, which identities
may act, and what success and failure promise. Distinguish an intended contract
from observed behavior. Route registration, migrations and deployment wiring
help locate ownership; they do not alone establish intended permissions or a
supported storage interface. State missing decisions and consequential
assumptions. A design or review can finish with those limits; do not silently
turn an unknown into a guarantee.

## Place responsibility and interfaces

Choose a runtime owner for each affected operation and resource. Prefer one
owner for a state transition so its validation, authorization and effects can
be understood together. Consider a separate service when independent authority,
lifecycle, scaling or failure isolation earns the operational cost; moving code
between repositories alone is not such a reason.

Describe the public operations and resource interfaces callers may rely on:
inputs, results, failures, allowed callers and relevant compatibility promises.
For an exposed bucket, directory or other store, include access rules, layout,
read/write meaning and needed consistency or durability guarantees. A deliberate
storage interface can be public; an accessible table or host path is not public
merely because a consumer can reach it.

Consumers use these interfaces instead of another service's private tables,
paths or implementation helpers. If an interface lacks a needed guarantee,
propose an owner-side contract or behavior change. Do not have consumers inspect
the owner's internals to manufacture that guarantee. Keep integration fixtures
under the test's ownership and use public setup and execution interfaces; sharing
private fixtures across repositories creates the same coupling as production
access. Share a fixture interface only when its owner intentionally supports it.

## Preserve behavior across transports

When HTTP and MCP expose the same operation, route them through the same
application operation and domain validation. Adapters translate inputs,
authenticate callers, preserve caller identity and map results and errors to
their protocol. Authorization must enforce the same allowed actions for the
same caller; an adapter must not grant a stronger role for convenience.

Keep business rules in the shared operation. Check required fields, defaults,
identity propagation, authorization, durable effects and failure meaning across
the affected paths. Equivalent behavior does not require identical wire formats
or status codes. Add only the transports the task needs.

## Define retry and concurrency behavior

For an operation with durable effects, establish how a caller distinguishes a
retry from a new request and what replay returns. Carry an established retry
identity through each affected transport and preserve its scope and replay
behavior. Consider a timeout after the effect commits: a caller may not know
whether the operation completed. Where semantics are missing, present the
decision and a reasoned proposal; do not invent an established guarantee or
require a separate approval for work already authorized.

When callers can race, define what concurrent requests may observe or change,
including duplicate retry identities and conflicting updates. Keep the invariant
with the state owner through an appropriate transaction, constraint, version
check or serialization mechanism. A preliminary consumer-side read cannot alone
protect a later write. State partial-effect and recovery behavior when an
operation spans owners; do not imply an atomic transaction across independent
services without a mechanism that provides it.

## Keep storage and operations under their owners

For multiple services, keep storage custody and runtime identities distinct.
Each service accesses another's state through the supported interface. Shared
infrastructure can host separate ownership boundaries; it need not mean separate
machines or databases. A single application does not need artificial service
roles or stores.

Keep credentials with the component that uses them and grant only its required
authority: migrations may need schema privileges, request handling a narrower
runtime role, and orchestration only its own operations. Deployment wiring owns
addresses and dependencies, not domain rules. Check the affected listener,
network exposure, timeouts, dependency failures and lifecycle responsibilities
when they bear on the task. Do not infer an authentication exemption from local
development or prescribe one authentication mechanism for every service.

## Match evidence to the work

For a design or review, trace the affected public paths through identity,
validation, state ownership and result mapping. Report what contracts, source or
existing results support and what needs execution to establish. Reading private
implementation to investigate ownership is different from making a consumer
depend on it.

For an implementation, exercise the changed boundary with the project's tests
or a suitable local instance within the task's authorization. As applicable,
cover equivalent valid requests, missing or insufficient credentials, invalid
inputs, retries, concurrent conflicts, missing resources and denied private
storage access. Check listener exposure when it changed. Handler tests alone
do not establish adapter mapping or identity propagation; configuration alone
does not establish live access. Exercise shared or live systems only when the
task authorizes that scope; otherwise report the evidence limit and complete
the work that does not depend on it.

Report the affected owners, public paths and callers, decisions and unresolved
assumptions, evidence obtained and remaining gaps. Distinguish proposed behavior,
implemented behavior and behavior actually exercised.
