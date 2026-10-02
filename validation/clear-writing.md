# Validation scenarios — Clear Writing

Use these cases when changing the skill. They describe observable outcomes;
they are not claims that an independent agent has passed them.

| Request and context | Expected outcome |
| --- | --- |
| Simplify a technical paragraph where the cause of a timeout is unknown | Improve sentence structure without inventing a cause, duration or successful recovery. |
| Edit a rule that says to stop unless both checks pass | Preserve the requirement that both checks pass; do not rewrite it as stopping only when both fail. |
| Tighten deployment instructions requiring owner approval and a verified backup | Preserve the approval, evidence and ordering requirements without adding a new approval flow. |
| Clarify a default that allows project-specific exceptions | Keep the permitted exceptions beside the default; do not make the default mandatory. |
| Rewrite a procedure containing commands and exact resource names | Preserve operational meaning and literal values; editing the procedure does not cause the commands to run. |
| Shorten the description of a growing repository | Describe its stable category and useful scope without embedding a list that becomes incomplete as contents change. |
| Write a confirmation after a backup command succeeds but no restore was attempted | Report the command's success without claiming that recovery was verified. |
| Edit explanatory text in an established personal voice | Improve comprehension while retaining the requested tone and distinctive voice. |
| The user requests a creative form or deliberately elaborate prose | Follow the requested form; do not impose terse technical prose as a universal style. |
| Fix one unclear sentence in a documentation set | Make the focused edit without reorganizing the documentation or adding unrelated diagrams. |
| Replace a metaphor whose word choice carries a distinction, such as "cheapest" meaning least information lost | Keep the distinction in plain wording, or keep the metaphor; do not substitute a near-synonym that changes the reason. |
| Clarify a sentence where "when available" could limit one action or all of them | Keep the scope visible or ask; do not move the condition so that it governs more actions than before. |

## Initial checks — 2026-09-29

The skill-creator manifest validator passed. The repository package validator
passed for all 11 packages, including this skill's two local reference links,
and `git diff --check` passed. The author reviewed the instructions against the
cases above.

An independent agent used this skill on three supplied texts without receiving
the expected answers:

| Input | Observed result |
| --- | --- |
| Deployment instructions with owner approval, a required restore, a preview exception and bounded retries | Preserved both production prerequisites, the preview exception, the invalid-credentials prohibition and the limit of two optional retries. |
| A growing skill collection described by a list of current contents | Replaced the inventory and praise with “Reusable agent skills.” |
| A successful backup command, no restore test, and an upload timeout of uncertain cause | Kept command success distinct from recovery verification and retained uncertainty about the timeout's cause. |

The procedural prose trial revised
[Bash Patterns](../skills/languages/bash-patterns/SKILL.md). An independent comparison with
its prior text found the requirements, exceptions and literal code preserved.
That review checked wording; it did not execute Bash examples.

An independent author also used the skill to revise the conceptual
[Source of Truth](../collections/project-foundation/skills/source-of-truth/SKILL.md) entrypoint. Review preserved
its six ordered options, structural exceptions and project authority; all ten
section headings and fourteen link targets remained intact. The author flagged
an existing contradiction: verification claimed that drift must become
impossible, although the later options detect or record it. The final wording
now asks for evidence appropriate to the selected option, consistent with those
options. The prose trial did not exercise the skill against a live codebase.

These checks cover the supplied cases. They do not establish performance on
every scenario above or in another project.

## Project foundations naming — 2026-09-30

Version 0.1.1 uses sentence case for the display name “Clear writing.” The
installation name and writing instructions are unchanged. Package and
skill-creator validation passed; no new behavioral trial was needed for this
metadata-only change.

## Package sweep — 2026-09-30

The skill was applied to the prose of eight packages it had not yet revised:
`change-workflow`, `diagrams`, `typescript-patterns`, `test-audit`,
`postgres-design`, `project-docs`, `runtime-operations` and the
`source-of-truth` references. This skill, `bash-patterns` and the
`source-of-truth` entrypoint were revised in the trials above;
`containerization` and `project-policy` were written with it.
`jonas-email-style` was excluded because its wording records a personal style
derived from a mail corpus.

For each package, one agent revised passages with a concrete clarity problem and
left the rest. A second agent, without the author's rationale, compared every
changed passage with the prior text. A script confirmed that fenced code, inline
code, link destinations, headings and frontmatter other than descriptions were
unchanged, and that every local heading anchor resolves. Package validation,
`git diff --check` and the `runtime-operations` helper tests passed.

33 of 35 files changed. Most edits replaced idioms and metaphors with the
behavior they stood for, split sentences carrying several ideas, and moved
conditions beside their actions. Review found four edits that changed meaning,
all corrected before commit:

| Package | Changed meaning |
| --- | --- |
| `project-docs` | Diagram inspection became conditional on the target renderer being available. |
| `typescript-patterns` | Placing a total mirror beside its declaration was said to cause the compile error, rather than to decide where it appears. |
| `postgres-design` | A rule forbidding JSON from *becoming* a way around relational integrity came to forbid only *using* it that way. |
| `runtime-operations` | "Use the same verbs" was rewritten to fit its option-name example, settling an ambiguity the source left open. |

Three of the four resolved an ambiguity while clarifying it, the failure the
instruction guidance warns against. Several nits restored a distinction that a
replaced metaphor had carried, such as "cheapest" rather than "easiest"
crossings. Authors also reported contradictions in the source that they left
unresolved; the confirmed ones are recorded on each package's validation page.

This was a text comparison. No behavioral scenario of a revised package was
rerun, and the description edits in `diagrams` and `typescript-patterns` were
not tested for changes in when the skill is selected.

## Rewrite checks — 2026-09-30

Version 0.2.0 adds two checks drawn from the package sweep's review findings: a
replaced metaphor keeps the distinction it carried, and the final comparison
looks for an ambiguity the revision settled, such as a condition moved to govern
more actions. The last two scenarios above cover them.

An independent agent used the revised skill on three supplied passages without
receiving the expected answers:

| Input | Observed result |
| --- | --- |
| "The cheapest columns to drop are the derived ones, since readers can recompute them" | Kept "cheapest" because the following clause explains the cost; declined near-synonyms that would change the claim. |
| A release check to use "the production theme when available" | Kept the condition on the theme rather than the whole check, and asked what to do when the theme is unavailable. |
| Retry an upload "but not when the server says the token is invalid — that's a dead end" | Replaced the idiom with the consequence, kept the exception beside the rule, and asked how many retries "a few" means. |

These three cases do not establish that the checks prevent the sweep's errors in
longer documents, where most of them occurred.
