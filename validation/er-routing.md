# ER routing trial — 2 October 2026

## Change and setup

The [previous modeling trial](relational-modeling.md) exposed a broad construction
route for a two-edge ER diagram. This revision routes a known ER task directly to
its reference, moves large-view decomposition to a conditional reference, and
separates reading, semantic review and construction. Verification now discovers
the project renderer before considering an existing local tool and reports
missing checks explicitly. No renderer dependency or new skill was introduced.

Three fresh agents worked in isolated tracked fixtures under
`/tmp/er-routing-_h1wm6zw`. Their project hooks and explicitly installed copies
used the working revision after `830cc2b`: diagrams-and-tables 0.6.0,
project-docs 2.2.0 and relational-modeling 0.2.0. Entry was through project
instructions, without giving agents an expected reference route or prior results.
They could read only fixture files, with no network, installation or runtime work.
The authoring repository and real Atlas were outside their task scope.

## Small conceptual model

The agent received the same [initial brief](relational-modeling/brief.md) as the
previous trial. Its [output patch](er-routing/small.patch) contains the model,
canonical ER, scenarios, glossary and README navigation.

It read 5,656 approximate whitespace words of guidance and 262 of project inputs:
about 5,900 combined, compared with the earlier agent’s roughly 9,100-word report.
The new count includes relational-modeling and scenarios; foundation entrypoint,
authority, authoring and friction; project-docs, structure and diagram ownership;
clear-writing; visual selection, ER and verification. It did not load general
composition, drawing, large-ER or PostgreSQL representation guidance into context.

The parent reviewed the actual documents. Both retrieval questions have paths and
expected answers; identity, absent participants, multiple services and multiple
roles have counterexamples. Cardinalities are explicitly provisional. The agent
chose a multiple-participant hypothesis, unlike the prior single-participant
hypothesis; neither was supplied as an adopted domain rule. The reduction in
reading did not depend on reproducing identical modeling choices.

Output review was about 1,233 words plus a final revised model excerpt. A mechanical
word-count audit opened all installed Markdown files, counting 24,274 words, but
returned counts rather than their contents to the agent. That overbroad filesystem
read was unnecessary; it is not an additional 24,274 words of model context. It
limits a claim of reading only needed files. Future accounting should count an
explicit read manifest. The missing `python` alias led to use of `python3` and
conditional friction capture.

## Large conceptual ER

The [large brief](er-routing/large-brief.md) supplied 18 entities, 17 relationships
and three ownership roots with five child types each. The
[output patch](er-routing/large.patch) contains one owning model document with a
root overview and three linked detail ER views.

The agent read 7,206 guidance words, 302 project-input words and 586 output-review
words. It reached ER, large-ER, composition and verification, alongside modeling,
scenario and documentation guidance. It did not read general Mermaid drawing.
The parent checked the output against the supplied relationships: all 18 entities
and 17 relationships appear, each relationship once, with supplied multiplicities
preserved. No keys, attributes or lifecycle rules were invented.

Decomposition remains discoverable. Composition still contains non-ER material;
this deeper route is not demonstrated to be minimal. The agent’s initial inventory
also listed Git metadata filenames unnecessarily, without reading their contents.

## Read an existing model and make a literal edit

The third agent received the earlier corrected model and two questions: whether
agreements can cover several services, and whether an organisation’s roles can
differ by covered service. It also had to replace only the README sentence
“No implementation exists.” with “Nothing is implemented yet.” The
[patch](er-routing/nearby.patch) contains that sentence change alone.

Its answer correctly described the service-specific role scope, proposal status
and unresolved counts, absence, identity and lifecycle. It read the model and
README (770 words), without reading scenarios, ER construction, PostgreSQL or
renderer guidance. It reported 3,224 guidance words including project instructions.
No renderer search occurred. Byte comparison checked the literal edit.

The remaining overhead matters: it followed relational-modeling, collection,
authority, authoring, clear-writing, short-text, visual selection and friction.
On review, the agent identified visual selection (431 words) as unnecessary and
shared authoring as avoidable for the exact replacement. “Before a substantive
explanation” was interpreted broadly enough to route the short answer through
visual selection. Further narrowing of general authoring entry is a separate
candidate; this revision does not claim the whole reading route is lightweight.

## Verification and limits

All agents reported local documentation/whitespace checks and accurate scope.
The two diagram tasks found no project renderer configuration or local `mmdc`.
They checked diagram source relationships, but did not parse or visually inspect
renders. No diagram rendering, theme, database or runtime correctness is claimed.
The rendering branch was exercised only for unavailable tooling, not a successful
render. No new diagram example was added to the reusable guidance; the notation
table retains the existing symbols.

Source package validation passed for 23 skills and one collection. Skill-creator
validation passed for all three changed skills. Parent review checked changed
routes, retained notation, artifact semantics and preservation of conditional
large-model guidance. Staged whitespace checks passed. Real Atlas and an unrelated
Python validation edit were left unchanged. No release tag or installation update
was made.

These are single behavioral trials with explicit project hooks. They support the
narrow routing change, not a general efficiency percentage or reliability claim.
A separate semantic-review-only task, a successful project renderer path, a fresh
relationship-correction handoff and collection dependency discovery remain
untested. Source-authoring behavior was exercised by the parent under repository
instructions rather than another independent trial.
