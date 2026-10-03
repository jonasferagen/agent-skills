# One project across repositories

A repository boundary does not necessarily define a separate project. Before
bootstrapping, establish whether this is an independent project, the shared
foundation owner, or a member of an existing project. Preserve an existing choice.

## Shared owners and local facts

Keep project-wide policy, boundaries and shared technical decisions in their
selected authoritative repository. Member repositories link to those owners and
record only local facts, implementation decisions and explicit exceptions. Do not
create three full foundation tables in every member merely to satisfy a scaffold.
A short local foundation entry point is sufficient when it supplies the routes
and the actual differences. Keep independent projects independently governed.

Keep role assignments in the shared boundary owner. Internal design and commands
belong to the repository that implements them. Shared plans, historical evidence
and per-repository status answer different questions and retain their own homes.

## Local scope and exceptions

State how shared decisions apply and which choices are delegated locally. Local
facts extend the shared foundation; an omitted row inherits the shared decision.
Omission never waives a rule. A conflicting local statement is not automatically
an override. For an adopted exception, identify the shared rule, affected scope,
replacement, reason, decision authority and review or expiry condition. Resolve
conflicts through the project's authority and policy workflow, using existing user
authorization. Do not invent an approval step or adopt an exception by proximity.

## Collection and access

Document ownership and skill distribution are separate choices. One complete
collection in the shared owner can serve members that have access to it. Route
member instructions directly to that installation and keep provenance with it.
Do not install another copy solely because a new Git repository exists. Separate
pinned installations are valid when independent checkout or execution requires
them; they must not create competing owners for project decisions.

Record how a member locates the shared owner from its main checkout, task worktree
and relevant execution environment. Verify those routes. Do not assume a sibling
relative path still works inside a nested worktree. If an authoritative source is
unavailable, report the missing dependency and defer decisions that need it;
do not silently fall back to a stale copy. A snapshot, when deliberately selected,
needs its revision and update mechanism recorded.

## Reconcile an existing project

Compare values before removing copies; move unique facts to their proper owner.
Repair active README and agent routes, and retain historical evidence as history.
Verify that a shared change is read by members, that a local choice does not alter
other members, and that conflicting or unavailable authority remains visible.
Bootstrap establishes documents and access routes, not an automatic inheritance
engine or proof that runtime behavior follows the documents.
