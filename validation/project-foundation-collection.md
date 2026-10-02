# Validation — Project foundation collection

## Git worktree default — 3 October 2026

Git worktrees joins the collection at unreleased version 0.1.0. Project bootstrap
2.0.0 installs its rule and concrete route in project instructions. Repository
edits use task worktrees unless local policy explicitly opts out; work outside
Git proceeds directly. Existing installed copies and instruction hooks require
deliberate updates. See [Git worktrees validation](git-worktrees.md) for evidence.

The dated sections below describe earlier collection revisions.

## Scope — 2 October 2026

The collection replaces independent installation for project-bootstrap,
project-policy and project-docs, and includes their clear-writing and
diagrams-and-tables dependencies. Templates and shared authoring guidance are
collection resources. The bootstrap, policy and documentation versions change
to 1.0.0, 1.0.0 and 2.0.0 respectively to reflect their new dependency contract.
These are unreleased versions.

The scaffold has four files: README plus boundaries, policy and glossary.
The three definitions carry date/revision fields and sparse tables. Policy has
exactly two initial columns: axis and current fact or decision. The former
project-policy template is removed; both bootstrap and policy use the same file.
Concrete adopted requirements can add detail as needed.

## Scenarios reviewed by the author

| Case | Expected outcome |
| --- | --- |
| Bootstrap with a name and little context | Establish sparse tables and concrete agent routes to the complete collection; leave missing facts unknown. |
| Read a blank recovery cell | Treat it as unknown; infer neither disposability nor a backup requirement. |
| Establish the policy through its own entry point | Use the same template as bootstrap, with shared authoring guidance. |
| A spike becomes a maintained application | Assess consequences across the project, select required reviews/audits, and track prerequisites and evidence. |
| Local development moves to cloud hosting | Review exposure, identity, operations, data, recovery and other affected areas; do not claim readiness from editing the profile. |
| A policy guarantee is relaxed | Assess simplification and deletion opportunities against remaining requirements and retained state; do not mandate a broad refactor. |
| A document contains a typo | Make a wording correction without rebuilding the profile or incrementing the decision revision. |
| The task needs a simple table | Use authoring guidance without loading Mermaid rendering mechanics. |
| A project already has instructions | Merge concrete routes; preserve existing authorization and project-specific rules. |

These are author-reviewed expectations, not independent behavioral trials.

Mechanical checks passed on 2 October 2026:

- Repository validation covered 22 skill entries, including the collection.
- Skill-creator validation passed for all three changed project entry points.
- 141 local link targets in the catalog, instructions, validation pages and
  collection resolved. Package validation also checked the standalone packages.
- An isolated copy of the complete collection passed validation at a different
  filesystem location. A link outside the collection, an omitted authoring skill
  and a duplicate skill name were each rejected.
- An isolated template copy resolved date, revision and project name fields,
  retained working README links and had exactly two initial policy columns.
- `git diff --check` passed.

Client automatic discovery,
user-wide installation, Atlas adoption and application policy transitions have
not been tested or performed.

Clear-writing and its instruction guidance informed the wording. Visual guidance
kept the scaffold as small tables. The policy transition reference retains the
full consequence review; reducing the document size does not reduce that review.

## Authority and source-of-truth — 2 October 2026

Added source-of-truth as the sixth collection entry, at unreleased version 2.0.0.
Shared foundation-authority guidance defines consultation at the start of
substantive work, on affected changes and before completion. Bootstrap must put
those rules and concrete routes into the target project's instructions.
Project-policy and project-docs now route definition conflicts and consumer drift
to source-of-truth.

Author review covered: implementation contradicting an adopted requirement;
an unknown cell mistaken for permission; a proposal mistaken for adopted policy;
and a new user decision requiring the authoritative documents and consumers to
be reconciled. The text preserves each distinction without requiring a full audit
on every read. These are reviewed scenarios, not independent agent trials.

Repository validation passed for 22 entries. Source-of-truth passed skill-creator
validation. All 102 documentation link targets and 63 targets in a relocated copy
of the six-entry collection resolved. `git diff --check` passed. No downstream
installation or Atlas adoption was performed.
