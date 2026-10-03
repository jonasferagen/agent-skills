# Reviewing a policy change

Use this for proposed, adopted or already-observed changes to operating facts or
obligations. Assess the affected delta; a proposal does not require rebuilding
unaffected axes or adopting the proposal. When the new circumstances leave needed
decisions unclear, use [requirement discovery](requirements.md).

During project work, review affected foundation facts when purpose,
responsibility, phase, delivery scope, terminology, users, data, exposure, lifetime, compatibility or
recovery changes, even if nobody has edited the policy. A wording-only edit may
record that it changes no obligations; every policy edit needs an impact assessment
outside the policy table. Substantive changes, including relaxation, need the
consequence review below. These task-based triggers do not start a watcher.

When the task includes writing or reconciling policy facts, use
[writing policy](writing-policy.md) for document shape, ownership and checks.
An assessment alone preserves the policy and records findings outside it.

A change to a project's assumptions can invalidate decisions made throughout
the system. Review the full range of consequences, then scope execution to the
areas affected. This is a manual starting point that can grow from experience.

Keep the policy section or separate policy file as the current axis table. Record this assessment in existing
work notes, downstream requirements in their owners, and verification in evidence
records. Link back to the affected policy axes and boundaries.

## Establish the delta

Compare the previous and proposed policy. Classify each changed requirement as
tightening, relaxing, mixed or clarification; one edit can contain several kinds.
Record the reason, affected environments and effective condition. A clarification
is small only if its meaning and obligations are unchanged.

When a changed circumstance is already true, record that truth immediately.
Distinguish the observed condition from permission and readiness: discovering real
user data does not authorize processing it or establish that protection is adequate.
Identify containment or remediation needed within the existing authorization.

## Trace the consequences

Use this table as a review prompt, not a fixed requirement to change everything.
For each area, identify affected owners and work, a reason it is unaffected, or
what remains uninspected. Search the repository for consumers of the changed
rule; include linked runbooks and known downstream consumers. Do not inspect
live accounts merely to complete the table.

| Area | Questions to resolve |
| --- | --- |
| Product and architecture | Do lifetime, scale, failure consequences or ownership boundaries change? |
| Stored data and migrations | Which retained state needs preservation, conversion, validation or deletion? What can be recovered? |
| Interfaces and consumers | Which compatibility promises, clients or integrations depend on the old rule? |
| Identity and permissions | Do exposure, credentials, actors, external effects or unattended authority change? |
| Tests and release checks | Which required outcomes need new evidence? Do old results still establish them? |
| Operations and recovery | Are startup, deployment, monitoring, incident response, backups or restore procedures affected? |
| Docs and agent guidance | Which instructions, diagrams, examples, skill selections or local adaptations state the old rule? |

## Turn the assessment into work

A spike becoming maintained software, or local development moving to cloud
hosting, is a substantive transition. Do not treat a profile label edit as its
completion. Use the consequence areas above to select the reviews and audits the
new use needs. For example, hosting can change network exposure, identity and
secrets, deployment and rollback, logging and monitoring, cost ownership, retained
data and recovery. Moving beyond a spike can change compatibility, maintenance,
failure consequences and the evidence needed before release. Derive the actual
requirements from the intended use rather than prescribing one universal checklist.

Separate assessment from implementation and verification. The transition record
must identify required reviews or audits, their scope and owner, resulting work,
and the acceptance evidence needed for the new use. Use available specialist
skills when useful; a missing specialist does not remove the review requirement.
Keep proposed hosting or stricter use distinct from approved and verified use.

Review phase and delivery scope as well as minimum guarantees. Remove future-only
design questions from the immediate queue when they do not block the current
outcome; keep their revisit conditions visible. A reduction in planned scope is
not evidence that retained data or current consumer obligations have disappeared.

Review simplification opportunities as well as missing safeguards. Record what
guarantee a mechanism protects, whether policy requires it, what a simpler design
would preserve or remove, and what evidence could establish that result. Higher
standards can sometimes be met with less machinery. Existing implementation
complexity is not itself a requirement; retained data and explicit commitments
still need deliberate treatment.

Use the project's existing task queue. Each affected requirement needs an owner
(a project role is sufficient), required work, dependencies, acceptance evidence
and a due milestone or condition. Unknown ownership stays an open item. Keep
policy facts in the policy, detailed procedures in their owners, tasks in the
queue and results in the verification record.

For tightening, identify prerequisites for the new use. Do not enable a proposed
expansion or report compliance while its prerequisites are unverified. If the
condition already exists, show the gap and authorized containment/remediation
instead of labelling it a future concern. An exception must state its scope,
reason, owner and review/expiry condition under the project's authority.

For relaxation, explain which guarantee is removed and who depended on it.
Look for machinery that exists only to meet that guarantee: abstractions, checks,
deployment steps, configuration, compatibility layers and operational procedures.
Consider refactoring, simplifying or deleting it when the remaining requirements
permit. Record the benefit and the evidence needed to preserve retained data,
active compatibility promises and other still-required behavior. This is a
cleanup opportunity to assess, not a requirement to launch a broad refactor.
Do not delete tests, migration history or retained data merely because a profile
label became lighter. Deliberately authorize and assess those changes separately
when they fall outside the requested policy work.

Carry out in-scope authorized work, in dependency order. Run checks appropriate
to the changed behavior and consequence. A policy-only edit cannot prove a restore,
safe migration, access boundary or deployed state. Leave out-of-scope actions as
concrete follow-ups, and continue unaffected work under its existing policy.

## Record the outcome

Record date, old/new requirements, assessed areas, linked work and evidence,
remaining gaps and the gate for the changed use. Report which
[state](../../../references/status-and-evidence.md#states) was reached: adopted policy, implementation or
verified compliance.

For now, this review and linked queue are the mechanism. Broader automation can
later detect policy changes, find consumers or select checks. Add it from actual
transitions rather than inventing a universal suite before the project needs one.

Keep the initial mechanism manual and proportional. A broad impact review does
not mean running every test or making every possible change on each edit.
Automate repeated checks after actual policy transitions show what they need to
protect. Changes to policy are not a reason to halt unaffected authorized work.
