---
name: project-docs
description: "Establish, review, or reconcile repository documentation, including domain glossaries, document ownership, project instructions, and high-level relationship diagrams. Use for project documentation structure and consistency work; not standalone office documents, generic copyediting, or application implementation."
metadata:
  version: "2.3.0"
---

# Project documentation

Follow [foundation authority](../../references/foundation-authority.md) when
consulting and reconciling project decisions. Use
[source-of-truth](../source-of-truth/SKILL.md) when a definition has competing
owners or its consumers need derivation or consistency checks.

Make the project understandable to its next reader: what it does, how its concepts
relate, how to work on it, and which statements are current or uncertain.

Use the collection's [shared authoring guidance](../../references/authoring.md)
when producing or revising documentation. The collection supplies the writing and
visual skills; their references are loaded only for the work at hand.

## Select the work

Infer the mode from the request. A review produces findings; an instruction to
apply them authorizes edits. Preserve the repository's existing conventions unless
changing them is part of the task.

- **Read:** answer from the owning page and relevant definitions. Preserve its
  status and uncertainty; reading a document does not require authoring guidance,
  diagram construction or renderer discovery.
- **Establish:** identify readers and their tasks, inspect the project, and create
  the smallest useful documentation set. When using the collection scaffold,
  record explicit unknowns for missing facts; member tables retain only local
  differences from their declared parent. Do not invent prose to fill them.
- **Review:** compare documentation with available implementation and records.
  Report concrete discrepancies, reader impact, and proposed fixes with file
  references. Separate observed faults from editorial preferences.
- **Reconcile:** update the owning pages, repair references, distinguish current
  guidance from historical evidence, and remove superseded active instructions.
  Preserve durable evidence and unresolved questions.

For decisions about document homes and reader routes, read
[structure and ownership](references/structure.md). Use the
[worked example](references/worked-example.md) only when that method needs an
example; it is not a schema or template to impose.

When an explanation needs a form decision, use the collection's
[diagrams-and-tables](../diagrams-and-tables/SKILL.md) entrypoint. Only when the
task adds, moves or reviews a diagram, read
[diagrams in a documentation set](references/diagrams.md) for its home and
freshness. Plain prose and scaffold tables do not need that reference.

## Ground the content

Read the project's policy when establishing or reconciling its documentation.
Use its users, data, exposure and recovery requirements to set the depth and
evidence needed. Keep the policy's facts and obligations in their canonical home;
link procedures, the active work queue and verification records. If a policy
change affects the docs, reconcile the affected instructions and preserve open
transition work. A project label that suggests less rigor, such as "prototype",
does not waive existing commitments. When no policy exists, keep consequential
unknowns explicit; a small editorial task does not require creating one or
installing another skill.

Start with repository instructions, the entry page, and affected files. Inspect
code, schemas, configuration and dated records as relevant. Avoid reading every
specialist document for a small editorial task.

Use domain terms from the project. Define ambiguous terms and separate concepts
that sound similar but have different behavior. Do not invent entities, foreign
keys, cardinalities, permissions or workflows to make a diagram look complete.
An implemented table does not establish an available UI feature.

Distinguish intended behavior, implementation, recorded verification and live
verification. A documentation edit proves neither implementation nor
verification, recorded or live. Conflicting or missing evidence should remain
explicit until resolved. Do not inspect live accounts or change services solely
to make a documentation claim look current.

## Shape the result

Give each fact an authoritative location and each page a reader purpose. Keep
navigation and brief summaries useful without duplicating changeable status.
Separate definitions, explanations, procedures and historical records where it
helps readers; retain an existing layout that already works.

Keep project invariants and routing in project instructions. Put operational
steps and checks in linked procedures. Generalize reusable techniques without
copying the source project's technology, access model, personal information,
Git policy or deployment commands into unrelated repositories.

Respect the user's requested scope. This skill does not require a new glossary,
a history folder, diagrams, a particular Git workflow, or a full documentation
rewrite for every task. It does not authorize publishing or external writes.

## Verify and finish

- Check changed local links and heading anchors. On moves or renames, search for
  the old path and name and reconcile affected references.
- When diagrams changed, verify their source and placement through the diagram
  ownership reference and their rendered result through the visual skill's
  verification guidance. Report limits to what was checked.
- Review examples for private information and unsupported behavior.
- Run the repository's relevant checks, including `git diff --check` where Git
  is available. Install dependencies only when a necessary check needs them;
  do not modify application lockfiles for an editorial task.
- Report what changed or what the review found, evidence used, checks performed,
  and material uncertainty. Follow the repository's authorized landing process.
