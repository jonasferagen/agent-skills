# Service foundation pilot — 2026-10-04

## Scope and mechanism

The Forge reader transition installed application-foundation but missed service
and runtime companion guidance. The companion list existed only in installation
material that ordinary consumers correctly skip. This pilot packages the two
service members together, routes maintained-service transitions to both, adds a
missing-service-guidance signal to ordinary application discovery, and verifies
whole-collection installation against an explicit inventory. It does not select
other collections or change member behavior.

Skill-creator informed the bounded entrypoint; clear-writing and its instruction
reference informed scope and update wording; diagrams-and-tables informed the task
matrix. Python-patterns, verification-design and test-writing informed the checker
and synthetic fixtures. Pattern-capture distinguished this observed routing gap
from the broader, still-proposed language and verification regrouping.

## Structural and behavioral checks

- All eight relocated member files matched their prior source bytes at
  `f0f3cf6c44759585b138b75636bbf1c44c4df748`; member names and versions are retained.
- `python3 scripts/validate-packages.py`: 27 skill entries, three collections.
- `python3 collections/service-foundation/scripts/check_installation.py`: 12 files,
  two members. Inventory includes the checker and its tests.
- `python3 -m unittest discover -s collections/service-foundation/tests -q`:
  nine passed, zero skipped. Missing membership, drift, retired overlay files,
  tampered manifest, empty inventory, missing route, undeclared member and symlink
  cases are exercised. A disposable mutation disabled the drift guard; modified
  and extra-file tests then failed.
- `python3 -m unittest discover -s collections/service-foundation/skills/runtime-operations/tests -q`:
  12 passed, zero skipped, with GnuPG available. No live credential or service was
  used. The collection's helpers are moved intact, not newly audited or repaired.

## Fresh-context routing trials

Fixtures outside the source repository held a complete collection copy, a project
AGENTS hook, synthetic project constraints and draft provenance. Agents received
ordinary tasks rather than expected routes, with no shared conversation context.
They could not inspect the source repository or other fixtures. Entry was through
project instructions; native client automatic discovery was not exercised. The
parent reviewed retained outputs and the literal edit's exact bytes.

| Case | Result | Displayed guidance/source words |
| --- | --- | --- |
| Promote a local catalog reader to maintained service use | Read both members; retained localhost, read-only and installed user-session choice; produced design and verification plan without provisioning | 2,363 |
| Application design with no service companion installed | Reported the missing runtime/service prerequisite and continued bounded application design without provisioning | 1,015 |
| Correct one spelling error in an operational guide | Read only project hook/scope and target; no collection activation; exact replacement verified | 96 instruction words, target excluded |
| Assess a staged collection update with a local member edit | Candidate passed; installed drift rejected; required preservation and a precise source pin before replacement; installation left unchanged | 2,802 |

The [transition result](service-foundation-trials/transition.md) and
[upgrade result](service-foundation-trials/upgrade.md) retain artifacts and read
accounting; the [wording record](service-foundation-trials/wording.md) retains its
countercheck. The [missing-companion result](service-foundation-trials/missing-companion.md)
and [read record](service-foundation-trials/missing-companion-reads.md) exercise
application-foundation 0.1.1's new ordinary-work route. No displayed reads were truncated. Mechanical word counts are
excluded from displayed instruction counts; these are not token totals.

The transition loaded the whole runtime member, including credential and database
sections irrelevant to this credential-free reader. That is a potential later
internal-routing improvement; this pilot does not split the member or claim reduced
context use. The upgrade intentionally reads changed guidance. Its missing precise
source pin is an explicit synthetic-fixture limitation, not a claimed installation.

## Limits

Each case demonstrates one route, not selection reliability across repeated runs.
No fresh source-authoring trial, native client registration, release tagging,
automatic updater or remote package resolution is claimed. Collection-level
self-conformance remains required before a future release tag. Project-local
adoption must retain source pins, compare old copies before removal and test its
actual instruction routes. No service runtime behavior changes with this packaging.

The repository package validator invokes installation checks for collections with
a manifest. A temporary member edit made that top-level validator fail on inventory
drift; restoring the bytes returned all 27 entries/three collections to passing.
This makes the authoring check catch forgotten inventory updates without relying
on an agent remembering the collection-specific command. It never rewrites an
inventory automatically.

## Optional service document extension — 2026-10-04

The user selected service-foundation as the single owner of repository-service
documentation and controls conventions. Version 0.4.0 moves the reference,
index/guide/dispatcher templates, structural validator and two scaffold test suites
from project-foundation `82aa3f4`. Their executable bytes and modes are unchanged.
Core 5.0.0 retains general extension adoption; the service extension has no core
runtime/tooling dependency. Existing projects can declare equivalent instruction
routes without adopting core. The collection's extension and installation guides
own migration; existing service paths, commands and guarantees are preserved.

Source `scripts/check.py` passed all five groups with 82 tests. Three fresh-context
consumer trials reached the service checker and its limits, both members for a
maintained-service transition, and local docs without service scaffolding for a
finite CLI. Unique displayed reads were 2,515, 14,104 and 3,120 words respectively;
no truncation or repeated content displays, and no live controls or source catalog
reads. The transition loaded unnecessary authoring guidance and unused sections
of broad references; ordinary-service entry loaded avoidable collection indexes.
Those limits remain; no context-reduction or routing-reliability claim is made.
Detailed evaluator accounting is retained by project-foundation's
`validation/service-extension.md` for the coordinated source migration.

The collection inventory was regenerated only in source. Forge separately records
committed pins, complete-copy adoption and repository validation. No release tag
or remote publication is selected by this task.


## 2026-10-04 — opt-in structured definitions

Unreleased collection revision 0.5.0 adds `service-definition/v1` inside existing
service guides, a standalone parser, and bounded discovery of selected homes.
The format owns field shape and routes; repositories own the values and local
operating prose. Existing guides need no migration. No runtime control changed.

Verification: `python3 scripts/check.py` passed all five check groups with no
skips; 32 collection tests include eight parser/discovery cases and two new
validator cases. An isolated mutation removing the version guard made
`test_unknown_or_duplicate_versions_are_rejected` fail; the intact suite passed.
The reviewed source inventory contains 25 files and two members. `git diff
--check` passed. These checks establish format/discovery behavior, not the truth
of consumer service claims or live readiness. No release tag was created.

Fresh-context routing trial `structured_routing` began with only the collection
entrypoint and a synthetic existing-guide/browser scenario. Actual reads:
`COLLECTION.md` → `references/extension.md` →
`references/service-definition.md` and `references/repository-services.md`.
The trial correctly identified per-guide opt-in, the extension format owner,
project adoption authority, repository prose/fact ownership, and the checker’s
structural limits. It did not load boundary/runtime skills, source history or
unrelated guidance, and operated no services. No routing finding remained.

## 2026-10-07 — a checked import contract for the runtime helpers

Unreleased collection revision 0.6.0 adds `runtimeApi`, which declares the
importable interface the bundled helpers offer, and a copy-deployed loader that
admits it. The review that prompted it found three consumer repositories had each
invented their own way in — a relative path append, a regex over a project
Markdown table, and a third copy of that regex inline — none asserting a version,
while installation replaces the whole directory at once. Discovery stays with the
project, which is the only owner that knows its own layout; admission becomes the
collection's. `runtime-operations` 1.5.0 routes to the contract and forbids an
unchecked path append. No member behavior, control action or service document
changed, and the interface is versioned separately from both the skill's prose
version and the collection version.

Verification: `python3 scripts/check.py` passed all six check groups with no
skips. Collection tests rose from 32 to 45; the 13 new cases are the first
coverage the copy-deployed templates have had, exercising the loader's refusals
(wrong major, absent minor surface, missing declaration, missing and symlinked
directory, non-integer version), that a refusal leaves `sys.path` unchanged, and
the dispatcher's option pass-through that 0.5.0 had dropped unnoticed. The
reviewed inventory contains 29 files and two members. `git diff --check` passed
and `scripts/sync-collection-tools.py` reported no drift.

Fresh-context routing trial [`consumer-controller`](service-foundation-trials/consumer-controller.md)
defined a service in a consumer fixture holding no installation, entering from its
own `AGENTS.md`. It reached `references/runtime-helpers.md` unprompted, deployed
the loader verbatim, named the offered interface, kept discovery in its own
function, and recorded the collection's stated check limits rather than claiming
readiness. Three routing findings remain, recorded in that trial.

One trial finding was folded back immediately: the trial resolved a declared
relative route against the wrong directory, caught it with its own test and fixed
it. Two of this workspace's three existing consumers had made the same choice,
one correctly and one surviving only because the declared target is absolute.
The reference now states where a declared route resolves.

Limits: the trial installed, started and enabled nothing, so no action that
changes runtime state is evidence here. Interface compatibility is exercised only
against major 1; a major replacement still requires reviewing each consumer. The
version check cannot make an incompatible replacement safe — it moves the failure
to the importing controller and names both sides. No release tag was created.
