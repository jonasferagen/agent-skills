# Project foundation 0.1.0 release evidence

The reviewed collection content is commit `e63aaf214a4bb97688df88d4f36452b61df1cbd7`.
The final release commit adds this evidence without changing the collection.
Three fresh reviewers covered every collection file and its catalog/instructions;
the coordinator reviewed both Python helpers and test files using Python Patterns
and the collection's consistency-check rules. The review compared the consolidated
source with both branch baselines, then independently checked all corrections.

## Review records

- [Policy, design, contracts and planning](policy-review.md).
- [Bootstrap, documentation, shared entry routes and authoring](docs-review.md).
- [Diagrams, tables and source of truth](visual-review.md), including correction
  checks and local light/dark rendering. The report's final disposition supersedes
  its initial snapshots. The whitespace finding is fixed in the reviewed commit.

Temporary image paths in these reports describe the actual inspection session;
they are not installed dependencies. Source, renderer versions and outcomes are
retained here. GitHub and editor-specific rendering were not verified.

## Fresh consumer trials

Each context began with fixture AGENTS and a complete copied draft collection;
no expected route or previous answer was supplied. The copy was based on
`fdbbb43` plus pending review corrections; the subsequently changed files concern
visual construction, not the exercised policy/model/spelling routes. Retained
files are the resulting fixture documents and actual read reports.

- [Policy assessment](trials/policy/trial-report.md): one recorded copy command
  and no restore, against a 24-hour loss limit and preservation of original photos.
  Original plan proposed daily cleanup. The result keeps recovery unverified and
  queues a scoped restore check without starting operational work or moving docs.
- [Conceptual modelling](trials/model/trial-report.md): two lots share a cultivar,
  one sample from lot A reports 82 percent, lot B is untested, and a shop draft
  attributes 82 percent to the cultivar. The initial model contained only cultivar
  and percentage. The result distinguishes lot, sample and observation, challenges
  a disagreeing second sample, and reconciles model, overview and existing queue.
- [Literal spelling](trials/spelling/trial-report.md): initial README said
  “A local photo archvie.” Only that spelling was changed; no skill body loaded.

Each case ran in its own fresh context. These establish observed routes, not
automatic client discovery, repeatability statistics or implemented project behavior.

## Consolidation and preservation

Merged the foundation task-routing branch with planning, modelling and shared
status/evidence work. Preserved phase/scope, canonical document homes, retired
worktree-skill behavior, policy-change consequences and source-authoring rules.

Historical experiments remain recoverable at `archive/bootstrap-run-2`,
`archive/web-stack-draft` and `archive/skill-discovery`. Their contents are not
part of the released collection. Clean task worktrees contained only disposable
Python caches beyond tracked files. The multi-repository worktree lock was removed
only after checking for active consumers and preserving its merged history.

## Checks

Package validation passes for 25 skill entries and one collection. All 14 helper
tests pass. The helpers read the template and document-home table at execution;
negative synthetic cases exercise ambiguous structure, undeclared references,
self-inheritance and misplaced/symlinked documents. They do not claim target access,
semantic compliance or operational readiness. No helper behavior changed in this
release consolidation.

All 314 checked current collection/catalog links and heading anchors resolve.
Whole-collection committed whitespace passes, including unchanged files. Mermaid
CLI 11.17.0 with Mermaid 11.16.1 rendered all examples locally; the visual report
records both themes and the corrected diagrams and tables. No material finding
remains open and no exception was adopted.
