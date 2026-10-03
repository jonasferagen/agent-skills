# Establish policy

Use [requirement discovery](requirements.md) to identify the decisions the actual
use needs, and [writing policy](writing-policy.md) for document owners, format and
verification. Establishment does not claim implemented or verified compliance.

Read project instructions, the active plan, architecture and relevant operations
guidance. Reuse an existing policy owner; otherwise adapt the bundled
[foundation template’s Policy section](../../../templates/docs/foundation.md#policy)
into the repository. A member inherits shared axes and records only local facts
and adopted exceptions; explicit unknowns remain unresolved without waiving shared
obligations. Keep the
populated policy outside the imported skill. Link it from the project's agent
instructions and entry page.

## Policy axes

Record the following axes separately. Add a domain-specific axis when it changes
a concrete requirement; avoid collapsing them into one maturity label or score.

| Axis | Establish | Requirements it can change |
| --- | --- | --- |
| Intended lifetime | Experiment, evolving product or maintained system; expected disposal or handoff | Investment in reuse, maintenance and documentation |
| Users and reliance | Who uses it and what failure prevents them doing | Release evidence, availability and support |
| Data | Synthetic or real, sensitivity, ownership and replaceability | Access, retention, deletion, migrations and recovery |
| Exposure and authority | Local/public reach, identities, external writes, spending or unattended actions | Authentication, isolation and execution boundaries |
| Compatibility | Existing consumers, interfaces and retained state | Versioning, migration and upgrade obligations |
| Recovery | Acceptable data loss and downtime, recovery owner | Restore evidence, rollback or forward recovery |

Use repository evidence and the user's decisions. Mark missing facts as unknown,
with the decision they block; ask only when the current task depends on them.
An experiment with real data still has real data obligations. Local development
does not establish that all local state is disposable. If environments differ,
give them separate scopes and identify shared requirements.

Map each relevant fact to an observable requirement and its owning document or
check. Link existing procedures rather than copying their details. Retain
explicit project commitments until deliberately changed: a lighter profile
cannot silently waive tests, migration rules or authorization boundaries.
Follow the user's existing authorization; neither the template nor a stricter
policy grants permission to contact users, access production or deploy.
