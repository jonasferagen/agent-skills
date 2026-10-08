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

## 2026-10-07 — one owner for adoption, one owner for the binding

Unreleased collection revision 0.7.0 answers the two routing findings the
import-contract trial left open. `references/extension.md` had restated
project-foundation's adopted-extensions contract almost item for item: what to
record, the shared-installation rule and the authority boundary. It now delegates
all three and keeps only what is service-specific, so a project reads that
contract once, from the project system that owns it. The collection still
requires no project-foundation installation; another project system declares
equivalent explicit routes in its own instructions. Its discovery section stops
restating the repository convention's layout and routes to it instead.

`references/runtime-helpers.md` gained the binding surface the previous trial had
to read from helper source: every `Service` field with what omitting it selects,
the constraints between fields, and how the five actions behave. The reference now
also states the offered interface version, which a consumer must pin and could
previously only find in the declaration's source. `runtime-operations` 1.6.0
routes to it and says to read it rather than infer the binding from the helper.

Verification: `python3 scripts/check.py` passed all six check groups with no
skips. Runtime tests rose from 39 to 50, pinning each documented omission as
behavior rather than prose: an absent `command` operating an installed unit, an
absent `directory` comparing nothing, `environment` reaching a transient launch
and never an installed unit, the transient port range, the structured-health
prerequisites, `status`'s exit status, a stop on an unloaded unit, a skipped
prerequisite on an already-active start, and the readiness bound. Collection
tests rose from 45 to 46 with a drift check between the stated interface and the
declaration. Three disposable mutations were exercised: accepting any port for a
transient command, leaking `environment` into an installed unit, and bumping the
declared minor version. Each failed the suite; the intact suite passed. The
reviewed inventory contains 29 files and two members. `git diff --check` passed.

Fresh-context routing trial [`http-binding`](service-foundation-trials/http-binding.md)
defined an HTTP service in a consumer whose adoption was already declared. It took
the binding entirely from the reference and stated that it opened no helper
implementation; the previous trial had read 687 words of `serviceControl.py` for
the same decisions. `extension.md` fell from a required restatement to a useful
confirmation, and the generic contract was read once from project-foundation.
Three gaps it found were fixed in this revision; a fourth report was a fixture
defect, not a product defect, and is recorded as such.

Limits: nothing was installed, started or enabled in either trial, so no control
action, readiness result or recovery path is evidenced here. Interface
compatibility is still exercised only against major 1. The adoption delegation is
verified by one trial against project-foundation 5.4.1; an earlier foundation or
another project system remains unexercised.

## 2026-10-07 — the scheduled service class

Unreleased collection revision 0.9.0 names two classes of service where the
convention previously assumed one. A **running** service holds a process while it
serves, so readiness is a live property. A **scheduled** service holds none
between runs: a schedule is what is installed, each run is a finite job, and
readiness is not a property it has. The five actions keep their names and operate
the schedule, with `status` owing the schedule, the last run and the durable
record of the last success together, because an active schedule read alone looks
like a working backup.

The review that prompted this found the gap in a working service rather than in
the guidance: the one real instance had opted out of the shared helper, redefined
`status`, and declared in its own guide that it was the only service starting
without being asked. Both properties now follow from its class. `runtime-operations`
1.7.0 owns what an unattended run may touch, generalized from that instance:
safe at the moment it happens because nobody chooses that moment, no attended
precondition, declining rather than taking a lock in use, one lock shared with
manual invocation, evidence kept outside the unit, and a stated decision about a
missed window, since skipping silently is the failure that looks like success.
`service-definition/v1` gains the scheduled shape, where `Readiness` is `None`
as the honest value rather than a gap.

Verification: `python3 scripts/check.py` passed all six check groups with no
skips; 47 collection tests and 50 runtime tests, unchanged in count, since this
revision adds guidance and no checked behavior. The reviewed inventory contains
29 files and two members. `git diff --check` passed.

Applied to the real instance in the consuming workspace: the off-host backup
guide dropped both self-justifications, adopted `service-definition/v1` with
`Readiness` as `None`, and now routes its class to this convention. The structural
checker rejected a first attempt that put explanatory prose inside the definition
table, which is the format behaving as specified. Running that service's `status`
to confirm the class description corrected the guide's own `Status` field: the
timer is installed and a scheduled run has shipped, which a stale note had denied.
That is the class's own rule paying for itself within an hour of being written.

Fresh-context routing trial [`scheduled-service`](service-foundation-trials/scheduled-service.md)
gave a consumer an operator request whose obvious design was partly
unschedulable. It scheduled only the already-finished work and left the
lock-taking build command alone, reaching from the guidance the conclusion the
real instance had reached from experience. It found one rule written too
absolutely, which was fixed in this revision, and one recurring departure, which
the convention now states as the class's expected shape.

Limits: nothing was installed, started or enabled in the trial, so this revision
is verified as guidance a consumer can follow, not as a running schedule. Whether
the shared helper should gain a schedule binding stays open; one real instance is
not a basis for that interface, and both current implementations own their units.
No release tag was created.

## 2026-10-07 — what a project-wide launch may touch

The convention gained a second closed vocabulary, `lifecycle`, on the report line:
`maintained`, `environment`, `scheduled`, `on-demand`. The report section states
which of them a project-wide launch acts on, why a state cannot answer that
question, and that an undeclared or unreadable class is unclassified and skipped.

It also states where such a launch belongs, which is the finding this revision
rests on. A consuming project proposed extending its dispatcher's bare `status`
form to `start` and `stop` with the same project-wide scope. That contradicts this
convention's own rule that reading is project-wide while mutation stays
checkout-local, and it would give each repository's dispatcher authority over the
others' runtime state — neither consequence was visible in the proposal. The
convention now says a launch is composed where the repositories are already
declared together, from the named checkout-local starts the dispatchers already
provide, and that the dispatcher keeps its five named actions.

This means the dispatcher template is unchanged by this revision, and so is the
convention's rule. Only the report line grew, which is the cheapest shape the
capability has: one optional key, and one keyword argument per controller that
adopts it.

Limits: guidance and a checked helper contract, with no controller declaring a
class and no launch reading one, so nothing here is verified as a working launch.
`python3 scripts/check.py` passes all five checks; `git diff --check` passes. The
same reasoning applied to a real instance is recorded by that project, not here.
No release tag was created.

## 2026-10-09 — members are named, not read out of a document

The dispatcher found the project's other checkouts by parsing a `## References`
table out of `project-docs/foundation.md`: a regex over two-column Markdown rows,
with a path resolved relative to that file, and a member without an executable
dispatcher reported only when that same file existed beside it. The location
belonged to a document layout the consuming project has since retired, so the
discovery path led to a file that no longer exists there and the project-wide form
silently reported one checkout.

Members are now named explicitly: repeated `--checkout` for one run, or
`SERVICE_CHECKOUTS` once for a project whose members do not change. A relative
value resolves against the selected checkout. Every named member is reported,
including one with no service home, which is no longer dropped for failing to look
like a repository — it was named deliberately, so silence about it is wrong. The
key in the `== key (path)` header is the checkout's directory name instead of a
table key. `--checkout` is rejected with a named service, as `--scope` and
`--report` already were. The repository-services manifest goes to 0.3.0: a default
is removed and consumers must supply what the parser used to guess.

Replacing the parser rather than pointing it at a different file is the decision
worth recording. A dispatcher reading a document cannot distinguish a stale row
from a member that is deliberately absent, and the table it read is written for a
reader, not for a program. The consuming project's own rule now keeps such paths
in one declared place; which place that is remains the project's choice, and a
program takes its members as an argument either way.

Checks: the package's 44 tests pass, including the rewritten project-wide case,
a new case for the environment form and a new case rejecting `--checkout` with a
named service. The repository check passes all five checks and the whitespace
check is clean. The earlier trial records under
`validation/service-foundation-trials/` describe the previous dispatcher and are
left as the observations they were; no release tag was created, and no consuming
project has been re-imported at this revision.

## Checked package copies — 2026-10-09

Repository-services 0.3.1 identifies the report schema and vocabulary owner
and preserves the standalone dispatcher and 0.3.0 member-selection interface.
The [reference-sharing sweep](reference-sharing-sweep.md) records checks,
compatibility evidence and remaining review limits.
