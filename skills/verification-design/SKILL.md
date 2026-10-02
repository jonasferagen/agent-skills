---
name: verification-design
description: "Choose proportionate checks for a change or milestone and consolidate overlapping validation by the failure each check can detect. Use when deciding which test layers to run, what evidence a claim needs, or whether repeated suites and setup can be combined."
metadata:
  version: "0.1.0"
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

## Keep feedback and completion distinct

Use a focused subset during implementation and name it as such. A complete
verification claim lists the required tiers, commands, environment and any
unrun checks. Do not make a fast subset look like a complete gate by giving both
the same verdict. Broaden checks when the change crosses a boundary or a focused
run reveals a concrete unresolved risk; stop repeating unaffected tiers once
the required evidence is in hand.

This skill designs evidence for active work. An audit of whether a settled suite
has weak assertions, mock drift or missing cases is a separate activity.
