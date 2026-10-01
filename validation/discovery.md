# Discovery review — 2026-09-30

## Scope and measured context

The review includes the 15 existing packages after reconciliation with main,
plus the new capture-pattern package. Word counts describe source text, not
token usage or a guarantee about host selection.

Existing descriptions: 978 → 479 words. The new capture-pattern description adds 36 words.

The three largest entrypoints now route to conditional references:

- `change-workflow`: 2200 → 1032 words.
- `diagrams-and-tables`: 2964 → 324 words.
- `source-of-truth`: 2339 → 518 words.

## Decisions

Descriptions were shortened for change-workflow, diagrams-and-tables,
node-patterns, source-of-truth, typescript-patterns, project-policy,
runtime-operations, containerization and postgres-design. Their distinctive
triggers remain; procedures and scope details remain in the bodies. Other
descriptions were already concise enough for this pass.

Existing domain instructions were moved, with their links updated, into
conditional references. This is a routing change; no project gate or workflow
authorization was intentionally altered. The default branch's recent skill
resolutions were preserved; the unrelated TypeScript casing branch was not
merged into this change.

Lesson capture owns recognizing and placing a reusable finding. Verification
design owns selecting evidence for active work; test-audit examines settled
tests. Shared-code design decides distribution boundaries; source-of-truth
decides authority for rules and vocabularies. A common subject alone does not
require loading every neighboring package.

## Activation cases

- Original Atlas/Work consolidation scan: inspect the relevant project; consider
  lesson capture when a concrete reusable finding emerges. Already-covered
  guidance should be identified without another addition.
- A requested literal spelling replacement: complete the edit or answer without
  invoking lesson capture.
- Choosing checks for an active change: verification-design.
- Reviewing whether settled mocks prove a real request: test-audit.
- Copied kit versus package: shared-code-design.
- Regex disagreement across application and database: source-of-truth.

## Verification and trial results

Package and moved-section verification is recorded below. Fresh-agent results
are recorded in [Capture Pattern validation](pattern-capture.md). The trial uses the current project, whose milestone work
has advanced since the original prompt; it does not reconstruct the earlier tree.

Structural verification before the trial:

- `python3 scripts/validate-packages.py`: 16 packages passed.
- System `quick_validate.py` for `lesson-capture`: passed.
- Local Markdown path and heading check: 254 links passed.
- Compared the relocated guidance with `d8895d1`: all 20 substantive sections
  remain verbatim apart from changed link destinations. The old symptom table
  was replaced by the narrower reference router.
- `git diff --check`: passed. No Mermaid source was changed.

The final renamed `capture-pattern` package also passed the system
`quick_validate.py` check and repository package validation. The rename adds
explicit invocation for small ideas and a simplicity check for accumulating
exceptions. Earlier trial names are preserved in their historical records.

## Applying our own guidance

README already said that skills should meet the standards they teach. The
authoring section and AGENTS.md now make selection of relevant guidance explicit,
including Capture Pattern. This clarifies the existing authoring principle and
extends its concrete routing beyond writing and visuals. The separate full
pre-release pass remains recommended; it is not a new release gate.

Impact: repository authoring instructions and this evidence record change.
Package interfaces, installed consumers, stored data, permissions, operations
and recovery obligations are unaffected. No full-catalog compliance audit is
claimed. Clear Writing was applied to the changed instructions; source-of-truth
informed keeping the principle in README with a routing link from AGENTS.md.
The discovery refactor itself applies conditional loading to this catalog.

Final checks: 16 packages passed repository validation; capture-pattern passed
the system quick validator; 258 local Markdown paths and heading anchors passed;
`git diff --check` passed. The explicit small-idea trial also passed, as recorded
in [Capture Pattern validation](pattern-capture.md). No runtime helper or Mermaid
source changed in this discovery pass.
