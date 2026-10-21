---
name: single-source-of-truth
description: "Reconcile a rule, vocabulary, shape or changing prose claim defined in several places. Use when copies drift, a change requires coordinated edits, or a consistency check needs to survive restructuring."
metadata:
  version: "3.5.0"
---

# Authoritative definitions

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

Let the project decide how much a disagreement matters and which checks are worth
their cost. If the project has stated no such decision, assess the consequence of
disagreement yourself (see [rank by how it fails](references/definitions.md#rank-by-how-it-fails)),
state the assumption, and ask the user when the cost is unclear. When
requirements change, revisit the affected copies and checks, and record any
requirement left unmet in the project's issue tracker, or in the report to the
user when there is none. A stated
requirement and observed behavior are separate facts; neither proves the other.
Missing facts remain explicit unknowns.

This skill traces authoritative definitions, their consumers and consistency
checks. A **gate** is an automated check that must pass before a change is
merged (typically the CI job required on the main branch); a check that only
runs on request is not in the gate. If the project has no gate, say so: a check
outside a gate records the risk (rung 6) rather than preventing it, and ask the
user whether to add one.

## Read for the decision at hand

- To find a concept's owner, choose a structured contract for machine consumers,
  decide which prose claims to retain, compare similar
  definitions, choose derivation or assess drift risk, read
  [definitions](references/definitions.md).
- For configuration, external identifiers or repository locations used in several
  places, read [one owner for a shared value](references/authoritative-values.md).
- When a language, build or runtime boundary prevents direct reuse, read
  [boundaries](references/boundaries.md).
- When keeping or adding a consistency check, read
  [check design](references/check-design.md); its links lead to the relevant
  durability examples.

Read the relevant reference when that decision arises; these are not a startup
reading list.

A **rung** is one of the six numbered options for deriving or checking a copy,
from removing the restatement (rung 1) to recording the duplication (rung 6);
the ladder is in [derive instead of restate](references/definitions.md#derive-instead-of-restate).

## Review and verification

Report the following to the user:

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
- Remove unnecessary prose restatements. Reconcile needed explanations with the
  current definition and point to its authoritative home; retain dated evidence
  as evidence of the conditions assessed.
- Run the project's own checks. Include any new gate check in the same change.
