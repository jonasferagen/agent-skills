---
name: service-boundaries
description: "Design or review service ownership and shared application behavior exposed through HTTP and MCP. Use when separating service responsibilities or adding a transport to an existing operation; container builds and protocol SDK setup are separate tasks."
metadata:
  version: "0.2.0"
---

# Service boundaries

Make service ownership and transport responsibilities explicit. Read the existing
contracts, application handlers, caller identities and data owners. Preserve the
project's chosen service boundaries; this guidance does not require splitting a
single application into services or adding another transport.

## Connect services through their contracts

Give each service its own storage and runtime identity. Other services use its
published contract rather than reaching into its private tables or storage.
Determine whether a filesystem location is private implementation storage or an
explicitly published resource before rejecting or wrapping access to it. A shared
file collection can be the intended interface; consuming it does not require a
new service or transport. Its owner publishes the contract once: interface,
selection, access and sharing rules, the semantics consumers may rely on, and
readiness and repair routes. Preserve that layout, access and write semantics,
and keep provisioning, credentials and storage lifecycle with their declared owner.
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

For a storage boundary, exercise both sides of the distinction: access through a
published resource contract must remain possible, while direct access to private
service storage must not bypass its owner. Check required access, missing-resource
behavior and the layout the consumer relies on. A completed write through a
published resource contract has the semantics that contract states; persistence
behind the interface is the provider's guarantee to check, not the consumer's.

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
