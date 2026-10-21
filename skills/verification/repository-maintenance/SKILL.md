---
name: repository-maintenance
description: "Review an existing repository or project for structural and semantic drift across its instructions, capabilities, dependencies, checks and open work. Use for an assigned maintenance review or coherence assessment; a focused edit or single failing check does not call for a repository sweep."
metadata:
  version: "0.2.0"
---

# Repository maintenance

Assess whether a maintained repository still forms a coherent whole: its stated
responsibilities, instructions, implementation and evidence should agree. Work
within the requested review or repair scope. Drift is any disagreement between
those parts, structural (a file, link or dependency that no longer exists or is
no longer reached) or semantic (a claim, rule or test that no longer matches
what the code does). The review boundary is the set of repositories, paths and
dependents you examine. This method needs no particular document layout or
dedicated maintenance file.

## Establish the review boundary

Start with the project's instructions (`AGENTS.md`, `CONTRIBUTING.md`, README or
similar) and what they point to: who maintains what, what the project claims to
do, how it is checked and where open work is tracked. Use local maintenance
guidance when present. Otherwise derive a bounded scope from the request and the
repository itself, such as its manifests, CI configuration and test commands, and
state what you inferred; missing maintenance scaffolding is not itself a defect.

Distinguish a review from authorized repairs. Review alone does not authorize
changing rules, removing capabilities, updating dependencies or changing the
projects that depend on this one. Work the user has already authorized stays
authorized; do not add a confirmation step for it. For edits, follow the
repository's branching and integration conventions and preserve unrelated work.

Use a previous review or plan only for its still-relevant findings. Compare those
findings with the current source, maintainers and pinned versions; planned
changes stay pending until evidence shows they landed. If no useful basis exists,
make a bounded baseline assessment. State which repositories and boundaries were
examined and which remain unknown.

## Follow the material relationships

Select the questions that matter to this repository and the assigned scope.
Follow a concrete claim or dependency rather than reading every file.

- **Scope and dependents.** Separate what the repository ships, what dependents
  (other projects or packages that import, pin or copy it) explicitly use, and
  what is demonstrably exercised. Trace whole-package and individual-file
  imports, generated copies, helper code and the commands or jobs that call them.
  Missing invocation evidence alone does not establish disuse; an import alone
  does not establish usefulness. Inspect live source and declarations before
  treating historical records as current use.
- **Ownership and containment.** Identify which document, configuration or code
  decides each important rule and what implements it. Check that an installation
  can perform its promised tasks using its shipped files and declared
  prerequisites. Follow prose directions as well as links and imports. Separate
  reusable methods, adopted conventions and local choices. Repair a copied rule
  at its source, then update the copies the way the project normally does
  (a sync script, a version bump, a re-import); patch a copy locally only when
  the project treats that copy as its own.
- **Current claims.** Compare relevant guides, templates, configuration, code
  and checks against the decisions they are meant to implement. Look for
  contradictory obligations, obsolete limits, unsupported promises and planned
  behavior stated as present. Exact copy equality establishes provenance or
  synchronization, not that surrounding instructions make sense together.
  Assess stated principles through concrete cases, not matching slogans.
- **Useful structure.** Trace representative narrow and broader tasks, plus a
  nearby request that should avoid the workflow. Judge whether the reader finds
  the deciding document and preserves necessary obligations before comparing
  reading cost. Different layouts may serve different tasks; avoid imposing
  uniformity or an arbitrary length target. Such a walkthrough (tracing a task
  through the documents as a reader would) is informed by what you already know;
  label it as such rather than claiming independent discovery.
- **Evidence and open work.** Separate reusable scenarios and inputs, executable
  checks, current limitations and unresolved decisions from dated execution
  output. Keep evidence that a present reader, decision or obligation still
  needs, and say when it can go. Age alone does not justify deletion, and a
  citation or index entry alone does not justify retention. Reconcile existing
  findings with current source before opening duplicates. An unmeasured
  possibility is not automatically pending work.

Where two sources define the same thing differently, decide which one the
project treats as authoritative and fix the other. Where a test suite's
effectiveness or a prose revision is in question, use the project's existing
methods and conventions for those; if it has none, say so and judge the case
directly.

## Check the findings and close the review

Run the documented checks that apply, within what the task permits you to
execute. Compare changes inside imported or vendored paths with their source when
available; commit age alone cannot establish an outdated import. Comparing
content with upstream is distinct from checking a recorded checksum or pinned
commit: a match there proves the copy is unchanged, not that upstream has not
moved. Report missing
prerequisites and what passing checks actually establish. A review does not by
itself authorize live service operations, paid calls or destructive cleanup.

For each material finding, give the supporting location, consequence, the
document or code that decides the rule, and the smallest useful correction.
Separate an established defect from a scope choice or untested hypothesis. State
what remains coherent, checks run, limits and the next useful action. If nothing
actionable remains, say so.

Report findings to the user and file required follow-up where the project
already tracks work (its issue tracker or open-work list); if it tracks work
nowhere, the report to the user is the record. Do not create a new tracker or
report solely because a review ran. Where the project requires a
retained record, keep the minimum evidence its current reader needs and say when
it can be removed. For authorized repairs, verify the affected boundary and
resolve the finding where it is tracked; do not maintain a parallel history of
successful reviews.
