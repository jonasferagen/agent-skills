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
collection yet; the selection table above is intended behaviour, not measured
discovery. Meet the [routing acceptance requirement](../README.md#routing-quality)
before a release tag.
