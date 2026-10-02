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
first. They decide the framework, the layers, the commands, the naming and what
the project tests thinly on purpose. Where that guidance contradicts this
package, follow the repository and report both passages to the user.

## Workflow

<!-- Package-boundary copy: runtime-operations/SKILL.md (Verification) states the denominator rule behind step 7. Keep both passages aligned. -->
1. **State the claim.** Say in one sentence what behavior the test protects
   and which failure would disprove it. A test whose failure you cannot name is
   not ready to be written. Whether a change needs a test at all, and at which
   layer, is a question of evidence. Settle that first; this skill starts once
   a test is to be written.
2. **Open the references the work needs,** from the table below: the one for
   your kind of test, and fixtures. Do this now, before you read the project's
   data.
3. **Locate the real data before you write a value.** Real data is any record
   of real people, accounts or business: a data directory, a dump, a log, the
   output of a tool run over those. A value quoted in the request counts as
   real too, unless you know it was made up. Read real data to learn the shape
   of the input. Copy nothing from it: no number, name, address or phrase, and
   no part of one. A value made by trimming a real one or changing a digit
   still carries it, and so does a file name built around a real name. This
   holds for tests, fixtures, test names, comments and assertion messages.
4. **Write the test** by the rules below.
5. **See it fail.** A test that has never failed has not shown that it can.
   Run the new test against the code without the change, or against a
   temporary copy with the behavior broken, and check that it fails for the
   reason you named. If you could not, say so in the report.
6. **Check for copied values.** If real data was within reach, check every
   file you added or changed before you report. That means the tests,
   fixtures and helpers, and also production code, docstrings, comments and
   documentation, where copied values end up too. `git status --short` lists
   them. Run the bundled [copiedValues.py](scripts/copiedValues.py) on them
   from the repository root:

   ```sh
   python3 <this skill's directory>/scripts/copiedValues.py --private <path to the real data> --term "<a name you saw there>" <the files you added or changed>
   ```

   Repeat `--term` for each name you saw, and add `--allow-file` with the
   project's allow file if it keeps one. The check reports the file and line
   of each number of six or more digits and each mail address that also
   occurs in the real data, whole or as part of a longer number, and of each
   name you listed. It never prints the value, and it does not see free text, so
   read what you wrote for phrases too.

   A finding in a file you created, or on a line that `git diff` shows you
   added, is yours. Replace each of yours with a made-up value and run the
   check again, until no finding of yours is left. A finding on a line you
   did not write was there before you: report it and leave it to the
   project. Only exit status 0 is a pass. Status 2 means the real data was
   not found, and 3 that the check could not run. If the project has a test
   that runs the check, run that test too. Without Python 3, search the files
   you changed for each identifier you saw in the real data.
7. **Report what ran:** the command, how many tests ran and how many were
   skipped. A run that skipped tests, or ran a chosen subset, is a partial
   result. Say so instead of reporting it as passed.

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
  and anything else that varies. Use no network, no sleeps and no dependence on
  the order of tests.
- **Made-up data only.** When the shape of a real value matters, make up a
  value with that shape: the same length and kind of characters, different
  content.
- **Own your state.** Create what the test needs in a place no other test
  uses, and remove it afterwards. Depend on nothing another test left behind.

## When a test is hard to write

Awkward setup usually describes the production code: a decision buried behind
I/O, a dependency that cannot be replaced, one function doing several jobs.
Report that as a finding about the code. Do not hide it under elaborate test
machinery, and do not restructure production code beyond the task without
asking.

## Scope

This skill covers writing tests and their fixtures. It does not choose which
checks a change or a milestone needs, audit a suite that is already settled,
pick a framework or set a coverage threshold.
