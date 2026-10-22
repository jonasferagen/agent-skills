# Boundary contracts

A contract states what the producing and consuming sides of a handoff can rely
on. It may be a package API, schema with notes, command interface, public database
view or a short written agreement between people. Keep it with its owning
interface. Use the applicable revision and actual caller evidence; a schema alone
does not describe every obligation.

For a reading task, explain the terms and unresolved ambiguities. For a review,
report omissions or violations with a concrete case. For authorized design or
change, propose or establish the needed terms. Do not turn inferred behavior into
adopted policy, or require fresh approval for work already authorized.

## Discover the terms the caller needs

Trace one exchange from both sides. Establish enough to answer:

- What is supplied, how is its identity or revision known, and which side owns it?
- What input, access and effects does the operation permit?
- What observable result establishes technical completion, and who accepts it?
- What remains valid after rejection, interruption or an unavailable dependency?
- Which side diagnoses failure, and what can the caller safely do next?

Choose precision from the actual decisions. A short handoff needs no universal
record schema. Execution success, human acceptance and downstream adoption can
be separate events. A result accepted against one input revision does not
automatically satisfy a revised input.

For durable effects, distinguish request identity from an attempt and its result.
State whether repetition returns an existing result, creates another effect or
refuses. A timeout can mean an unknown outcome; establish reconciliation before
resubmission that could duplicate work or spending. Withdrawal of interest does
not prove cancellation. Retain earlier accepted state and the evidence required
to recover; do not invent guarantees the provider does not supply.

## Change a contract deliberately

For an external resource, identify three responsibilities: the consumer's use,
the adapter's promised behavior and the deployment's implementation obligations.
They can belong to different owners even when their code shares a repository.
Specify observable semantics, not the mechanism a current host happens to use.
For a filesystem, define the required read/write visibility, publication and
unavailability behavior. Do not imply full POSIX semantics from a mounted path.
Persistence across application restarts does not imply backup, protection from
application deletion or survival of host loss; those require separate operational
policies when needed. A backup policy should not become an application save state.

A consumer checks valid, complete data through the supported interface. The
adapter's tests establish its declared behavior, and deployment checks establish
that the installed backing fulfills it. Replacing an implementation preserves
existing contents and accounts for pending writes and visibility before changing
routes. A successful rename of a configuration field establishes none of these.

Distinguish the publisher's newest revision from the revision each consumer has
adopted. Identify affected consumers from their declared dependencies and actual
uses. Compare old and new behavior, retained records and error semantics; adding
a field or keeping the same format label does not prove compatibility.

An independently distributed contract needs a stable identity and a declared
adoption or upgrade path. Publish new bytes under a new immutable identity; do not
change the meaning of a selected release in place. A consumer may accept one
version or a supported range according to its requirements. Neither automatic
upgrades nor indefinite backwards compatibility is a default obligation.

When an old record's contract cannot be loaded, expose that uncertainty. Do not
reinterpret the record under the latest schema or treat its reserved identity as
available. Specify migration and refusal behavior where that operation needs it.

## Challenge and report

Choose a valid exchange and a consequential rejection, interruption or dependency
revision. Look for a case in which both sides obey the written terms yet disagree
about the outcome. Distinguish a missing term, implementation violating a clear
term, and unavailable evidence. For each gap, name the decision, affected owner
and dependent work; continue work that does not need the missing answer.

Report the terms examined, cases exercised and evidence limits. A walkthrough
can reveal a contradiction but cannot demonstrate runtime compliance. A design
document does not grant permission to execute its described operations.
