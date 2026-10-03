# Establish or change policy

Use this workflow when establishing policy or assessing changed circumstances
and obligations. A proposal needs an impact assessment of the proposed delta;
it does not require rebuilding unaffected axes or adopting the proposal.

## Discover what the circumstances require

Trace a concrete use through the people relying on it, the state it retains and
the actions it permits. Ask where an owner would have to guess a required outcome
or where the same stated facts could lead to incompatible obligations. Use the
axes below as prompts; a filled table alone does not establish that the important
decisions are covered. Include a domain-specific circumstance when it changes a
concrete requirement, even if these instructions do not name it.

For each consequential unknown, identify the missing decision, affected use,
responsible owner and work that depends on it. Propose requirements using available
evidence and existing authority; distinguish them from adopted decisions. Keep
unaffected work moving. An unavailable verification result is an evidence gap,
not grounds to weaken the requirement.

## Keep facts and consequences in their owners

Keep the Policy section of `docs/foundation.md` (or an established separate
policy owner) to one two-column table:
`Axis | Current fact or decision`. Use short, formal entries; separate facts with
semicolons and state unknowns explicitly. The
[foundation format](../../../references/foundation-format.md) owns document shape
and inheritance; keep interpretation instructions out of the foundation.
Record operating circumstances and adopted constraints, such as offline-only use
or a recovery target. Exclude repository procedures, implementation reports,
impact assessments and change history.

Interpret that table together with the established boundaries to derive downstream
requirements. Record durable requirements in their affected design or operational
owner; repository working rules belong in `AGENTS.md` or its linked contributor
guide. Put transition tasks and impact assessments in existing work notes, and
verification results in evidence records. Create another document only when no
existing owner serves the reader. Do not add a requirements table to the policy section.
Keep the originating policy axis and boundary traceable from downstream decisions.

When reconciling an expanded policy, relocate useful rules and evidence before
removing their sections. Preserve adopted obligations and repair consumers; moving
a requirement does not relax it. Use project-docs to choose appropriate homes.

## Establish the policy

Read project instructions, the active plan, architecture and relevant operations
guidance. Reuse an existing policy owner; otherwise adapt the bundled
[foundation template’s Policy section](../../../templates/docs/foundation.md#policy)
into the repository. A member inherits shared axes and records only local facts
and adopted exceptions; explicit unknowns remain unresolved without waiving shared
obligations. Keep the
populated policy outside the imported skill. Link it from the project's agent
instructions and entry page.

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

## Change the policy

During project work, review affected foundation facts when purpose,
responsibility, terminology, users, data, exposure, lifetime, compatibility or
recovery changes. Compare the affected documents with the new evidence even if
nobody has edited the policy section. Update only the affected decisions and their
consequences; a terminology correction need not reconstruct the full profile.
These are task-based review triggers, not a background monitoring service.

Every policy edit needs an impact assessment, recorded outside the foundation tables in
the existing task notes or hand-back. A wording-only change may record that it
changes no obligations. For a substantive change, including relaxing a
rule, read [policy changes](policy-changes.md) and examine downstream
requirements across the project. A change in real circumstances also triggers
this review even if nobody has edited the policy yet.

Stricter requirements can create substantial work across code, stored data,
tests, operations and docs. Record that work in the project's active queue,
with owners, dependencies, required evidence and the condition that gates the
new use. Carry out the work already authorized within the task; preserve visible
gaps for work outside its scope. Do not describe the project as meeting the new
requirements before the evidence exists.

Keep the initial mechanism manual and proportional. A broad impact review does
not mean running every test or making every possible change on each edit.
Automate repeated checks after actual policy transitions show what they need to
protect. Changes to policy are not a reason to halt unaffected authorized work.

## Verify the application

- When establishing or substantively revising policy, check that each axis has
  evidence, a decision or an explicit unknown. For wording-only edits, verify
  that obligations are unchanged without reconstructing the profile.
- Check that the policy body contains only the axis table, with concise facts,
  decisions and explicit unknowns; keep consequences and evidence in their owners.
- Trace changed requirements to their consumers, work items and acceptance
  evidence. For unaffected areas, record a short reason when reviewing a change.
- Confirm that existing commitments and live state were preserved unless their
  change was authorized. Separate current scope from a proposed future scope.
- Check local links and the repository's applicable documentation checks.
  Report which checks ran and which operational claims remain unverified.
