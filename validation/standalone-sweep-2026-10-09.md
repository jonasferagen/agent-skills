# Standalone catalog sweep — 2026-10-09

A source-maintenance review of all 28 skill packages, the README, the
repository instructions, the decision log and the validation routes, looking
for gaps, inconsistencies between packages and places where a package or a
maintenance page still depended on something outside this repository. It
started at `78f69c6b` in a task worktree. One agent reviewed and edited; the
routing observations below are an informed reading, not independent discovery
acceptance. No release tag or consumer installation is created here.

## Findings and dispositions

| Finding | Disposition |
| --- | --- |
| clear-writing, diagrams-and-tables and source-of-truth opened with a restatement of the consumer reporting checkpoint, and godot-gdscript closed with an older wording of it; the other 24 skills carried none, although the 8 October decision gives that trigger one home in project instructions | Restatements removed; the [decision](../DECISIONS.md#state-the-reporting-checkpoint-once--adopted) records why. Patch versions 0.4.1, 0.12.1, 3.1.1 and 0.1.1. project-contracts keeps its boundary sentence |
| relational-modeling told the reader to use `project-docs`, a skill no longer in this catalog, and "the available visual skill" without naming it | Names clear-writing and the ER route of diagrams-and-tables, each "when available"; 0.2.1 |
| python-patterns, python-design, typescript-patterns and typescript-design each deferred class or language questions to anonymous "repository design/language guidance", while the README says the pairs belong together | Each names its companion as suitable when available, in the body and not the description, so triggering is unchanged; patch versions 0.2.1, 0.1.1, 2.0.3, 1.0.3 |
| Six `agents/openai.yaml` display names and two manifest titles used title case against the sentence case of the other 22; one section heading in typescript-design likewise | Normalized; no version change |
| Paragraphs in test-writing, verification-design and test-audit were left ragged when sibling links became skill names in the 7 October flattening | Reflowed; no wording change |
| README Origins described `project-docs` and `shared-code-design` as present, two paragraphs after calling one of them retired, and eight catalog rows carried `(draft)` without a stated meaning | Origins corrected; `(draft)` defined once at the top of the catalog |
| DECISIONS.md linked three `collections/` paths removed on 7 October, and listed a follow-up idea for a skill that left the repository | Links point at the current homes or the pinned pre-flattening commit; the idea is annotated |
| work-records and repository-services were the only skills with no `validation/<name>.md`; their intended behaviour lived under collection names | `process-design.md` renamed to `work-records.md` with its intro and selection table brought to the skill's name; `repository-services.md` added, linking the service-foundation history and trials |
| `validation/agent-workflow-trial/read.md` linked a fixture file that was never retained | Link replaced with a description of the unretained source |
| Package validation checked link files but not fragments, so a renamed heading could silently orphan a route; nothing checked the live maintenance pages' links at all | `validate-packages.py` checks fragments against rendered heading anchors, repeated headings and explicit HTML anchors; `scripts/tests/test_validate_packages.py` covers that and applies the same check to README.md, AGENTS.md and DECISIONS.md. A second shipped-content test fails on the name of a retired skill |

## Reviewed and left as they are

- The test-audit and test-writing authority paragraphs are recorded as copies
  but differ in wording ("lenses" against "method"). The README allows a
  contextual application to keep distinct wording; both state the same rule.
- The python and TypeScript authority paragraphs are byte-identical to their
  counterparts; the TypeScript module-syntax copy is compared by the shared
  contract check.
- Skill names in prose appear both bare and in backticks. Neither form links,
  so the difference changes no route; it was not normalized.
- source-of-truth's title and display name read "Authoritative definitions"
  while its name stays `source-of-truth`; this is a deliberate pairing of a
  stable identifier with a descriptive title.
- The three reference pages in typescript-design that repeat "Why", "Rules" and
  "When not to use" under several sections are reachable by their first anchor
  and numbered suffixes; no link relies on the repeats.
- Dated records under `validation/` keep collection-era paths and the names of
  the projects they tested, as the workspace convention allows for records.
- Empty untracked directories `.agents`, `.aws` and `.codex` sit beside the main
  checkout. They are not part of the repository and were left alone.

## Checks

- `python3 scripts/validate-packages.py`: 28 packages, including the new anchor
  check over 132 fragment links inside packages.
- `python3 scripts/check.py`: all checks passed, including the new
  `scripts/tests/test_validate_packages.py` suite and the extended
  `test_shipped_content.py`. The run used the main checkout's TypeScript
  dependency through a worktree link; no lockfile changed.
- `git diff --check`: clean.
- No discovery trial was run. None of the edits changes a description, trigger
  or route inside a skill: the removed paragraphs stated a duty that project
  instructions now carry, and the companion sentences name a skill the reader
  may already have installed. The routing acceptance requirement still applies
  before the next release of any edited skill.

## Limits

Clear writing was applied by the author to the new prose without an independent
prior-text comparison. Removing the four restatements relies on consuming
projects carrying the README's checkpoint; a project that installed one of these
skills alone before 8 October and never adopted the checkpoint loses the inline
reminder, which the decision log records as the intended shape. The new
validation pages state intended behaviour; neither skill has had a fresh-context
trial as a standalone package.
