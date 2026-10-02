# Unit tests

<!-- Package-boundary copy: test-audit/references/principles.md states these rules as the standard an audit judges against. Keep both aligned. -->
A unit test checks a decision where it is made: a rule, a calculation, a
parser, a state change. It runs in memory and shares nothing with other tests.
Use it for the cases of a rule. What happens when the rule meets a file, a
database or another process belongs to an [integration
test](integration-tests.md).

## Shape

Arrange the input, act once, assert the outcome. If a test needs a second
action to make its point, it is usually two tests. A test of repetition is the
exception, such as one that runs an import twice to show that the second run
changes nothing.

Name the test for the behavior and its condition, such as "rejects an order
without lines", in the form the repository already uses. Where a behavior has
a named requirement, make the link visible in the name or a short comment.

## Choose the cases

Work from the rule's branches, not from the lines of the code.

- The ordinary case.
- Each boundary: empty, zero, one, the largest allowed value, and the first
  value outside the range.
- Each rejection and error path. Assert the specific error, not only that
  something was raised.
- Absence and degenerate input: a missing field, an empty string, a null, the
  wrong type where the boundary lets it in.
- For a defect, the case that exposed it. The test fails without the fix, and
  its name or a comment says which defect it guards.

When one behavior varies only by input, state the cases as a table: a name, an
input and an expected outcome per row, run by one test body that reports each
case by name. Keep only rows you can explain. A case nobody can justify hides
the ones that matter.

Leave thin what is thin on purpose. Pass-throughs, type-only modules and
framework wiring gain little from a unit test.

## Assert the behavior

- Compare a specific outcome. "Returns the three parsed lines" can fail.
  "Returns something" and "does not raise" rarely can.
- For an error, assert its kind and the part a caller relies on, such as a
  code or a field name. Do not pin a whole message that is free to be reworded.
- Treat a broad snapshot as a supplement. When it changes, nobody can tell
  whether it should have.
- Assert a call or an order only when that call or order is the contract, such
  as "sends exactly one payment request".

## Use doubles only at real boundaries

Keep pure logic real: parsers, validators, calculators. Replace what is slow,
external or unpredictable: I/O, other processes, remote services, the clock.

A double must behave like the thing it stands in for: the same parameters, the
same shape of result, and the same ways of failing, including absence and
errors. Reset doubles between tests, and prefer one runner setting to cleanup
code that every file has to remember.

**A double answers whatever it is asked.** The request your code makes of it,
such as a field name, a flag, a format string or an expected exit status, is
therefore the one thing that no test built on that double can check. Two
defences:

- Design so that nothing essential depends on a name you guessed. Key the
  behavior on something that cannot be absent, and let the guessable field
  only add detail.
- Read the answer off the real system once, and pin what you observed, with a
  note of where and when. The suite then guards against regression. It was
  never proof that the first observation was right.

## Keep it deterministic

Pass in the clock, the seed, the time zone and the locale. Wait for an event,
never for an amount of time. Prefer input built in memory to files read from
disk. If the code reads the environment, set the variable in the test and
restore it afterwards.

## When the unit test will not come easily

If the decision can only be reached through the whole stack, look at the
production boundary before adding another wide test. A thin adapter around a
rule that can be called directly is usually the missing piece. Report it. Do
not paper over it in the test.
