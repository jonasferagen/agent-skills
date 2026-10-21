# Repository maintenance scenarios

These cases exercise review decisions and scope boundaries. Supply the request
and context without the expected behavior when evaluating independently. Reading
through a case with the skill can assess interpretation; it does not establish
reliable discovery or prove runtime behavior.

## Library with a stale README claim

Request: Review this library repository for current structural and semantic
drift.

Context: The README lists the library's modules and what each does, module
docstrings define their scope, and a linter checks local links. The README still
claims a feature that was removed from its module. Test output that used to be
committed is now replaced by a fixtures directory.

Expected: Compare the README claim with the current module and identify the
reader consequence despite passing lint. Assess the new fixtures layout without
treating an old plan as current structure. Report findings to the user where
work is already tracked; do not recreate the retired output archive. A package
containing instructions and examples does not gain runtime acceptance merely
because its files validate.

## Vendored code and dependents

Request: Assess whether this repository is self-contained and still supports
what the projects depending on it need.

Context: The repository vendors a whole upstream package and one standalone file
from another upstream. A downstream project pins this repository at a version.
One public function has no observed callers. Upstream has newer commits outside
the vendored paths. A vendored file is byte-identical to its source, but the
instructions around it contradict how this repository uses it.

Expected: Trace both whole-package and single-file vendoring. Distinguish
shipped, used-by-dependents and observed-in-use; do not propose deletion solely
from missing caller evidence. Compare the vendored paths with their source
rather than commit dates. Detect the contradiction despite copy equality and
identify which source should change. Review alone changes no source or
downstream pins.

## Implementation repository without maintenance scaffolding

Request: Review the current repository for maintenance drift. Report actionable
findings; do not change files or start services.

Context: Existing project instructions link a runtime contract, tests and an
open-work list. There is no maintenance section. The guide claims a service check
covers public startup; its test exercises an in-process handler. A dated work
item says a route is absent, but the current implementation and focused test
contain it.

Expected: Use the existing documents without requiring a new one. Report the
evidence mismatch with its consequence; distinguish missing verification from
proof the service is broken. Report the outdated work item as a finding without
editing it under review-only scope. State untested runtime boundaries and respect
the prohibition on starting services.

## Bounded, already-authorized repair

Request: Repair the documented stale README entry and verify it; no broad sweep.

Context: The module's current scope is clear. Repository instructions specify a
branching convention and a documentation check. The user already authorized the
edit.

Expected: Keep the work focused and follow the repository's editing conventions.
Do not turn the task into a repository review or seek fresh permission for the
already authorized repair. Preserve module behavior, unrelated changes and scope.

## Evidence with a present reader

Request: Review accumulated evidence and open findings for useful retention.

Context: An index links every old run, including obsolete successful output.
One older record supports an unresolved compatibility decision; another must be
kept under a stated retention requirement. Several current findings repeat an
existing open issue.

Expected: Distinguish the index's self-sustaining links from current decision and
retention needs. Preserve the required record and explain how long it is needed;
age alone is not a deletion rule. Reconcile duplicates against the existing
issue. Say which obsolete output can go and when, within scope, without
constructing a new archive.

## No actionable drift

Request: Perform a bounded maintenance review of the documented vendoring
boundary.

Context: Current source, vendored bytes, call sites and prerequisites agree; the
existing open issue concerns a different boundary.

Expected: State the examined boundary and checks, conclude that no actionable
drift was found, and leave unrelated work alone. Do not invent a backlog item,
require a new report or claim the entire project was reviewed.

## Nearby work

Request: Correct a spelling error in this operating guide.

Context: The task names the sentence and replacement. No inconsistency or broader
review is requested.

Expected: Do the literal correction without selecting this skill or
inspecting dependents, retention, the issue tracker or runtime checks.
