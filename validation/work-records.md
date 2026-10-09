# Work records validation

Scope boundaries worth testing for [work-records](../skills/workflow/work-records/SKILL.md).
Until the catalog was flattened on 7 October 2026 this was the page of the
[process-design collection](https://github.com/jonasferagen/agent-skills/blob/914aa01b1915d190ee0429d18a570e72c179fd5d/collections/process-design/COLLECTION.md),
whose only member was work-records; the dated sections below keep that name and
the paths they tested. This page records intended behaviour and actual results;
it establishes no consumer adoption.

## Intended selection

| Request | Should select | Should not select |
| --- | --- | --- |
| Commission a bounded assignment for another owner | work-records, then the project’s work definition | Any process-page or contract guidance |
| Record what a run produced and what it does not establish | work-records, then a dated record | The brief, as a results section |
| Compare candidates for an open choice | work-records, then a comparison record | A project's architecture or planning owner |
| Transfer a result with what the receiver can rely on | work-records, then a transfer record | An existing delivery contract's terms, which stay with that contract |
| Fix a typo in an existing brief | Not work-records | Any record authoring workflow |
| A small task the active plan already tracks with a short result | Not work-records | A brief, worklog and decision record |
| Author or migrate a named process page | The project's own framework | work-records, which does not own that document type |

A record organizes work and grants no authority. A recorded disposition is not
acceptance by an owner who did not give it, and `Workflow: done` is not adoption
of the subject.

## Checker behaviour — verified 2026-10-05

`scripts/validate-work-records.py` over explicitly selected paths, with the
22-case suite in `collections/process-design/tests/`:

- Unselected Markdown is counted and skipped. Run over Forge's ten existing
  briefs, which carry `Brief ID:` without a format line: 0 selected, 10 skipped,
  0 problems. Adoption forces no migration of existing records.
- `Brief ID:` is accepted as an alias of `Record ID:` and reported as such, so a
  consumer already parsing that field keeps working.
- A selected record with an unsupported version fails rather than falling back
  to prose. Missing required fields, reordered or duplicated fields, empty
  values, unknown fields, values outside the closed `Kind`/`Workflow`
  vocabularies, a non-integer or zero revision, an unreal calendar date, an
  uppercase identifier and a non-link `Worklog` are each rejected with their own
  message.
- A copied template whose placeholders are still unfilled is named as such
  rather than reported as a malformed identity line. The four shipped templates
  are intentionally invalid instances; the suite asserts this.
- Directory selection does not follow symlinks, refuses a symlinked selection,
  skips dotted directories including `.git`, and reports a missing path without
  crashing. Duplicate identifiers within one invocation are rejected.

Installation drift, membership, overlay residue, consumer manifest regeneration
and symlink rejection are covered by `tests/test_installation.py` against the
synchronized canonical checker.

## Limits

These are structural and routing checks. They do not establish that a linked
worklog exists or says what the record claims, that criteria are well chosen,
that described work or review occurred, or that any disposition reflects a real
owner's decision. No fresh-context routing trial has been run for this
collection; the selection table above is intended behaviour, not measured
discovery. That trial is covered by an accepted exception recorded below.

## Self-conformance review — 2026-10-05

Reviewed the whole collection for its 0.1.0 release, every file rather than a
diff. The reviewer authored the collection in this session and so did not have a
fresh context; that is a limit on this review, not a passed independence check.
Reviewed working tree content later committed as the tagged release.

### Mechanical checks

| Check | Result |
| --- | --- |
| `scripts/validate-packages.py` | Passed: 22 skill entries, six collections; frontmatter, local link targets and unit containment |
| `collections/process-design/tests` | Passed: 35 tests, zero skipped |
| `scripts/tests` | Passed: 16 tests, including the staged-copy check that covers every inventoried collection |
| Whole-collection whitespace against the empty tree | Clean |
| `scripts/check.py` | Passed: six checks, zero failed, after `npm ci` supplied the declared TypeScript dev dependency |

The earlier report that the full gate could not run no longer applies; the
missing dependency was installed and the gate passes. `package-lock.json` is
unchanged.

### Rules applied and findings

| Rule owner | Covered | Finding and disposition |
| --- | --- | --- |
| Source of truth | Vocabularies, field order, paths and counts across the four references, four templates, member and catalog text | **F-1, fixed.** `Kind` and `Workflow` were defined in both `record-format.md` and `work_record_format.py` with no stated owner, so the two could drift silently. The checker is now named as owning the exact field names and vocabularies, following the `forge-creative-docs/v1` precedent, and three bundled tests fail if the reference and checker disagree. **F-2, fixed.** `COLLECTION.md` restated the process-ownership boundary that `references/extension.md` owns; the entrypoint now states it briefly and links the declaration |
| Source of truth, check design | `work_record_format.py`, `validate-work-records.py` and their tests | No finding. A negative control confirmed the new drift tests fail on a real mismatch: adding `archived` to the documented `Workflow` row failed `test_documented_workflows_match_the_checker`, and the restored text passed |
| Status and evidence | The validation page above, the checker's own limit statements and the templates' claims | No finding. Structural passes are stated as structure only; the selection table is labelled intended behaviour |
| Clear writing | All prose, including the member description, references and template prompts | No finding requiring revision. No passage was rewritten during this review, so no independent prior-text comparison was needed |
| Diagrams and tables | The one Mermaid flowchart in `record-chain.md` and every table | No finding. The diagram is byte-identical to the already-reviewed Forge original it generalizes. Rendered with Mermaid 11 in a browser at a 720px reading width: renders without error, six nodes and six edges matching source, 625px wide so no horizontal overflow, zero overlapping node pairs, 16px labels, all six edge labels present. Verified by rendered structure and geometry; no retained image |
| Project documentation | Links, document ownership, current versus historical text | No finding. All in-package links resolve and stay inside the unit, checked by package validation |
| Routing quality | Entry points, triggers and conditional references | **Exception accepted, below** |
| Application design | Not applicable: the collection produces no application design or runtime helper |  |

### Accepted exception: routing trial

- **Rule:** the [routing acceptance requirement](../README.md#routing-quality),
  which makes practical trials an acceptance condition before a collection release.
- **Reason:** Jonas's judgement that routing defects are better discovered through
  real skill use than through synthetic pre-release trials, and that the
  repository already has mechanisms for this in pattern capture and the
  consuming project's friction capture and repair route.
- **Scope:** this release only. It covers the absent trial, not the standard; the
  README rule is unchanged and still applies to later releases.
- **Accepted by:** Jonas, the repository owner, on 2026-10-05. Proposed by the
  reviewer after reporting the unmet requirement.
- **Review condition:** revisit when real use produces a captured routing
  finding against this collection, or before its next release if no use has
  exercised it. A captured finding is the evidence this exception substitutes for.

The README still states trials as a release requirement, so this release deviates
from a recorded rule under an explicit exception rather than establishing a new
practice. Changing the rule itself remains a separate decision.

### Release

Mechanical checks pass and both material findings are fixed; the routing
requirement is covered by the exception above. Tagged `process-design/v0.1.0`.


## Bounded assignments and separate reports — 2026-10-05

Unreleased source revision 0.2.0 extends work-record guidance. Named-process
ownership and actual project exchange contracts retain their current owners.
The metadata parser and `work-record/v1` field vocabulary are unchanged.
Document purposes are explicit prose/templates, not inferred metadata types.
No Forge installation or existing brief is migrated by this source change.

### Changes and review

- `record-chain.md` owns the distinction between briefs, reports, worklogs,
  studies and handoff records. Its six linked concepts do not require six files.
- `assignment-contract.md` owns bounded assignment splitting, discoverable
  required context, executor discretion and the requested return. Split by
  independent decisions/completion evidence, not length or repository count.
- The brief form separates required inputs, optional background, excluded prior
  results, deliverables and reporting. The new report form records an assessed
  basis, criterion-linked findings, checks, limits and disposition. Worklogs link
  assessments rather than maintaining another copy.
- A report does not automatically close its brief. `ready` is an authored framing
  assessment, not verified prerequisite availability or execution authority.

Clear-writing and its instruction guidance were applied to the changed prose;
diagrams-and-tables and its table guidance were applied to the new document and
assignment-boundary tables. The existing Mermaid view is unchanged. An
independent prose comparison against `e5793d94b239d1bce0ac554e57f90f456da5e582`
found no material unintended authority change, approval gate, mandatory
paperwork or ambiguity requiring repair. The source was then reconciled with
the self-conformance fixes at `a2eec55459ff78d3476ab5ee8b184bbdf85f9ee1`.
That review is evidence about these passages, not consumer readiness.

### Fresh-context routing trials

Three independent agents started from a synthetic project's `AGENTS.md` outside
the authoring repository. It routed bounded work to a complete staged collection
and named-process work to a separate framework owner. They were not given the
expected route. No live Forge state, engine, external generation or service was
used. Trials selected draft 0.2.0 before the later prose tidy and reconciliation;
the assignment contract and template behavior tested are unchanged.

| Request | Observed route and artifact | Result and limit |
| --- | --- | --- |
| Shape creature concepts, models and an encounter into independent work | Collection → work-records → assignment contract, brief/report forms and record chain; proposed three dependent briefs | Each has its own inputs, exclusions, evidence and return; missing domain choices remain explicit. No assets or runtime behavior established |
| Pick up a portrait-rendering brief whose selected geometry exists only in a prior chat | Collection → work-records → assignment contract, report form, record chain and optional record format/checker; returned a partial-work report | Did not invent the selection, use excluded results, redefine the commission or mark rendering complete. Selected report metadata passed; rendering remains unperformed |
| Clarify an existing proposed import process | Project framework and existing process source; collection entry was an optional boundary check | Preserved named-process ownership, source anchor and proposed status. No record skill, parser migration or service selected |

The commissioning trial materially read seven complete instruction/template
files, approximately 3,888 whitespace words. The executor trial read eight
complete files, approximately 4,920 words including its brief source. Both had
one displayed read per file and separate mechanical count/hash rereads, without
truncation. The named-process trial read three instruction files (495 words)
and its 23-word process source, 518 total; it classified the collection entry
as optional and unnecessary once the framework route was resolved. No source
authoring routes were loaded by the consumer trials. No required applicable
guidance was observed missing. The extra collection read is a bounded overhead
observation, not a reason to require that route for process work.

The reviewer inspected all returned artifacts and read traces. These trials
demonstrate assignment framing, missing-input handling, reporting and the nearby
framework boundary. They establish neither successful production from a complete
brief nor routing reliability. There was no matched baseline trial, routine-fix
trial or source-authoring trial. Consumer link/access validation and a real
completed assignment remain useful next evidence; no autonomous execution or
framework migration is claimed.

### Mechanical verification

The complete source gate `PYTHONDONTWRITEBYTECODE=1 python3 scripts/check.py`
passed all six checks with no failures after normal local process access was
provided. A restricted run first failed the unrelated GPG roundtrip and Node
child-process EOF checks; the process-design suite and package checks already
passed there. The successful run used the repository's existing exact TypeScript
dependency through a temporary task-worktree link; no lockfile changed.

The process-design suite, source inventory checker, package link/containment
checks and `git diff --check` pass. The existing template-placeholder check now
covers all five shipped forms. These are structural checks; they do not verify
actual project selections, useful criteria, execution authority or acceptance.

## Settled named-process owner — 2026-10-06

Revision 0.3.0 withdraws the takeover 0.2.0 had recorded as this collection's
next step. The division is now stated as one of document home and subject: a
named process is a standing explanation of recurring work inside the consuming
framework's governed document root, and a work record is a dated document about
one assignment, kept with that work. `review-feedback-section` stays core's as an
in-place section pattern beside this collection's standalone report and worklog,
and neither deprecates the other.

The reason was reader cost, not duplication. Nothing here ever defined the
process format: project-foundation holds the `project-process/v1` reference, the
`process_format.py` parser, the process template, `validate-project-docs.py` and
its tests, and a consumer's own alignment checker loads that parser by path. What
the pendency cost was certainty — a reader had to know which release they held,
and what was planned, before they could say who owns a process page today.

### Changes and verification

| File | Change |
| --- | --- |
| `COLLECTION.md` | Scope boundary states a settled division; version 0.3.0 |
| `references/extension.md` | `## Not owned by this release` becomes `## Owned by the project framework`, states the home-and-subject division, settles `review-feedback-section`, and records the withdrawal |
| `references/installation.md` | `## Watch for a second owner` becomes `## One owner per document type`: no upgrade moves the type, and two active definitions of one type are the defect to repair |
| `references/assignment-contract.md` | Drops "in this release" and follows the renamed anchor |
| `README.md` | Catalog entry drops "in this release" and links the boundary |
| `collection.json` | Version and the five changed hashes |

Both inbound links to the renamed anchor were updated; no other file referenced
it. Mechanical verification: the collection's own `check_installation.py`
regenerated and then re-validated the inventory at 18 files and one member;
`scripts/validate-packages.py` passed 22 entries and six collections;
`scripts/check.py` passed all six checks with zero failures, using the
repository's existing TypeScript dependency through a temporary worktree link
with no lockfile change; `git diff --check` clean.

This is a prose-only change to scope statements, so no discovery trial applies
under the README's routing requirement. No template, script, check or metadata
behaviour changes, and no existing record is reclassified. The structural checks
establish the package's shape; they do not establish that a consuming project
has reconciled its own routes, which is that project's own change. Reopening the
transfer would be a new decision in both collections, with its own migration,
deprecation path and version impact.

## Generic shapes and standalone methods — 2026-10-09

Version 1.0.0 removes the five templates and assigns concrete shape ownership to
the consuming project or framework. The [source and trial record](document-shapes-2026-10-09.md)
retains the compatibility review, standalone consumer output and verification.
Earlier sections describe the revisions they tested; their old template paths are
historical evidence, not current authoring routes.
