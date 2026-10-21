# Test Audit — Triage Reference

Load this only when scanner mechanics, cast-shaped stubs, or coverage are
relevant to the audit.

## Reading a test scanner

This skill carries no scanner. Where the repository provides one, these are the
signals worth having and how to weigh them.

**What a useful scanner reports:**

- **Colocated source/test asymmetry** — production files with no neighbouring
  test. Only meaningful where tests are colocated; see below.
- **Focused-test markers** — markers that confine the run to the focused tests.
  These are the one class worth failing a gate over, because a focused marker
  silently skips every unfocused test in its scope (its file in some runners,
  the whole run in others) while the run can still report green.
- **Skip markers, cast-shaped stubs, determinism patterns, mock candidates, and
  call-count assertions** — advisory. Each is a prompt to read the test, not a
  verdict. A runner still counts a skipped test in its summary, so a skip marker
  does not hide the denominator.

**What it cannot do:** infer coverage asymmetry when the production and test
trees are separate. Trace those by class or endpoint name instead.

**A scanner's exemption list, and any baseline snapshot it carries, are judged as
a check in their own right, not as test coverage.** An exemption list names files
that predate a convention and are exempt from it (for example, "these legacy
test files may still use the old mocking helper"); it may only shrink, so a new or
increased violation fails. A baseline snapshot is a frozen count or file list the
scanner diffs against with nothing acting on the diff; such a report-only check
is an anti-pattern. Run the scanner against the live tree instead.

## Cast-shaped stub triage

A stub forced to a type it does not fully implement (in TypeScript, an
`as unknown as X` cast; in other languages, a partial fake passed where a full
interface is declared) usually means the consumer accepts a concrete class while
using only a narrow slice of it.

**First list the collaborator members the consumer actually calls, then compare
the stub.** Missing members can reveal a branch the test never executes — which
makes this correctness evidence rather than style noise.

Count casts **by target type**, not only by file; for TypeScript:

```bash
rg -o 'as unknown as [A-Za-z_]\w*' <scope> | sort | uniq -c
```

Repeated casts to one type can indicate **one missing port** (a narrow
interface declaring only the members the consumer uses). Check whether the
package that defines the type already exports a fixture whose overrides can
express the needed or absent states, then inspect the consumer's actual
dependency contract. A narrow structural port fits when the consumer needs only
those methods and no hidden lifetime or identity guarantee. Otherwise use a real object or a justified
local cast. Do not widen the production contract just to make a stub compile.

## Optional coverage

Use coverage to locate untested branches, rather than inventing a target number.
Preserve any threshold the repository already requires. Run through its own test
runner; a complete coverage claim needs the complete selected suite (every
test the repository's test command would run for the scope under audit). A
fail-fast run that stops early or a fast subset reports only partial coverage
under the run rule in [SKILL.md](../SKILL.md).

Scope the coverage report to the surface under audit, not the test selection. A
test elsewhere, such as an integration test, may cover that surface.
