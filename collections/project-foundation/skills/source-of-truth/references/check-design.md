# Designing a consistency check

## Keep the check durable

The check added at rung 5 can itself become a restatement if it hard-codes the
structure it checks. A durable check must:

- Protect a named consequence at a cost proportionate to that consequence.
- For parity between current owners, compute its answer when it runs instead of
  comparing with a committed baseline, or "golden", that copies structural facts.
- Read each structural fact from the home that declares it.
- Resolve its location from its own file or module.
- Use tests that create their own fixtures.
- Fail only when the homes disagree.

A check built this way survives the next restructure without changes.

A selected artifact's identity is a different invariant: which exact files and
bytes were reviewed for that revision? A release manifest or hash inventory can
record that selection and compare a staged installation with the trusted source.
It does not replace a live parity check between current owners or prove behavior.
See [artifact identity](durable-checks.md#compute-the-invariant-live) for that boundary.

Hard-coded directory sets, member lists and expected counts copy facts that
already have a home. Failures caused by an absent tool can create the same
problem: the check fails because the environment changed, even though the homes
still agree. Updating the copied literal and approving a new baseline then
becomes routine. That routine teaches reviewers to approve diffs they have not
read.

<!-- Package-boundary copy: test-audit/references/triage.md applies the report-only rule below to scanner drift stamps. Keep both passages aligned. -->
| Ask of the check | If yes |
| --- | --- |
| Is it missing a concrete consequence to protect? | do not add the check until you can name that consequence concretely |
| Is there cheaper evidence that observes the same consequence? | use that evidence instead |
| Can it fail for a change that cannot affect that consequence? | narrow the trigger, or explain why using that change as a proxy costs less than a missed defect |
| Does it hold a name, a list or a count that also lives in the home? | read the home instead: that is rung 1 applied to the check |
| Would it break if a directory moved, or if an optional component were absent? | resolve paths from its own location and make its tests create their fixtures |
| Does it fail when a tool or service is missing, rather than when the homes disagree? | fail at the boundary where the environment contract requires that dependency; if no contract requires it, skip with a prominent notice |
| Does it only produce a report, with nothing consuming that report? | make it check an invariant using current facts and fail a real gate, or remove it |

[Checks that survive restructuring](durable-checks.md) states
requirements two to six as five properties, with examples of checks that violate
and satisfy each. Read it while writing the check. The project's own policy
decides whether a check is worth its recurring cost; these requirements keep a
retained check working as the project changes.
