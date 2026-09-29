# Testing Conventions

## Contents

- [File naming](#file-naming)
- [Port, fixture, or justified cast](#choose-a-port-fixture-or-justified-cast)
- [Fixture ownership](#fixture-ownership-and-location)
- [Coverage expectations](#coverage-expectations)
- [Boundary completeness](#boundary-completeness-ratchets)
- [Mechanical checks](#mechanical-checks)
- [Test structure and assertions](#structure-and-assertions)

Repository-owned docs define the runner, environment, setup files, coverage
commands, and integration lanes. This page owns the transferable shape of a
TypeScript test: where it lives, what kind of double it uses, and what evidence
counts.

## File Naming

- Name tests `*.test.ts` or `*.test.tsx` and colocate them with the production
  unit when the repository supports colocation.
- Fixture modules are the test-only exception to class-per-operation naming.
  Use `camelCase.ts`, export plain `make*` functions, and keep runner imports out
  of them.
- Promote fixtures into a package-local `testing/` surface only after multiple
  tests need the same domain value. Keep one-test fixtures local.
- Add a `testing/` barrel only when the directory is a real shared surface, not
  as folder paperwork.

## Choose A Port, Fixture, Or Justified Cast

A test-side `as unknown as X` or `as any` suppresses the check that keeps a stub
aligned with production use. Classify the cast before changing production.

| Situation                                                     | Response                                                          |
| ------------------------------------------------------------- | ----------------------------------------------------------------- |
| The test reaches through privacy                              | Assert observable behavior or add an honest public projection     |
| The target is an opaque browser, platform, or vendor conduit  | Keep one narrowly scoped cast and explain the external constraint |
| The owning package publishes a factory for the domain value   | Use or extend that fixture                                        |
| The consumer accepts a concrete class but uses a stable slice | Add a production [dependency port](dependency-ports.md)           |
| The test deliberately supplies malformed parser input         | Cast at the parser boundary and assert rejection                  |

Prefer this order for ordinary collaborators:

1. **Port** — narrow the dependency to the complete downstream capability it
   needs. A checked literal then stays aligned with production.
2. **Fixture** — build real domain data through the owning package's factory.
   Do not reproduce a rich object as a bag of mocked methods.
3. **Cast** — reserve it for deliberately invalid input or an external conduit
   whose runtime surface cannot be represented economically.

Private reach-in is a test-design defect, not a missing port. Conversely, do
not add a false abstraction when production genuinely needs the concrete
dependency; a justified boundary cast is safer.

## Fixture Ownership And Location

The package that defines a domain type owns its fixture factory. A fixture may
import production code but must not import the test runner, so consumers can use
it under any supported runner.

- Derive the override type from the production type where practical, so a new
  field does not leave the factory behind.
- Let fixtures express absent and empty states. A factory that always populates
  every optional deletes fallback and rejection lanes from the suite.
- Extend the canonical fixture when it is almost sufficient. Do not create a
  near-copy beside each consumer because the override surface was one field too
  narrow.
- Keep browser/platform doubles in test infrastructure only when no production
  domain owns them. Domain fixtures stay with their domain.

## Coverage Expectations

Test observable contracts: successful behavior, edge conditions, and rejection
paths. A missing sibling test is a candidate, not a verdict, and a basename
match is not coverage. Classify each candidate with
[coverage-gap classification](test-gap-classification.md), which owns the
buckets — including the one that stays unclassified — the evidence each
requires, and the false positives that name a unit without executing it.

## Boundary-Completeness Ratchets

A hand-written boundary can silently drop a new field while ordinary fixtures
stay green. Add a completeness ratchet when code copies a wire/schema contract
field by field, deliberately supports a subset, or owes one explicit decision
per contract member.

- Derive the inventory from the owning type or runtime schema. Do not maintain
  an unrelated test-only field list.
- Prefer `satisfies Record<keyof Contract, Decision>` when every field needs a
  policy decision.
- When a runtime schema can drive the transformation, consume it directly.
- To prove survival through several transformations, use a complete source
  fixture plus one named far-end probe per contract member. Counts and
  existence checks cannot say which field disappeared.
- For intentionally partial support, classify every member with an explicit
  decision such as `modeled`, `passthrough`, or `unsupported`.

Use `selfcheck-guard` before turning a completeness check into a gate. A guard
that inventories current files or fields independently of the owner will rot on
the first structural change.

## Mechanical Checks

Search touched tests for focused markers, skipped cases, unpaired temporary
resources, cast-shaped stubs, ambient time/randomness, real delays, and
call-count assertions. The hard/advisory split — a focused marker fails,
everything else is a candidate for a human read — is the upstream
`test-audit` skill's mechanical-check rule;
the notes below are TypeScript-specific readings of its advisory tier.

- A stale exemption should be reported so the ledger shrinks; line numbers are
  too unstable to be exemption keys.
- An exact-float matcher is not automatically wrong: exact equality is correct
  for a carried literal and suspicious for computed output.
- A call-count assertion may pin a real boundary (`dispose`, dispatch) or an
  implementation detail. The scanner cannot decide which.

Use the repository's own scanner and ledger when it has them. Shared method
must not hardcode product paths, runner configuration, or the current exception
inventory.

## Structure And Assertions

- Group by unit or module and write concise test names that state observable
  behavior.
- Keep a named reference to each mock function a test asserts against. If a
  mock object is typed as an interface, build the mocks first, assign them, and
  assert against the original references.
- Let repository runner configuration own automatic mock clearing. Add local
  restoration only when a test replaces an implementation or environment value
  that the global configuration does not restore.
- Build branded IDs and other validated values through their production
  boundary or fixture helper rather than assigning raw primitives.
- For event-driven code, prove both halves: the emitted payload and the
  consumer's reaction.
- Drive clocks, animation frames, retries, and loops through controlled seams.
  Waiting on real time is nondeterministic and encodes scheduler behavior the
  contract did not promise.
