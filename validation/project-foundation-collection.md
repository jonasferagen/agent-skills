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

## Conditional authority and setup routes — 3 October 2026

The collection entrypoint now selects task guidance. Installation, provenance and
template details have a conditional owner in references/installation.md, reached
from the entrypoint and bootstrap. Worktree defaults, unknowns, authority and
inheritance remain visible. Contracts, docs and policy clarify when authority
reading is needed; known-scope reading/application can use relevant owners directly.
Changed scope/circumstances and authority conflicts still require deeper guidance.

Policy 3.2.0 separates establishment, requirement discovery, change assessment and
policy-document writing. The previous policy-change consequence/readiness text is
preserved verbatim. The six axes, discovery, format, impact and verification
obligations remain reachable at their task-specific owners. Historical references
to establish-and-change.md remain evidence of prior revisions; no active caller
uses the removed reference.

A fresh [source review](foundation-routing-trial/source-review.md) found two issues:
the direct contracts route needed an explicit changed-circumstances condition,
and moved installation text needed to name the complete project-foundation directory.
Both were corrected. Source review otherwise confirmed preservation of policy and
installation obligations. No source-maintenance reference was added to consumer
routes. The existing source authoring convention already covers this finding;
no additional generalized rule was needed.

### Consumer trials

[Retained fixtures and outputs](foundation-routing-trial/README.md) are synthetic,
separate fresh contexts entered through project instructions. The author reviewed
the answers and read logs, not only evaluator summaries.

- Narrow interpretation read six source files, 1,186 whitespace words, and loaded
  no authority, installation, policy-change or establishment references. It
  preserved the distinction between the adopted loss limit and verified recovery.
  The prior fresh trial of the same fixture read 1,813 words across seven files;
  the observed difference is 627 file words. These counts describe displayed file
  inputs, not total tokens or a general context-saving guarantee.
- An already-observed public exposure reached foundation-authority and policy-changes,
  identified a current conflict with offline/no-transfer policy, and specified
  containment/evidence follow-ups without performing them or silently amending
  policy. It loaded neither establishment nor policy-writing nor installation.
  The read log reports 2,977 distinct source words, plus a targeted search that
  repeated relevant lines to find consumers.
- Installation reached the relocated reference and bootstrap, preserved full-copy,
  provenance/draft, explicit instruction-hook and worktree requirements, and
  performed no setup. It read 2,184 source words; substantial bootstrap detail and
  one authoring-reference read were unnecessary to parts of this explanation.
- The literal edit changed only the requested phrase and reported no obligation
  change separately. It avoided authority, establishment and change workflows,
  but loaded the policy entrypoint and an unnecessary evidence file. This is no
  demonstration that every narrow task gets cheaper.

- A fresh proposed-handoff assessment reached change and requirement-discovery
  guidance without establishment or policy-writing detail. It preserved existing
  guarantees and found successor access, custody and recovery decisions. It read
  3,264 source words, including an unnecessary 248-word authoring-reference read.
  The prior change trial reused context; its 2,529 newly displayed words are not
  a comparable baseline for this fresh trial.
- Direct entry through project-contracts detected newly external/public delivery
  despite confirmed content acceptance, and reached authority, policy and change
  review. It preserved accepted-file obligations and performed no external actions.
  It read 3,618 source words, including 803 words of unnecessary foundation format.
  This exposed another conditional-read defect in foundation-authority, corrected
  by explicitly limiting format reads to declarations or inherited values.

- A separate fresh repeat of the direct-contract case after that correction
  reached authority and policy-change review without foundation-format. The answer
  retained the changed-exposure finding, accepted-content distinction and required
  follow-up evidence. It read 2,847 source words, including 14 unnecessary words
  of project provenance. This follows the 3,618-word draft run; targeted search
  snippets are outside both full-file counts.

### Preservation, checks and limits

The source reviewer rechecked both fixes and the final authority-to-format condition.
Declared inheritance, shared lookup, cycle handling, missing-owner rules and
changed-circumstance triggers remain reachable; no additional source finding was
reported. This was source review, not a fresh inherited-policy consumer test.

All seven consumer runs used fresh contexts. The final direct-contract run includes
the final format-read clarification; earlier runs describe their respective drafts.
The author inspected all full answers and read logs. Trial inputs and installed
copies were preserved. Reports distinguish whole-file reads, repeated search
snippets, mechanical word counts and generated-output checks. No content truncation
was reported. Prompted guidance-gap reporting is not spontaneous friction capture.

The trials establish representative routes, not routing reliability, automatic
client discovery, live compliance or universally lower reading cost. Actual bootstrap
output, full establishment/adequacy review, unavailable inherited owners and direct
project-docs reading were not independently exercised in this round. The installation
trial explains adoption; it does not perform or verify a real installation.
Remaining observations include occasional unnecessary authoring, project provenance
and evidence reads. Do not weaken consequential review to meet a word budget.

Package validation passed for 25 skills and one collection. Quick validation passed
for policy, contracts, docs and bootstrap; all five foundation helper tests passed.
Existing detailed policy-change consequence text was mechanically confirmed intact.
Whitespace checks passed. Authoring reused skill-creator, clear-writing, the source
collection convention and relevant visual guidance for preserved tables; no diagrams
or helper code changed. No release, global installation or downstream adoption was
performed.
