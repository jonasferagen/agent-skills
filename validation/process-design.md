# Process design validation

Scope boundaries worth testing for the [process-design collection](../collections/process-design/COLLECTION.md)
and its [work-records](../collections/process-design/skills/work-records/SKILL.md) member.
This page records intended behaviour and actual results; it establishes no
consumer adoption.

## Intended selection

| Request | Should select | Should not select |
| --- | --- | --- |
| Commission a bounded assignment for another owner | work-records, then the brief template | Any process-page or contract guidance |
| Record what a run produced and what it does not establish | work-records, then the worklog template | The brief, as a results section |
| Compare candidates for an open choice | work-records, then the study template | A project's architecture or planning owner |
| Transfer a result with what the receiver can rely on | work-records, then the handoff template | An existing delivery contract's terms, which stay with that contract |
| Fix a typo in an existing brief | Nothing from this collection | Any record authoring workflow |
| A small task the active plan already tracks with a short result | Nothing from this collection | A brief, worklog and decision record |
| Author or migrate a named process page | The project's own framework | This collection, which does not own that type in 0.1.0 |

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
