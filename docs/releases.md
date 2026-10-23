# Skill releases


Version each skill independently. Its `SKILL.md` declares a string under
`metadata.version`, such as `"1.0.0"`. Publish an annotated Git tag named
`<skill-name>/v<version>` on the committed release; never move a published tag.
The tagged package and manifest version must agree. Unreleased skills can remain
pinned by commit until their first release. Tags of the retired collection
layout, `<collection>/v<version>`, remain as history and are not reused.

The version on `main` can also describe an unreleased revision after an earlier
tag. The tag remains the last released version until that revision is validated
and tagged; consumers keep their selected pins. A version bump alone publishes
nothing.

Use semantic versions for the skill's behavioral contract: its scope, required
behavior, defaults, exceptions and bundled resource interfaces.

- **Patch:** clarify or correct wording without changing intended requirements.
- **Minor:** add compatible guidance or capabilities within the existing contract.
- **Major:** change defaults, mandatory rules, scope or exceptions in a way that
  requires consumers to review their adoption.

Before tagging, review the package and its scenarios by hand, repeat the applicable
routing trials, and complete the release review below for a skill that bundles
scripts, templates or an extension declaration. A release must contain no
unfinished scaffold or project-specific credentials or identifiers. Consumers
pin the full commit as well as the release label because tags are names, not an
integrity guarantee. Other skills in the repository need no version bump when
one skill is released.

### Release review

For a skill that bundles scripts, templates or an extension declaration, a
release review applies the standards the skills teach to the package itself.
Review the whole package before
its release is tagged against the rules its own content and this repository's
authoring skills state — every file, not only the changes since an earlier
release — together with the catalog text and instructions that describe it.
Ordinary edits need only the checks in [AGENTS.md](../AGENTS.md#verification). A
finding that recurs is a candidate for a mechanical check.

Run the mechanical checks first; they decide structure only:
`python3 scripts/check.py` (a package
without tests reports that coverage as absent rather than treating a zero-test
run as evidence), and
`git diff --check $(git hash-object -t tree /dev/null) HEAD -- skills/<area>/<name>`
for whitespace errors in every committed file of the package.

Then apply each owner's own review steps to the package's files:

| Rule owner | Apply to | Review steps |
| --- | --- | --- |
| Source of truth | Rules, vocabularies, paths and counts stated in more than one package file or in the catalog | [Review and verification](../skills/design/single-source-of-truth/SKILL.md#review-and-verification) |
| Source of truth, check design | Bundled scripts and their tests | [Keep the check durable](../skills/design/single-source-of-truth/references/check-design.md#keep-the-check-durable) |
| Verification design | Scenarios, examples and claims about what a skill or check proves: each names the boundary observed and the evidence, and distinguishes a walkthrough from an exercised run | [Match each claim to an observable boundary](../skills/verification/verification-design/SKILL.md#match-each-claim-to-an-observable-boundary) |
| Clear writing | All prose, including descriptions, templates and examples | [Check the result](../skills/authoring/clear-writing/SKILL.md#check-the-result), plus [instruction guidance](../skills/authoring/clear-writing/references/instructions.md) for instructions |
| Diagrams and tables | Each diagram and table, and passages that would explain better as one | [Semantic review](../skills/authoring/diagrams-and-tables/references/review.md) and [visual verification](../skills/authoring/diagrams-and-tables/references/verification.md) |
| Documentation | Links resolve, including anchors and links outside the package; each statement has one current owner; historical text is labelled as such | Check each link's target and anchor; compare current and historical passages |
| Routing quality | Entry points, triggers and conditional references | [Routing trial method](verification.md#routing-trial-method) |
| Application design | Application designs and runtime helpers produced by a skill, when present | [Check behavior at the owning boundary](../skills/design/application-design/SKILL.md#check-behavior-at-the-owning-boundary) |
| Other skills in this repository | Helpers and tests, such as Python scripts and their suites | Select from the catalog by trigger |

A skill gaining a rule owner adds a row here in the same change.

For each finding, record the rule, the file, the concrete consequence and its
disposition: fixed, or an explicit exception stating its reason, scope, who
accepted it and the condition for reviewing it again. The reviewer proposes an
exception; the repository owner accepts it. When the package cannot follow one
of its own rules, report that against the rule or the package rather than
exempting it silently. Wording changed during the review needs an independent
comparison of each changed passage with the prior text before release.

Record with the release — in the annotated tag or the change that tags it — the
commit reviewed and whether the reviewer had a fresh context; whether the
evidence is an informed review, a walkthrough or an independent acceptance trial
under the routing trial method's isolation rules; the rules applied and the files
each covered; findings with dispositions and exceptions with review conditions;
and checks that could not run, separately from checks that passed. The skill is
ready to tag when the mechanical checks pass, the routing trials meet the
[routing acceptance requirement](verification.md#routing-quality), and every material finding is
fixed or covered by an accepted exception.

### Authoring skills

Skills in this repository should meet the standards they teach. Apply relevant
guidance to the packages, helpers and documentation we maintain here. Start
with the named package when one is known; use the catalog to select additional
guidance from the task's actual trigger. Load only needed references. For example,
use single-source-of-truth when reconciling copied rules, verification-design when
selecting evidence. Report a relevant conflict or gap rather than silently
exempting the repository.

During authoring, AGENTS.md requires writing and visual guidance where relevant.
A skill that bundles scripts, templates or an extension declaration needs the
whole-package [release review](#release-review) before tagging, which already
applies both skills below. Before tagging any other release, also apply them to
the content changed since the skill's last tag, or to the whole package for a
first release:

- [Clear writing](../skills/authoring/clear-writing/SKILL.md), to the prose.
- [Diagrams and tables](../skills/authoring/diagrams-and-tables/SKILL.md), to existing
  diagrams and tables and to passages a diagram or table would explain better.

This changed-content pass is a recommendation, not a release requirement.
Clear Writing does not yet cover every kind of prose a skill package contains,
such as trigger descriptions, defined terms, worked examples, pattern catalogs
and templates.

When this pass rewrites wording, have a reviewer without the author's rationale
compare each changed passage with the prior text, as release review requires for
the packages it covers: the first Clear Writing sweep found four meaning changes
that way, now kept as regression cases in that skill's scenarios. Note which
skills were applied in the change's record; "no change needed" is a valid
result.
