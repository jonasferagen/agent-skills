---
name: application-design
description: "Turn a workflow into application operations, state ownership and dependency interfaces, or revise those boundaries. Use when deciding where behavior belongs inside an application; not for choosing a provider, language idioms or literal document edits."
metadata:
  version: "0.3.0"
---

# Application design

Open an application's internal design around a concrete operation. Produce enough
structure to implement the requested slice, or identify the decisions that block
it. Use the project's existing architecture, interface agreements (whatever
written statement says what each side of a handoff may rely on: an API
description, a schema with notes, a README section), implementation and scope.
If no architecture or agreement covers the operation, state what you infer from
the code and ask the user before building on it. Label each design statement as
**proposed** (your suggestion), **adopted** (decided by the project, cite where)
or **observed** (what the current code or a run does, cite the evidence). In
this skill, the **owner** of a rule, state or dependency is the component (and
the people maintaining it) responsible for deciding and changing it.

## Bound the work

For a focused change, start with the affected operation and its callers. For a
new application, trace one representative request from input to result. Identify
who uses the result, which decisions the application owns and which belong to
another actor. Preserve existing ownership; if the trace exposes a conflict,
name the affected owner and resolve only what the user's task covers.

A read-only operation may finish with a returned value. A durable operation may
need state transitions and recovery. Do not impose a job system, persistence or
a layered directory tree before an actual responsibility requires it.

## Give behavior and dependencies owners

Name the rules that must hold at the operation boundary and the information
needed to enforce them. Put each rule with the application or domain owner that
can decide it. An input adapter parses and translates; a dependency adapter maps
an external mechanism. Neither should silently decide a second version of the
operation's rules. Check the same boundary when there is only one caller.

When several entrypoints expose the same operation, trace each relevant path:
commands, UI handlers, background workers and maintenance workflows can each
accumulate their own selection, validation and publication rules. Compare the
rules and effects, not just similar code. Prefer one owned operation with thin
adapters; convenience workflows compose it rather than reconstructing it from
internal helpers. Keep differences that serve distinct caller obligations.

Describe collaborators by what the operation needs from them. Keep external wire
formats and SDK objects at their boundary when their changes would otherwise
spread through application decisions. Preserve provider details that affect
meaning or recovery; a common result shape must not erase a consequential state.
For external calls, read [external integrations](references/external-integrations.md).

Separate construction from behavior: identify where configuration, credentials
and concrete collaborators enter, and which component owns their lifetime. This
can be ordinary startup code. Follow the language's and runtime's usual conventions; a
container or dependency-injection framework is a separate choice.

Choose modules from cohesive behavior and reasons to change. A new interface
should protect a real caller or external boundary; a future second implementation
alone does not justify factories or registries. Trace the impact of changing one
input rule or dependency to see whether unrelated owners must move together.

## Make state changes recoverable

For each durable effect, identify its owner, the point at which it becomes
authoritative and what a caller can observe after interruption. Keep operation
identity, external identity and result identity distinct when they serve different
purposes: for a payment, the order id names the request, the provider's payment
reference names the external attempt, and the stored receipt id names the
result; resubmitting the order must not mint a new receipt. Determine how
repetition and changed input under an existing identity are handled. Do not add
these identities to an operation that has no need for them.

Where several writes must agree, establish the transaction or publication boundary
and how work resumes on either side. Choose the mechanism against the actual
writers and readers. A local file layout still needs an answer for competing
writers or partial publication if those are possible. If concurrency is deferred,
state how the first implementation will prevent it.

Distinguish durable records and outputs from reconstructible state and scratch.
State what must be retained before reporting completion, and who can release it.
An intermediate export used only to feed the next operation need not become a
user-managed stage: consider passing a coherent captured input directly, while
retaining explicit export where interchange or inspection needs it. A recoverable
save and a derived build have different success conditions; do not make saving
incomplete work depend on a successful build unless the product requires it.
An operation that hands off a result may complete before the receiving actor
accepts its quality; keep that distinction in the interface agreement between
the two sides.

For operations needing retained stage outcomes, input identities or publication
evidence, use [run records](references/run-records.md).

Shared discovery or storage machinery does not imply a single acceptance rule.
Finding a record, checking its integrity, confirming durable storage and accepting
its output for use establish different guarantees. Name the guarantee each caller
needs and preserve it when consolidating implementations; avoid one ambiguous
"valid" flag that callers interpret differently.

## Exercise the boundary and choose the increment

Trace a successful case and a failure or change that could invalidate the design.
Follow the records and observable result through the interruption point, including
what the next invocation can safely do. Choose cases from this operation's risks;
do not run a fixed distributed-systems checklist for every function.

For each consequential promise, identify a check that can observe it at the owning
boundary, and put it in the project's existing test suite. A fake dependency
can exercise the application's decision; it cannot establish a real provider's
contract. Keep design traces, implemented behavior and execution evidence distinct.

Present a compact design: operation and rules, responsibilities and dependencies,
relevant state transitions, traced cases, and
the smallest next implementation with its unresolved prerequisites. Report this
to the user; when the task calls for a document in the repository, put it where
the project keeps its design documents, or beside the code if there is no such
place, and say which you chose. A table or short explanation may suffice; create
separate documents only when they have distinct readers or owners. A review request can end with findings and needs no rewrite.
Add language conventions, transport setup and deployment guidance only
when the requested implementation reaches them.
