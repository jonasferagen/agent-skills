# Self-conformance review

Skills in this repository should meet the standards they teach
([authoring skills](../README.md#authoring-skills)). For a skill that bundles
scripts, templates or an extension declaration, this is a release requirement:
before its release is tagged, review the whole package against the rules its
own content and this repository's authoring skills state. A package is released
as one unit, so the review covers every file in it, not only the changes since
an earlier release. Also cover the catalog text and instructions in this
repository that describe the skill.

Ordinary edits do not need this review; [AGENTS.md](../AGENTS.md#verification)
lists their checks. When a review finding recurs, consider turning it into a
mechanical check.

Until 7 October 2026 this review applied to collections; the dated records under
`validation/` that cite it were produced under that rule.

## Mechanical checks

Run these first. They must pass before the review is recorded.

- `python3 scripts/validate-packages.py`: frontmatter, local link targets and
  containment within each package, unique names, and recorded package-boundary
  copies. It does not check heading anchors or links outside packages; the
  documentation row below covers those.
- `python3 scripts/check.py`: the package check plus every bundled helper suite
  under `scripts/` and `skills/`. A skill without such tests reports that
  coverage as absent or not applicable rather than treating a zero-test run as
  evidence.
- `git diff --check $(git hash-object -t tree /dev/null) HEAD -- skills/<area>/<name>`:
  whitespace errors in every committed file of the package, not only recent
  changes.

These checks decide structure only. They do not establish that the text follows
the rules.

## Rules to apply

Apply each owner's own review steps to the package's files. This table selects
the owner; the linked steps are the checklist, so they are not repeated here.

| Rule owner | Apply to | Review steps |
| --- | --- | --- |
| Source of truth | Rules, vocabularies, paths and counts stated in more than one package file or in the catalog | [Review and verification](../skills/design/source-of-truth/SKILL.md#review-and-verification) |
| Source of truth, check design | Bundled scripts and their tests | [Keep the check durable](../skills/design/source-of-truth/references/check-design.md#keep-the-check-durable) |
| Verification design | Validation records, examples and claims about what a skill or check proves: each claim names the boundary observed and the evidence that establishes it, and distinguishes a walkthrough from an exercised run | [Match each claim to an observable boundary](../skills/verification/verification-design/SKILL.md) |
| Clear writing | All prose, including descriptions, templates and examples | [Check the result](../skills/authoring/clear-writing/SKILL.md#check-the-result), plus [instruction guidance](../skills/authoring/clear-writing/references/instructions.md) for instructions |
| Diagrams and tables | Each diagram and table, and passages that would explain better as one | [Semantic review](../skills/authoring/diagrams-and-tables/references/review.md) and [visual verification](../skills/authoring/diagrams-and-tables/references/verification.md) |
| Documentation | Links resolve, including heading anchors and links outside the package; each statement has one current owner; historical text is labelled as such and not rewritten to imply it tested the current layout | Check each link's target and anchor; compare current and historical passages |
| Routing quality | Entry points, triggers and conditional references | [Routing trial method](discovery.md#routing-trial-method) |
| Application design | Application designs and runtime helpers produced by a skill, when present | [Exercise the boundary and choose the increment](../skills/design/application-design/SKILL.md#exercise-the-boundary-and-choose-the-increment) |
| Other skills in this repository | Helpers and tests, such as Python scripts and their test suites | Select from the [catalog](../README.md) by trigger |

A skill gaining a rule owner adds a row here in the same change.

Skills that govern projects apply to this repository where its instructions
adopt them, as AGENTS.md adopts authoring and verification guidance. Whether
this repository adopts a project framework is a separate decision; until then,
the review does not treat its absence as a finding.

## Findings and exceptions

For each finding, record the rule, the file, the concrete consequence and its
disposition: fixed, or an explicit exception. An exception states its reason,
scope, who accepted it and the condition for reviewing it again. The reviewer
proposes an exception; the repository owner accepts it. When the package cannot
follow one of its own rules, report that as a finding against the rule or the
package; do not exempt the package silently.

Wording changed during the review needs an independent comparison of each changed
passage with the prior text before release. A rewrite for clarity must not change
an obligation, condition or level of certainty.

## Record and release

Add a dated section to the skill's validation page, such as
[service-foundation](service-foundation.md) for the services skills, with:

- the commit reviewed and whether the reviewer had a fresh context;
- the rules applied and the files each covered;
- findings with their dispositions, and exceptions with their review conditions;
- checks that could not run, reported separately from checks that passed.

The skill is ready to tag when the mechanical checks pass, the routing trials
meet the [routing acceptance requirement](../README.md#routing-quality), and every
material finding is fixed or covered by an accepted exception.
