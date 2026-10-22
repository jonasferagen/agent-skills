---
name: repository-design
description: "Design or review a repository's responsibilities, public boundaries and external dependencies, including handoff contracts and acceptance. Use for cross-repository coupling, dependency discovery, compatibility or independent build and verification; not for routine edits inside an established boundary."
metadata:
  version: "1.1.0"
---

# Repository design

Make a repository understandable, changeable and verifiable from its own contents
and declared prerequisites. Start with the requested decision, local instructions,
published interfaces and the code or documents that actually consume them. A review
can end with findings; a design proposes choices; an implementation changes only
the authorized scope. Keep observed behavior, adopted requirements and proposals
distinct. Follow the project's existing place for decisions; report in chat when
no document is requested or needed.

## Establish what belongs here

Trace one concrete input through the repository to its output and consumer. Name
what this repository decides, what it publishes and what another owner decides.
For authored content, distinguish the source, its prepared output and the runtime
that uses it. For tools or libraries, distinguish public operations from internal
helpers. Execution, acceptance of the result and adoption downstream can have
different owners and evidence.

Choose boundaries from cohesive responsibilities and reasons to change. A
repository can contain content, instructions, libraries or several applications;
it need not become a service or a deployment unit. Trace a revised input and an
unavailable dependency to expose competing writers, cycles or changes that force
unrelated owners to move together. Prefer the smallest boundary that addresses
the demonstrated problem. Do not invent a shared framework for hypothetical reuse.

## Make dependencies explicit

For each affected external dependency, establish its purpose, supported interface,
selected revision or compatibility policy, and the operations that require it.
Distinguish documentation discovery, build inputs, test prerequisites and runtime
services. A development checkout may supply a declared dependency, but its directory
name or presence beside this repository must not silently become the interface.

Consumers use published artifacts, package APIs, commands or service contracts.
Imports from another checkout's private modules, reads of its internal tables,
parsing its configuration and reuse of its test fixtures create implementation
coupling. Replace them with an owned public boundary where useful. A documented
file format or database view can be that boundary; a network API is not required.
Renaming a private path as an alias does not make it public.

Separate a resource's public guarantees, the adapter that exposes them, and the
deployment that fulfills them. The adapter owns the consumer contract; the host
or provider operates its backing implementation. A persistent filesystem can be
the entire interface: consumers own file meaning and complete publication, while
the provider owns storage persistence and any caching, replication or backup
policy. Consumers should not reconstruct those guarantees by selecting internal
routes, inspecting caches or confirming individual remote uploads. If the backing
implementation cannot meet the promised contract, fix or qualify that boundary
at its owner rather than adding provider orchestration to every consumer.

An owner decides a contract's meaning; a consumer decides which supported
publication it adopts. Prefer immutable artifacts with recorded source revision
and integrity when reproducibility matters. Use the ecosystem's existing manifest
and lock for packages. A live service instead needs a supported interface and
capability policy; a source commit alone cannot identify its running behavior.
Explicitly supported workspace dependencies can remain, with their affected
commands and verification requirements stated.

For discovery aliases, external prose and locator configuration, read
[external references](references/external-references.md).
For defining or reviewing acceptance, failure and compatibility obligations, read
[boundary contracts](references/contracts.md).

## Preserve independent change

A consumer's normal gate checks its selected contract. The publisher checks that
its publication matches the source revision it claims. Comparing a consumer with
the publisher's latest checkout is an integration or upgrade check, not proof of
the consumer's own correctness. Pinning an artifact preserves authority without
forcing all consumers to update simultaneously. Do not prescribe simultaneous
releases or multiple-version support unless the actual deployment requires them.

Retained records must keep the interpretation promised when they were written.
Record the contract identity needed to read them; do not silently revalidate them
against a mutable upstream schema. If a necessary dependency is unavailable,
report that state rather than treating the record as absent or granting reuse of
its identity. A deliberate migration needs explicit acceptance and preservation
rules. An alias or a pin is discovery evidence, not proof of availability, trust
or compatibility.

Keep essential local instructions available with the repository. Shared policy
can be adopted as a pinned publication; a change elsewhere should not silently
change this repository's obligations. Link to external owners for their contracts
through the declared references, without copying their implementation procedures.

## Verify and report the boundary

Exercise the smallest relevant case: relocate the checkout, omit an optional
sibling, change a private upstream detail, supply an incompatible contract, or
interrupt a handoff. Use disposable copies or fixtures; do not alter a live
dependency to prove isolation. Read [verification](references/verification.md)
when designing a standalone gate or separating local and integration checks.

Report each material finding with the dependency, concrete trigger, consequence,
evidence and proposed owner of the fix. Identify which operations work alone,
which require declared dependencies, and what remains untested. Successful local
tests establish local behavior; they do not prove real interoperability. Keep
legitimate public dependencies when they support the repository's purpose.
