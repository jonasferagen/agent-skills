# Self-conformance review

Skills in this repository should meet the standards they teach
([authoring skills](../README.md#authoring-skills)). For a collection this is a
release requirement: before a collection release is tagged, review the whole
collection against its own members' rules. A collection is released as one unit,
so the review covers every file in it, not only the changes since an earlier
release. Also cover the catalog text and instructions in this repository that
describe the collection.

Ordinary edits do not need this review; [AGENTS.md](../AGENTS.md#verification)
lists their checks. When a review finding recurs, consider turning it into a
mechanical check.

## Mechanical checks

Run these first. They must pass before the review is recorded.

- `python3 scripts/validate-packages.py`: frontmatter, local link targets and
  containment within each installation unit, and recorded package-boundary copies.
  It does not check heading anchors or links outside packages; the project
  documentation row below covers those.
- Run each bundled helper's tests, including member-owned test directories.
  Use `python3 -m unittest discover -s <test-directory>` for Python helpers;
  top-level discovery does not necessarily descend into member packages.
  Collections without such tests report that coverage as absent or not applicable
  rather than treating a zero-test run as evidence. The shared installation
  checker is exercised by `python3 -m unittest discover -s scripts/tests`, including
  staged copies of every inventoried collection.
- `git diff --check $(git hash-object -t tree /dev/null) HEAD -- collections/<name>`:
  whitespace errors in every committed file of the collection, not only recent
  changes.

These checks decide structure only. They do not establish that the text follows
the rules.

## Rules to apply

Apply each owner's own review steps to the collection's files. This table selects
the owner; the linked steps are the checklist, so they are not repeated here.

| Rule owner | Apply to | Review steps |
| --- | --- | --- |
| Source of truth | Rules, vocabularies, paths and counts stated in more than one collection file or in the catalog | [Review and verification](../skills/design/source-of-truth/SKILL.md#review-and-verification) |
| Source of truth, check design | Bundled scripts and their tests | [Keep the check durable](../skills/design/source-of-truth/references/check-design.md#keep-the-check-durable) |
| Status and evidence | Validation records, examples and claims about what a skill or check proves | Compare each claim with the [states](https://github.com/jonasferagen/agent-skills/blob/9093cfca4ffa93df1be35b1bb7ebffaef0baac65/collections/project-foundation/references/status-and-evidence.md#states) and [evidence table](https://github.com/jonasferagen/agent-skills/blob/9093cfca4ffa93df1be35b1bb7ebffaef0baac65/collections/project-foundation/references/status-and-evidence.md#what-evidence-establishes) |
| Clear writing | All prose, including descriptions, templates and examples | [Check the result](../skills/authoring/clear-writing/SKILL.md#check-the-result), plus [instruction guidance](../skills/authoring/clear-writing/references/instructions.md) for instructions |
| Diagrams and tables | Each diagram and table, and passages that would explain better as one | [Semantic review](../skills/authoring/diagrams-and-tables/references/review.md) and [visual verification](../skills/authoring/diagrams-and-tables/references/verification.md) |
| Project documentation | Links, document ownership, and current versus historical text | [Verify and finish](https://github.com/jonasferagen/agent-skills/blob/9093cfca4ffa93df1be35b1bb7ebffaef0baac65/collections/project-foundation/skills/project-docs/SKILL.md#verify-and-finish) |
| Routing quality | Entry points, triggers and conditional references | [Routing trial method](discovery.md#routing-trial-method) |
| Application design | Application designs and runtime helpers produced by a collection, when present | [Exercise the boundary and choose the increment](../collections/application-foundation/skills/application-design/SKILL.md#exercise-the-boundary-and-choose-the-increment) |
| Other skills in this repository | Helpers and tests, such as Python scripts and their test suites | Select from the [catalog](../README.md) by trigger |

A collection gaining a rule owner adds a row here in the same change.

Members that govern projects, such as bootstrap, policy and planning, apply to
this repository where its instructions adopt them, as AGENTS.md adopts authoring and verification guidance. Whether this repository adopts a project foundation is a separate
decision; until then, the review does not treat its absence as a finding.

## Findings and exceptions

For each finding, record the rule, the file, the concrete consequence and its
disposition: fixed, or an explicit exception. An exception states its reason,
scope, who accepted it and the condition for reviewing it again. The reviewer
proposes an exception; the repository owner accepts it. When the collection cannot follow
one of its own rules, report that as a finding against the rule or the
collection; do not exempt the collection silently.

Wording changed during the review needs an independent comparison of each changed
passage with the prior text before release. A rewrite for clarity must not change
an obligation, condition or level of certainty.

## Record and release

Add a dated section to the collection's validation page, such as
[project-foundation-collection](https://github.com/jonasferagen/agent-skills/blob/9093cfca4ffa93df1be35b1bb7ebffaef0baac65/validation/project-foundation-collection.md), with:

- the commit reviewed and whether the reviewer had a fresh context;
- the rules applied and the files each covered;
- findings with their dispositions, and exceptions with their review conditions;
- checks that could not run, reported separately from checks that passed.

The collection is ready to tag when the mechanical checks pass, the routing trials
meet the [routing acceptance requirement](../README.md#routing-quality), and every
material finding is fixed or covered by an accepted exception.
