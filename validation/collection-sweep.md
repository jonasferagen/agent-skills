# Collection quality and consistency sweep — 4 October 2026

This source sweep started at `a30ca1bb83591bfaa2ad67272163f98a730a5db4` in
the isolated `review/collection-sweep` worktree. The user confirmed that
“forge-foundation” meant project-foundation. Subagents reviewed each collection's
individual skills and resources before reviewing its consistency; the coordinator
reviewed the combined changes and shared packaging. Assignments ran within the
available concurrency, with subagent contexts reused for later collection
reviews and cross-evaluations.

## Coverage and changes

| Collection | Member coverage | Main changes | Detailed review |
| --- | --- | --- | --- |
| Application | application-design and both references | Design scope, conditional retention, record privacy, run-record route and installation integrity | [Application sweep](application-foundation-sweep.md) |
| Service | service-boundaries and runtime-operations, including helpers | Runtime-helper conformance and isolated verification | [Service sweep](service-foundation-sweep.md) |
| Python | python-design, python-patterns and all eight references | Text-file contracts, async/text-I/O routes and generator source links | [Python sweep](python-foundation-sweep.md) |
| TypeScript | typescript-design, typescript-patterns, node-patterns and all sixteen references | Strict/sparse tuple validation, record completeness, nominal markers, symbol links and process outcomes | [TypeScript sweep](typescript-foundation-sweep.md) |
| Verification | verification-design, test-writing, test-audit and all references | Evidence/task handoffs, strict-double limits, isolated integration boundaries and preserved privacy/gates | [Verification sweep](verification-foundation-sweep.md) |
| Project | All nine members, references, templates and helpers | Mapped document owners, descendant-index enforcement, complete installation checking and artifact identity | [Project sweep](https://github.com/jonasferagen/agent-skills/blob/9093cfca4ffa93df1be35b1bb7ebffaef0baac65/validation/project-foundation-sweep.md) |

The shared packaging change adds inventories and installation checkers to
application-foundation and project-foundation. All six now use the canonical
checker in `scripts/collection_installation.py`. Package validation requires each
inventory and rejects unsynchronized checkers. The checker rejects non-string and
malformed collection versions under [SemVer](https://semver.org/), and its success
message names the installation root it actually measured. Member metadata now
uses the same version contract. A regression exposed a preexisting frontmatter
parser defect: it split inside a valid prerelease containing `---`. Delimiters
now match complete lines, and that case passed after first failing. JSON and
Markdown reads declare UTF-8. Shared tests use synthetic trees and discover
inventories rather than copying collection names.

Self-conformance instructions now select each helper's actual test directory,
including nested member helpers, and distinguish absent coverage from a passing
test run. Bootstrap's old standalone scenarios are explicitly historical.
The undated diagram expectation now agrees with the maintained Mermaid direction
guidance and its [documented limitation](https://mermaid.js.org/syntax/flowchart.html#direction-in-subgraphs).
No diagram source changed, so this correction claims no new render result.

A Python consumer review also found that an example described JSON syntax
translation as generic decoding failure. Its explanation now distinguishes JSON
syntax from text decoding, file acquisition and application-schema validation;
the example's code and routing are unchanged.

## Coordinated verification

The final source checks passed:

- `scripts/validate-packages.py`: 27 skill entries across six collections,
  including all 20 reviewed members. The seven standalone entries received
  structural package checking, not an individual quality sweep.
- All six inventories were reconciled to their declared versions and regenerated
  after reviewed edits. Application and project now have the same inventory
  contract as the other collections. The shared suite checks staged copies from
  an unrelated working directory and rejects a modified entrypoint.
- 76 helper tests, with no skips: five shared packaging tests, 11 installation
  tests, 26 project-doc validator tests and 34 runtime-helper tests.
- All 20 collection members passed Skill Creator's `quick_validate.py`.
- Package validation also passed under an ASCII locale with Python UTF-8 mode
  disabled. `git diff --check` passed.
- Maintained authoring-document links and collection-local Markdown destinations
  and heading fragments were checked separately, with no missing targets found.

The runtime suite used temporary synthetic GnuPG material outside the sandbox
because its agent could not launch inside it. Credential, systemd, Docker and
database boundaries were mocked. This establishes tested helper behavior, not
live daemon cleanup, provider access or a real database restore. The TypeScript
review separately checked examples using TypeScript 5.9.3 and Node 24.15; Python
examples were probed on CPython 3.14.4. Python 3.10 grammar was checked where
required, but a native 3.10 runtime was unavailable.

Individual review pages preserve the checks actually run and transient failures
while other agents were editing. Retained consumer evidence is linked below;
these are bounded cross-evaluations with reused reviewer context, not blind
fresh-context trials or a test of automatic host discovery.

| Consumer cases | Retained evidence |
| --- | --- |
| Python: async cleanup, declared text encoding, wording-only change | [Reads, requests, answers and probe output](collection-sweep-trials/python.md) |
| Verification: regression, evidence plan, read-only audit, wording-only change | [Reads, requests, answers and regression output](collection-sweep-trials/verification.md) |
| Application: pure calculation, provider status, local run records, wording-only change | [Reads, requests and answers](collection-sweep-trials/application.md) |
| Project: installation explanation, mapped workflow homes, wording-only change | [Reads, requests and answers](collection-sweep-trials/project.md) |
| Service: ordinary PostgreSQL helper fit, maintained HTTP-service transition | [Draft and final reads, requests, answers and final inventory](collection-sweep-trials/service.md) |

These 16 distinct cases reached their needed guidance and preserved the requested
scope. Wording-only cases avoided skill bodies. Service's two cases were repeated
against complete final source-checked copies after its initial draft fixtures
showed stale inventories and subsequently clarified timeout cleanup. Both draft
answers and the informed second pass remain recorded; the repeats are not
independent fresh cases. TypeScript's changed examples had compiler/runtime
probes, without a new routing trial because its triggers and routes did not change.

The Python async probe covered ordinary sibling failure, task-creation failure and
one caller cancellation. Repeated cancellation during cleanup awaits was not
tested, and is outside that bounded example's demonstrated guarantee. Reading
counts record displayed material rather than total model context or a controlled
efficiency comparison. The Python JSON explanation correction followed its trial;
the retained trial copy was preserved and that wording alone was not re-evaluated.

## Further improvements

1. Put package checks and bundled helper suites in one maintained CI job. Keep
   routing trials separate from structural validation and report missing host
   prerequisites explicitly.
2. Add narrow compiler/runtime checks for executable examples, starting with
   strict TypeScript tuples and Node process outcomes. Use supported project
   versions; avoid introducing a universal toolchain upgrade.
3. Maintain reproducible consumer-routing fixtures for changed task boundaries,
   including nearby requests that should avoid the skill. Re-run them before a
   collection release and preserve read/behavior evidence, not wording goldens.
4. Add current-review pointers to older member validation pages as they receive
   new evidence. Preserve dated outcomes, source pins and their original limits.
   The new collection reports and this index supply the current sweep's route.

These are follow-up candidates, not adopted gates or newly created skills. Source
review and bounded trials do not establish live provider behavior, automatic host
discovery, platform-wide reliability or release readiness. This task leaves
reviewable source changes in its worktree; it does not update Forge's installed
pins or publish releases.

## Merge review — 4 October 2026

A separate reviewer inspected the uncommitted sweep in its existing worktree,
including the changed helpers and tests, packaging, guidance and retained routing
evidence. The branch started at `a30ca1bb83591bfaa2ad67272163f98a730a5db4`;
local main had advanced to `2196a0ae042d2b53f660b06a2fa1b9c124a0ac66`.
The existing consumer trials were reviewed, not rerun in fresh contexts.

One helper defect was repaired before integration. The wrong-passphrase parser
matched the last token's suffix instead of the ERROR status's code field. It
missed a bare `BAD_PASSPHRASE` and a code followed by detail, and could classify an
unrelated code or trailing detail as verified denial. The
[GnuPG status contract](https://raw.githubusercontent.com/gpg/gnupg/master/doc/DETAILS)
allows symbolic codes, optional numeric prefixes and optional trailing fields.
The parser now checks that field exactly while still requiring decryption
failure. Four added subcases failed against the original sweep parser, then
passed after the repair; inputs are synthetic public-contract examples.

Before integration, package validation and all 76 helper tests passed without
skips. The sandbox initially prevented GnuPG's temporary agent from starting;
the isolated runtime suite passed outside the sandbox. Database, credential and
service boundaries remained mocked. This adds no live Docker, systemd, provider
or database recovery evidence and does not remove the trial limits above.

Integration preserves main's optional repository-format template and shared-format
ownership guidance. Project-foundation is `1.3.0`, combining that newer `1.2.0`
content with the sweep's installation capability; project-docs is `6.2.1` rather
than reverting main's `6.2.0`. Its regenerated inventory contains 83 files and
nine members. The staged whitespace check also caught and removed one trailing
space in the newly tracked verification-trial transcript.

The combined tree passed `python3 -B scripts/validate-packages.py` (27 skills,
six collections), the shared packaging suite (five tests), and the project helper
suite (26 tests). Package validation also passed with `LC_ALL=C`,
`PYTHONUTF8=0` and `PYTHONCOERCECLOCALE=0`. The previously passed installation
suite (11 tests) and repaired runtime suite (34 tests) were unchanged by integration.
A separate Markdown scan checked 568 local destinations and heading fragments
in 138 files, with no missing targets. No material finding remains for local
landing; this review does not tag a release or update consumer installations.


## Follow-up sweep — 4 October 2026

The follow-up adds one maintained source command, `python3 scripts/check.py`,
and CI using that command on Python 3.11 and 3.14 with Node 24. Its declared
prerequisites include GnuPG and the locked TypeScript 5.9.3 compiler; missing
prerequisites, empty suites, failures, skips and timeouts cannot report success.
The command discovers nested helper suites rather than maintaining a duplicate
list. It checks every collection inventory through package validation.

The example probes extract the published tuple and `outcomeOf` code blocks,
compile the tuple with strict checking and `noUncheckedIndexedAccess`, and execute
valid, short, long, sparse, non-number and non-finite inputs. Real Node child
processes cover successful and failed exits, missing executables, timeout,
overflow, abort, EOF, external signals and a child that exits zero after wrapper
cancellation. The wrapper's decision remains separate from the child's outcome.
These source dependencies do not change consuming projects' selected toolchains.

Running the complete check under an ASCII locale exposed default-encoding reads
in the project foundation fixture and both project validators. Their Markdown
inputs now specify UTF-8, and project-foundation is patched to 1.3.1 with a reviewed
inventory. All 82 tests and package checks passed under that locale on Python
3.14.4, Node 24.15.0 and TypeScript 5.9.3, including the real GnuPG round trip.
The configured GitHub workflow has not run remotely; Python 3.11 is unavailable
locally. Action configuration was checked against the official
[checkout](https://github.com/actions/checkout/blob/v5/README.md),
[Python](https://github.com/actions/setup-python/blob/v6/README.md) and
[Node](https://github.com/actions/setup-node/blob/v6/README.md) documentation.

Three independent agents evaluated fresh consumer contexts with complete copied
collections and minimal project inputs. They received realistic requests without
expected routes, prior conclusions or proposed fixes. Retained raw requests,
reads, commands and answers are [focused Python](https://github.com/jonasferagen/agent-skills/blob/9093cfca4ffa93df1be35b1bb7ebffaef0baac65/validation/collection-followup-trials/focused.md),
[maintained service](https://github.com/jonasferagen/agent-skills/blob/9093cfca4ffa93df1be35b1bb7ebffaef0baac65/validation/collection-followup-trials/boundary.md) and
[literal wording](https://github.com/jonasferagen/agent-skills/blob/9093cfca4ffa93df1be35b1bb7ebffaef0baac65/validation/collection-followup-trials/literal.md). Their distinct guidance
read counts and whitespace-delimited word totals were 12/5,969, 19/8,924 and
6/1,550, including local instructions/foundation. No guidance was reread or
truncated; all consulted routes resolved. The focused task reproduced its bug,
verified UTF-8 receipt bytes and avoided class redesign. The service plan reached
both members and preserved review-only scope and unselected infrastructure.
The wording change preserved the actual exit behavior without a service or
language implementation pass. It read two additional collection indexes to
check task fit; this is reading cost, not a missing boundary route.

[Prepare fresh fixtures](https://github.com/jonasferagen/agent-skills/blob/9093cfca4ffa93df1be35b1bb7ebffaef0baac65/validation/collection-followup-trials/prepare.py) in a new directory
outside the authoring repository, for example
`python3 validation/collection-followup-trials/prepare.py /tmp/new-consumer-trials`.
Preparation was executed successfully. Input fixtures preserve the starting state;
result artifacts are retained separately. Future evaluators should receive only
their prepared input, request and scope. These three trials are a bounded sample,
not coverage of all skill routes, live systems or artistic acceptance. No further
routing correction is supported by this pass. Forge installation and consumer
alignment evidence belong to Primary's adoption record.
