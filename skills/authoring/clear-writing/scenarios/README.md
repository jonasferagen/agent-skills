# Clear writing scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Cases

| Request and context | Expected behavior |
| --- | --- |
| Simplify a technical paragraph where the cause of a timeout is unknown | Improve sentence structure without inventing a cause, duration or successful recovery. |
| Edit a rule that says to stop unless both checks pass | Preserve the requirement that both checks pass; do not rewrite it as stopping only when both fail. |
| Tighten deployment instructions requiring owner approval and a verified backup, with a preview exception and bounded retries | Preserve the approval, evidence and ordering requirements, the exception's scope and the retry limit without adding a new approval flow. |
| Clarify a default that allows project-specific exceptions | Keep the permitted exceptions beside the default; do not make the default mandatory. |
| Rewrite a procedure containing commands and exact resource names | Preserve operational meaning and literal values; editing the procedure does not cause the commands to run. |
| Shorten the description of a growing repository | Describe its stable category and useful scope without embedding a list that becomes incomplete as contents change. |
| An overview says "no release has been made yet", but readers only need the repository's purpose | Omit the release snapshot without replacing it with another status claim or creating a status page. |
| Readers need to choose an available release, and the repository has a releases page | Link the releases page with useful context rather than copying its current contents into prose. |
| A guide says the loader does not verify hashes, and a dated report records one successful load | Preserve the current limitation and the dated result's tested scope; neither becomes a general verification claim. |
| A keeper entrypoint's Maintenance section recounts adoption, a move and planned work | State current upkeep and routes; retain history and proposed work with their record or plan owner, with useful pointers. |
| An overview mixes supported commands, a migration story and a future feature promise | Keep the supported interface and current limitations; link the history and plan instead of embedding their narrative. |
| A worklog, changelog or proposed design intentionally describes another time scope | Preserve that purpose, assessed conditions and proposal state; the current-guidance rule is not a universal present-tense rewrite. |
| Instructions say what to do when an existing operation fails | Keep the operational steps and conditions; future-tense wording does not make the supported procedure a roadmap. |
| Write a confirmation after a backup command succeeds but no restore was attempted | Report the command's success without claiming that recovery was verified. |
| Edit explanatory text in an established personal voice | Improve comprehension while retaining the requested tone and distinctive voice. |
| The user requests a creative form or deliberately elaborate prose | Follow the requested form; do not impose terse technical prose as a universal style. |
| Consolidate a guide that repeats its canonical command page and has an empty future-work section | Keep a useful command-page link and remove the empty scaffold, preserving required evidence and limits; create no replacement index. |
| Fix one unclear sentence in a documentation set | Make the focused edit without reorganizing the documentation or adding unrelated diagrams. |
| Replace a metaphor whose word choice carries a distinction, such as "cheapest" meaning least information lost | Keep the distinction in plain wording, or keep the metaphor; do not substitute a near-synonym that changes the reason. |
| Clarify a sentence where "when available" could limit one action or all of them | Keep the scope visible or ask; do not move the condition so that it governs more actions than before. |
| Replace the idiom "that's a dead end" in a retry rule with an exception | State the consequence, keep the exception beside the rule, and ask what an unquantified "a few retries" means. |

### Regressions from applying the skill to long documents

Each of these meaning changes was made and caught during a sweep of several
packages. A revision must not repeat them.

| Source passage | Changed meaning to avoid |
| --- | --- |
| "Inspect the rendered diagram" in a documentation rule | Inspection made conditional on the target renderer being available. |
| A rule saying where a compile error appears when a mirror is placed beside its declaration | The placement said to cause the error rather than to decide where it appears. |
| A rule forbidding JSON from *becoming* a way around relational integrity | Forbidding only *using* it that way: a result became an intent. |
| "Use the same verbs across scripts", illustrated with option names | Rewritten to fit the example, settling an ambiguity the source left open. |

## Limits

- The settled-ambiguity and metaphor checks were trialled on short supplied
  passages. Most of the sweep's meaning changes occurred in longer documents,
  where the checks are least established.
- Independent comparison of each changed passage with the prior text remains the
  reliable safeguard; the skill's own check does not replace it.
