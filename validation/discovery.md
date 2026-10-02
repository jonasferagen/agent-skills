# Discovery and routing validation

## Routing trial method

The [routing requirement](../README.md#routing-quality) owns acceptance. Use this
method when triggers, entrypoints, shared guidance or packaging change, and before
a collection release. Routine prose edits do not require repeating it.

Select realistic cases for the changed routes:

| Case | Observe |
| --- | --- |
| Cold entry into ordinary consumer work | Reads before useful work and irrelevant activation |
| Work requiring deeper guidance | Whether required references are reached and obligations preserved |
| Nearby work outside the changed skill's scope | Whether the agent avoids unrelated guidance |
| Source authoring when consumption/authoring routes change | Whether relevant maintenance rules still apply |

Use a fresh agent context when available. Place the consumer fixture outside the
authoring repository with an installed copy, a realistic project instruction hook
and provenance. Start from that hook or normal discovery metadata; do not provide
the expected route. Record whether entry was explicit invocation, supplied metadata
or project instructions. A source-authoring trial instead starts in an isolated
copy of this repository. Keep live systems outside the trial.

Have the evaluator record files actually read, approximate whitespace words,
repeated reads, truncation and reused context. Distinguish instruction/template
reads from catalogs, generated output review and mechanical checks. Do not call a
partial subtotal total context use. For each material read, classify it as required,
useful or irrelevant with a reason; also report required guidance missed and the
output constraints preserved or violated. An unexercised case is a limitation.

The reviewer checks artifacts and routing evidence. A consumer reaching source
maintenance material without a task reason is a finding. Missing necessary deeper
guidance is also a finding, even if reading falls. Compare equivalent tasks across
revisions; use no universal word threshold. Record the smallest supported fix and
remaining gaps. A single successful run demonstrates a route, not its reliability.

The Atlas catalog incident is an initial failure case: the third bootstrap trial
read a large source README while consuming a collection. Its 6,262-word
instruction subtotal excluded an additional catalog read, including truncated
output. See [the trial](atlas-bootstrap-experiment.md#selection-only-routing-trial--2-october-2026).
Installation location and authoring instructions were part of the trial setup;
this does not establish that an installed collection necessarily causes those reads.

Keep observations from ordinary usage between trials. Capture a demonstrated
problem or candidate in its existing validation record; do not turn every
observation into another mandatory instruction.

# Earlier discovery review — 2026-09-30

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

## Port to main — 2026-10-01

The branch this record came from grouped the packages by area and built a plugin.
Main keeps flat packages, so that layout was not ported, nor were the things that
came with it: the plugin build and `identifiers.toml`, the package-layout
validation, sentence-case display names, plugin-qualified invocations and the
matching link edits in AGENTS.md. The discovery work was ported with its
validation records:

| Package | Version on main, before to after | Brought over |
| --- | --- | --- |
| shared-code-design, verification-design | new, 0.1.0 each | The two skills from `d8895d1` |
| pattern-capture | new, 0.3.0 | The skill, called lesson-capture and then capture-pattern on the branch, with the guidance on learning from skill use |
| containerization | 0.2.0 to 0.5.0 | Image reuse, separate environments, applying values where the tool reads them |
| test-audit | 0.2.0 to 0.3.0 | Integration-test advice narrowed to the failure each test can observe |
| source-of-truth | 1.3.0 to 1.4.0 | Entrypoint split into references; the external identifier rule |
| change-workflow, diagrams-and-tables | 0.2.0 to 0.2.1 | Entrypoints split into conditional references |
| node-patterns, postgres-design, project-policy, runtime-operations | patch bump each | Shortened descriptions |

No release tag was created or moved. A version bump alone publishes nothing.

Where main differs from the measurements above:

- Main's `typescript-patterns` (2.0.0) and `bash-patterns` were rewritten
  independently and keep their own descriptions, 30 and 34 words against 32 and 42
  on the branch. Main's `typescript-design`, `python-patterns` and `python-design`
  (26, 28 and 24 words) arrived after this review and were not part of it.
- The 13 packages that already existed on main had 874 words of description before
  the port and 393 after it. With the three new skills, the 19 descriptions total
  589 words and none exceeds 42.
- The three splits were checked line by line against main's text, ignoring link
  targets. Every body line of `change-workflow` is still present. In
  `diagrams-and-tables` and `source-of-truth` the missing lines are the routing
  prose and the old symptom table that the reference router replaced.
- The activation trials above ran on the branch. They were not repeated on main,
  so they do not show how the merged descriptions select skills there.

Checks on main's tree: `python3 scripts/validate-packages.py` passed for 19
packages; 252 relative links and anchors in 96 Markdown files resolved; and
`git diff --check` against main was clean. No Mermaid source changed, and no helper
script changed.

## Source grouping — 2 October 2026

Moved the six TypeScript, Python, Bash and Node packages under
`skills/languages/`. Package names, metadata, invocation names and contents are
unchanged; all moved files matched their previous HEAD versions byte for byte.
The catalog now separates languages and runtimes from code and data design.
Existing consumers keep their pinned provenance; future imports use the new
source paths and retain the same installed package names.

Package validation now descends through category directories and rejects duplicate
package names. All 21 packages passed. Isolated validator trials covered a mixed
flat/grouped layout, duplicate names, a directory missing its manifest, and a
cross-package link. The invalid cases were rejected. Catalog, agent instructions
and validation-page local link targets passed, as did `git diff --check`.

Clear-writing guidance informed the installation and layout wording;
diagrams-and-tables guidance retained the catalog tables for comparing skill
responsibilities. Python-patterns guided the validator change. No skill content
or runtime helper changed. These checks establish source-package integrity;
client discovery and user-wide installation were not exercised.

## Full catalog grouping — 2 October 2026

Moved the remaining 15 packages into `projects/`, `authoring/`, `design/`,
`verification/`, `operations/` and `workflow/` under `skills/`. Together with
`languages/`, these are browsing categories based on the task that selects a skill.
The catalog, agent instruction links and affected validation links and commands
now use the grouped source paths. Installed names and pinned consumer provenance
remain unchanged.

Compared every moved package file against a snapshot taken immediately before
this move: all contents were byte-for-byte unchanged. All 21 packages passed
package validation, 86 local link targets in the catalog, agent instructions and
validation pages resolved, and `git diff --check` passed. The stale-path search
found no remaining old paths for these packages in those current references.
No behavioral skill split or client installation was performed.

The next proposed specialization is runtime-operations: credential handling,
local service control, and database backup/recovery. Containerization and
source-of-truth are subsequent candidates. Those remain proposals; directory
placement alone does not resolve their overlapping responsibilities.
