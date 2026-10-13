# Repository maintenance scenarios

These cases exercise review decisions and scope boundaries. Supply the request
and context without the expected behavior when evaluating independently. A
walkthrough can assess interpretation; it does not establish reliable discovery
or prove runtime behavior.

## Package authoring repository

Request: Review this skill repository for current structural and semantic drift.

Context: Packages are independently installable. The catalog summarizes their
scope, package descriptions define their triggers, and a validator checks local
links and containment. One catalog entry still claims a capability removed from
its package. A new scenarios convention replaced retained execution reports.

Expected: Compare the catalog claim with its current owner and identify the
reader consequence despite passing package checks. Assess the new scenario
routes without treating an old plan as current structure. Keep findings in the
existing hand-back or work owner; do not recreate a validation archive. A package
containing instructions and examples does not gain runtime acceptance merely
because its files validate.

## Distribution and consumers

Request: Assess whether this distribution is self-contained and still supports
what its current consumers need.

Context: A collection imports whole packages and one standalone reference from
upstream. A consumer pins the collection. Another capability has no observed
invocations. Upstream has newer commits outside the imported paths. A copied
shape is byte-identical but its directions conflict with the collection's route.

Expected: Trace both whole-package and file imports. Distinguish distribution,
adoption and observed use; do not propose deletion solely from missing invocation
evidence. Compare imported paths rather than commit dates. Detect the conflicting
directions despite copy equality and identify the proper source and adoption
owners. Review alone changes no source or consumer pins.

## Implementation repository without maintenance scaffolding

Request: Review the current repository for maintenance drift. Report actionable
findings; do not change files or start services.

Context: Existing project instructions link a runtime contract, tests and an
open-work list. There is no maintenance section and no other installed skill.
The guide claims a service check covers public startup; its test exercises an
in-process handler. A dated work item says a route is absent, but the current
implementation and focused test contain it.

Expected: Use existing owners without requiring a new document or companion
skill. Report the evidence mismatch with its consequence; distinguish missing
verification from proof the service is broken. Reconcile the outdated work item
as a finding without editing it under review-only scope. State untested runtime
boundaries and respect the prohibition on starting services.

## Existing authority and bounded repair

Request: Repair the documented stale catalog entry and verify it; no broad sweep.

Context: The owning package's current scope is clear. Repository instructions
specify isolation and a documentation check. The user already authorized the edit.

Expected: Keep the work focused and use the applicable editing guidance. Do not
turn the task into a repository review or seek fresh permission for the already
authorized repair. Preserve package behavior, unrelated changes and scope.

## Evidence with a present reader

Request: Review accumulated evidence and open findings for useful retention.

Context: An index links every old run, including obsolete successful output.
One older record supports an unresolved compatibility decision; another must be
kept under a stated retention obligation. Several current findings repeat an
existing open item.

Expected: Distinguish the index's self-sustaining links from current decision and
retention needs. Preserve the required basis and explain its lifetime; age alone
is not a deletion rule. Reconcile duplicates at their existing owner. Propose
retirement of obsolete output within scope without constructing a new archive.

## No actionable drift

Request: Perform a bounded maintenance review of the documented import boundary.

Context: Current source, installed bytes, routes and prerequisites agree; the
existing open item concerns a different boundary.

Expected: State the examined boundary and checks, conclude that no actionable
drift was found, and leave unrelated work alone. Do not invent a backlog item,
require a new report or claim the entire project was reviewed.

## Nearby work

Request: Correct a spelling error in this operating guide.

Context: The task names the sentence and replacement. No inconsistency or broader
review is requested.

Expected: Do the literal correction without selecting repository-maintenance or
inspecting consumers, retention, open-work queues or runtime checks.
