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
| Write a confirmation after a backup command succeeds but no restore was attempted | Report the command's success without claiming that recovery was verified. |
| Edit explanatory text in an established personal voice | Improve comprehension while retaining the requested tone and distinctive voice. |
| The user requests a creative form or deliberately elaborate prose | Follow the requested form; do not impose terse technical prose as a universal style. |
| Consolidate a guide that repeats its canonical command page and has an empty future-work section | Keep a useful command-page link and remove the empty scaffold, preserving required evidence and limits; create no replacement index. |
| Organize a skill entrypoint with a common workflow, provider-specific requirements and maintenance history | Keep common decisions at entry, link provider details with their applicability conditions, and preserve every applicable obligation without making ordinary readers follow maintenance history. |
| Edit a short guide whose conditional instructions already fit beside their rules | Keep it self-contained when splitting it would only add navigation; progressive disclosure does not require extra files. |
| Fix one unclear sentence in a documentation set | Make the focused edit without reorganizing the documentation or adding unrelated diagrams. |
| Replace a metaphor whose word choice carries a distinction, such as "cheapest" meaning least information lost | Keep the distinction in plain wording, or keep the metaphor; do not substitute a near-synonym that changes the reason. |
| Clarify a sentence where "when available" could limit one action or all of them | Keep the scope visible or ask; do not move the condition so that it governs more actions than before. |
| Replace the idiom "that's a dead end" in a retry rule with an exception | State the consequence, keep the exception beside the rule, and ask what an unquantified "a few retries" means. |
| Restructure a repository README that mixes a public catalog, developer setup and emergency recovery; existing guides and incoming fragments already exist | Keep useful catalog discovery and common constraints at entry; route tasks directly to authoritative guides, keep recovery prerequisites and preserve incoming links. Do not create another generic index or duplicate argument lists. |
| Find the ordinary verification route after a README split, then find the additional evidence required for a service change | Both routes remain reachable; the source gate is not presented as live-health evidence and conditional obligations remain discoverable. |
| Correct a spelling error in a README | Keep the edit local; do not activate a routing restructure or require a fresh-agent trial. |

### Regressions in long documents

Meaning changes a revision must not make. Each has occurred in practice.

| Source passage | Changed meaning to avoid |
| --- | --- |
| "Inspect the rendered diagram" | "Inspect the rendered diagram when the renderer is available": an unconditional step became conditional. |
| "JSON must not become a way around relational integrity" | "Do not use JSON as a way around relational integrity": a rule about results became a rule about intent. |
| "Use the same verbs across scripts", illustrated with option names | "Use the same option names across scripts": the example replaced the rule, settling an ambiguity the source left open. |

## Limits

- The settled-ambiguity and metaphor checks are least reliable in long
  documents. Independent comparison of
  each changed passage with the prior text remains the reliable safeguard; the
  skill's own check does not replace it.
