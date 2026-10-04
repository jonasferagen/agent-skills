# Companion collections — 2026-10-04

## Scope

The service collection pilot established whole-group installation, explicit task
routing and inventory checks. This follow-up groups Python, TypeScript/Node tooling
and verification companions using the same model. All 45 moved member files remain
byte-for-byte identical to source commit `a2019e3809e57698b704db9be22f762e80f8e9a2`.
No member behavior, invocation name or language/toolchain adoption is implied by
moving a directory.

The canonical checker is maintained in one source file and copied into complete
installation units. The source package validator detects diverging distributed
copies. Existing public helper functions remain compatible; this change generalizes
collection identity without reshaping those APIs. Consumers need no external helper
at runtime. The source sync tool updates only checker copies and never regenerates
inventories or silently accepts member drift.

## Applied guidance

Skill-creator and clear-writing/instruction guidance informed collection boundaries
and conditional loading. Diagrams-and-tables informed the task matrices.
Verification-design, test-writing and Python patterns guided the checker tests;
Python design's preservation of public contracts kept the existing helper API.
No provider documentation or live account was needed for these packaging changes.

## Checks

- `python3 scripts/validate-packages.py`: 27 entries, six collections.
- Self-checks: Python 15 files/two members; TypeScript 25 files/three members;
  verification 14 files/three members; service 12 files/two members.
- `python3 -m unittest discover -s collections/service-foundation/tests -q`:
  11 passed, zero skipped. New cases exercise the three collection identities and
  rejection of a different collection's manifest. Prior drift/membership cases
  remain in place. The earlier drift-guard mutation is retained in pilot evidence.
- A temporary changed distributed checker made top-level validation fail on its
  mismatch with canonical source; restoring the bytes returned validation to passing.
- Member code did not change, so its runtime and product suites were not repeated.

## Routing evidence

Fresh-context consumers outside the source repository use complete installed draft
copies, local project hooks and synthetic constraints. Prompts name ordinary tasks
rather than expected member selections. Native client discovery is not exercised.
The parent reviewed the [retained reports](companion-collection-trials/), their
read accounting and exact negative-case bytes. Each run demonstrates its route;
repeated-run reliability is not claimed.

| Ordinary task | Observed route | Unique instruction words | Result |
| --- | --- | ---: | --- |
| [Python importer design](companion-collection-trials/python-active.md) | Both Python members and verification design | 3,985 | Explicit validation, immutable output and caller-owned stream lifetime; honest unexecuted plan |
| [TypeScript CLI design](companion-collection-trials/typescript-active.md) | Both TypeScript members, Node patterns and verification design | 11,634 | Distinct process outcomes, bounded capture and cleanup, no shell interpolation; honest unexecuted plan |
| [Active parser regression sketch](companion-collection-trials/verification-active.md) | Verification design and test writing | 4,000 | Specific rejection plus caller-input preservation; no suite audit or invented passing run |
| [Settled-suite audit](companion-collection-trials/verification-audit.md) | Test audit only | 1,288 | One real test passed; two incorrect substitutions also passed, demonstrating assertion weakness; source unchanged |
| [Python literal edit](companion-collection-trials/python-wording.md) | Project instructions only | 77 | Exact spelling replacement; no collection loaded |
| [TypeScript literal edit](companion-collection-trials/typescript-wording.md) | Project instructions only | 77 | Exact spelling replacement; no collection loaded |
| [Verification literal edit](companion-collection-trials/verification-wording.md) | Project instructions only | 77 | Exact spelling replacement; no collection loaded |

The TypeScript trial reread two references after a globally truncated tool response,
adding about 2,186 words. Its larger unique load comes from existing design/type
references; some sections had low value for this particular operation. That is
retained as a loading-cost limit, not treated as a reason to expand this packaging
change into member redesign. All other displayed instruction reads were complete
and unrepeated; mechanical counting reads are disclosed separately in reports.
No installation guide, source catalog or unrelated member was selected in these
consumer tasks. No code compilation or importer/process runtime correctness is
claimed by a design trial.

## Limits

No release tags, publishing, remote dependency resolver or automatic client
registration are selected. A future release still needs collection self-conformance.
The new language design members apply to scoped design tasks under project constraints;
installation alone grants no repository-wide rewrite. Bash, Godot, containerization
and data-specific packages remain in their existing homes.
