# Validation scenarios — Project Docs

## Collection adoption — 2 October 2026

The current entry point belongs to the project-foundation collection. See
[collection validation](project-foundation-collection.md) for the shared templates,
required authoring guidance and policy review behavior. Earlier standalone-package
and template-copy results below describe the previous structure.

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

## Clear writing pass — 2026-09-30

Version 1.2.1 revises the manifest, `structure.md` and `diagrams.md`; the worked
example needed no change. See the [package
sweep](clear-writing.md#package-sweep--2026-09-30). "Altitude" is now explained
inline, because this package must work without the diagrams skill. Review caught
one meaning change: diagram inspection had become conditional on the target
renderer being available. The original scope was restored, with one clarity
regression and one nit. No behavioral trial was run.

Left unresolved: "A documentation edit proves none of the latter" follows four
items and does not say whether it covers the last two or the last three.

## Diagrams and tables pass — 2026-09-30

No change; see the [package
pass](diagrams-and-tables.md#package-pass--2026-09-30). The reader-question and
view-ownership tables are complete, and both worked-example diagrams were
rendered and read clearly in light and dark themes. Newly found: the glossary
defines "Evidence", but the diagram labels the node "Evidence reference",
although `diagrams.md` asks diagrams to use glossary names.

## Resolutions — 2026-09-30

The owner accepted each proposal from the contradiction research. No version was
bumped.

- Verification: "proves none of the latter" followed four items → "proves
  neither implementation nor verification, recorded or live"; the sentence
  makes no claim about intended behavior.
- Glossary name: the diagram labelled the node "Evidence reference" while the
  glossary defines "Evidence" → the node is labelled "Evidence", as
  `diagrams.md` requires. The diagram was re-rendered with Mermaid CLI 12.0.0
  in the default and dark themes and read clearly in both.
- Handoff: "links to its remaining checks" did not say whose → it links to the
  release record for acceptance checks still outstanding.

## Canonical document homes — 2026-10-03

The collection owns a closed document-type map under project-docs/. Repository technical documentation keeps its own homes. Governance records and technical evidence are classified separately.

This changes placement defaults and is reflected in a major member version.
The ten collection helper tests cover foundation shape and allowed document paths.
No runtime or external authority changes are implied.

## Conditional collection routing — 3.0.1, 3 October 2026

Authority reads are conditional for existing known terms; establishment, reconciliation, conflicts and changed circumstances retain the authority route.

See [collection validation](project-foundation-collection.md#conditional-authority-and-setup-routes--3-october-2026)
for source review, fresh consumer cases, findings and limitations. Those tests
exercise representative routes; they do not establish every entrypoint or native
discovery behavior. No release or downstream installation was performed.

## Managed technical explanations — 2026-10-03

Unreleased collection 0.3.0 adds design, architecture, models, process descriptions
and handoff contracts to the closed home map. Project-docs 5.0.0 changes the
placement default; existing layouts migrate deliberately. Commands, setup,
implementation references, creative content and technical evidence keep local
homes. Design, model and contract templates supplement the existing view/process
templates. Semantic/template enforcement and a procedure template are deferred.

Clear writing and instruction guidance were applied to the changed scope and
routes; diagram/table guidance informed the type map. The map keeps placement,
content ownership and workflow ownership distinct. No diagram source changed.
The unchanged path helper reads the expanded map. Its fixture now accepts indexed
technical explanations and continues to reject operating-procedure categories,
attachments and a missing model index.

A bounded fresh consumer trial used an installed draft outside this source tree
at `/tmp/managed-doc-routing-xnyj4hdn`. Entry was through project instructions. It
created a proposed source/session/finding model using the model template and its
required index, answered the process/procedure boundary, then corrected one typo
in a local command guide. The output preserved proposal status, contextual
findings and the distinction between content identity and byte retention. It
selected no runtime, serialization or browsing convention. No source-maintenance,
installation or bootstrap guidance was read. The evaluator reused context for
its second and third requests; those are not separate cold trials.

The actual read list and artifacts remain in that temporary trial's report. The
connected-view reference was also read for association/template guidance despite
no diagram being drawn; this trial does not establish minimal context use.
Design and contract template use were reviewed as source, not exercised by this
consumer trial. No broad reliability, parser or structural-completeness claim is
made. Package validation, all 15 foundation/path helper tests, affected skill
manifest checks, collection links/anchors and whitespace checks passed.
