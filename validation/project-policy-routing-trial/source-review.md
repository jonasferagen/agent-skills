# Source maintenance review

This review reuses the earlier contract-consumer trial context. It is not a fresh source-authoring discovery trial. No repository files were edited.

## Findings

No blocking coherence or routing defect found in the inspected diff.

One small preservation concern: the former project-policy introduction explicitly required verifying affected behavior when simplifying a mechanism. The replacement at SKILL.md:14–17 preserves required outcomes but omits that explicit verification step. The substantive change reference still requires evidence and appropriate checks, so policy transitions retain that obligation. For simplifications that do not change policy, consider retaining the short explicit verification instruction in the entrypoint if exact preservation is intended.

The six policy axes, table-only owner, relocation-before-removal rule, every-edit impact assessment, substantive relaxation review, observed-transition treatment, authorized execution limits, and evidence/readiness distinction survive the move to establish-and-change.md. Its relative reference paths are consistent with its deeper location.

The convention is scoped to source maintenance through AGENTS and README; consumer routes do not acquire a dependency on docs/project-foundation-authoring.md. It requires relevant task distinctions without a universal mode taxonomy. The policy entrypoint separates interpretation, compliance, establishment/change and adequacy review, while the changed-circumstances escape route prevents narrow interpretation from suppressing a necessary impact assessment.

The recorded decision to retain diagrams-and-tables is coherent with its current entrypoint: reading and semantic review are shared, construction routes are conditional, and tables avoid diagram-family guides. The decision states reconsideration triggers rather than claiming a split was experimentally disproved. No new families or empty directories are introduced. I inspected the entrypoint, not all family implementation details.

## Checks and remaining evidence

- Package validation passed: 25 skill entries, including one collection.
- git diff --check passed.
- Read the complete tracked diff and both new untracked documents. Validation checks do not establish routing behavior.
- Current policy validation records predate this task-routing revision; the acceptance requirement still needs applicable practical trials and a durable record. This review did not run or inspect those new trials and makes no claim about their status elsewhere.
- No rendering, runtime verification, external action, source edit, or release was performed.

## Reads and limits

Read AGENTS first. The current tracked diff supplied old/new policy text and the changed portions of DECISIONS, README, COLLECTION, AGENTS and UI metadata. Full files read below have approximate whitespace word counts:

- `AGENTS.md`: 491 words.
- `docs/project-foundation-authoring.md`: 787 words.
- `collections/project-foundation/skills/project-policy/references/establish-and-change.md`: 1085 words.
- `collections/project-foundation/skills/project-policy/references/policy-changes.md`: 919 words.
- `collections/project-foundation/skills/diagrams-and-tables/SKILL.md`: 514 words.
- `validation/project-policy.md`: 1176 words.

Additional partial reads: README lines 200–300 plus routing-quality section (roughly 900 words); validation/discovery.md routing method and adjacent history (roughly 550 words); policy SKILL first 28 numbered lines (roughly 220 words). The full tracked diff was approximately 3,800 words including removed text and diff syntax; this is not a total context measurement.

Useful reads: maintenance instructions/convention, policy old/new text and references, diagram entrypoint, routing acceptance and current behavioral scenarios. Unnecessary reads: policy validation's dated history was read with the whole file, although only scenarios and absence of current revision evidence were needed; adjacent README capture instructions and discovery history also exceeded the focused need. AGENTS additions and policy introduction were repeated through the diff/numbered excerpt. Mechanical counting reread full files without presenting them again. No tool output was truncated. The initial README heading search missed level-three headings and was corrected with focused reads.

No required source-authoring guidance was missed for this read-only review: no worktree creation/edit, prose revision, diagram construction, family change or pattern-capture implementation was performed. Existing consumer-contract knowledge was reused only as context, not as evidence for policy routing performance. The review itself does not demonstrate cold-start behavior or quantify context savings.
