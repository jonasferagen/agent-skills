# Repository boundary scenarios

These synthetic cases exercise decisions; they are not executed results. Give a
fresh evaluator the request and input context without the expected behavior.

## Isolated checkout and local verification

Request: “Make this library's ordinary tests work in a standalone checkout.”
Context: A publication test supplies a temporary directory, but its resolver calls
`../storage/tools/resolve`. The real resolver uses a documented JSON interface.
Expected: separate the local decision from resolver interoperability, inject or
fixture the local boundary, retain an explicit real-interface check and report
what each establishes. Do not remove required integration coverage or insist that
database-dependent operations need no database.

## Mutable schema and saved identities

Request: “Review why a saved draft disappeared after another repository changed.”
Context: Draft reads load schemas from a sibling checkout. Identity discovery
catches unreadable-record errors and treats those records as absent.
Expected: identify mutable interpretation and unsafe absence, select an immutable
contract with provenance, preserve saved interpretation and fail closed for identity
reuse when the required contract is unavailable. A path alias alone is insufficient.

## Private implementation imports

Request: “Reduce coupling in our browser's catalog command.”
Context: The command adds a compiler and runtime checkout to its import path and
imports both implementations before listing records. Published CLI interfaces exist.
Expected: propose a narrow public operation or pinned public package, keep optional
execution dependencies out of catalog-only work and avoid introducing a network
service without a need. Identify what interoperability evidence remains necessary.

## Prose references and existing locks

Request: “Use local aliases for current external references in our guides.”
Context: Current prose embeds sibling names and URLs. A package lock selects the
schema release; historical records cite exact commits. The project has no alias
renderer, and a shell example contains an actual package import name.
Expected: a local declaration and readable discovery table; defined human lookup
and actual machine resolution; no duplicate package pin; preserved historical
citations and required protocol literals. Missing aliases refuse explicitly.
Do not claim Markdown or the shell automatically expands aliases.

## Relocation and public fixture boundary

Request: “A renamed worktree cannot set up storage, and our image runner broke.”
Context: Storage checks the checkout basename against a provider's member map.
The image runner reuses the provider's test Compose fixture and unrelated engine pin.
Expected: stable consumer identity independent of checkout name; a public runner
interface rather than private fixture coupling. A shared directory or manifest can
be a valid public contract when explicitly owned and specified.

## Healthy dependency and narrow edit

Request: “Review this offline package consumer, then correct a label in its guide.”
Context: It has pinned complete contract artifacts, independent oracles and an
explicit integration job; the guide's label has a spelling error.
Expected: retain the healthy dependency. The label edit does not trigger an
architecture rewrite, new declaration format, service split or forced rollout.

## Human handoff

Request: “Define the handoff from an author to a reviewer.”
Context: Review concerns a named document revision; acceptance and publication
are different decisions. The workflow uses files and people, with no service.
Expected: enough terms for identity, acceptance, rejection and revised input; no
mandatory API, queue, common record schema or invented approval stage.

## Filesystem adapter and host operations

Request: Simplify an editor's save path. It uses a mounted persistent store but
selects an uncached route and polls an object service before declaring a save.
Context: All writers are local. The host owns replication and backup; the editor
must retain complete valid checkpoints before dropping disposable working state.
Expected: one consumer filesystem interface with explicit semantics; adapter-owned
contract and host-owned backing operations. Keep completeness and reset guards,
remove remote-backup states from the editor, test application behavior with local
fixtures and deployment semantics separately. Preserve existing data and pending
writes during transition. Do not assert cached writes meet durability promises
without evidence or introduce an unnecessary storage service.
