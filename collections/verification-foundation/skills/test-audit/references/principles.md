# Testing principles

Testing lenses, independent of runner, framework, or project layout. Apply them
within the local testing standard described in [`test-audit`](../SKILL.md).
For runner specifics and commands, see the owning repository's own testing guide.

<!-- Package-boundary copy: test-writing/references/unit-tests.md and test-writing/references/integration-tests.md restate these rules for an author writing tests. Keep them aligned. -->
Tests are executable evidence: they prove **observable behavior and named
invariants**, not the implementation inventory the source already exposes.

## Test structure

- **Arrange** — set up data, mocks, and the system under test.
- **Act** — execute one behavior.
- **Assert** — verify user-observable output or state.

**One behavior per test.** If assertions span multiple behaviors, split the test.

## Prefer behavior over implementation

Assert against what a consumer of the code can observe — return values,
externally visible state, events emitted to known listeners. **Do not assert on
internal call counts, private fields, or implementation details** that could
change without affecting correctness.

Test public methods and exported functions, not private internals. Private
behavior is exercised transitively through the public API; testing it directly
couples the test to implementation details.

## Test decisions where they are made

Many systems have an outer adapter — a CLI entry point, HTTP controller or queue
consumer — and an inner layer that makes domain decisions. Test a rule's cases
close to that decision when the layer can be exercised directly. Keep adapters
thin so the rule does not require a full process for every branch. If awkward
tests can reach a decision only through the whole stack, inspect the production
boundary before adding more wide tests.

Integration tests answer questions the inner layer cannot: whether the adapter
passes the right input and identity, whether the real database grants access or
serializes writers, whether processes communicate, and whether a built artifact
starts. Keep tests for those distinct boundaries. Their number follows the
failure modes and the project's own gate, not an entry-point quota.

An integration test that repeats every case of a rule already proven at the
decision layer adds cost when it sees no new failure. Retain a representative
case showing the public path reaches the rule; keep additional cases when the
outer boundary can change the outcome. Conversely, public wiring cannot prove
an untested decision matrix. Compare the failure each test detects before
calling two assertions duplicates.

## Cover edge cases

For each behavior, consider empty inputs, boundary values (zero, one, maximum),
and error conditions. **The happy path alone rarely catches regressions** — most
real bugs live at the boundaries.

## Trace named requirements

When behavior has a named requirement, make the connection visible in the test
name, the fixture name, or a short comment.

## Mocking

- **Mock only external boundaries** — I/O, external processes, heavy dependencies
  that would make the test slow or non-deterministic.
- Keep pure logic — parsers, normalizers, validators, calculators — unmocked when
  practical.
- **Mock state must not leak between tests.**

The goal: a failing test points to a real regression, not to a mock drifting away
from the thing it stands in for.

**A double does not establish the real system's contract.** A strict fake can
reject a wrong field, flag or request relative to its expectation. If that
expectation was guessed, it may reject the right request or accept the wrong
one. This differs from drift: the expectation was never independently checked.

Check the expectation against an authoritative contract or a controlled
observation of the real system, within the task's permissions. Pin its source
and date when useful. The fake then protects the verified expectation against
regression; a green run alone does not verify the external contract. If the
evidence is unavailable, report that limit rather than silently reaching a live
service. Where a field is only diagnostic, keep core behavior independent of it;
where it is required by the contract, test its absence or failure explicitly.

Watch for the consequence as well as the cause: a request that is wrong usually
produces a degenerate value, such as an empty field or a missing key. A fixture
that only builds well-formed input can never express that value. That is the
*helpers that cannot express absence* smell with its cause upstream, in the
request, so fixing only the fixture leaves the wrong question being asked.

Prefer a runner setting that resets mock state when it covers the required
cleanup, rather than relying on every file to opt in. Per-file cleanup remains
necessary where the setting does not reach, such as restoring a replaced
implementation or environment variables. During an audit, report a missing
reset guarantee; change configuration or tests only within authorized edit scope.

## Keep tests deterministic

- Unit tests replace network dependencies. Integration tests may use a real
  network boundary when the claim requires it, with isolated resources and a
  bounded wait. Do not depend on an unrelated live service.
- No dependence on wall-clock timing.
- No random values without fixed seeds.
- Prefer in-memory fixtures over real filesystem reads where feasible.

Non-deterministic tests either flake or silently mask regressions. Neither is
acceptable.

## Run the mechanical check

Much of the advice above is greppable, and a scanner can grep it — the untested
sibling, the skipped test, the wall-clock call, the stub forced past the type
system, the focused-test marker. Run it over what you touched instead of
re-reading for these by eye.

**Two tiers, carrying different authority:**

- **Hard** — a **focused-test marker** (`.only`, `fit`, `fdescribe`, and
  equivalents) silently skips every unfocused test in its scope (its file in
  some runners, the whole run in others), so the suite can still report green
  over a denominator it never names. That is a defect in the check
  rather than a preference, and it is the one finding worth failing on.
- **Advisory** — everything else. These are **candidates for a human read, not a
  list of defects to fix.** A scanner can find an untested sibling but cannot
  tell a real gap from a pure pass-through; it can find a call-count assertion
  but cannot tell a boundary contract from implementation coupling. Read the
  count as drift against the last audit, not as a defect total. **A healthy
  suite does not score zero.**

**A mechanical check that raises false alarms gets muted**, so keep the hard
tier small enough to stay obeyed and leave the judgment calls advisory.
