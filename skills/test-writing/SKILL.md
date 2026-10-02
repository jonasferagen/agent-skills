---
name: test-writing
description: "Write or change unit tests, integration tests and the fixtures they use. Use whenever a test, a test helper, a fixture or any example input is added or edited, especially with real records at hand; choosing which checks a change needs and auditing a settled suite are separate tasks."
metadata:
  version: "0.1.0"
---

# Test writing

A test is evidence. It earns its place when it can fail for the behavior it
names, gives the same result on every run, and carries nothing that should stay
out of the repository.

<!-- Package-boundary copy: test-audit/SKILL.md opens with the same repository authority rule. Keep both aligned. -->
**Local docs own the testing standard; this package supplies the method.** Read
the nearest agent-instruction file and the repository's own testing guidance
first. They decide the framework, the layers, the commands, the naming, the
checks a test change must pass and what the project tests thinly on purpose.
Where that guidance contradicts this package, follow the repository. Report the
contradiction to the user, quoting both passages, and edit neither side. Do not
use it as permission to pick the easier rule.

## Workflow

<!-- Package-boundary copy: verification-design/SKILL.md (Match each claim to an observable boundary) states the rule behind step 1. Keep both passages aligned. -->
<!-- Package-boundary copy: runtime-operations/SKILL.md (Verification) states the denominator rule behind step 6. Keep both passages aligned. -->
1. **State the claim.** Say in one sentence what behavior the test protects
   and which failure would disprove it. A test whose failure you cannot name is
   not ready to be written. Whether a change needs a test at all, and at which
   layer, is a question of evidence. Settle that first; this skill starts once
   a test is to be written.
2. **Open the references the work needs,** from the table below: the one for
   your kind of test, and fixtures. Do this before you look at real records.
3. **Make up every value.** Real records show the shape of the input: a data
   directory, a dump, a log, the output of a tool run over those, and a value
   quoted in the request unless you know it was made up. Read them only where
   the project allows it. Copy nothing from them into a test, a fixture, a
   test name, a comment or an assertion message: no number, name, address or
   phrase, and no part of one. A value made by trimming a real one or changing
   a digit still carries it, and so does a file name built around a real name.
   Values that are public, or that the code itself fixes, such as a provider's
   name that a rule matches, may stay as they are. The project's policy
   decides what is private. Where it is silent, treat anything that identifies
   a person, an account, a contract or a payment as private, and ask.
   [Fixtures](references/fixtures.md#make-up-every-value) shows how to make up
   a value of the same shape.
4. **Write the test** by the rules below.
5. **See it fail.** A test that has never failed has not shown that it can.
   Run the new or changed test against the code without the change, or
   against a temporary copy with the behavior broken, and check that it fails
   for the reason you named. If you could not, say so in the report.
6. **Run the project's checks and report what ran.** Run the tests and any
   check the project's testing guide names for test changes, such as a check
   for values copied from real data. Report each command, how many tests ran
   and how many were skipped. A run that skipped tests, or ran a chosen subset,
   is a partial result. Say so instead of reporting it as passed. When no test
   ran at all, the honest report is a refusal, not a pass.

## Start by task

| You are about to | Read |
| --- | --- |
| Test a rule, a calculation, a parser or a decision that can run in memory | [Unit tests](references/unit-tests.md) |
| Test what crosses a boundary: files, a database, a process, a service, a built artifact, or the contract between two components | [Integration tests](references/integration-tests.md) |
| Write any input a test supplies: a value, a record, a message, a file, a directory tree, or a helper that builds one | [Fixtures](references/fixtures.md) |

Most work needs two of these: the kind of test, and fixtures.

## Rules for every test

- **One behavior per test, named for that behavior.** A failure then says what
  broke before anyone reads the body.
- **Assert what an outsider can observe:** a returned value, stored state, a
  file, a response, a message sent. Private fields, incidental calls and
  internal order can change while the behavior stays correct.
- **Same result on every run.** Pass in the clock, the random seed, the locale
  and anything else that varies. Use no sleeps and no dependence on the order
  of tests. Reach no service from outside the test; one the test starts for
  itself, such as a disposable database, is part of the test.
- **Made-up data only.** When the shape of a real value matters, make up a
  value with that shape: the same length and kind of characters, different
  content. Public values and values the code itself fixes are the exception
  that step 3 names.
- **Own your state.** Create what the test changes in a place no other test
  uses, and remove it afterwards. Tests may share what none of them changes,
  such as a read-only fixture built once. Depend on nothing another test left
  behind.

## When a test is hard to write

Awkward setup usually describes the production code: a decision buried behind
I/O, a dependency that cannot be replaced, one function doing several jobs.
Report that as a finding about the code. Do not hide it under elaborate test
machinery, and do not restructure production code beyond the task without
asking.

## Scope

This skill covers writing tests and their fixtures. It does not choose which
checks a change or a milestone needs, audit a suite that is already settled,
pick a framework or set a coverage threshold. It supplies no check for copied
values: a project that keeps real data at hand owns one, and the fixtures
reference says what it needs.
