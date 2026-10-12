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

For discovery or reporting acceptance, start a new agent for each case with no
forked conversation history, prior case results, expected findings or preloaded
skill bodies. Record the context configuration and the exact skill metadata
supplied at startup, including any stale or absent entries. Fresh conversation
context does not establish fresh metadata. If the host cannot provide or establish
this isolation, record the run as an informed review or walkthrough; it cannot
pass independent discovery or reporting acceptance.

Place the consumer fixture outside the authoring repository with an installed
copy, a realistic project instruction hook and provenance. Start from that hook
or normal discovery metadata; do not provide the expected route. Record whether
entry was explicit invocation, supplied metadata or project instructions. A
source-authoring trial instead starts in an isolated copy of this repository.
Keep live systems outside the trial. Reused agents can implement fixes and review
known findings, but their results remain separate from independent acceptance.

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
output. See [the trial](https://github.com/jonasferagen/agent-skills/blob/9093cfca4ffa93df1be35b1bb7ebffaef0baac65/validation/atlas-bootstrap-experiment.md#selection-only-routing-trial--2-october-2026).
Installation location and authoring instructions were part of the trial setup;
this does not establish that an installed collection necessarily causes those reads.

Keep observations from ordinary usage between trials. Capture a demonstrated
problem or candidate in its existing validation record; do not turn every
observation into another mandatory instruction.

## Reporting acceptance trials

Use these trials when adopting or changing the shared reporting and repair
checkpoint, or claiming that agents spontaneously report guidance problems.
Before a run, keep an evaluator-only record of the seeded problem, its consequence
and the expected observable behavior. Give the agent an ordinary task, installed
skills and project instructions. Do not mention the seeded problem, reporting as
the task, the desired skill or expected finding in the task prompt.

Exercise a consequential guidance or routing problem and another relevant case,
such as an unavailable capture or source-repair route. Include a nearby successful
case that should complete without a capture pass or generic improvement proposal.
Start every case under the isolation requirements above. Freeze prompts, inputs,
source pins and grading criteria before the run; retain intervening prompt changes
as distinct runs rather than silently treating a coached retry as spontaneous.

Retain each prompt, fixture and input revision, startup metadata, context
configuration, tool-call/read trace, resulting artifacts and final answer. Grade
the agent's first completed answer and artifacts before asking diagnostic
follow-ups. A retrospective claim about files read is supporting testimony, not
an observed read trace. If the trace is unavailable, mark read-based conclusions
unverified and assess only behavior visible in retained artifacts and output.

For a problem case, grade each criterion separately:

- The agent identifies the concrete problem and explains its effect on the task.
- It retains or routes the finding with its disposition, or reports the missing
  route and preserves the candidate in the hand-back.
- It uses Pattern capture when the finding meets that workflow's trigger, and
  identifies an existing home or states what evidence or source location is missing.
- It continues unaffected work and keeps source repair and installation changes
  within the task's authorization.

For the successful control, verify that the ordinary task finishes without an
unnecessary capture pass or improvement proposal. Record missed obligations,
unnecessary activation, observed evidence and unverified criteria for every case.
Report results per case and across repeated independent runs; one pass proves
that run, not reliable activation. Package checks and manual instruction reviews
cannot substitute for these behavioral trials.

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
are recorded in [Capture Pattern validation](https://github.com/jonasferagen/agent-skills/blob/183148d34dd1434df0402a0c6e69b195da84a525/validation/pattern-capture.md). The trial uses the current project, whose milestone work
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
in [Capture Pattern validation](https://github.com/jonasferagen/agent-skills/blob/183148d34dd1434df0402a0c6e69b195da84a525/validation/pattern-capture.md). No runtime helper or Mermaid
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

## Consumer and authoring route trials — 2 October 2026

Two fresh subagents tested revision `617af2a` in isolated fixtures under
`/tmp/routing-trials-7ayu3ssm/`. Entry was through project/repository instructions,
not host automatic discovery. They received ordinary tasks rather than expected
routes. Source repositories and real Atlas were unchanged. The parent inspected
both edits.

### Cold consumer: shorten a README introduction

The installed collection lived outside the authoring repository. The agent changed
“A local planning project, currently at the planning stage” to “A local project
currently in planning.” It read no source catalog or maintenance material and
preserved local scope and planning status.

| Guidance read | Words | Agent's reason |
| --- | ---: | --- |
| Project AGENTS | 31 | Project constraints and route |
| Installed COLLECTION | 332 | Find writing entrypoint |
| Foundation authority | 339 | Interpret consultation rules |
| Clear-writing entrypoint | 549 | Preserve meaning during edit |
| Shared authoring | 171 | Collection authoring and revision rules |
| Short-text reference | 365 | Explicit route for brief descriptions |

Total displayed guidance was 1,787 whitespace words, once per file, without
truncation. Machine reads for counting and README inspection were excluded.
The agent classified all six as required by current instructions. Parent review
agrees that they follow the routes, but necessity to follow a route is not evidence
that every read helped this small edit. Authority and revision guidance had low
marginal value here. A narrower routine-writing route remains a candidate; no
further rule was added during this trial.

Exact-content and whitespace checks passed. The fixture lacked Git, so its first
`git diff --check` attempt failed, and `python` was absent so the agent used
`python3`. These are fixture/tooling limitations, not evidence of a collection
routing defect. No network or dependencies were used.

### Source authoring: clarify proposed versus completed action

The agent worked in an isolated Git clone and added “proposed or” to the existing
short-status instruction in clear-writing. It avoided duplicating the rule and
ran package validation (22 entries, one collection) and `git diff --check`.
The resulting edit remains only in the trial fixture.

It requested approximately 6,906 words across AGENTS (362), README (4,751),
clear-writing (549), instruction guidance (506), the target short-text reference
(365), and the first 20 lines of its validation page (373). The combined read was
truncated in README history, so 6,906 is requested content, not measured delivered
context. The agent identified unrelated origins and release history as unnecessary.
A heading search also exposed prior verification snippets, which it reported as a
minor departure from the instruction to avoid prior trial reports.

This demonstrates that authoring obligations remain reachable. It also shows
continued source-catalog overreading on a narrow authoring task. The next candidate
is clearer section-level routing or separating maintained catalog/authoring rules
from long historical material; this trial alone does not select that design.

### Acceptance and remaining evidence

The consumer/source boundary worked in this cold-entry case; appropriate writing
rules and authoring checks remained reachable. Neither task activated diagram
construction, policy-transition work or unrelated source maintenance. The earlier
[diagram countercheck](https://github.com/jonasferagen/agent-skills/blob/9093cfca4ffa93df1be35b1bb7ebffaef0baac65/validation/atlas-bootstrap-experiment.md#diagram-countercheck-at-the-same-revision)
provides evidence of deeper routing at its named revision, not a new trial here.
No policy-transition or automatic-host-selection trial was run. These results
support the scoped routing change but do not establish collection-wide efficiency
or reliability. No release is being declared ready from these two runs.

## Focused authoring routes — 2 October 2026

The [authoring routing trials](https://github.com/jonasferagen/agent-skills/blob/9093cfca4ffa93df1be35b1bb7ebffaef0baac65/validation/authoring-routing.md) test lighter consumer entry
and direct source-maintenance sections. The source rerun avoided full catalog and
validation-history reads but still exposed historical snippets through a broad
search; its isolation limit remains explicit.
