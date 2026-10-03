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
| Describe a new proposed process beside an existing flat process page | Create one named-process README linked from the process index; keep the existing owner in place, proposal status explicit, diagrams optional and commands/evidence in their local homes. |
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

Unreleased collection 0.4.0 adds design, architecture, models, process descriptions
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

The source was reconciled with the concurrent passive-guidance update at
`7bcf89dc41ad3c22fc1198995123f5bfb2be6c7b`. Its conditional discovery/repair routes
are preserved; this migration supplies no new external repair authorization.
The consumer trial used the preceding 0.3.0 draft. The merged 0.4.0 collection
passed package, path-helper, link and whitespace checks; passive-repair behavior
retains its separate validation record and was not rerun here.

## Named process directories — 2026-10-04

Unreleased collection 1.0.0 and project-docs 6.0.0 change the default for a new
named process to `project-docs/processes/<process>/README.md`. The existing
process template moved to `templates/project-docs/process/README.md`; active
routes use that owner. Historical read logs retain the original template name.
One process entry is sufficient, with optional direct supporting Markdown pages.
Existing flat process pages remain accepted until deliberate migration; keeping
both forms for the same name is rejected. No release tag or downstream adoption
is part of this source change.

Clear-writing and its instruction guidance were applied to the default,
compatibility and migration wording. The existing document-home table columns
were retained, adding the entry and supporting-page paths without inventing a
new document type. The template now makes prose or numbered steps sufficient
and a diagram optional. Commands, contracts and run evidence retain their
existing homes. No diagram changed, so no rendering check applied.

The path helper derives the bounded `<process>` family from the map. Its ten
new synthetic filesystem cases cover a README-only process, direct supporting
pages alongside a distinct flat process, the required parent index and entry, conflicting
owners, names, nesting, artifacts, symlinks and a changed map root. Eight cases
failed against the old helper for the intended missing behavior. The remaining
two caught in-memory mutations that accepted arbitrary process descendants or
linked external process directories. All 25 foundation/path tests passed with
no skips after restoring the real helper. This checks paths, not process
semantics, headings, link completeness or implementation status.

`python3 scripts/validate-packages.py` passed for 27 skill entries and two
collections, including installation-unit links and manifest versions. The helper
suite ran with `python3 -m unittest discover -s collections/project-foundation/tests`.
`git diff --check` passed. A collection release's full self-conformance review
has not been performed; this revision remains unreleased.

A consumer subagent used a copied draft, provenance and project instruction hook
outside the authoring repository at `/tmp/forge-process-consumer-20261004`.
Without supplied route hints, it wrote a proposed process as a 297-word README
with four numbered stages, added its process index, and linked an 86-word
supporting explanation for a tied decision. It also refined the existing command
guide in `docs/` and linked it to the process. Review of all five changed pages
confirmed one process owner, scoped proposal status, explicit revision/selection
responsibilities, retained state on interruptions and no copied runtime or run
artifacts. The process contained no diagram. Path validation, seven local links
and whitespace checks passed; a synthetic walkthrough checked textual consistency,
not implemented behavior.

The evaluator recorded its reads and results in
`/tmp/forge-process-consumer-20261004-report.md`: approximately 7,464 words of
instructions/templates, 184 words of initial project inputs and 512 words of
output review. It reached workflow design, the document map, new template,
writing/status guidance and only the shared-template excerpt of connected views.
It read no source maintenance, installation, bootstrap or generated-browser
guidance; no required read was identified as missed. No guidance was reread into
context or truncated. The supporting-page and adjacent-guide requests reused
the initial context, so they do not establish independent cold routing. The
subagent shared the parent's conversation/tool environment; this was not a
blinded external installation. This is one practical trial; it establishes
neither reliable discovery across projects
nor minimal context use.
