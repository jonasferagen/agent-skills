---
name: verification-design
description: "Choose proportionate checks for a change or milestone and consolidate overlapping validation by the failure each check can detect. Use when deciding which test layers to run, what evidence a claim needs, or whether repeated suites and setup can be combined."
metadata:
  version: "0.4.0"
---

# Verification design

Choose evidence for the behavior being claimed. Start with the project's
requirements and existing test commands (its CI configuration, Makefile or
package scripts); keep a check the project already requires unless the user asks
to change it. If the project has none, infer the commands from its test tool and
manifests, state that assumption and ask the user; when the user cannot be
asked, record the assumption in the report and mark the affected checks
outstanding. A fast edit loop, a milestone
gate (the checks a change must pass before it is accepted, usually named in CI
configuration or the contributing guide; if neither names one, ask the user) and
a production release may need different evidence.

The deliverable is a short claim-to-check list: each claim, the command that
checks it, and what that check does not establish, for example:
`orders total correctly: npm test -- pricing; does not show the HTTP route
reaches it`. Report it to the user, and put it in the change or pull-request
description where the project uses one, with the commands run and their
results.

## Match each claim to an observable boundary

For each important claim, name the failure that would disprove it and the
cheapest check able to observe that failure. A schema test can show that an
example parses. A domain test can show what a command writes. A public client
test can show routing and authentication. Independent sessions can show a race;
one embedded connection cannot. A built artifact can show packaging and startup;
source-level tests cannot. These are examples of boundaries, not a required
test taxonomy.

When a suite has grown hard to reason about, extend the claim-to-check list
with the failure each check detects, its prerequisites and its cost. Mark an
unavailable prerequisite as an outstanding check. Record the exact commands and
results that ran in that report; an earlier run proves only the code and
environment it exercised.

A check performed while an artifact is built is build evidence: it establishes
what the artifact contains, not that it runs. Where a service is packaged, the
claims worth separating are that the artifact was built, that it starts with its
declared dependencies, that a useful public operation succeeds through it, and
that state survives a restart. An in-process or embedded substitute for a
dependency supports that work without establishing any of them. A missing
required tool is an unmet prerequisite, not a passing check.

## Consolidate by failure signal

Two checks overlap when they fail for the same relevant defect and neither
observes an additional boundary. Compare the assertions, fixtures and setup,
not just their names or counts. Retain distinct evidence when one check reaches
a real database, process, network, permission boundary or built package that the
other replaces with a double or in-memory implementation.

If checks truly overlap, prefer the one with clearer assertions and cheaper,
more reliable setup. Share a fixture or artifact only when cases can remain
independent: shared mutable state can make failures order-dependent. Before
removing a check, demonstrate that the retained check fails for a representative
defect the removed one caught. A check that only parses an example and one that
executes it may use the same data but answer different questions.

Repeated setup can be consolidated without merging the assertions. Reuse a
built artifact or immutable fixture where the inputs are identical, while each
case keeps the state and identity needed to reveal its own failure. Measure the
cost first; a new test runner or wrapper also needs maintenance.

## Select suites from affected inputs (optional)

Use this section only where the project already has, or wants, a map from
changed paths to suites. When broad verification repeatedly runs unaffected
checks, separate suites by the boundary each proves. Give each a command, inputs, prerequisites and a
statement of what it covers. Reuse these commands in both the full run and the
selected run so their check lists cannot drift. Keep a full run available.

Keep a path-to-suite map in the repository, from changed paths to suites,
including shared contracts, generators, fixtures, configuration and
dependencies between suites, for example:

```yaml
"*": [lint]                                # always runs, whatever changed
docs/**: [docs-check]
src/**: [unit, integration]
schema/**: [unit, integration, contract]   # shared contract: both sides
```

Select the union of affected suites and their dependencies from the change as it
will actually be merged, compared against its target branch
(`git diff --name-only $(git merge-base HEAD <target>)`). Consider both sides of
renames and deleted paths. Extension alone is insufficient:
a Markdown file consumed by code can affect code tests, while ordinary prose
may need only document checks.

Checks that apply to every change (the `"*"` entry above) run in both the full
and the selected run. Use full verification for
anything the map cannot place: an unknown path, an executable or symlink whose
effect the map cannot see, an empty file, or the selection machinery itself.
Refuse an invalid map instead of silently omitting checks. Test representative
docs-only, code, shared-contract, mixed, rename and fallback selections,
including that a failed selected check blocks acceptance of the change. Revisit
the map when inputs or suites change.

This pattern needs identifiable input boundaries. When dependencies are unclear,
keep the broader check until the scope can be established. A path map does not
prove coverage by itself or replace independent expectations in tests. Avoid
introducing a selection framework for a small, cheap suite with no measured
omission or setup problem.

## Keep feedback and completion distinct

Use a focused subset during implementation and name it as such. A complete
verification claim lists the required suites, commands, environment and any
unrun checks. Do not make a fast subset look like a complete gate by giving both
the same verdict. Broaden checks when the change crosses a boundary or a focused
run reveals a concrete unresolved risk; stop repeating unaffected suites once
the required evidence is in hand.

This skill selects the evidence. Writing a missing test, or reviewing a settled
suite for weak assertions, mock drift and missing cases, is separate work; do it
when the request reaches it, following the project's testing conventions.
