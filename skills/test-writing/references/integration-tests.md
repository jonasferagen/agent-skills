# Integration tests

<!-- Package-boundary copy: test-audit/references/principles.md (Test decisions where they are made) and verification-design/SKILL.md (Match each claim to an observable boundary) state when a boundary needs its own evidence. Keep these passages aligned. -->
An integration test answers a question that no inner test can. Does the adapter
pass the right input and identity? Does the real database accept, reject or
serialize? Do two processes reach each other? Is the file written where the
next step reads it? Does the built artifact start? Write one when the claim is
about a boundary. A rule's own cases are proved more cheaply, and named more
clearly, by [unit tests](unit-tests.md).

## Name the boundary first

Write down four things before the test:

- **Inside:** what runs for real.
- **Outside:** what is replaced by a double, or absent.
- **What crosses:** the input and its form going in, and what comes out: files,
  rows, a response, an exit status, a message.
- **What must not change:** the inputs themselves, source data, records that
  belong to someone else.

When two components meet at a contract, such as a file format, a schema or a
message shape, that contract is the boundary. Name it.

## Enter through the boundary

Call the entry point a real caller uses: the command, the public function, the
route, the function that takes the directory. Arrange state through the same
public surface where that is practical. Reaching into internals to set state
tests an arrangement that production never has. Keep collaborators inside the
boundary real, and use doubles only outside it.

<!-- Package-boundary copy: containerization/references/database-tests.md (Give each test run a complete lifecycle) states this lifecycle for database tests. Keep both passages aligned. -->
## Give each test its own state

- Create a fresh temporary directory, database, queue or namespace for the
  test. Use unique names so that parallel runs cannot collide.
- Dispose of it even when setup or an assertion fails. Keep the original
  failure as the result, and report a failed cleanup as well. If only cleanup
  fails, fail the run.
- If setup fails, fail with the reason. Skip, saying what is missing, only
  when the test needs something optional that this environment does not
  offer, such as a live service that nobody set up here. Never fall back to a
  developer's, a shared or a production resource.
- Depend on no other test having run first.
- Share only what no test changes, such as a built artifact or a read-only
  reference set.

## Assert both sides of the boundary

- **What it produces.** Compare the observable output precisely: parse the
  file or the response and compare its content. A substring match on raw text
  passes for many wrong outputs.
- **What it leaves alone.** Where the promise is "reads only" or "writes only
  here", prove it. Compare a digest or a listing of the protected inputs
  before and after, and assert that nothing appeared outside the output
  location.
- **How it fails.** Give it a missing input, a malformed input, a refused
  permission or a timeout where those can happen. Assert what a caller then
  sees: the status, the error, and that no partial output remains.
- **What a repeat does.** Where the contract promises it, run twice and assert
  one result.

## Keep the set small

Write one representative case for each path through the boundary. Add cases
only where the boundary itself can change the outcome: encodings, transactions,
concurrency, permissions, partial writes. Before adding a case, name the
failure it would see that no existing test sees. If there is none, the case
belongs in a unit test or nowhere.

## Contracts between components

When the output of one component is the input of another, three kinds of test
keep them honest and let each be worked on alone.

1. **The producer against the contract.** Its real output passes the
   contract's check: required fields are present, references resolve, recorded
   hashes match.
2. **The consumer from a reference input.** Build the reference with the same
   check the producer is held to, or generate it by running the producer. A
   reference that only the consumer's tests read is a second definition of the
   contract, and nothing checks it.
3. **One chain test.** Feed the producer's real output to the consumer. It
   catches what the references miss.

## Cases as data

When several cases share one procedure, state them as a table: a name, an
input and an expected outcome per case, run by one test body that reports each
case by name. Describe the expected outcome as what can be observed, not how
it is produced. Keep the table beside the tests, and fill it with made-up
values as [fixtures](fixtures.md) describes.

## Say what ran

A test that needs something optional that this environment lacks, such as
local data or a live service, skips with the reason. That is neither a pass
nor a failure. Report the run as step 7 of the [workflow](../SKILL.md#workflow)
says: a run with skips, or a fast subset run for feedback during the work, is
partial.
