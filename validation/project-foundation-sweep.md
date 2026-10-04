# Project-foundation sweep — 4 October 2026

Current follow-up evidence: [collection sweep](collection-sweep.md), including
executable example checks, locale-sensitive helpers and independent consumer trials.
The dated results below retain their original scope and limits.

This review covered the source collection in the isolated `collection-sweep`
worktree. Individual skill quality was reviewed first; collection consistency
was reviewed afterward. These source edits have not been released or adopted by
Forge or another consumer.

## Individual skill quality

All nine entrypoints, their UI metadata and supporting references were read.
Shared references, templates, both helpers and both helper test modules were
also inspected. Skill-creator, clear-writing and its instruction guidance, the
collection authoring convention and relevant diagram/table guidance informed the
pass. Existing behavior scenarios were consulted; earlier trial reports remain
evidence of their own revisions rather than new results from this sweep.

| Member | Coverage and result |
| --- | --- |
| Project bootstrap | Reviewed establishment, sparse five-table scaffold, existing-work preservation, installation and shared-entry routes. Retained the small starter and separate Git/setup authority. |
| Project policy | Reviewed interpretation, compliance, establishment, adequacy, delta review and writing routes. Requirement discovery and concrete consequences are already present; retained separate project/evidence gaps and unchanged obligations. |
| Project design | Reviewed conceptual models, workflows, integration choices, failure/change exercises and next-step compatibility route. Corrected the workflow reference's obsolete placement of processes/contracts inside architecture. |
| Project planning | Reviewed outcome/dependency sequencing, shared/local queues, partial results, deferred choices and the synthetic worked plan. No unsupported requirement or missing substantive route found. |
| Project contracts | Reviewed reading, application, design, adequacy, compatibility and interruption/unknown outcomes. Retained case-based discovery beyond the template and separate execution/acceptance/adoption. |
| Project documentation | Reviewed structure, connected views, diagram ownership, status and templates. Reproduced a helper false pass for architecture subtopics lacking their owning index and corrected it. |
| Source of truth | Reviewed authority selection, boundary/rung options and check durability. Clarified selected-artifact integrity as a separate invariant from live structural parity; behavioral literal expectations and existing golden guidance remain intact. |
| Clear writing | Reviewed prose, instruction strength/conditions and short text. Existing scope, factual preservation and uncertainty guidance was sufficient; no expansion made. |
| Diagrams and tables | Reviewed task/form routing, shared composition/verification, flowchart, ER and data-flow reading/construction/examples. Preserved house defaults, split thresholds and conditional rendering. No diagram source changed. |

## Collection consistency

Compared task routes, authority and status meanings, canonical document homes,
template callers, inheritance/bootstrap routes and installation procedures.

- Workflow design and multi-repository guidance now agree with the document map:
  process explanations and exchange obligations use their mapped owners, linked
  from architecture. Existing homes still require deliberate migration.
- Installation now specifies source directory/SHA/version/tag provenance, staged
  trusted-source checking, local-change preservation, complete-directory updates
  and route/provenance reconciliation. The collection entrypoint exposes that
  route; ordinary consumption still needs no installation pass.
- Collection version is `1.1.0` for the compatible installation integrity addition.
  Project-design `0.9.1`, project-docs `6.0.1` and source-of-truth `2.1.1` describe
  focused corrections. The coordinator owns the manifest and distributed checker.
- The source-of-truth check references distinguish a hash inventory that
  identifies reviewed revision bytes from a structural snapshot meant to track
  changing current owners. Regenerating a consumer inventory cannot accept drift.

## Checks and limits

The new architecture-index regression used isolated temporary fixtures for
`architecture/proposals/sample.md` and `architecture/examples/sample.md`.
Both were incorrectly accepted without `architecture/README.md`; the new test
failed on both cases before the helper fix. Afterward, absence is rejected and
adding the owning index passes. The helper still derives allowed homes from the
document map, without copying a new topology into its code.

- `python3 -m unittest discover -s collections/project-foundation/tests -q`:
  26 tests passed after the change, including all 25 existing tests.
- Skill-creator's `quick_validate.py`: all nine member packages passed.
- Coordinator-generated installation self-check: 82 files and 9 declared members
  passed. This checks the source inventory; a trusted-source staged-copy check
  remains part of the coordinated installation trials.
- `git diff --check -- collections/project-foundation`: passed.
- Whole-repository package validation was attempted during concurrent work; it
  stopped on stale service-foundation hashes for its checker and helper tests.
  The coordinator will refresh reviewed inventories and record the final result.
- No diagram source changed, so no new render check was run. Source review does
  not re-establish old renderer or theme claims.

Whole-repository package validation, inventory generation and fresh routing trials
are coordinated with the other collection changes. The required representative
routes are adoption/update checking, narrow reading or a literal edit avoiding
installation, and workflow design preserving mapped owners. Source inspection and
helper tests alone do not establish those routes, native discovery, inheritance
resolution, live compliance or downstream installation integrity.

## Further improvements to evaluate

- Use the next real bootstrap/update to verify a generated shared-installation
  hook from both a main checkout and an actual nested task worktree. Static links
  and checksum checks cannot establish access through those contexts.
- Extend source-of-truth's behavioral evidence with a real build-time generation
  boundary and a check invoked from another directory; its existing validation
  records limits around those cases. Select meaningful failures before adding tests.
- If ordinary architecture tasks repeatedly load irrelevant runtime/content-split
  detail, move that conditional detail to one design reference and trial the
  narrow and deeper routes. No restructuring is justified by entrypoint length
  alone.
- Add sequence/state family guidance only after a concrete notation or semantic
  gap appears. Current generic construction and declared-notation routes support
  those forms; empty family scaffolds would not make the collection more complete.

## Coordinated completion

The [coordinated sweep](collection-sweep.md) records the final source inventories,
combined checks and retained consumer trials. Earlier pending or partial results
on this page describe the review stage at which they were recorded. No release
or installed Forge pin was changed.
