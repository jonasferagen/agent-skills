---
name: project-docs
description: Establish, review, or reconcile repository documentation, including domain glossaries, document ownership, project instructions, and high-level relationship diagrams. Use for project documentation structure and consistency work; not standalone office documents, generic copyediting, or application implementation.
---

# Project documentation

Make the project understandable to its next reader: what it does, how its concepts
relate, how to work on it, and which statements are current or uncertain.

## Select the work

Infer the mode from the request. A review produces findings; an instruction to
apply them authorizes edits. Preserve the repository's existing conventions unless
changing them is part of the task.

- **Establish:** identify readers and their tasks, inspect the project, and create
  the smallest useful documentation set. Do not generate empty scaffolding.
- **Review:** compare documentation with available implementation and records.
  Report concrete discrepancies, reader impact, and proposed fixes with file
  references. Separate observed faults from editorial preferences.
- **Reconcile:** update the owning pages, repair references, distinguish current
  guidance from historical evidence, and remove superseded active instructions.
  Preserve durable evidence and unresolved questions.

For structure, prose and instruction design, read
[structure and ownership](references/structure.md). When creating or changing
visuals, read [diagram conventions](references/diagrams.md). The
[worked example](references/worked-example.md) illustrates the method with a
synthetic domain; it is not a schema or template to impose on other projects.

## Ground the content

Start with repository instructions, the entry page, and affected files. Inspect
code, schemas, configuration and dated records as relevant. Avoid reading every
specialist document for a small editorial task.

Use domain terms from the project. Define ambiguous terms and separate concepts
that sound similar but have different behavior. Do not invent entities, foreign
keys, cardinalities, permissions or workflows to make a diagram look complete.
An implemented table does not establish an available UI feature.

Distinguish intended behavior, implementation, recorded verification and live
verification. A documentation edit proves none of the latter. Conflicting or
missing evidence should remain explicit until resolved. Do not inspect live
accounts or change services solely to make a documentation claim look current.

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
- Trace diagram relationships to evidence, render changed diagrams when tooling
  is available, and inspect labels, crossings and readability. Report rendering
  limitations rather than claiming visual verification.
- Review examples for private information and unsupported behavior.
- Run the repository's relevant checks, including `git diff --check` where Git
  is available. Install dependencies only when a necessary check needs them;
  do not modify application lockfiles for an editorial task.
- Report what changed or what the review found, evidence used, checks performed,
  and material uncertainty. Follow the repository's authorized landing process.
