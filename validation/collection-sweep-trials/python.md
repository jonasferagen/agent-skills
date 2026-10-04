# Installed Python consumer trials — 4 October 2026

The evaluator did not author Python-foundation. It started each case at that
fixture's `AGENTS.md` and `request.txt`, followed the installed project hooks and
made no Python source-collection changes. No source repository or prior Python
validation report was read during these trials. Inputs, raw answers, proposed
functions and execution probes remain in the fixture directories.

## Context and method limits

These are cross-evaluation trials in one reused conversation, not blind fresh
evaluations. The evaluator inherited repository maintenance instructions,
skill-creator/clear-writing guidance and its completed project-foundation sweep.
That inherited context includes knowledge of proportionate task routing,
authority and evidence requirements. No claim of spontaneous native discovery
or independent fresh selection is made.

The three fixtures were read in parallel initially, then their files and narrow
routes were inspected in the same conversation. Async and encoding each loaded
their own installed copy of the collection entrypoint and Python-patterns.
Those identical passages were therefore displayed twice across the cases. Each
listed file was displayed once within its case, with no truncated consumer
output. Word counting later reread files mechanically without displaying their
contents. Directory listings, execution output and generated-artifact review
are not counted as guidance reads.

## Files actually read

Counts are approximate whitespace-word counts of displayed input files. They
are instruction/artifact subtotals, not total tokens or conversation context.
The unchanged word count of the wording README also describes its original text.

| Case | File relative to fixture | Words | Classification and reason |
| --- | --- | ---: | --- |
| Async | `AGENTS.md` | 22 | Required: interpreter, function layout and installed route |
| Async | `request.txt` | 45 | Required: proposed fix and caller-visible ownership outcome |
| Async | `worker.py` | 15 | Required: actual function to correct |
| Async | `.agents/collections/python-foundation/COLLECTION.md` | 209 | Required by hook: selects async patterns while retaining local design |
| Async | `.agents/collections/python-foundation/skills/python-patterns/SKILL.md` | 383 | Required: minimum-version adaptation and narrow async route |
| Async | `.agents/collections/python-foundation/skills/python-patterns/references/async-work.md` | 288 | Required for task/failure/cancellation ownership. Its blocking-I/O and concurrency-limit material was not needed for this bounded fix. |
| Encoding | `AGENTS.md` | 27 | Required: UTF-8 exchange versus intentional locale contract |
| Encoding | `request.txt` | 43 | Required: focused correction and preserved error meanings |
| Encoding | `files.py` | 18 | Required: compare both readers and preserve existing functions |
| Encoding | `.agents/collections/python-foundation/COLLECTION.md` | 209 | Required by hook: selects text-I/O patterns without design restructuring |
| Encoding | `.agents/collections/python-foundation/skills/python-patterns/SKILL.md` | 383 | Required: narrow text-I/O/error route and local interpreter constraint |
| Encoding | `.agents/collections/python-foundation/skills/python-patterns/references/errors-and-resources.md` | 480 | Required for encoding/error distinctions. Context-manager and subprocess sections were unnecessary for this focused request. |
| Wording | `AGENTS.md` | 11 | Required: literal-edit scope and conditional implementation route |
| Wording | `request.txt` | 8 | Required: exact spelling replacement |
| Wording | `README.md` | 11 | Required: actual sentence being edited |

Async displayed-input subtotal: **962 words**, including **880** installed-guidance
words. Encoding subtotal: **1,160 words**, including **1,072** installed-guidance
words. Wording subtotal: **30 words**, with no installed Python guidance loaded.
Combined displayed-input subtotal: **2,152 words**; it includes the repeated
collection/skill passages and excludes inherited maintenance context and outputs.

No Python-design, installation guide, source catalog, provenance, types/defaults
reference or other collection route was loaded. The implementation requests
needed no class-design change; the literal request did not select Python
implementation guidance. The installed references were reached through their
hooks without an expected-route prompt.

## Outcomes and execution evidence

### Async ownership

Raw answer: `python-async/answer.md`. Proposed function: `python-async/proposed.py`.
Probe and raw output: `python-async/check.py` and `python-async/checks.txt`.
Original `worker.py` remains unchanged because the request asked for a proposal.

The proposal retains the function and standard-library `asyncio` layout. It puts
task creation and gathering inside `try/finally`, cancels pending children and
awaits them with `return_exceptions=True`, preserving the original failure or
caller cancellation. It does not select Python 3.11 TaskGroup or upgrade anything.
The deeper async reference was reached; the entrypoint's minimum-version warning
prevented copying the newer example directly.

The safe probe passed ordered success, ordinary child failure with sibling cleanup
completed before the error reached the caller, single caller cancellation with
child cleanup and preserved `CancelledError`, and creation failure after an earlier
child had been created. It ran on **Python 3.14.4**; Python 3.10 grammar parsing
passed but no Python 3.10 runtime execution was performed.

The answer explicitly bounds its cancellation claim. A child that refuses to
finish can keep its owner waiting. A further caller cancellation while cleanup is
being awaited can interrupt that await; this case was not exercised and the
proposal does not establish a general repeated-cancellation guarantee. The
coordinator accepted keeping that limitation explicit for this bounded trial.

### Text encoding and error meanings

Raw answer: `python-encoding/answer.md`. Proposed readers:
`python-encoding/proposed.py`. Probe and raw output: `python-encoding/check.py`
and `python-encoding/checks.txt`. Original `files.py` remains unchanged because
the request asked for a proposal.

`read_exchange` now specifies `encoding="utf-8"`; `read_locale` retains
`encoding="locale"`. The proposal does not change layout, substitute replacement
decoding, swallow errors or introduce parsing. The answer distinguishes text
decoding, filesystem acquisition and later application syntax errors.

The probe ran on **Python 3.14.4** in a subprocess with UTF-8 mode/coercion disabled
and `LC_ALL=C`, confirming configured `ANSI_X3.4-1968` encoding. Valid UTF-8
exchange bytes decoded correctly; the locale reader retained ASCII behavior.
Valid empty text, malformed UTF-8 (`UnicodeDecodeError`) and a missing file
(`FileNotFoundError`) kept their meanings. Python 3.10 grammar parsing passed.
Python 3.10 runtime execution, permission denial and format parsing were not
exercised; no claim of those checks is made.

### Nearby literal edit

Raw answer: `python-wording/answer.md`; edited artifact:
`python-wording/README.md`; exact-result check: `python-wording/checks.txt`.
Only `asyncronously` became `asynchronously`. A safe exact-content assertion
confirmed the requested sentence and remaining README text. No Python skill or
collection was loaded for this case, and no implementation was changed.

The extra answer/probe/output files are retained trial evidence, not additions
to the consuming product. No service, package installation, source update,
real data or external mutation was involved.

## Observed source-quality finding

The encoding trial's installed errors-and-resources reference says its example
"translates only decoding failure", but the example performs `read_text` before
the `try` and catches `json.JSONDecodeError` around `json.loads`. It translates
JSON syntax failure; `UnicodeDecodeError` and acquisition errors pass through.
This contradictory example description could obscure the error distinction
the requested answer must preserve. The answer follows the actual code and the
reference's surrounding encoding-contract rule.

The installed raw input remains unchanged. The coordinator reports correcting
the source prose to identify JSON syntax failure without changing its code or
router. This trial observed the original issue; it did not reread or validate
that source repair. No other missed necessary reference was observed in these
bounded requests. These cases establish their demonstrated routes and behavior,
not overall Python skill reliability or universally minimal reading.

## Retained requests and raw answers

The original report above names temporary runtime artifacts. The requests, raw
answers and selected execution output are retained below for source review.

### python-async

Request:

Please propose a focused fix to run_batch: when one child raises, sibling tasks keep running after the caller gets the error. The parent must cancel and await its remaining children before returning. Preserve Python 3.10 support. Give the corrected function and explain its failure/cancellation behavior.

Raw answer:

Put task creation and waiting inside the cleanup boundary:

```python
import asyncio


async def run_batch(work):
    tasks = []
    try:
        for item in work:
            tasks.append(asyncio.create_task(item()))
        return await asyncio.gather(*tasks)
    finally:
        for task in tasks:
            if not task.done():
                task.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)
```

Successful results retain input order. On a child failure, `finally` cancels the
remaining children and waits for their cleanup before the original error reaches
the caller. Cleanup exceptions are collected without replacing that error. Caller
cancellation also runs cleanup and propagates `CancelledError`; it is not turned
into success. Keeping each created task in the list also permits cleanup if a
later task factory raises during creation.

This uses Python 3.10 APIs and preserves the function layout. Cancellation is
cooperative: a child that refuses to finish can keep the parent waiting. A new
cancellation arriving during the cleanup await can interrupt that await; a
stronger repeated-cancellation guarantee needs an explicit shield/join policy.

The retained execution probe passed success, child failure, single caller
cancellation and task-creation failure on Python 3.14.4. Python 3.10 grammar
parsing passed; the proposal was not run on a Python 3.10 interpreter.

checks.txt:

```text
interpreter: 3.14.4
Python 3.10 grammar: parsed
success: result order retained
child failure: sibling cleanup completed before error reached caller
caller cancellation: child joined and CancelledError preserved
creation failure: previously created child joined
```

### python-encoding

Request:

read_exchange fails to read a valid UTF-8 exchange file when this job runs under an ASCII locale. Propose the focused correction and state which error meanings must remain visible. read_locale serves a different file contract and should continue to follow the configured locale.

Raw answer:

Use the exchange file's declared encoding:

```python
def read_exchange(path: Path) -> str:
    return path.read_text(encoding="utf-8")
```

Leave `read_locale` as `path.read_text(encoding="locale")`. Its configured-locale
contract differs from the UTF-8 exchange contract.

Keep malformed UTF-8 visible as `UnicodeDecodeError`, and file acquisition failures
such as `FileNotFoundError` and `PermissionError` visible with their existing
meanings. Do not use replacement decoding or return an empty string on error.
An empty successfully decoded file remains a valid empty string. Decoding does
not validate application format syntax; any later parser retains its separate
syntax errors. No exception translation or new parsing is needed here.

The retained probe passed under a forced ASCII locale on Python 3.14.4. It
exercised UTF-8 exchange decoding, the separate locale contract, empty text,
malformed UTF-8 and a missing file. Python 3.10 grammar parsing passed; no
Python 3.10 execution or permission-denial case was run.

checks.txt:

```text
Python 3.10 grammar: parsed
interpreter: 3.14.4
configured locale: ANSI_X3.4-1968
UTF-8 exchange: decoded under ASCII locale
locale contract, valid empty text, decode error and acquisition error: preserved
```

### python-wording

Request:

Fix only the spelling of asyncronously in README.md.

Raw answer:

Fixed `asyncronously` to `asynchronously` in README.md. No other wording changed.

checks.txt:

```text
Exact spelling-only result confirmed.
```
