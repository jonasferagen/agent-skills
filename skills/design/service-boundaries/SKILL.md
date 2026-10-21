---
name: service-boundaries
description: "Design or review service ownership and shared application behavior exposed through HTTP and MCP. Use when separating service responsibilities or adding a transport to an existing operation; not for container builds or protocol SDK setup."
metadata:
  version: "0.5.0"
---

# Service boundaries

Make service ownership and transport responsibilities explicit. Preserve the
project's chosen boundaries: this guidance never requires splitting one
application into services or adding a transport. Proposing a boundary change is
in scope as a proposal to the user; carrying it out is a separate decision.

## Procedure

1. Read the request: which operations, transports (HTTP, MCP) or storage
   resources it touches, and whether it asks for a change or a review.
2. Read the evidence: contracts (OpenAPI or similar interface files, route
   tables, MCP tool schemas, README sections), application handlers, the
   authentication and authorization code each transport runs, which service's
   migrations create each table or store, and decisions recorded in design
   documents or issues. Where no decision is recorded, assume what the code
   settles and state the assumption: the service whose migrations create a
   table owns it; the callers a route's registration and middleware admit are
   its permitted callers. Ask the user instead of assuming when the task would
   widen who may call what, when an operation with durable effects has no
   retry identity, when no service's migrations create a table a consumer
   uses, or before exercising a shared or live service.
3. Decide the boundary (next section) for each affected operation or resource:
   owner, **public paths** (the routes or tools through which callers reach
   it), **permitted callers** (the identities or roles that may invoke it),
   retry identity and replay behavior. One line each, for example:
   `orders.create — owner order-service; paths POST /orders, MCP tool
   create_order; callers role clerk; retry key Idempotency-Key, replay returns
   the existing order.`
4. Verify what the change touches (section after) against a running instance.
5. Report to the user (deliverable at the end).

## Connect services through their contracts

When both HTTP and MCP expose an operation, route them through the same
application handler and validation. Adapters translate protocol inputs, establish
the caller identity and map results; they do not duplicate business rules or
grant a stronger role. When an operation can cause durable effects, carry its
**retry identity** (an idempotency key or request id that marks a resubmission
as the same request) through both paths, and keep the established **replay
behavior** (what a duplicate submission returns: the existing result, a new
attempt or a refusal). If the project has defined neither for such an
operation, flag it and ask the user which behavior is intended; do not invent
one. Add only the transports the task calls for.

When the project has several services, give each its own storage and runtime
identity; a single application needs none of this. A resource one service
exposes to others (an API, a bucket, a directory) needs a documented interface:
how consumers reach it, its layout, access rules and what reads and writes
mean. Consumers use that interface and do not hard-code another service's
internal paths or tables; storage no interface covers is reached only through
its owner. If a consumer needs a guarantee the interface does not state, raise
it with the resource's owner (its service's maintainers, or the repository's
code-owners file; otherwise ask the user) rather than checking the owner's
internals. Where a shared resource has no documented interface, say so and ask
the user whether current access is the intended interface or one should be
written.

Keep credentials with the component that uses them and no wider: a migration
process may need DDL privileges, a request handler the service's narrower runtime
role, an orchestrator only what its operations need. A composition file (a
`docker-compose.yml` or a deployment manifest) may wire addresses and
dependencies without owning domain rules; independent services need not share a
source tree or release together.

## Verify the boundary being changed

Verify against a running instance; configuration text or a passing source check
alone cannot establish a live boundary. Use a local instance the task started,
and ask the user before exercising a shared or live service. The project's own
tests are the first evidence; add these manual checks where tests do not cover a
case:

- Listener: `ss -ltnp` (or `docker compose ps`) shows the service bound only to
  the intended interface and port.
- Access: an equivalent valid request on each transport (`curl` for HTTP; the
  project's MCP client or a scripted tool call for MCP) gives the same result,
  while a request without credentials, with insufficient permission or with
  invalid input is rejected.
- Retry: for an operation with a retry identity, resubmit with the same identity
  on each transport and confirm the established replay behavior.
- Storage: a shared resource is reachable through its documented interface,
  including the missing-resource case; direct access to another service's
  private storage is refused or absent.

Trace each public operation from transport input through identity and validation
to its application handler and result mapping: domain rules stay in the handler,
and each adapter preserves the operation's authorization and retry semantics.
Handler tests alone cannot establish that an adapter maps requests or identities
correctly. Local development establishes neither an authentication exemption nor
a need for a particular authentication mechanism. If users, exposure or allowed
actions would exceed the scope recorded in contracts, design documents or issues,
or no scope is recorded, raise it with the user before work relies on that
expansion; report unknowns and continue unrelated work.

## Deliverable

Report to the user: for each affected operation or resource, its owner, public
paths and permitted callers; the decisions taken and the assumptions standing in
for missing ones; which paths were verified, how, and with what evidence; and any
adapter, guarantee or proposed boundary change left unverified or open.
Container startup and database migration mechanics are outside this skill.
