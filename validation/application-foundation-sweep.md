# Application foundation sweep — 2026-10-04

This review assessed application-design and its references for skill quality
before reviewing the collection's consistency. It used Skill Creator, Clear
Writing and its instruction guidance, and Diagrams and Tables' table guidance.
No diagram or runtime helper was authored or changed by this pass.

## Phase 1: skill quality

The member review covered `application-design/SKILL.md`, its UI metadata,
`external-integrations.md`, `run-records.md`, the scope document and the current
member validation scenarios and trial limits. The main workflow was coherent:
start with a concrete operation, retain existing owners, distinguish application
decisions from external mechanisms, and add state or layering only for actual
responsibilities. Its UI metadata needed no change.

Focused corrections:

| Surface | Finding and change |
| --- | --- |
| Design output | The entrypoint implied writing a repository design even when the request only needed a proposal. It now presents the design and uses the existing repository owner when a repository artifact is requested. Review findings still need no rewrite. |
| External operation result | Retained-byte and publication rules are now conditional on a retained deliverable. An ordinary lookup or status read retains only what its project contract requires. |
| External evidence | An unavailable current contract is an explicit assumption and implementation prerequisite; independent local design can continue. A design trace stays distinct from authorized runtime experiments, live provider calls and paid retries. |
| Run records | Diagnostic and attempt retention now explicitly follows project data and retention policy, excluding secrets and prohibited input content. |

The review preserved effect identity before submission, the uncertainty window
before provider identity is saved, explicit disposition of unresolved attempts,
safe-read versus effectful retry distinctions, late-output ownership, complete
deliverable capture and acceptance authority. Run-record guidance still separates
byte identity from provenance, one-file replacement from transactions and
durability, and equal observed source states from proof of no intermediate edits.

## Phase 2: collection consistency

The collection remains one self-contained application-design member. Its two
conditional references serve the same operation trace; neither justifies another
skill or a general job framework. The task table now links application-design
directly for external work, exposes the existing retained-run-record route, and
includes checking installation integrity.

Project-wide architecture, provider selection, handoffs and document ownership
remain project concerns. Language, service and verification companions stay
independently pinned and routed through project instructions; no cross-installation
relative links were added. Missing companions do not block the core workflow,
while project-required guidance remains a prerequisite for the affected
implementation task.

Installation guidance now covers a selected-source checker against a complete
staged copy, manifest and file inventory comparison, limits of consumer self-checks,
preserving local changes before replacement, updating provenance and routes
together, and source-only regeneration after reviewed edits. It does not introduce
automatic client registration, dependency resolution, upstream tracking or
authority to accept consumer drift.

Collection version: `0.2.0`, for the compatible installation-integrity capability.
Member version: application-design `0.1.1`, for the corrected scope conditions.
The root sweep owns the new manifest and synchronized checker; this pass did not
create, regenerate or modify those files.

## Verification and limits

- System Skill Creator `quick_validate.py` passed application-design.
- `git diff --check -- collections/application-foundation` passed.
- A local path check resolved all nine Markdown file links inside the collection's
  installation unit; the existing UI short description met its 25–64 character
  range. This did not validate rendered output or heading anchors.
- Revised passages were compared with their prior text for preserved scope,
  project ownership, execution authority and uncertain-outcome handling.
- These are static checks. No new behavioral agent trial, provider request,
  crash-recovery test, native discovery test or consumer adoption ran in this pass.
- The dated 3 October design trials remain evidence for their pinned revision;
  they were not regraded as evidence for this revision or its installation tool.
- Final inventory synchronization, whole-repository package checks, complete-copy
  integrity and checker tests belong to the root sweep.

Changed routes need installed-consumer trials outside the authoring repository:
a pure read-only operation without companions; an external operation with an
uncertain submission and retained deliverable; a local retained run record with
an interrupted publication; a literal wording-edit near-miss; and a staged
installation check after the root's checker is available. Observe actual reads,
conditional references reached, proposal versus execution claims and preserved
input/output ownership. A status-read case should avoid durable deliverable or job
machinery unless its contract requires it.

## Additional improvements

- Point the existing member validation page and scope document to the current
  sweep and installation-integrity capability while preserving their dated
  evidence and explicit limits.
- Run a retained-run-record implementation trial against a disposable local
  fixture. The existing design evidence does not establish atomic publication,
  crash recovery, competing-writer exclusion or durable storage.
- Exercise a core-only, pure read-only application case. Existing trials have not
  shown that the collection avoids state or companion machinery for that case.
- When an actual provider adapter is implemented, retain the official capability
  evidence and separately verify authorized execution. General operation guidance
  should not accumulate provider-specific commands or capabilities.

## Coordinated completion

The [coordinated sweep](collection-sweep.md) records the final source inventories,
combined checks and retained consumer trials. Earlier pending or partial results
on this page describe the review stage at which they were recorded. No release
or installed Forge pin was changed.
