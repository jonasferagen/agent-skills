---
name: repository-maintenance
description: "Review an existing repository or project for structural and semantic drift across its instructions, capabilities, dependencies, checks and open work. Use for an assigned maintenance review or coherence assessment; a focused edit or single failing check does not call for a repository sweep."
metadata:
  version: "0.1.0"
---

# Repository maintenance

Assess whether a maintained repository still forms a coherent whole: its stated
responsibilities, instructions, implementation and evidence should agree. Work
within the requested review or repair scope. This method requires no companion
skill, prescribed document shape or dedicated maintenance file.

## Establish the review boundary

Start with the project's instructions and existing routes to ownership,
capabilities, verification and open work. Use local maintenance guidance when
present. Otherwise derive a bounded scope from the request and repository;
missing maintenance scaffolding is not itself a defect.

Distinguish a review from authorized repairs. Review alone does not authorize
changing policy, removing capabilities, updating dependencies or applying changes
to consumers. Existing authorization remains valid; do not add a confirmation
step for work already within scope. For edits, follow the repository's isolation
and integration rules and preserve unrelated work.

Use a previous review or plan only for its still-relevant findings. Compare those
findings with current owners and installed revisions; planned changes stay
pending until evidence shows they landed. If no useful basis exists, make a
bounded baseline assessment. State which repositories and boundaries were
examined and which remain unknown.

## Follow the material relationships

Select the questions that matter to this repository and the assigned scope.
Follow a concrete claim or dependency rather than reading every file.

- **Scope and consumers.** Separate what is shipped, explicitly adopted and
  demonstrably exercised. Trace whole-package and individual-file imports,
  generated copies, helper code and named task routes. Missing invocation
  evidence alone does not establish disuse; an import alone does not establish
  usefulness. Inspect live source and declarations before treating historical
  records as current adoption.
- **Ownership and containment.** Identify what decides each important rule and
  what implements it. Check that an installation can perform its promised tasks
  using its shipped files and declared prerequisites. Follow prose directions as
  well as links and imports. Separate reusable methods, adopted conventions and
  local choices. Repair a copied rule at its owner, then use the authorized
  propagation route; local patches need an explicit local ownership basis.
- **Current claims.** Compare relevant guides, templates, configuration, code
  and checks against their governing decisions. Look for contradictory
  obligations, obsolete limits, unsupported promises and planned behavior stated
  as present. Exact copy equality establishes provenance or synchronization,
  not that surrounding instructions make sense together. Assess stated
  principles through concrete cases, not matching slogans.
- **Useful structure.** Trace representative narrow and broader tasks, plus a
  nearby request that should avoid the workflow. Judge whether the reader finds
  the right owner and preserves necessary obligations before comparing reading
  cost. Different layouts may serve different tasks; avoid imposing uniformity
  or an arbitrary length target. Label informed walkthroughs as such rather than
  claiming independent discovery.
- **Evidence lifetime and open work.** Separate reusable scenarios and inputs,
  executable checks, current limitations and unresolved decisions from dated
  execution output. Retain evidence for a present reader, decision or applicable
  obligation, with an end condition suited to that need. Age alone does not
  justify deletion, and a citation or index entry alone does not justify
  retention. Reconcile existing findings with current source before opening
  duplicates. An unmeasured possibility is not automatically pending work.

When available and needed, use `source-of-truth` to resolve competing definitions,
`test-audit` to assess suite effectiveness, `verification-design` to choose
checks, and `clear-writing` to revise prose. These are specialist routes, not a
required reading list or installation dependency. Use the project's existing
methods when they are unavailable.

## Check the findings and close the review

Run applicable documented checks within the task's execution scope. Compare
changes inside imported paths with their source when available; commit age alone
cannot establish an outdated import. Keep source comparison distinct from a
check against recorded hashes. Report missing prerequisites and what passing
checks actually establish. A review does not by itself commission live service
operations, paid calls or destructive cleanup.

For each material finding, give the supporting location, consequence, owning
source and smallest useful correction. Separate an established defect from a
scope choice or untested hypothesis. State what remains coherent, checks run,
limits and the next useful action. If nothing actionable remains, say so.

Use the existing coordination owner for required follow-up. Do not create a new
queue or report solely because a review ran. Where a retained record is required,
keep the minimum evidence its current reader needs and its retirement condition.
For authorized repairs, verify the affected boundary and reconcile the finding
in its current home; do not maintain a parallel history of successful reviews.
