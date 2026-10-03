# Validation — Project foundation collection

## Release 0.1.0 — 3 October 2026

The full [self-conformance review](project-foundation-v0.1.0/README.md) covers
collection content `e63aaf2`, every member, shared reference, template and helper,
and the source catalog/instructions. Three independent fresh reviewers and the
coordinator applied the declared rule owners. All material findings are fixed;
no exception was needed. This is the first collection release.

Consolidation preserves both the conditional task-routing work and the newer
phase/scope, managed document homes, planning, conceptual modelling and shared
status guidance. Review corrected unsupported Mermaid layout and numeric-cast
claims, unreadable visual examples, stale navigation and a whitespace failure.
Independent comparisons checked meaning after each correction.

Package validation, 14 helper tests, 314 current relative paths/heading anchors,
and whole-collection whitespace pass. Three fresh consumer trials cover policy
assessment plus planning, domain modelling beyond the bundled example, and a
literal spelling edit. Local diagram and table rendering is recorded with its
renderer and theme scope. GitHub/editor rendering and native automatic skill
discovery are unverified; the collection makes no claim of either.

The annotated release tag is `project-foundation/v0.1.0`. Forge adoption records
its full source commit and release label in its existing provenance owner.


## Worktree skill retirement — 3 October 2026

The collection no longer includes `git-worktrees` or imposes its worktree default.
Bootstrap 5.0.0 preserves project working agreements and omits the retired route.
See [bootstrap validation](project-bootstrap.md) for current removal checks.
The earlier worktree adoption and trial results below are historical.


## Self-conformance gate and status reference — 3 October 2026

Base: `4edb9c4`, with uncommitted changes in a task worktree. This change adds the
[self-conformance review](self-conformance.md) as a collection release requirement,
a shared [status and evidence](../collections/project-foundation/references/status-and-evidence.md)
reference, and three mechanical checks. The full review itself has not been run;
the first collection release requires it.

### Mechanical evidence

- The new foundation-checker tests were run against the previous checker and
  failed on each new case, while every earlier case still passed. The `Unknown`
  authority case was later changed to be accepted, after review finding 2 below.
- Package validation's new copy-record check failed on test-audit's ledger record,
  which still named source-of-truth's entry point after the report-only rule moved
  to check design. Repointing the record made it pass.
- The project-docs checker now reads the document-homes table. The paths it derives
  equal the previous hard-coded set. A test with a fabricated map shows a new home
  becoming valid and an old one invalid; an unreadable map is reported as such.
- All four Forge foundations and `project-docs/` directories pass both checkers.
  Package validation, 14 collection tests and `git diff --check` pass.

### Independent meaning comparison

A fresh-context reviewer compared each rewritten passage with its prior text and
the linked targets. It found four material and ten minor problems; all were
addressed before the trials below were recorded.

| Finding | Disposition |
| --- | --- |
| The new authority section named adopted decisions as a source of authority | Authority comes from the user and their delegation; documents record it without expanding it. The removed "expand execution permissions" clause is restored. |
| Requiring known declaration values made an unidentified parent read as "no parent" | Reverted. `Unknown` is again a valid authority, and the format says so. |
| The method implied ordinary edits need only mechanical checks | It now defers to AGENTS.md for ordinary edits. |
| A reviewer could accept their own exception, and trials only had to be recorded | The owner accepts exceptions; trials must meet the routing requirement. |
| Ten minor wording, scope and link issues | Fixed, including restoring "design agreement" and "selected design" and limiting "seen to fail" to consistency checks as its source does. |

The reviewer confirmed that every deleted README statement is still stated in
the collection.

### Routing trials

Two fresh contexts worked in a synthetic consumer project outside this repository,
with the draft collection installed, provenance and a project hook modelled on
Forge's. Entry was through project instructions. The status trial ran before the
review fixes above; its route was unchanged by them.

| Case | Outcome | Reads |
| --- | --- | --- |
| Update the plan after implementing a backup whose test passes | Recorded "Implemented, not verified" with the reason, kept the dependent timer blocked, and told the owner that the restore rehearsal the policy requires is missing. It also showed the test fails without an archive. No private data was read. | 10 files, about 3,890 words |
| Fix a README spelling mistake | Fixed one word; read no skill or the new reference | 4 files, about 1,250 words |

Reading classification:

- The status reference (about 560 words) was useful rather than strictly required:
  the foundation's recovery row and the plan also implied the result.
- Its link to source-of-truth reached all of `durable-checks.md` (about 1,230 words)
  for a one-sentence rule. The link now points to that rule's section.
- Both trials read `foundation-format.md` (about 860 words) because the hook says to
  read the foundation through it, although the fixture's declarations were empty.
  This is an existing hook pattern, not part of this change; see the candidates
  below.

One run per case shows that the routes work, not that they are reliable.

### Candidates for the first full review

- Entry hooks send every task through `foundation-format.md`; a project without
  declarations, or a literal edit, may not need it.
- State terms still vary across skills, for example "design agreement", "selected
  design" and "approved use". Unifying them needs a decision on their meanings.
- Status and evidence limits "seen to fail" to consistency checks, as its source
  does. Applying it to all tests would be a deliberate tightening; the status trial
  did this unprompted and found it useful.
- The prose has many negative caveats; a clear-writing pass could state more rules
  positively.
- Whether this repository adopts a project foundation of its own.
- The unmerged `foundation-task-conventions` branch rewrites several files this
  change also edits; whichever lands second reconciles them.


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

## Passive guidance discovery and repair — 3 October 2026

Unreleased collection revision 0.3.0 adds conditional discovery hooks to all nine
members and a shared capture/source-repair procedure. Standing source-maintenance
scope belongs to consuming project instructions; source correction and pin
adoption remain separate. Bootstrap records that delegation only when authorized.
[Validation](passive-guidance-repair.md) retains five fresh consumer trials,
independent meaning review, mechanical checks and limits. Real-task reliability
and overhead remain to be established through use.
