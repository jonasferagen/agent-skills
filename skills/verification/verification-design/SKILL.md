---
name: verification-design
description: "Choose proportionate checks for a change or milestone and consolidate overlapping validation by the failure each check can detect. Use when deciding which test layers to run, what evidence a claim needs, or whether repeated suites and setup can be combined."
metadata:
  version: "0.3.1"
---

# Verification design

Choose evidence for the behavior being claimed. Start with the project's
requirements and existing test commands; preserve an explicit gate until its
owner changes it. A fast edit loop, a milestone gate and a production release
may need different evidence.

<!-- Package-boundary copy: test-writing/SKILL.md (Workflow, step 1) and the opening of test-writing/references/integration-tests.md restate this rule for an author writing the test. Keep them aligned. -->
## Match each claim to an observable boundary

For each important claim, name the failure that would disprove it and the
cheapest check able to observe that failure. A schema test can show that an
example parses. A domain test can show what a command writes. A public client
test can show routing and authentication. Independent sessions can show a race;
one embedded connection cannot. A built artifact can show packaging and startup;
source-level tests cannot. These are examples of boundaries, not a required
test taxonomy.

Keep a compact map of claim, check, failure it detects, prerequisites and cost
when a suite has grown hard to reason about. Mark an unavailable prerequisite as
an outstanding check. Record the exact commands and results that ran; an earlier
run proves only the code and environment it exercised.

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

## Select suites from affected inputs

When broad verification repeatedly runs unaffected checks, separate suites by
the boundary each proves. Give each a command, inputs, prerequisites and a
coverage verdict. Reuse these commands in the full gate and the selected route
so their check lists cannot drift. Keep a full route available.

The repository owns a compact map from changed paths to suites, including shared
contracts, generators, fixtures, configuration and dependencies between suites.
Select the union of affected suites and their dependencies from the change
actually being integrated: after rebase or merge, against the intended base.
Consider both sides of renames and deleted paths. Extension alone is insufficient:
a Markdown file consumed by code can affect code tests, while ordinary prose
may need only document checks.

Run checks that apply to every change in either route. Use full verification for
unclassified paths and changes to the selection machinery; refuse an invalid map
instead of silently omitting checks. Test representative docs-only, code,
shared-contract, mixed, rename and fallback selections, including that a failed
selected check blocks integration. Revisit the map when inputs or suites change.

This pattern needs identifiable input boundaries. When dependencies are unclear,
keep the broader check until the scope can be established. A path map does not
prove coverage by itself or replace independent expectations in tests. Avoid
introducing a selection framework for a small, cheap suite with no measured
omission or setup problem.

## Keep feedback and completion distinct

Use a focused subset during implementation and name it as such. A complete
verification claim lists the required tiers, commands, environment and any
unrun checks. Do not make a fast subset look like a complete gate by giving both
the same verdict. Broaden checks when the change crosses a boundary or a focused
run reveals a concrete unresolved risk; stop repeating unaffected tiers once
the required evidence is in hand.

When the selected evidence requires writing a test, use the `test-writing`
skill. For weak assertions, mock drift or missing cases in a settled suite, use
the `test-audit` skill. Load those skills only when the requested work reaches
their task.
