# Verification consumer trials — 4 October 2026

These four requests used installed consumer fixtures only, entered through each
fixture's `AGENTS.md` and `request.txt`. The evaluator did not author the
verification collection. During this evaluation no source repository or prior
validation report was read, and no source package was edited.

## Independence and context limits

This evaluator previously reviewed Python foundation. Its inherited maintenance
context included the source catalog, repository authoring rules, and Python
consumer trial records mentioning verification routing. It had not authored or
reviewed verification members. That prior context remained available and limits
the independence of these consumer trials.

All four requests were evaluated in one agent context. The initial instructions
and requests were read in parallel, then the raw task artifacts and relevant
collection entrypoints were read. Each task was completed in its own fixture,
with routing selected from its request and installed hook rather than its
directory name. Earlier request and guidance content remained in context for
later cases, especially overlapping test-writing and test-audit principles.
These are independent task outcomes, not four cold-agent trials or evidence of
host automatic discovery.

All content reads completed without truncation. Each listed file was displayed
once for guidance or task work. The collection entrypoint was displayed from
three separate fixtures, with identical content; AGENTS.md was likewise displayed
from all four fixtures. This repeats equivalent content across cases, although
not the same path. A later mechanical word-count pass reread every listed file
without displaying its contents. The unchanged production and wording checks
also reread names.py and README.md mechanically. The regression test file was
read for copying into its temporary countercheck.

`rg --files --hidden` listed every fixture before selecting task materials. It
exposed installed resource names, not their contents. That broad file-name
inventory was unnecessary for the literal wording task; the named README alone
would have sufficed. No irrelevant instruction file was loaded from that fixture.

## Outcomes and artifacts

| Request | Outcome | Raw artifacts and evidence limit |
| --- | --- | --- |
| Add the specified empty/whitespace regression and demonstrate detection of old behavior | Selected test writing, unit tests and fixtures. Added one unittest with two synthetic subcases. Fixed implementation passed; both cases failed against temporary old behavior because ValueError was not raised. Production function remained unchanged. | `verification-regression/test_names.py`, `ANSWER.md`, `focused-test.txt`, `countercheck.txt`; focused test only, one test/two subcases/no skips on CPython 3.14.4 |
| Choose evidence for zipapp packaging without writing tests or auditing a suite | Selected verification design only. Planned resource membership and shipped-artifact checks outside the source tree, schema rejection, malformed input and direct exit-status observation. Explicitly identified missing artifact, schema/build details and exit contract. | `verification-evidence/ANSWER.md`; plan only, no checks claimed as executed or passing |
| Read-only focused audit of strict fake and isolated loopback integration | Selected test audit and its principles reference. Distinguished guessed expectation from verified external contract; retained owned isolated loopback networking as legitimate boundary evidence. Proposed authoritative contract evidence and inspection of bounded waits/state/cleanup. | `verification-audit/ANSWER.md`; no code/configuration changes, suite run, service run, timing or complete-coverage claim; integration implementation absent |
| Correct only a documentation spelling | Selected no verification member. Replaced sythetic with synthetic and verified exact complete-file contents. | `verification-wording/README.md`, `ANSWER.md`; no tests run |

Answers are preserved as produced in the named `ANSWER.md` files. Runtime output
is preserved without rewriting its temporary-path tracebacks. No live services,
external systems, private data or dependency installation were used.

## Guidance-read record

All paths below are relative to the named fixture. `VF` abbreviates
`.agents/collections/verification-foundation/`. Word counts use whitespace
splitting, include Markdown markup and are approximate. Required means the
installed route or task needed the instruction file; it does not imply every
section of a long file added value to this small request.

### Regression

| Guidance file | Words | Classification and reason |
| --- | ---: | --- |
| AGENTS.md | 32 | Required: framework, local scope and collection hook |
| VF/COLLECTION.md | 221 | Required: select test authoring without automatic evidence design or suite audit |
| VF/skills/test-writing/SKILL.md | 1157 | Required: authoring, synthetic inputs, failure countercheck and scoped reporting |
| VF/skills/test-writing/references/unit-tests.md | 701 | Required: in-memory rule, precise error assertion and table-driven input cases |
| VF/skills/test-writing/references/fixtures.md | 1357 | Required by authoring route: synthetic small inputs; real-data and stored-fixture sections had low value in this fixture |
| **Guidance subtotal** | **3468** | All required files reached; no irrelevant guidance selected |

Task material: request.txt 46 words and names.py 11 words. Total displayed
content for this task: 3525 words. No verification-design, test-audit,
integration-tests, installation or provenance content was read in this fixture.

### Packaging evidence

| Guidance file | Words | Classification and reason |
| --- | ---: | --- |
| AGENTS.md | 32 | Required: project constraints and collection hook |
| VF/COLLECTION.md | 221 | Required: distinguish an evidence plan from authoring or auditing tests |
| VF/skills/verification-design/SKILL.md | 546 | Required: match packaging claims to actual built-artifact boundaries and report unavailable prerequisites |
| **Guidance subtotal** | **799** | Member is self-contained for this plan; no deeper reference needed |

Task material: request.txt 28 words and CHANGE.md 42 words. Total displayed
content: 869 words. No test-writing, test-audit, installation or provenance
content was read in this fixture.

### Focused settled-test audit

| Guidance file | Words | Classification and reason |
| --- | ---: | --- |
| AGENTS.md | 32 | Required: local policy and collection hook |
| TESTING.md | 43 | Required: local contract provenance and deliberate integration-networking scope |
| VF/COLLECTION.md | 221 | Required: select settled-suite audit while preserving read-only scope |
| VF/skills/test-audit/SKILL.md | 1017 | Required: focused audit, evidence limits and conditional principles route |
| VF/skills/test-audit/references/principles.md | 1059 | Required: independent evidence for strict fake expectations and intentional isolated networking |
| **Guidance subtotal** | **2372** | Needed deeper judgment guidance reached; no scanner, cast or authored-test route needed |

Task material: request.txt 42 words, client.py 5 words and test_client.py 30
words. Total displayed content: 2449 words. There was no scanner or additional
integration implementation in the fixture. No triage, test-writing,
verification-design, installation or provenance content was read in this fixture.

### Literal wording

| Guidance file | Words | Classification and reason |
| --- | ---: | --- |
| AGENTS.md | 32 | Required: local instructions; verification hook applies only to check selection, test writing or suite review |
| **Guidance subtotal** | **32** | No verification decision required |

Task material: request.txt 11 words and README.md 9 words. Total displayed
content: 52 words. No VF file was opened in this fixture. Other cases' equivalent
collection instructions were already visible in the shared context, so this is
not a fully isolated negative routing trial.

Across the four cases: 6671 guidance words, or 6895 displayed words including
task materials. `verification-read-counts.json` preserves per-file counts.

## Routing result and limits

The installed hooks reached the necessary unit/fixture and audit-principles
guidance. No needed deeper reference was missed in the supplied tasks. Evidence
planning remained a plan, active regression authoring did not become a settled
suite audit, and the literal edit loaded no verification content from its own
fixture. The consumer records explicitly preserve scope and evidence limits.

The collection routes support these scoped outcomes. Shared and inherited
context means they cannot establish cold discovery efficiency or independence.
The packaging and networking claims remain outstanding where their executable
artifacts were unavailable; no plan or static review has been described as a
runtime pass.

## Retained requests and raw answers

The original report above names temporary runtime artifacts. The requests, raw
answers and selected execution output are retained below for source review.

### verification-regression

Request:

The fix in names.py now rejects an empty display name. Add a focused regression test for empty and whitespace-only input using our unittest framework, and verify that the test can detect the old behavior (returning the stripped value without a guard). Work only on this regression.

Raw answer:

# Regression result

Added `test_names.py` with one unittest and two independently reported subcases:
empty input and mixed whitespace-only input. It asserts the caller-visible
`ValueError`, without pinning an incidental error message. Inputs are synthetic;
production code was unchanged.

On CPython 3.14.4, `python3 -m unittest -v test_names.py` ran one test, with two
subcases and no skips, and passed against the fixed implementation. This is a
focused regression result, not a complete project gate.

The same test ran in an isolated temporary copy where `display_name` only
returned `value.strip()`. Both subcases failed with `ValueError not raised`:
one test, two failures, no skips. This detects the old behavior for the stated
reason. The temporary old implementation was removed automatically and the
fixed `names.py` was checked unchanged afterwards.

Raw output is preserved in `focused-test.txt` and `countercheck.txt`. Existing
test commands, thresholds and framework were not changed. No suite audit,
integration setup or live data was used.

focused-test.txt:

```text
test_rejects_empty_or_whitespace_only_input (test_names.DisplayNameTests.test_rejects_empty_or_whitespace_only_input) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

countercheck.txt:

```text
test_rejects_empty_or_whitespace_only_input (test_names.DisplayNameTests.test_rejects_empty_or_whitespace_only_input) ...
  test_rejects_empty_or_whitespace_only_input (test_names.DisplayNameTests.test_rejects_empty_or_whitespace_only_input) (value='') ... FAIL
  test_rejects_empty_or_whitespace_only_input (test_names.DisplayNameTests.test_rejects_empty_or_whitespace_only_input) (value=' \t\n') ... FAIL

======================================================================
FAIL: test_rejects_empty_or_whitespace_only_input (test_names.DisplayNameTests.test_rejects_empty_or_whitespace_only_input) (value='')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/tmp/agent-skills-sweep-trials/verification-regression/.old-behavior-r8azlsz9/test_names.py", line 10, in test_rejects_empty_or_whitespace_only_input
    with self.assertRaises(ValueError):
         ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
AssertionError: ValueError not raised

======================================================================
FAIL: test_rejects_empty_or_whitespace_only_input (test_names.DisplayNameTests.test_rejects_empty_or_whitespace_only_input) (value=' \t\n')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/tmp/agent-skills-sweep-trials/verification-regression/.old-behavior-r8azlsz9/test_names.py", line 10, in test_rejects_empty_or_whitespace_only_input
    with self.assertRaises(ValueError):
         ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
AssertionError: ValueError not raised

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=2)
```

### verification-evidence

Request:

Choose proportionate evidence before we call this packaging change verified. Give the check plan and what each check proves. Do not add tests or audit the existing suite.

Raw answer:

# Packaging evidence plan

The existing source parser tests and successful build are useful, but do not yet
verify that the zipapp can find its bundled schema or return the right process
status. This request calls for a plan only; no tests were added or suite audit
performed.

Use one built `tool.pyz` across the checks below. Run it with the supported Python
interpreter from an isolated temporary directory that contains only the artifact
and synthetic inputs, without the source tree on the import path or a neighboring
schema.json. Keep each case's output and input state independent.

| Claim | Check and failure detected | What it proves | Prerequisite and cost |
| --- | --- | --- | --- |
| The archive includes its schema | Inspect archive membership for the expected schema resource | Detects a resource omitted by packaging; does not prove runtime lookup | Built artifact and intended resource path; cheap static check |
| The shipped command locates and uses the bundled schema | Run `python tool.pyz validate valid.json` with a synthetic valid record from the isolated directory, then a syntactically valid record that violates a known schema constraint | Runtime startup, command routing and resource access through the shipped artifact; contrasting outcomes show schema validation is reached | Built artifact, documented synthetic valid shape and one schema constraint; two short process runs |
| Malformed input remains a validation failure | Run `python tool.pyz validate malformed.json` with deliberately invalid JSON; inspect the promised diagnostic and process status | Real file-to-parser-to-CLI failure behavior | Built artifact and malformed synthetic file; short process run |
| Success and failure statuses reach the caller | Record the direct subprocess return code for all cases and compare it with the documented CLI exit contract; avoid a pipeline that hides status | The shipped entrypoint preserves the promised success/failure outcome | An explicit exit-status contract, currently not supplied; no additional process runs needed |

Treat the prior parser/build runs as reported evidence for their original source
and environment. Do not repeat every parser branch through the CLI when the
source tests already cover it: retain representative artifact cases for resource
loading, schema rejection, malformed JSON and exit status. Preserve existing
project commands and gates; none were supplied beyond unittest as the framework.

The fixture contains only a change description. There is no artifact, schema,
build command or exact exit-status contract here, so these checks remain planned
and prerequisites remain outstanding. Once available, record the artifact
revision, interpreter, exact commands, statuses, diagnostics and results. The
packaging change cannot yet be called verified from this fixture.

### verification-audit

Request:

Do a read-only focused audit of this settled test setup. Explain what the strict fake does and does not prove, whether isolated loopback integration networking is itself a problem, and any focused follow-up. Do not change configuration or run a live service.

Raw answer:

# Focused audit

The strict fake protects agreement with its own programmed request, but the
provider contract is still unverified. `client.py` calls `/names` with
`fields=["name"]`; `test_client.py` rejects a different path or field selection
and checks that the fake's name list is returned. That is useful regression
evidence for the programmed interaction. `TESTING.md` says the fields were
guessed and records no provider documentation or independent observation.

**No evidence yet:** a green fake test cannot show that the real provider accepts
the field name, returns this response shape, or implements the semantics the
consumer expects. This is missing original contract evidence, rather than
evidence that a once-verified contract later drifted. The smallest follow-up is
to check path, field selection and result shape against an authoritative provider
contract, or a controlled observation when separately available and permitted,
and record its source/date. Keep the fake aligned with that verified expectation.
If the field is required, add focused absence/error coverage when test edits are
authorized; diagnostic-only fields should not determine core behavior.

**Keep intentionally:** isolated integration networking is appropriate when the
claim concerns real socket behavior. `TESTING.md` describes a disposable loopback
server that the test starts and owns. That alone is not a determinism defect and
does not justify replacing it with a mock. The focused follow-up is to inspect
the integration implementation for bounded waits, independent state and cleanup
on both failure and success. Its source is absent here, so those guarantees are
unverified rather than failed. The socket check and strict fake observe distinct
boundaries; the fake cannot replace real networking evidence.

The supplied fake is constructed fresh per test and has no mutable state to
reset. No configuration, tests or production code were changed. No suite or
service was run; this is static focused evidence, with no timing, coverage or
complete-suite claim.

### verification-wording

Request:

Fix only the spelling of sythetic in the README documentation example.

Raw answer:

Changed only `sythetic` to `synthetic` in README.md. An exact-content comparison
confirmed the complete file differs only by that requested replacement. No
verification collection member or helper was opened in this fixture, and no
test or live service was run.
