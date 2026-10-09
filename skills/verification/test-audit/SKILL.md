---
name: test-audit
description: "Audit a settled test suite for weak assertions, gaps, brittle cases, mock drift, non-determinism and misleading coverage claims. Use when asking whether existing tests actually protect behavior; choosing evidence for an active change is a separate task."
metadata:
  version: "0.3.3"
---

# Test audit

<!-- Package-boundary copy: test-writing/SKILL.md opens with the same repository authority rule. Keep both aligned. -->
**Local docs own the testing standard; this package supplies the lenses.** The
standard covers which frameworks, layers and commands a repository uses, and
what it has decided to test thinly on purpose. Read the nearest
agent-instruction file and the repository's own testing guidance first. If that
guidance contradicts a lens here, judge against the guidance. Report the
contradiction to the user as documentation drift, quoting both passages, and
edit neither side. Do not use it as permission to pick the easier rule.

Assess whether settled tests protect behavior or are thin, brittle, redundant,
flaky, or silently missing.

**Stay read-only** for tests, fixtures, and production code unless the user asks
for edits. When the work already authorizes repository edits, repair stale prose
that the audit surfaces where the fix is mechanical, such as a renamed path or
command. **A focused-test marker is a hard finding:** it silently skips every
unfocused test in its scope (its file in some runners, the whole run in others),
so the suite can still report green over a denominator it never names. Report it
prominently and remove it only when the user's request authorizes test edits.
Writing tests for discovered gaps is follow-up work; use the `test-writing`
skill when that work is authorized.

Three neighbouring passes are not this one. Tests inside a change under review
belong to that review. A finding whose subject is the production contract behind
an awkward test, rather than the test itself, is an architecture finding. Whether
a custom check or gate survives structural change is its own question. Hand those
on rather than settling them here.

## Authority and modes

- **Default / suite** mode, for a package or directory: map source-to-test
  asymmetry, scan cross-cutting smells, then inspect representative files.
- **Focused** mode, for one test file, unit, or small related set: start from its
  assertions and observable contract, then expand only to public API, peers, and
  traced requirements.

An audit can inspect files without running the suite. If it reports suite timing
or complete coverage, run the complete selected suite and name what it measured.
A fail-fast run that stops early or a fast subset leaves tests unrun; report its
result as partial feedback, not as complete verification. The reading project's
own policy decides which runs are required for a change or release.
When a fast lane lists its members, the full lane must still select every
listed test; membership is a performance classification, not a coverage exception.
Use the `verification-design` skill when the task asks which checks an active
change needs.

## Workflow

1. **Establish scope and read its rules.**

   ```bash
   git status --short --untracked-files=all
   find <scope> -name '<agent-instruction-file>' -print
   ```

2. **Run the repository's own test scanner, and its report of source files
   without tests**, if it has them. This skill carries no scanner. Which
   scanner signals are worth having, and how to read the output, are in
   [references/triage.md](references/triage.md#reading-a-test-scanner).

   **Scanner output is a set of signals to weigh, not findings in itself.**
   A focused-test marker is the one hard failure; gaps, skip markers, casts,
   determinism patterns, mocks, and call-count assertions are advisory
   candidates.

   **Where the test tree is not colocated with production code** — a separate
   `tests/` tree, common in service frameworks — a scanner cannot infer coverage
   asymmetry. Trace production classes and endpoints into the test tree by name
   instead. A public operation with no test, and a peer family with one untested
   sibling, are candidate gaps; pass-throughs, type-only modules, framework
   scaffolding, fixtures, and integration-covered contracts may be intentional.

3. **Read representative tests against these lenses.** The standard they encode
   is in [references/principles.md](references/principles.md): structure,
   behavior-over-implementation, edge cases, mocking, determinism, and the two
   tiers of mechanical check. Read it when a judgment call needs the full rule
   rather than the headline.

   - **Behavior:** observable output or state, instead of private fields,
     incidental calls, or implementation order.
   - **Assertion strength:** the test can actually fail for the promised
     behavior. A 200, a no-throw, or a broad snapshot is not automatically
     sufficient.
   - **Edges:** empty, boundary, rejection, validation, and error paths.
   - **Mocks:** only at real boundaries; faithful types and signatures; reset
     between tests.
   - **Cast-shaped stubs:** verify the collaborator methods actually used against
     the stub members supplied. **A mismatch can hide a live branch defect** —
     this is correctness evidence, not style noise. Triage in
     [references/triage.md](references/triage.md#cast-shaped-stub-triage).
   - **Unverified external contracts:** a strict double can reject a request that
     differs from its programmed expectation. It cannot establish whether that
     expectation matches the real system's fields, flags, format or exit codes.
     Ask where the expectation came from and what independently checked it.
     When it was never checked, distinguish that missing evidence from later
     drift. See [references/principles.md](references/principles.md#mocking).
   - **Fixtures:** prefer fixture factories from the package that owns the
     type, and branded values; flag duplication, over-building, inaccessible
     existing fixtures, and helpers that cannot express absence.
   - **Determinism:** wall clock, unseeded randomness, network, sleeps, and real
     filesystem dependencies.
   - **Traceability:** one observable behavior per test, and visible requirement
     links where the repository traces requirements.

4. **Treat awkward test construction caused by a production contract as a
   finding about that contract**, not about the test. Do not hide it with
   workarounds in the test: convoluted test construction usually signals a
   design problem.

## Classification and output

Classify findings as **Quick win**, **Coverage gap**, **Brittleness**,
**Determinism risk**, **Production smell**, **Keep intentionally**, or **No
evidence yet**.

Lead with the highest-signal findings. For each give the path, the concrete
smell, the failure it permits or the refactor it blocks, the evidence, and the
smallest useful fix. For a suite audit, include the source-to-test asymmetry map;
for a focused audit, include only relevant gaps and peers. Record intentional
thin tests with their rationale, the commands run and their caveats, and any
verified stale-prose cleanup.
