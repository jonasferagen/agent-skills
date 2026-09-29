# Testing principles

Universal testing advice, independent of runner, framework, or project layout —
the standard [`test-audit`](../SKILL.md)'s lenses judge against, and the one to
apply when writing tests rather than auditing them. For runner specifics and
commands, see the owning repository's own testing guide.

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

## The decision layer is the layer worth testing

Most systems have an outer layer that adapts — a CLI entry point, an HTTP
controller, a queue consumer, an event handler — and an inner layer that decides.
**The inner layer is where the tests belong**, and it is where coverage should
come from.

The outer layer's job is parsing inputs, choosing a mode, rendering output, and
returning a status. That work is mostly the framework's, and **testing it tests
the framework**: that the router routes, that the CLI parses a flag, that the
container injects. The framework's own suite already proves those, and a test
that re-proves them is slow, wide, and pins nothing you own.

So the split is a design obligation before it is a testing one:

- **Keep the adapter thin enough to be uninteresting.** If the entry point holds
  the decisions, there is no inner layer to test, and the only way to reach the
  logic is through the whole stack. That is a structural defect surfacing as a
  testing problem — the fix is extraction, not a bigger integration test.
- **Extract so the logic takes plain inputs and returns plain results.** Pure
  functions, value objects, and injected collaborators are what make the decision
  layer reachable without booting anything.
- **Aim coverage at that layer deliberately.** When a branch is only reachable
  through the full stack, that is the signal it is in the wrong place.

**Integration tests are a second, thinner layer, and they are not the coverage
vehicle.** One per entry point is usually right: it proves the wiring — that the
adapter reaches the logic, passes the parsed inputs, and maps the result to the
right status or response. It does not re-prove the rule matrix the inner layer
already owns. Full integration coverage is a cost paid per case forever, in
runtime and in fixtures, for evidence a unit test gives more precisely.

**A rule matrix proved twice is worse than proved once.** The duplicate is slower,
it fails in pairs so a real regression reads as two failures, and the two copies
drift until one is quietly wrong. When the inner layer owns a rule, the
integration test asserts that the rule *ran*, not what it concluded.

The reverse failure is real too: an integration suite is not a licence for an
untested inner layer. Wiring proved and decisions unproved leaves a suite whose
green measured none of the rules it claims to protect — a defect in the evidence,
not coverage.

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

**A double cannot falsify the request you make of it.** Drift is the double
becoming wrong; this is the double never having been independently right. Whatever
the code asks — a label name, a `--format` template, a flag, a response field, an
expected exit code — the fake answers in the shape it was written to answer, and
agrees. So the request is the one part such a suite structurally cannot check, and
no number of cases changes that: they all ask the same wrong question.

Two things contain it, and the first matters more because it survives being
forgotten:

- **Design so nothing load-bearing depends on the guessable name.** Key the
  behavior on something that cannot be absent, and let the guessable field
  decorate the diagnosis. A wrong name then degrades a message instead of
  inverting an answer.
- **Read the answer off the real system once, and pin what you observed.** The
  suite is the regression net. It is not evidence that the first observation was
  right, and treating a green run as that evidence is the mistake.

Watch for the consequence as well as the cause: a request that is wrong usually
produces a degenerate value — an empty field, a missing key — which a fixture
that only builds well-formed input can never express. That is the *helpers that
cannot express absence* smell arriving from upstream, and fixing only the fixture
leaves the wrong question being asked.

**Configure the no-leak guarantee at the runner; do not ask every file to
remember it.** Where the runner can reset mock state itself, turn that on and
delete the per-file boilerplate. **A rule each new test file has to opt into is a
rule that decays.** Per-file cleanup then earns its place only where the
runner's setting genuinely does not reach — restoring a replaced implementation,
unstubbing environment variables.

## Keep tests deterministic

- No network calls.
- No dependence on wall-clock timing.
- No random values without fixed seeds.
- Prefer in-memory fixtures over real filesystem reads where feasible.

Non-deterministic tests either flake or silently mask regressions. Neither is
acceptable.

## Run the mechanical check

Much of the advice above is greppable, and a scanner can grep it — the untested
sibling, the parked test, the wall-clock call, the stub forced past the type
system, the focused-test marker. Run it over what you touched instead of
re-reading for these by eye.

**Two tiers, carrying different authority:**

- **Hard** — a **focused-test marker** (`.only`, `fit`, `fdescribe`, and
  equivalents) silently disables every sibling test in its file, so the suite
  reports green over a denominator it never names. That is a defect in the check
  rather than a preference, and it is the one finding worth failing on.
- **Advisory** — everything else. These are **candidates for a human read, not a
  punch list.** A scanner can find an untested sibling but cannot tell a real gap
  from a pure pass-through; it can find a call-count assertion but cannot tell a
  boundary contract from implementation coupling. Read the count as drift against
  the last audit, not as a defect total. **A healthy suite does not score zero.**

**A mechanical check that cries wolf gets muted**, so keep the hard tier small
enough to stay obeyed and leave the judgment calls advisory.
