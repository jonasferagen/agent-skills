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
| Reconcile docs after a policy changes from synthetic testing to retained real data | Consult the policy, update affected instructions, link procedures and transition work, and preserve unverified requirements. |
| A prototype label appears while explicit migration/testing guarantees still apply | Keep those commitments; the label alone does not relax them. |
| A diagram renders in a standalone tool but is tiny or low contrast in the project's preview | Inspect the target preview at a normal reading width and in the themes readers use; reflow or adjust paired text and background colors there. Keep renderer-specific settings in the project. |

## Initial checks — 2026-09-19

The skill manifest passed the skill-creator validator. All nine local links
resolved and the staged diff passed `git diff --check`. Both Mermaid examples
rendered successfully and were visually inspected. The author reviewed the
instructions against the cases above; no independent behavioral evaluation or
second-project trial has been performed.

## Release 1.0.0 — 2026-09-29

Added manifest version metadata for the per-skill release and commit pinning
convention. The instruction body and references are unchanged.
The manifest validator passes, and all 4 internal links and heading anchors
resolve. Behavioral scenarios remain the review basis above; this packaging
release does not claim a new independent behavioral evaluation.

## Project foundations update — 2026-09-30

Version 1.2.0 adds policy-aware documentation reconciliation and uses the display
name “Project documentation.” Installation path unchanged. Author review covered
the new policy/commitment scenarios and existing small-edit and standalone cases.
Package validation and the skill-creator manifest check passed. The independent
policy trials are recorded in [project-policy](project-policy.md); this skill did
not receive a separate new behavioral trial.
