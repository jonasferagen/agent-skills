---
name: single-source-of-truth
description: "Reconcile a rule, vocabulary, shape or changing prose claim defined in several places. Use when copies drift, a change requires coordinated edits, or a consistency check needs to survive restructuring."
metadata:
  version: "4.0.0"
---

# Authoritative definitions

Give each concept one authoritative home: the owner that decides its rule and
publishes changes. Consumers derive their appearances from that home or check
agreement with the revision they have adopted. An immutable publication with
provenance is a valid source for a consumer; it need not follow the publisher's
latest revision.

Use this guidance when a value, list, rule, pattern or shape appears in several
places, when adding a vocabulary member requires edits to several files, or when
deciding where a new constant, type or rule belongs. A vocabulary is a set of
allowed values. An independently maintained restatement can drift; a selected
publication preserves an intentional adoption decision.

The guidance covers concepts shared across schemas and application code,
configuration and the code that reads it, different languages, repositories,
and code and its documentation. Start with the project's guides: an explicit
project convention takes precedence. Adopting this skill does not call for
renaming anything, moving code, changing a schema or upgrading a dependency.
Examples are synthetic.

Keep publication, adoption and integration distinct. The publisher owns the
rule and any generation from its selected source. A consumer owns its adopted
revision and verifies its behavior against that contract. Integration checks
verify compatibility between explicitly selected participants. None requires a
consumer's ordinary checks to read a sibling checkout, a private database or a
moving upstream head.

Let the project decide how much disagreement matters and which checks earn
their cost. If the project has stated no consequence, assess how disagreement
would fail (see [rank by how it fails](references/definitions.md#rank-by-how-it-fails)),
state the assumption, and ask the user when the cost is unclear. Record unmet
requirements in the project's tracker, or in the report when it has none.
A stated requirement, a correctly derived artifact and observed behavior are
separate facts; none alone proves the others. Missing facts remain unknowns.

A **gate** is an automated check required before merging or publishing the
change it protects. A manual or optional check supplies evidence when run but
does not prevent that change by default. Report any gap in required coverage
without implying the check supplied no evidence.

## Read for the decision at hand

- To identify ownership, distinguish publication from adoption, choose a
  structured contract, assess prose or drift risk, read
  [definitions](references/definitions.md).
- For configuration, external identifiers or repository locations used in several
  places, read [one owner for a shared value](references/authoritative-values.md).
- When a language, build, repository or runtime boundary affects reuse, read
  [boundaries](references/boundaries.md).
- When keeping or adding a consistency check, read
  [check design](references/check-design.md); follow its durability reference
  when writing the check.

Read the relevant reference when that decision arises; these are not a startup
reading list. A **rung** is one of the six options for reuse, derivation or
checking in [derive instead of restate](references/definitions.md#derive-instead-of-restate).

## Review and verification

Report the following to the user:

- Name the concept, its authoritative owner, any selected publication and the
  chosen rung. Distinguish an intentional older revision from accidental drift.
- Show how the choice addresses the observed risk: removal, derivation with
  provenance, a required consistency check, or recorded manual coordination.
  An earlier missed copy is evidence of risk, not proof that it is now removed.
- For retained duplication, name the boundary, its maintenance owner and what
  remains unprotected. Derivation still needs checks of the generator and of
  behavior where correctness matters.
- For each check, state whether it protects publication, consumer adoption or
  integration; name the revisions, root and set it measured. State missing
  dependencies and coverage limits separately from disagreement.
- Remove unnecessary prose restatements. Reconcile needed explanations with the
  contract they describe and point to its home; retain dated evidence with the
  revision and conditions assessed.
- Run the project's applicable checks. Include a new required check in the
  change whose publication or adoption it protects.
