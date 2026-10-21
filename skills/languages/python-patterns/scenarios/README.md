# Python patterns scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Cases

| Request and context | Expected behavior |
| --- | --- |
| JSON is cast to a TypedDict | Validate the runtime boundary; annotations and casts supply no validation. |
| Validated records retain Any throughout downstream processing | Carry precise validated types; allow TypedDict at a mapping boundary and separate variants when payloads differ, without demanding dataclasses for every dictionary. |
| Distinct numeric values become the same formatted dictionary key | Separate display labels from identity; preserve every record or report duplicate keys instead of silent replacement. |
| A single epsilon is used for lengths, squared distances and volume | Identify units and error sources and choose policies for each decision; do not transplant one threshold across dimensions. |
| A fixed absolute-error contract uses isclose at large coordinates | Set relative tolerance to zero and choose the contract's absolute tolerance; exercise zero, the threshold and representative large values. |
| Approximate equality is used to deduplicate numeric keys | Explain non-transitivity and require an explicit grouping rule; do not silently substitute approximate key equality. |
| Finite inputs overflow or distinct values collapse in float32 output | Check consequential derived values and decoded output invariants; exercise the actual encoding rather than only the in-memory model. |
| An integer field receives `True` | Reject it when the domain excludes booleans, despite bool being an int subclass. |
| A timeout of zero becomes the default | Test absence explicitly and preserve meaningful zero. |
| Two dataclass instances share a list | Use a per-instance factory and make ownership explicit. |
| A frozen record contains a list | Do not claim deep immutability or assume it is hashable. |
| A 2-D coordinate pair is unpacked, sorted and used as a set member | Choose a NamedTuple and accept its whole tuple contract: indexing, `len`, iteration, equality with any tuple of the same items, and no `__new__` override for a construction invariant. Use a frozen dataclass when tuple behavior is not wanted or construction must validate. |
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
| Asked to reorganize public operation classes | Treated as a structural decision outside this skill; the project's existing layout is followed. |
| Asked to migrate tooling or raise coverage | Deferred to the project's conventions or the user; this skill mandates neither. |
| The project documents no Python version | The minimum is inferred from `requires-python`, CI and tool-version files, and the assumption is stated in the report. |

## Limits

- The fenced examples are verified on CPython 3.11 and 3.14 on Linux; other
  interpreters and platforms are not exercised.
- The encoding case is verified for reads, not writes. Locale-dependent text
  handling that is intended is not a defect.
