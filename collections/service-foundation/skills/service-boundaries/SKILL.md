---
name: service-boundaries
description: "Design or review service ownership and shared application behavior exposed through HTTP and MCP. Use when separating service responsibilities or adding a transport to an existing operation; container builds and protocol SDK setup are separate tasks."
metadata:
  version: "0.1.0"
---

# Service boundaries

Make service ownership and transport responsibilities explicit. Read the existing
contracts, application handlers, caller identities and data owners. Preserve the
project's chosen service boundaries; this guidance does not require splitting a
single application into services or adding another transport.

## Connect services through their contracts

Give each service its own storage and runtime identity. Other services use its
published operations rather than reaching into its tables or mounting its data.
A composition file may wire addresses and dependencies without owning domain
rules. Independent services need not share a source tree or release together.

When both HTTP and MCP expose an operation, route them through the same
application handler and validation. Adapters translate protocol inputs, establish
the caller identity and map results; they do not duplicate business rules or
grant a stronger role. Carry the operation's retry identity through both paths
when it can cause durable effects. Add only the transports the task calls for.

Keep credentials scoped to the component using them. A migration process may
need DDL privileges; a normal request handler should use the service's narrower
runtime role. An orchestrator receives only the access its operations need.

## Verify the boundary being changed

Trace each public operation from transport input through identity and validation
to its application handler and result mapping. Check that domain rules remain in
the handler and that each adapter preserves the operation's authorization and
retry semantics.

When changing HTTP and MCP adapters, exercise each affected public path. Compare
an equivalent valid request and relevant rejection cases, including insufficient
permission and invalid input. For operations with durable effects and a retry
identity, verify that both paths carry that identity to the shared handler and
preserve the established replay behavior. Handler tests alone cannot establish
that an adapter maps requests or identities correctly.

Report which ownership decisions and public paths were checked, what evidence
supports them, and any unverified adapter. Keep container startup and database
migration mechanics in their own workflows. No companion skill is required.
