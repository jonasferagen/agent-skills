# Documentation and records scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Cases

| Request and context | Expected behavior |
| --- | --- |
| A README's Maintenance section recounts the project's adoption, a move and planned work | State current upkeep; preserve history and proposed work in the project-designated record location; link only when useful. |
| A project keeps official documentation in Git and designates an external record location; a package README mixes a supported procedure, completed work and a proposed feature | Keep the procedure and current limits; preserve the narrative and proposal in the designated location without inventing a new repository archive or treating the proposal as current support. |
| A current index maps every retired source path and removed setting to a Git commit, while active readers need only the replacement or withdrawal of the retired whole | Keep current lookup entries and any needed commit references; do not treat the path inventory as required retirement information unless the project's conventions require it. |
| An overview mixes supported commands, a migration story and a future feature promise | Keep the supported interface and current limitations; link the history and plan instead of embedding their narrative. |
| A log, changelog or proposed design intentionally describes another time scope | Preserve that purpose, assessed conditions and proposal state; the current-guidance rule is not a universal present-tense rewrite. |
| Instructions say what to do when an existing operation fails | Keep the operational steps and conditions; future-tense wording does not make the supported procedure a roadmap. |
| A feature has shipped; its guide still says "will support" and an appended "Implementation notes" section recounts the work | Rewrite the guide to describe the supported behavior; move the implementation account to the project's record location or drop it if nothing needs keeping. |
| Asked to "write up what we did today" in a project with no designated record location | Report that no location is designated and ask; do not create a docs/history folder. |
| A plan's work is complete and its repository copy is about to be deleted | Confirm the stored copy is complete first, then remove the original and repoint links to the current guide or the stored record. |
| Rewrite a project's changelog entries into the present tense so they match the docs | Keep each entry's version, date and scope; do not restate entries as current behavior. Follow a verb form only where the changelog's own convention prescribes one. If the docs and changelog disagree about current behavior, correct the owning guide. |
| Tighten the wording of a paragraph in a current guide | Not this skill's task: the wording edit belongs to a writing skill unless the paragraph also mixes current guidance with history or plans. |

## Limits

- A record location without naming rules leaves file names to the agent; the
  skill does not supply a naming scheme, by design.
