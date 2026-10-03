# Connected documentation views — 2026-10-03

## Scope and ownership

Base: `25761e7c99498d01da4eedbe482a2e92e167b193`, the released collection
0.1.0. This task adds compatible documentation guidance at collection version
0.2.0, project-docs 4.1.0 and a project-design routing clarification at 0.6.1.
This is an unreleased source revision; no release tag is created.

The observed mechanism was a manually authored architecture browser maintaining
view summaries, status, navigation and relationship details separately from their
document owners. A current Forge review also found multiple views per file,
reused Mermaid IDs, mixed claim status and symbolic member routes. Equal labels,
adjacent tables and missing detail links cannot safely resolve those associations.

[Project-docs connected views](../collections/project-foundation/skills/project-docs/references/view-structure.md)
owns the shared source/navigation associations. Project-design retains model
meaning, diagrams-and-tables retains form and rendering, source-of-truth retains
derivation choices, and existing status/evidence and foundation reference rules
remain authoritative. No new discoverable skill or parser dependency is needed.

The collection supplies starting [view](../collections/project-foundation/templates/views/view.md)
and [process](../collections/project-foundation/templates/project-docs/process/README.md)
templates. Existing adequate structures remain usable; irrelevant sections are
omitted. Machine browsing requires a separately selected, versioned input
convention. Ordinary reading and prose edits need neither metadata nor migration.

Jonas suggested future foundation-managed architecture/process pages in
`project-docs/`, referenced by member implementation docs. That placement remains
an option, not an adopted type or migration. Current document-home rules and their
validator are unchanged. A future decision must settle the managed types and
owners, update templates and validation, and reconcile consumer routes before
moving authoritative pages.

## Review and checks

An independent source review compared the draft with document-home,
foundation-format and workflow guidance. It found no material ownership,
scope or routing defects. The updated Forge atlas supplied another case: a
scoped actual trial can use a proposed general process without adopting it.
Navigation preserves each source's status and scope.

Mechanical checks passed: 25 skill entries in one collection, quick validation
of both changed skill manifests, collection-local paths and heading anchors,
and `git diff --check`. No helper behavior or diagram source changed.

## Practical consumer trials

Fresh agents entered isolated synthetic projects through their AGENTS hook and
installed collection. They did not receive source-maintenance material or
expected answers. Fixture inputs distinguished staff acceptance from catalogue
success, adopted overview collaboration from proposed information flow, two local
`C` node occurrences with different meanings, an intentionally closed catalogue,
supporting-resource rows and explicit detail/context links. No live systems or
network were used.

- **Ordinary reading:** correctly identified staff acceptance and the limits of
  catalogue success. The agent read project sources and status guidance without
  connected-view, authoring or template activation. Instruction reads were
  approximately 978 whitespace words; source review was 214 words.
- **Nearby wording task:** shortened a README paragraph while preserving its
  meaning and architecture link. It used clear-writing, with no browsing or
  template activation. Instruction reads were approximately 937 words; source
  and changed-artifact review was 64 words.
- **Initial browsing review:** found six consequential binding errors: merged
  identities, false verified status, lost arrow/acceptance meaning, table rows
  promoted to participants, closure treated as missing implementation, and
  label-inferred detail links. It preserved the architecture and left syntax
  and implementation unselected. Its 7,240 guidance words included unnecessary
  full construction and broad derivation reading. The new route was narrowed to
  the disposition inventory and relevant derivation options.
- **Follow-up browsing review:** preserved the same six findings and task scope.
  Both the main evaluator and its independent cross-check read only the
  composition inventory rather than the full construction reference. Their
  instruction consumption was 7,178 and 6,568 words respectively (13,746 combined),
  with 1,527 combined project/artifact words. Broader derivation and semantic
  guidance still appeared; this run does not establish lower total context cost.
- **Initial process-template task:** found and used the shared template,
  preserved current paths and responsibilities, and discovered unresolved
  completion, review and record questions without choosing their answers.
  Instruction/template consumption was 6,780 words, including 1,413 unnecessary
  installation/bootstrap words caused by the collection's broad template route.
  The collection now distinguishes foundation scaffolding from view/process
  templates; project-docs also supplies a direct starting-template route.
- **Follow-up process-template task:** reached the same process template without
  installation, bootstrap or the machine-browsing section. It preserved process
  meaning, paths, synthetic evidence and unresolved decisions. Selected
  instruction/template text was 5,127 words, plus a 92-word heading scan; project
  and proposal review was 874 words. Some broader ownership and generated-check
  material was still over-read. These paired observations support the scoped
  routing correction without establishing general efficiency or reliability.

These runs demonstrate their recorded routes, not general routing reliability,
automatic extraction, diagram readability or runtime behavior. No collection
release or whole-collection release review is claimed.
