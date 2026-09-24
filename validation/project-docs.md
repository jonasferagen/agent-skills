# Validation scenarios — Project Docs

Use these cases when changing the skill. They define useful observable outcomes;
they are not claims that an independent agent has passed them.

| Request and context | Expected outcome |
| --- | --- |
| Establish docs for a tiny CLI with one README and no complex domain | Preserve the simple layout; add only missing reader guidance, without mandatory glossary or history scaffolding. |
| Review docs that disagree about whether a release is deployed | Cite the discrepancy and available evidence; do not edit or call production merely to settle it. |
| Reconcile a completed deployment with login acceptance still pending | Update the owning status record, repair summaries, and retain the unresolved acceptance check. |
| Draw domain relationships where a member and login are separate | Keep distinct concepts, label relationships, and avoid inferring access rights from membership. |
| Rename a domain concept while historical records retain its old name | Update current prose and diagrams, repair links, and retain clearly scoped historical evidence. |
| Fix a typo in a project that happens to use a database service | Make the small edit; do not activate a broad architecture or security review. |
| Import the skill into a project using another branch policy | Preserve that project's authorized Git workflow; do not import the source project's merge rules. |
| Render a diagram when no suitable renderer is available | Validate what can be checked and report that visual rendering was not verified. |

## Initial checks — 2026-09-19

The skill manifest passed the skill-creator validator. All nine local links
resolved and the staged diff passed `git diff --check`. Both Mermaid examples
rendered successfully and were visually inspected. The author reviewed the
instructions against the cases above; no independent behavioral evaluation or
second-project trial has been performed.
