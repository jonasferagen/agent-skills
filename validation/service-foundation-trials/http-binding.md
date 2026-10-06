# HTTP binding trial — 2026-10-07

Fresh-context trial for revision 0.7.0, which delegated the generic adoption
contract to the project system and documented the helper binding surface. The
fixture was a consumer whose adoption was **already declared** in its own
agreements, holding one existing service, and the task was to define a second
one with HTTP readiness. Primary held both an installed service-foundation and an
installed project-foundation, so the delegated contract was reachable. Nothing
was installed, started or enabled.

## Result

Both changes did what they were meant to.

The binding surface was taken from the reference, not from source. The evaluator
read `references/runtime-helpers.md` as required and stated plainly that it did
not open `serviceControl.py`, `serviceHealth.py` or any other helper
implementation, because the field table was sufficient. The previous trial had
read 687 words of `serviceControl.py` to make the same decisions. It used the
table's omission column as intended, recording in the controller why
`environment`, `ready_seconds` and `before_start` were each left out, and it
reached the transient-versus-installed decision partly *from* the documented
consequence of setting `health_service` on an installed unit.

`references/extension.md` dropped from a required read that restated the adoption
contract to a useful one that confirmed adoption was already complete and that no
registry or manifest registration was needed. The generic contract was read once,
from project-foundation, where it now lives; the evaluator followed it to the
policy-change workflow and correctly declined to widen the adopted scope itself.

## Findings

- **The offered interface version was stated nowhere in prose.** The evaluator had
  to open `runtimeApi.py` to learn that `major=1` is the value to pin. The
  reference explained the semantics of both numbers and named the declaration as
  their owner, but a consumer needs the current value to write the call. Fixed in
  the same revision: the reference states the offered interface, and a collection
  test fails if that sentence and the declaration disagree.
- **`control`'s return convention was undocumented**, so the evaluator guessed a
  forwarding rule. Fixed: every action returns an exit status and reports failure
  by raising.
- **`command`'s shape was undocumented.** The evaluator inferred an argument
  vector from the runtime member's own rule, which was right. Fixed in the table.
- **Not a product defect:** the evaluator reported the relative-route rule as
  ambiguous, having found that `../primary` in the fixture's
  `project-docs/foundation.md` would resolve to a path that does not exist. The
  rule is correct and matches project-foundation's foundation format, which
  resolves a relative root against the declaring foundation's directory. The
  fixture declared the wrong route and the evaluator worked around it. No change
  was made; the fixture was repaired.

## Limits

One trial, one fixture, one task shape, exercising cold entry and deeper guidance
for a consumer with adoption already declared. The nearby-work and
source-authoring cases remain unexercised. The fixture's existing service carried
an `exit 0` controller, which the structural checker accepts and the evaluator
again identified as something the convention forbids shipping. Nothing changed
runtime state, so no control action, readiness result or recovery path is
evidenced; the service defined in the trial cannot start at all until its
application exists.
