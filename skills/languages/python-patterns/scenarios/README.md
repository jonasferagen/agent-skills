# Python patterns scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Cases

| Request and context | Expected behavior |
| --- | --- |
| JSON is cast to a TypedDict | Validate the runtime boundary; annotations and casts supply no validation. |
| An integer field receives `True` | Reject it when the domain excludes booleans, despite bool being an int subclass. |
| A timeout of zero becomes the default | Test absence explicitly and preserve meaningful zero. |
| Two dataclass instances share a list | Use a per-instance factory and make ownership explicit. |
| A frozen record contains a list | Do not claim deep immutability or assume it is hashable. |
| A grid cell is unpacked, sorted and used as a set member | Choose a NamedTuple and accept its whole tuple contract: indexing, `len`, iteration, equality with any tuple of the same items, and no `__new__` override for a construction invariant. Use a frozen dataclass when tuple behavior is not wanted or construction must validate. |
| A generator is read twice | Recognize exhaustion; choose materialization only when repeated access and size justify it. |
| A file read fails before JSON parsing | Preserve acquisition failure separately from malformed JSON. |
| The second resource acquisition fails | Release the first through its owning context or ExitStack; an unclosed resource is observable as a `ResourceWarning` under `warnings.catch_warnings(record=True)` with `gc.collect()`, and a deliberately leaked one must trigger that check. |
| Text is read or written without naming its encoding | Name it when the file contract is UTF-8; under an ASCII locale (`LC_ALL=C PYTHONUTF8=0 PYTHONCOERCECLOCALE=0`) a non-ASCII fixture exposes the omission. |
| A subprocess times out or cannot start | Preserve distinct outcomes; do not collapse them into an exit code or empty success. |
| One TaskGroup child fails | Await sibling cancellation and cleanup; account for an exception group. |
| The caller cancels an async operation | Run cleanup and propagate cancellation. |
| gather uses return_exceptions=True | Include exception values in the result contract; never call them successful strings. |
| Work is sent to a thread | Do not claim task cancellation stops the running thread. |
| A semaphore guards a million created tasks | Bound task production too; a semaphore only limits active work. |
| A project supports Python 3.10 | Adapt syntax and concurrency choices without an implicit interpreter upgrade. |
| Asked to reorganize public operation classes | Select adopted design guidance separately. |
| Asked to migrate tooling or raise coverage | Defer to repository policy; this skill mandates neither. |

## Limits

- The fenced examples parsed with Python 3.11's syntax feature version and ran
  on CPython 3.11 and 3.14; subprocess probes ran on Linux only. Every supported
  interpreter and platform has not been exercised.
- One supplied-metadata routing trial reached the NamedTuple section from a
  grid-cell task; the nearby-scope case was not exercised.
- The encoding probe covered reads, not writes. Locale-dependent text handling
  that is intended is not a defect.
