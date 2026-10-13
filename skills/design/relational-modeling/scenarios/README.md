# Relational modeling scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here. The
[scenario guidance](../references/scenarios.md) under references teaches domain
modeling to a user of the skill; it is not a test of the skill.

## Cases

| Request and context | Expected behavior |
| --- | --- |
| A brief with known entities, retrieval questions and undecided cardinalities ([agreements fixture](agreements/brief.md)) | Each retrieval question traces through the model; provisional assumptions stay visible in the ER view and scenarios; terms have one home; unresolved choices are named as blocking decisions rather than guessed. No SQL, migration or seed document is produced. |
| A later relationship correction to that model ([second input](agreements/brief.md#correction)) | The model, ER view, glossary and scenarios agree on the new meaning; unrelated assumptions and open rules are preserved; scenarios distinguish the old and new interpretations. A compact representation that depends on a provisional assumption says so. |
| A question about an existing model | Read its owning document and the terms needed; cite the source and keep unresolved meaning; start no modeling pass. |
| A model review against stated requirements | Findings and blockers, not rewritten documents. |
| A literal wording edit in a project that has this skill installed | No modeling or database-design guidance is loaded. |
| The project also has PostgreSQL guidance installed | Not loaded for a conceptual model; representation is selected only when the work reaches it. |
| A rendered check of the ER view is unavailable | Reported as unperformed; source review is not claimed as rendering. |

## Fixture

`agreements/` holds a synthetic brief and its correction. Give a fresh agent the
brief alone, then the correction only after the first result exists. A second
fresh agent gets the nearby wording task. Judge the artifacts against the
expectations above; reading fewer words is not acceptance by itself.

## Limits

- One initial run, one warm correction and one nearby task have been observed;
  this shows the route, not its reliability. A fresh agent discovering an
  existing model during a handoff has not been tried.
- The fixture had no renderer, so Mermaid parsing and readability stayed
  unverified in that run.
