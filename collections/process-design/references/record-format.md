# Structured work records

Use this reference when deliberately preparing a work record for consistent
reading or machine browsing. Ordinary authoring and prose corrections need no
format selection. Placement stays owned by the project's document conventions;
status stays owned by the record itself.

## Select the format

A record opts in with `Record format: work-record/v1` on its own paragraph
directly after the title. Records without that line remain valid and are not
checked. Installing or upgrading this collection opts nothing in. A selected
record with an unsupported version or a malformed block fails the checker rather
than silently falling back to prose.

Document purposes such as brief, report and worklog are defined by the
[record chain](record-chain.md). They are not values of `Kind`, which describes
the assignment's purpose. This version adds no metadata field for document type
or brief-to-report associations; consumers must not infer them from `Kind`.

Selection makes a record's identity and coordination fields consistent. It does
not establish that the described work happened, was reviewed or was accepted.

## The metadata block

A selected record starts with its title, a blank line, the format line, a blank
line, then the metadata lines in this order:

```text
# Party portrait card — graphical rendering

Record format: work-record/v1

Record ID: `hud-portrait-card-graphics` · Revision: 1 · Date: 2026-10-05
Kind: concept
Workflow: ready
Owner: Primary — brief and review; UI artist — delivery; Jonas — selection.
Status: Designer 2B is the selected layout basis. Finished art is still open.
Worklog: [Work record](../templates/repository-docs/work-records/worklog.md)
```

Lines appear in this order; present fields keep it, absent ones leave no gap.
The [checker](../scripts/work_record_format.py) owns the exact field names and
the closed `Kind` and `Workflow` vocabularies; this table explains how to apply
them, and a bundled test fails if the two disagree.

| Field | Required | Value |
| --- | --- | --- |
| `Record ID` | Yes | A backticked lowercase hyphenated identifier, unique within the checked root. `Brief ID` is an accepted alias, retained for records and readers that already use it; a record uses exactly one of the two |
| `Revision` | Yes | A positive integer on the identity line, after ` · ` |
| `Date` | Yes | A real ISO calendar date on the identity line, after ` · ` |
| `Kind` | No | One of `concept`, `experience`, `experiment`, `integration`, `assessment` |
| `Workflow` | No | One of `draft`, `ready`, `in-progress`, `in-review`, `done`, `parked` |
| `Owner` | Yes | Nonempty prose naming the responsible repository and person or agent, or stating that ownership is unresolved |
| `Status` | Yes | Nonempty prose: what is proposed, selected, checked or still open |
| `Worklog` | No | A Markdown link to the record that retains dated evidence |

An absent optional field stays unrecorded. Never infer one: a passing test, a
generated image, an imported asset or an old dated entry does not set `Workflow`,
and a subject name does not set `Kind`. Reordered, duplicated, empty or
misplaced fields are rejected. Prose after the block is free.

## Kind describes purpose, workflow describes coordination

`Kind` names the main purpose of this assignment, not its subject, provenance or
current state. Choose the main question when purposes overlap.

| Kind | Typical path and evidence | Completion means |
| --- | --- | --- |
| `concept` | Frame intent, explore candidates, review, select or refine; retain candidates and their basis | A scoped selection, rejection or next commission is recorded; a living specification may stay open |
| `experience` | Define the experience, build an approximation, observe use, revise; retain routes, conditions and findings | The scoped experience has a disposition and any further work has an owner |
| `experiment` | State a question, define conditions, compare, observe, interpret; retain setup, observations and limitations | Evidence supports an answer, or an explicitly inconclusive result |
| `integration` | Identify inputs and interfaces, assemble, verify, inspect in context, hand off; retain source identities and reproducible checks | A reproducible result has findings and a disposition for the requested use |
| `assessment` | Identify an existing subject and review basis, inspect, report, decide; retain criterion-linked findings | Findings and useful next questions are recorded within the requested review scope |

`Workflow` is coordination state only. Framing often corresponds to `draft`,
preparation to `ready`, work to `in-progress` and review to `in-review`. These
are aids to interpretation, not automatic transitions. `done` needs a recorded
scoped disposition and does not mean the subject was accepted or adopted; link
the actual disposition and keep the prose `Status` for that distinction. Any
kind can be `parked`, which retains its reason and next owner.

A new kind needs a concrete distinction from these five, not a new template or
a subject that lacks a home.

## Run the checker

```sh
python3 <process-design>/scripts/validate-work-records.py <path>...
```

Each path is a Markdown file or a directory of them. The checker reads only the
given paths, does not follow symlinks and does not descend into `.git`. It
checks selected records for a supported version, the required fields in order,
allowed optional values, a parseable identity line and identifiers that are
unique within one invocation. Unselected records are counted and skipped. A
copied template whose placeholders are still unfilled is reported as such.

A structural pass does not establish semantic adequacy, that the linked worklog
exists or says what the record claims, that the criteria are good ones, or that
any described work, review or acceptance occurred. Link resolution, rendering
and discovery remain the consuming project's responsibility.

## Backfilling an existing record

Treat the fields as a present-day assessment. Read the record and its linked
evidence, identify the bounded work being classified, and leave uncertain fields
unrecorded. Do not classify a whole lifecycle from one record or infer
acceptance from completed implementation.

Retain the original date, revision, intent, criteria and source pins when only
adding coordination metadata; changed intent or criteria still needs a new
revision. Record the assessment date, actor, source basis and reason in a short
worklog entry. Do not invent earlier transitions the original assignment never had.
