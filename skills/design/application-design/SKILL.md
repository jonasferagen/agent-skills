---
name: application-design
description: "Design or review application operations, internal boundaries, state ownership and injected dependencies. Use for duplicated orchestration, coupled application logic, recovery or changed saved-state meaning; not for repository ownership, service transport or literal prose edits."
metadata:
  version: "1.0.0"
---

# Application design

Shape the application around a concrete operation: the behavior a caller requests
and the result or effect it can rely on. Start with the affected callers,
implementation, existing design decisions and interface agreements. An agreement
may be an API description, a schema with notes or a README section. Treat code
as evidence of current behavior, and distinguish it from adopted obligations and
proposed changes. When a consequential expectation is missing, state the
assumption and the work that depends on resolving it; continue the part the
request and known constraints support.

Here, an **owner** is the component responsible for a rule, state or dependency
and for changing it. Repository placement, process boundaries and deployment do
not by themselves decide these internal responsibilities.

## Start from the operation

For a focused change, follow the affected operation from input to result. For a
new application, choose one representative request. Identify its callers, rules,
effects and returned information. A read may finish with a value; a durable
operation may need publication and recovery. Add persistence, a job system or a
layered directory tree only when an actual responsibility requires it.

Put each decision with the component that owns its meaning. An input adapter
parses and translates a caller's request; a dependency adapter translates an
external mechanism. Neither should acquire a separate version of the
application's selection, validation or publication rules. Check ownership even
when there is only one entrypoint.

When a command, UI handler, worker or maintenance workflow exposes the same
operation, compare its decisions and effects. Prefer one owned operation with
thin entrypoints. A convenience workflow calls or composes supported operations;
it must not reconstruct them by reaching into private helpers and recreating
validation, state transitions or publication. Preserve differences required by
distinct caller obligations. Move a genuinely shared responsibility to a clear
owner rather than making every helper public.

## Define dependencies at their seam

Describe each collaborator by what the operation needs from it. Inject concrete
dependencies where the application is constructed, using ordinary parameters,
constructors or the project's existing conventions. Identify who supplies
configuration and credentials and who opens and closes resources. A dependency
injection framework, registry or factory needs a present reason of its own.

Keep SDK objects, transport payloads and provider source structures behind the
adapter when their changes would otherwise spread through application decisions.
Preserve details that affect meaning, supported capabilities or recovery; a
common result shape must not erase a consequential provider state. Verify the
capabilities and effects of each external operation against its actual contract
before relying on them, including lookups and preflight calls that may transmit
data or incur cost. State uncertainty when current evidence is unavailable. For an
external operation with submission or retained output, read
[external operation boundaries](references/external-integrations.md).

A dependency's source files being reachable does not make them its supported
interface. If application logic imports another component's private model or
helpers, identify the behavior it actually needs and the public seam that should
supply it. An adapter may translate a supported data format into an internal
model. Do not duplicate a provider's authoritative rules to make the seam appear
independent. If the available interface cannot express the needed behavior,
state the missing capability and propose the smallest change at its owner.

Choose modules from cohesive behavior and reasons to change. Trace a change to
one input rule or dependency: unrelated owners should not have to move together
merely because an internal representation leaked. A possible second
implementation alone does not justify a new abstraction.

## Own state and its meaning

For each durable effect, identify who may write it, when it becomes authoritative
and what a caller can observe after interruption. Distinguish request identity,
external attempt identity and result identity when they serve different purposes.
For example, an order, a provider payment reference and a stored receipt can have
different identities. Define whether repetition returns an existing result,
creates another attempt or refuses, including changed input under one identity.
Do not add identities an operation does not need.

Where writes must agree, define the transaction or publication boundary and how
work resumes on either side. A local file layout also needs an answer for partial
publication and competing writers when they are possible. If concurrent use is
out of scope, explain how the implementation prevents it.

Separate retained input, durable working state and accepted output from derived
builds, caches and scratch. Name what must be retained before reporting completion
and who can release it. Saving incomplete work need not depend on a successful
preview or build unless that is a product requirement. An intermediate export
used only by the next operation may be replaced by coherent captured input;
retain explicit export where interchange or inspection needs it.

When changing a saved state format or the rules that interpret it, trace an old
record through the new reader. State which rules or model revision give its
values meaning. A checkpoint that stores only coordinates may change meaning
when a map or ruleset changes even if its schema still parses. Choose an explicit
compatibility check, migration, retained interpreter or rejection according to
the product's obligations; do not silently reinterpret earlier state. Keep the
original evidence needed to diagnose or recover from a failed transition.

Finding a record, checking its integrity, confirming durable custody and accepting
its output for use establish different guarantees. Share mechanisms only while
preserving the guarantee each caller needs and its failure meaning. Avoid one
ambiguous `valid` flag. An operation may complete its handoff before the receiver
accepts the output's quality; describe these as separate outcomes when they differ.

For retained stage outcomes, input identities and publication evidence, read
[run records](references/run-records.md).

## Check behavior at the owning boundary

Trace a successful case and a failure or change that could invalidate the design.
For durable work, follow the state through interruption and show what the next
invocation can safely do. Select cases from the operation's risks; a read-only
function does not need a distributed-systems checklist.

Use focused tests with supplied dependencies to check the application's decisions,
including failure and repetition where relevant. Such tests should not require a
provider's source checkout merely to create its private objects or call its
helpers. Use representative public inputs and a local double at the supported
seam. Check real interoperability separately against the actual dependency or its
published artifact, recording the version and environment involved. A double
cannot prove the real provider's contract; a successful integration does not
replace checks of application rules.

Present the operation, responsibility changes, dependency seams, relevant state
transitions and cases traced, with the smallest useful implementation increment
and unresolved prerequisites. Cite evidence for adopted decisions and observed
behavior where it matters. Use the project's existing place for design records
when the task needs a document; a short explanation or review findings can
otherwise suffice. Keep design traces, implemented behavior and execution evidence
distinct.
