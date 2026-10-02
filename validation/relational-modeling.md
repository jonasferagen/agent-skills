# Validation — Relational modeling

## Scope — 2 October 2026

Draft 0.1.0 is a modeling workflow and synthetic-scenario reference. It is currently
a standalone candidate under `skills/design/`, not an implemented data-foundations
collection. The trial explicitly supplies project-foundation and postgres-design;
this setup does not implement dependency discovery, installation or pinning.

The user authorized a bounded experiment with organisation, agreement and service,
two retrieval questions, and initially undecided cardinalities and participant
roles. The model is not an adopted design for real Atlas. No SQL, migration runner,
seed loader, application or database environment is in scope.

## Cases

| Case | Evidence sought |
| --- | --- |
| Initial brief to model | Retrieval questions trace through a model, assumptions stay visible, terms have one home and unresolved choices remain explicit. |
| A subsequent relationship correction | Affected model, ER view, glossary and scenarios agree; unrelated decisions are preserved and the old interpretation is distinguishable. |
| Literal README wording edit | No modeling or database-design guidance is loaded merely because the project has those skills installed. |

A fresh modeling agent gets the initial brief without the correction or expected
model. A second fresh agent gets the nearby wording task. The relationship update
is delivered only after the initial artifact is complete. Record actual reads,
artifact review and limits; reading fewer words alone is not acceptance evidence.

## Draft checks

Package validation passed for 23 entries; skill-creator validation and staged
whitespace checks passed for the new package. Skill-creator, domain-modeling and
the repository's authoring guidance informed the draft. Glossary content is domain
meaning; database representation and implementation readiness are separate.

## Results

The trial used source commit `4f5877f`, a tracked isolated fixture and explicitly
copied dependencies. The [supplied brief](relational-modeling/brief.md),
[initial document patch](relational-modeling/initial.patch) and
[correction patch](relational-modeling/correction.patch) preserve the inputs and
outputs. Paths inside patches refer to the fixture. Its baseline was `5fdd818`,
initial result `c92fe28`, and corrected result `a527e2d`. Real Atlas was unchanged.

### Initial model

The fresh agent produced model, scenarios and glossary documents, with owner links
in the project README. A database directory README was unnecessary at this size.
One canonical conceptual ER view showed the explicitly provisional single-
organisation and single-service assumptions. Synthetic examples exercised both
retrieval questions, no results, matching names with different identities and
counterexamples for extra participants and missing or multiple services.

The agent reported reading 19 source files, approximately 9,100 words. These
covered project inputs, modeling and scenarios, foundation authority/authoring,
project-docs, clear-writing and visual references. PostgreSQL representation
guidance was installed but not needed for the conceptual model. No migration or
seed-loading documents were created.

### Relationship correction

After the initial commit, the same agent received this new requirement:

> An agreement may cover several services. An organisation’s participant role may differ for each service covered by that agreement.

The corrected model introduced coverage as an agreement/service association.
Role meaning changed to organisation + agreement + service in both model and
glossary. The scenarios distinguish different roles across services, preserve
distinct agreement results and prevent role facts leaking across agreements
sharing a service. The ER changed consistently to represent multiple coverages.

The agent preserved the unrelated single-organisation assumption, identity
assumption and unresolved lifecycle rules. Its compact role representation
explicitly depends on the single-organisation assumption; it is not a general
solution for multiple participants. Missing coverage, simultaneous roles and
missing-role meaning remain open. These artifacts are a coherent proposal with
blocking decisions, not an implementation-ready schema.

This was a continuation with retained context: zero additional guidance words
were reported, plus approximately 1,050 words reread from the existing project
documents. It does not test a fresh agent discovering an existing model during
a handoff.

### Nearby wording task

A separate fresh agent changed only “No implementation exists.” to “Nothing is
implemented yet.” Its diff contained that sentence change alone. It read project
instructions and the friction reference after encountering a missing `python`
alias; it used `python3`. It loaded no modeling or database guidance and created
no extra deliverables. The environment observation does not justify another
universal rule.

## Review and verification limits

The parent reviewed the initial documents and full correction diff against the
supplied questions and correction. Assumptions remained visible, the new role
scope agreed across document owners, and affected scenarios distinguished the old
and new interpretations. Both agent passes reported 12 valid local links and
clean whitespace, alongside manual relationship and retrieval checks.

No renderer or `mmdc` was available in the fixture. Mermaid was reviewed as
source; parsing and rendered readability remain unverified. No database, SQL,
application, network, dependency installation or runtime checks were performed.
The source package validator passed for 23 skill entries.

The initial agent listed external skill filenames during discovery, but reports
reading no external skill contents or source-authoring repository. This weakens
a strict isolation claim. Explicit project routes also mean this trial does not
establish unaided catalog discovery or working collection dependency resolution.
One initial run, one warm correction and one nearby task establish examples of
behavior, not reliability across repeated runs.

## Captured friction and next experiment

The two-edge ER task loaded composition, drawing and ER references containing
substantial large-diagram and flowchart guidance. Source inspection confirms the
route explicitly asks for all these references. Conditional routing worked for
the nearby prose edit, but the selected diagram route is still broad.

Candidate: give small ER tasks a compact route for source grounding, cardinality
notation and verification; load large-view decomposition and flowchart layout
only when needed. Keep this inside the existing visual skill and references.
A new microskill or copied modeling-specific diagram rules would add ownership
without resolving the underlying route.

Before claiming an improvement, compare a fresh small-ER run against this
baseline, exercise a large ER that still needs decomposition, and repeat a nearby
prose task. Check preserved semantics and verification duties as well as reading
cost. No routing change is bundled into this evidence commit. Collection
dependency packaging and a fresh-agent correction handoff remain separate trials.
