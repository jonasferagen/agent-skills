---
name: test-audit
description: "Audit existing tests for brittleness, coverage asymmetry, mock drift, weak assertions, fixture bloat, non-determinism, focused or skipped cases and untraced requirements. Use when asking whether a settled suite actually protects behavior: a suite that has never failed, a green run after a risky refactor, a doubled collaborator nothing has checked against the real thing, a snapshot or no-throw standing in for an assertion, a focused-test marker, or a source file with no test beside its tested siblings. Reach for it when coverage is high and confidence is not. Audits settled tests; a change under review is a different pass."
metadata:
  version: "0.2.0"
---

# Test Audit

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
prominently and remove it only with user approval. Writing tests for discovered
gaps is follow-up work, not part of the audit.

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

**Audit and timing runs use the complete suite** (the full lane, not a fast
subset), so their results describe the selected surface. Many repositories keep
a fail-fast or fast-subset lane for the edit loop: it stops early or excludes
tests by design, so a verdict from it does not name the denominator it measured.
Such a lane is **non-certifying and must never be reported as complete
coverage** or as a verification result. Where such a lane lists its members
explicitly, treat membership as a performance classification, not a coverage
exception: the full lane must still select every listed test. Where the
reading project's own policy states when a verdict must name what it measured,
that policy governs.

## Workflow

1. **Establish scope and read its rules.**

   ```bash
   git status --short --untracked-files=all
   find <scope> -name AGENTS.md -print
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
   - **Unfalsifiable requests:** a double answers whatever the code asks it, so
     the request — label and field names, format templates, flags, expected exit
     codes — is unverified by every suite built on that double. Ask what the code
     *claims about an external contract*, and whether anything has ever checked
     that claim against the real thing. This is not drift: there was nothing to
     drift from. See [references/principles.md](references/principles.md#mocking).
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
smallest useful fix. Include an asymmetry map, intentional thin tests with their
rationale, the commands run and their caveats, and any verified stale-prose
cleanup.
