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
[Bash Patterns](../skills/bash-patterns/SKILL.md). An independent comparison with
its prior text found the requirements, exceptions and literal code preserved.
That review checked wording; it did not execute Bash examples.

An independent author also used the skill to revise the conceptual
[Source of Truth](../skills/source-of-truth/SKILL.md) entrypoint. Review preserved
its six ordered options, structural exceptions and project authority; all ten
section headings and fourteen link targets remained intact. The author flagged
an existing contradiction: verification claimed that drift must become
impossible, although the later options detect or record it. The final wording
now asks for evidence appropriate to the selected option, consistent with those
options. The prose trial did not exercise the skill against a live codebase.

These checks cover the supplied cases. They do not establish performance on
every scenario above or in another project.
