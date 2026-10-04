# Synthetic JSON importer design

Use a stateless `SyntheticRecordImport` operation with a static `read` method.
The caller lends a text stream for one pass; the importer returns a tuple of
immutable `SyntheticRecord` values. This is a proposed contract and verification
plan, not an implemented or tested importer.

## Wire contract and types

Assume newline-delimited JSON: each physical line contains exactly one JSON
object with exactly two keys, `record_id` and `quantity`. `record_id` is a string
containing at least one non-whitespace character, preserved verbatim. `quantity`
is an integer greater than or equal to zero; booleans, floats and numeric strings
are invalid. IDs need not be unique: the operation preserves input order and
repeated records. Empty input is valid and returns `()`. Blank lines are invalid;
a final newline is optional. Text decoding belongs to the caller.

The public shape uses Python 3.10-compatible standard-library types:

```python
from collections.abc import Iterable
from dataclasses import dataclass

@dataclass(frozen=True)
class SyntheticRecord:
    record_id: str
    quantity: int

    def __post_init__(self) -> None:
        if not isinstance(self.record_id, str) or not self.record_id.strip():
            raise ValueError("record_id must contain a non-whitespace character")
        if isinstance(self.quantity, bool) or not isinstance(self.quantity, int):
            raise ValueError("quantity must be an integer")
        if self.quantity < 0:
            raise ValueError("quantity must be non-negative")

class InvalidRecordError(ValueError):
    # Implementation stores one-based line_number and a bounded reason.
    pass

class SyntheticRecordImport:
    @staticmethod
    def read(source: Iterable[str]) -> tuple[SyntheticRecord, ...]:
        ...  # Proposed operation; steps below specify its behavior.
```

`Iterable[str]` expresses the only required capability: a single traversal of
text lines. A caller-owned text file, `StringIO` or synthetic iterator can satisfy
it; no new protocol or large stream API is needed. Runtime validation still
rejects an item that is not a string. Parsed JSON starts as `object`, then is
narrowed by actual checks; annotations, casts and a `TypedDict` cannot establish
validity. The output tuple owns its collected snapshot. Each record has immutable
scalar fields, so there is no nested mutable object shared with decoded JSON.
Frozen values protect ordinary API use, not deliberate low-level bypasses.

## Ownership and processing

`SyntheticRecordImport.read` owns traversal, JSON parsing, object-shape checks,
line context and accumulation. `SyntheticRecord` owns its field invariants in
ordinary construction as well as import construction. Private parser helpers may
remain module functions. No service instance, global state, factory hierarchy or
dependency injection framework is warranted for this operation.

For each line, the operation:

1. Obtains the next item from the caller's iterator and checks that it is text.
2. Decodes JSON inside a narrow parsing boundary. Configure duplicate-object-key
   detection through `object_pairs_hook`, and reject nonstandard `NaN` and
   infinity tokens through `parse_constant`. Private parser exceptions become
   `InvalidRecordError` with their cause preserved.
3. Requires a JSON object with exactly the two expected keys. Null, arrays,
   scalars, omitted fields and extra fields fail explicitly.
4. Constructs `SyntheticRecord`, translating its expected validation failure
   into `InvalidRecordError` with the one-based physical line number and cause.
5. Adds the value to a fresh local list. After EOF, converts that list to a tuple.

Validation is eager and fails at the first invalid line. No partial collection
escapes as a successful result. Materializing all values costs memory proportional
to the number of records; this design is intended for small synthetic inputs.
No cross-record rule or size limit is inferred.

## Invalid input and borrowed resource outcomes

| Outcome | Observable contract |
| --- | --- |
| Valid empty source | Return `()` |
| Malformed JSON, blank line, duplicate key or nonstandard numeric token | Raise `InvalidRecordError` with line number and bounded reason; retain parser cause |
| Invalid object shape or domain field | Raise `InvalidRecordError` with line number and field/shape reason; retain a validation cause when one exists |
| Non-text item | Raise `InvalidRecordError` at that item number |
| Stream iteration or decoding fails | Propagate the original exception, such as `OSError` or `UnicodeDecodeError`; do not mislabel it as an invalid record |
| Interrupt, exit or unexpected programmer failure | Propagate; no broad exception-to-success handling |

Error messages identify the location and rule without dumping the whole supplied
record. Missing input, explicit null and an invalid value do not select defaults.
In particular, zero is valid and remains zero.

The caller owns acquisition and closure. The importer never invokes `close`,
enters the source as a context manager, wraps it in a closing adapter, seeks or
rewinds it. This holds after success, invalid input and stream failure. Successful
imports leave the stream open at EOF; failed imports leave it open after whatever
the iterator already consumed, with no promise to roll consumption back or drain
the remainder. A provider may buffer ahead or close itself independently; the
importer cannot override those provider behaviors.

The operation closes no resource because it acquires none. A caller that opened
a file encloses its own import call in its own file context and decides when to
release it.

## Focused verification plan

Use Python 3.10+ and `unittest`, without dependencies, network or live data. The
following checks are planned, not executed; there is no importer implementation
to exercise yet. Test-writing guidance must be selected before authoring tests
or fixtures. No settled-suite audit or integration infrastructure is needed for
this design-only request.

| Claim | Cheapest observable check and defect caught | Prerequisite / cost |
| --- | --- | --- |
| Values and sequence preserve valid input | One public-operation test imports multiple synthetic lines including zero, repeated IDs and a last line without newline; assert exact ordered tuple and field values | Implementation; tiny in-memory input |
| Valid emptiness remains distinct from failure | Empty `StringIO` returns `()`; an actual blank line raises `InvalidRecordError` at line 1 | Implementation; two boundary assertions |
| Validation is real | Table-driven public-operation checks cover malformed JSON, top-level non-object, missing/extra/duplicate keys, null, invalid ID, negative count, boolean/float/string count, nonstandard numeric tokens and non-text item; assert error category and line context | Implementation; independent small inputs |
| Errors are eager and do not expose partial success | Valid first line, invalid second line and a sentinel iterator tail; assert line 2 error and no request for the tail | Implementation; one iterator double |
| Domain construction maintains invariants | Construct the value directly with valid zero and representative invalid field types/ranges; assert value or `ValueError` | Implementation; no stream setup |
| Returned values are immutable through normal use | Assert tuple output and `FrozenInstanceError` on record field assignment; check equality of independently constructed values | Implementation; standard-library assertions |
| Borrowing preserves the caller's lifetime | Use a tracking stream whose `close` and context-entry methods are observable; exercise success, validation failure and iteration failure, then assert it remains open and those methods were not invoked | Implementation; fresh stream per case |
| Operational failures keep their identity | Inject a specific `OSError` or `UnicodeDecodeError` during iteration; assert that same exception propagates and source stays open | Implementation; small iterator double |
| Translation preserves useful causes | Assert parser/domain errors have the expected cause and bounded messages omit an untrusted payload marker | Implementation; focused error assertion |

After implementation and test authoring, run
`python -m unittest discover -s tests -p 'test_*.py'` in this consumer, using the
project-supported interpreter. Record interpreter version, exact command and
result. These runtime checks establish the local operation contract; they do not
prove static typing or file-decoding correctness owned by the caller. If an
existing type-check command is later found, run that adopted command without
installing a competing tool. No checks have been represented as passing here.

## Instruction-read record

All paths below are relative to this synthetic consumer. Each file was read in
full once. There were no repeated content reads and no truncated reads. A later
`wc -w` pass read the same files only to calculate counts; if counting every file
access as a repeated read, that is one count-only reread of each of the 13 files.
Whitespace word counts are approximate and include Markdown markup.

| Instruction file actually read | Words | Classification and reason |
| --- | ---: | --- |
| `AGENTS.md` | 26 | Required: consumer routing |
| `project.md` | 51 | Required: runtime, local scope and verification constraints |
| `.agents/collections/python-foundation/COLLECTION.md` | 198 | Required: new Python operation routing |
| `.agents/collections/verification-foundation/COLLECTION.md` | 222 | Required: verification-plan routing |
| `.agents/collections/python-foundation/skills/python-design/SKILL.md` | 396 | Required: operation ownership member |
| `.agents/collections/python-foundation/skills/python-patterns/SKILL.md` | 369 | Required: language-boundary member |
| `.agents/collections/verification-foundation/skills/verification-design/SKILL.md` | 535 | Required: evidence selection |
| `.agents/collections/python-foundation/skills/python-design/references/class-shape.md` | 400 | Required: stateless operation owner and construction boundary |
| `.agents/collections/python-foundation/skills/python-design/references/values-and-call-sites.md` | 349 | Required: invariant-owning immutable values |
| `.agents/collections/python-foundation/skills/python-design/references/dependency-boundaries.md` | 297 | Required: borrowed stream and actual consumer capability |
| `.agents/collections/python-foundation/skills/python-patterns/references/types-and-boundaries.md` | 339 | Required: runtime narrowing and Python 3.10 syntax |
| `.agents/collections/python-foundation/skills/python-patterns/references/values-and-collections.md` | 373 | Required: snapshot immutability and single-pass iteration |
| `.agents/collections/python-foundation/skills/python-patterns/references/errors-and-resources.md` | 430 | Required: precise error translation and resource ownership |
| **Total content read** | **3,985** | No useful-only or irrelevant instruction files loaded |

Not selected: installation, async, names/modules, test writing and test audit
guidance. Their decisions were not required here; test writing is deferred until
actual authoring. `README.md` was discovered but not opened or changed. Its
reported spelling sample has no bearing on this task.

Preserved constraints: isolated synthetic consumer only; no source-repository
or other-fixture inspection; Python 3.10+ and standard-library `unittest`; no
dependency installation, live data, services, secrets or network; class-based
house operation ownership; repository authority over product/tool/test policy;
no repository-wide refactoring; validate rather than trust annotations; reject
booleans for integer counts; preserve empty input and zero; immutable scalars and
tuple result; caller owns stream closure; focused plan only, with evidence limits
explicit. The parent-provided routing validation authorization selected this
fresh-context trial. No conflicting owner guidance or missing required route
was encountered.
