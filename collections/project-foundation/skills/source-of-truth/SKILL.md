---
name: source-of-truth
description: "Reconcile a rule, vocabulary or shape defined in several places. Use when copies drift, a change requires coordinated edits, or a consistency check needs to survive restructuring."
metadata:
  version: "2.1.0"
---

# Authoritative definitions

If execution exposes a consequential guidance or routing problem, use
[friction capture and repair](../../references/friction.md). Successful work needs
no capture pass.

Give each concept one authoritative home: the place that decides its value or
rule. Derive every other appearance from that home, or make a check fail when the
two disagree.

Use this guidance when a value, list, rule, pattern or shape appears in several
places, when adding a vocabulary member requires edits to several files, or when
deciding where a new constant, type or rule belongs. A vocabulary is a set of
allowed values. A restatement is a separate definition of the same concept.

The guidance covers concepts shared across schemas and application code,
configuration and the code that reads it, different languages, and code and its
documentation. Restatements across these media are especially hard to find and
likely to drift, because no single search finds both sides.

Start with the project's guides for the area you are working in. They may already
name a concept's home, and an explicit project convention takes precedence over
this guidance. Adopting this skill does not call for renaming anything, moving
existing code or changing a schema. Examples below are synthetic.

Use the project's policy to judge the consequence of disagreement and the
evidence worth maintaining. A policy change can alter that consequence: revisit
affected copies and checks, and record unmet requirements in the active queue.
Keep project policy authoritative for its facts and adopted decisions, downstream
owners authoritative for derived requirements, and implementation owners
authoritative for observed behavior; one cannot prove the other. A prototype
label does not by itself waive an existing guarantee. Missing policy facts remain
explicit unknowns.

This skill belongs to the [project-foundation collection](../../COLLECTION.md).
Follow its [foundation authority guidance](../../references/foundation-authority.md)
when project decisions and their implementations disagree. Use
[project-policy](../project-policy/SKILL.md) to assess the consequences of changed
requirements, and this skill to trace their authoritative definitions, consumers
and consistency checks. For authored explanations, use the collection's
[authoring guidance](../../references/authoring.md).

## Read for the decision at hand

- To find a concept's owner, compare similar definitions, choose derivation or
  assess drift risk, read [definitions](references/definitions.md).
- When a language, build or runtime boundary prevents direct reuse, read
  [boundaries](references/boundaries.md).
- When keeping or adding a consistency check, read
  [check design](references/check-design.md); its links lead to the relevant
  durability examples.

Read the relevant reference when that decision arises; these are not a startup
reading list.

The numbered “rungs” below are the [options for deriving or checking a copy](references/definitions.md#derive-instead-of-restate).

## Review and verification

- Name the concept, its authoritative home, and the rung you stopped at.
- Show evidence of the drift risk and how the chosen option addresses it: a
  removed restatement, derivation from the authoritative home, a required check
  that fails on disagreement, or a record of structural duplication and what
  must be edited together. An earlier extension that missed a copy is evidence
  of the risk; it does not prove that the risk has been removed.
- If you stopped at rung 5 or 6, name the boundary that prevented the higher
  rungs and state what remains unprotected.
- If you added or retained a check, state what it reads on each side when it
  runs. Its verdict must name the root and the set it measured.
- Update the documents that state the concept to agree with its current
  definition. Use the present tense and name the authoritative home in the guide
  responsible for that concept.
- Run the project's own checks. Include any new gate check in the same change.
