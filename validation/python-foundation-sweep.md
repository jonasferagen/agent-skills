# Python foundation sweep — 4 October 2026

Reviewed the Python collection at base commit
`a30ca1bb83591bfaa2ad67272163f98a730a5db4`, then made the focused changes below
in the shared collection-sweep task worktree. The delegated reviewer inherited
the maintenance task context. This was a source review with a focused runtime
probe, not a blind consumer trial or a release self-conformance declaration.

## Phase 1: skill quality

Reviewed both member entrypoints, both `agents/openai.yaml` files and all eight
references before reviewing collection consistency:

- Python design: class shape, values and call sites, dependency boundaries, and
  names and modules.
- Python patterns: types and boundaries, values and collections, errors and
  resources, and async work.

The split is useful: design owns the intentional class-based house preference;
patterns owns language correctness and failure handling. Both preserve local
product, framework, tooling and test authority. The design exceptions remain
narrow, references are reachable by concrete symptoms, and neither member
implies an interpreter upgrade or broad refactor. No changes were needed to
Python design or either UI metadata file.

Two quality findings were fixed:

1. The UTF-8 example in errors and resources demonstrated an encoding, but did
   not state the reusable text-file contract. Existing consumer evidence in
   [Python patterns validation](python-patterns.md#consumer-evidence-and-testing-techniques--2026-10-02)
   recorded failure under an ASCII locale. Added concise guidance to select the
   file contract's encoding on reads and writes, preserve deliberate locale
   contracts, and distinguish decoding, acquisition and format failures. Added
   an entrypoint symptom route for machine-dependent text I/O. The guidance
   does not infer UTF-8 for arbitrary external files or add a mandatory test lane.
2. The synchronous generator-closure passage cited only `aclosing`. Its source
   list now distinguishes synchronous `closing` and async-generator `aclosing`.
   The ownership rule itself is unchanged.

Checked the additions against official Python documentation for
[text-file encoding](https://docs.python.org/3/library/functions.html#open),
[closing](https://docs.python.org/3/library/contextlib.html#contextlib.closing)
and [aclosing](https://docs.python.org/3/library/contextlib.html#contextlib.aclosing).
Other technical claims received static review; this sweep did not independently
retest every historical example or interpreter version.

Applied Clear Writing and its instruction reference to the edits, and
Diagrams and tables to the existing lookup form. Pattern capture supported
putting the observed encoding mechanism in its existing owner rather than
adding another skill or duplicating consumer-specific test instructions.

## Phase 2: collection consistency

Reviewed `COLLECTION.md`, installation guidance, manifest membership and the
distributed installation checker. Also reviewed both existing member validation
pages and the active and literal-wording Python collection trial records.

The installation unit correctly pairs the two members, keeps adoption choices
outside imported files and routes focused fixes without reopening class design.
The collection lookup omitted async work even though the member explicitly owns
it. Split the patterns row into types/defaults and failure/resource work, making
async tasks and text I/O visible without requiring both members. Installation
and helper behavior needed no local change.

Python patterns and Python foundation are now `0.2.0`: the text-file contract
adds compatible guidance, while the route additions expose existing and newly
stated scope. Python design remains `0.1.0`. Names, invocation metadata,
membership, house style and repository-authority copies are unchanged. No tag
or commit was created. The root reviewer owns the final checker synchronization
and reviewed inventory regeneration.

## Actual verification and limits

- Both members passed the system skill creator's `quick_validate.py`.
- `git diff --check -- collections/python-foundation` passed.
- A temporary standard-library probe on CPython `3.14.4` on Linux reproduced
  omitted-encoding read and write failures with `LC_ALL=C`, `PYTHONUTF8=0` and
  `PYTHONCOERCECLOCALE=0`. It checked that UTF-8 mode was `0` and the locale
  encoding was `ANSI_X3.4-1968`. Explicit UTF-8 reads and writes preserved the
  synthetic non-ASCII content. A separate ASCII file with an explicit locale
  contract also succeeded. The temporary fixture was removed automatically.
- `python3 scripts/validate-packages.py` ran and failed while the source sweep
  was in progress: Python's edited file hashes awaited root regeneration, and
  the distributed Python, service, TypeScript and verification checkers differed
  from the concurrently updated canonical source. This is not a passing package
  check; final synchronization and validation are delegated to the root reviewer.
- No runtime helper changed, so no helper-behavior test was selected. This pass
  did not repeat strict typing probes, inspect table rendering, test other
  platforms, adopt the collection into a real consumer or verify live discovery.

The entrypoint changes require practical routing evidence. The root reviewer
plans fresh consumer trials for:

- An async ownership or cancellation fix in a Python 3.10 consumer: select
  Python patterns and async work, preserve the supported interpreter and local
  tools, and avoid unrelated class organization or installation reads.
- A UTF-8 file defect under a constrained locale: select Python patterns and
  errors/resources, preserve meaningful encoding contracts and distinct errors,
  and avoid blanket UTF-8 rewrites.
- A nearby literal wording edit: select no Python member.

These are pending behavioral checks, not results established by source review.

## Additional improvements

Give the member validation pages a dated current-status note after the final
collection checks. Their original standalone-install statements describe the
earlier package layout; preserve that history while making the current complete
collection installation and newer consumer trials easy to find.

Keep packaging, multiprocessing and performance guidance conditional on actual
consumer needs. The current starting set states those limits clearly; making it
a Python handbook would weaken the focused design and language routes.

## Coordinated completion

The [coordinated sweep](collection-sweep.md) records the final source inventories,
combined checks and retained consumer trials. Earlier pending or partial results
on this page describe the review stage at which they were recorded. No release
or installed Forge pin was changed.
