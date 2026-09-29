# Test Audit — Triage Reference

Load this only when scanner mechanics, cast-shaped stubs, or coverage are
relevant to the audit.

## Reading a test scanner

This skill carries no scanner. Where the repository provides one, these are the
signals worth having and how to weigh them.

**What a useful scanner reports:**

- **Colocated source/test asymmetry** — production files with no neighbouring
  test. Only meaningful where tests are colocated; see below.
- **Focused and parked markers** — the disabling footgun. These are the one class
  worth failing a gate over, because a focused marker silently shrinks the suite
  to a single case while still reporting green.
- **Cast-shaped stubs, determinism patterns, mock candidates, and call-count
  assertions** — advisory. Each is a prompt to read the test, not a verdict.

**What it cannot do:** infer coverage asymmetry when the production and test
trees are separate. Trace those by class or endpoint name instead.

**A scanner's exemption ledger, and any drift stamp it carries, are judged as a
check in their own right, not as test coverage.** A ledger lists files
grandfathered out of a settled convention, and it may only shrink: a new or
increased violation fails. A report-only drift *stamp* — a frozen snapshot the scanner
diffs against, with no consumer acting on the diff — is that anti-pattern
exactly: run the scanner against the live tree instead.

## Cast-shaped stub triage

An `as unknown as X`-style cast usually means the consumer accepts a concrete
class while using only a narrow slice of it.

**First list the collaborator members the consumer actually calls, then compare
the stub.** Missing members can reveal a branch the test never executes — which
makes this correctness evidence rather than style noise.

Count casts **by target type**, not only by file:

```bash
rg -o 'as unknown as [A-Za-z_]\w*' <scope> | sort | uniq -c
```

Repeated casts to one type usually indicate **one missing port**. The
`typescript-patterns` skill's testing conventions own the port → fixture →
justified-cast order and when a port is the wrong answer; apply that order here.
For a class with a private constructor, use a narrow structural port over the
methods in use, or build the real object and spy on it.

Before declaring a fixture absent, **inspect what the owning package already
exports** — the actual gap is often an override surface that cannot express a
needed or absent state, not a missing fixture.

## Optional coverage

Use coverage **only to locate untested branches, never as a target number.** Run
it through the repository's own test runner, scoped to the surface under audit.

Run it on the complete suite: a fail-fast or fast-subset lane is non-certifying
under the audit-run rule in [SKILL.md](../SKILL.md), so it can report only a
partial run.
