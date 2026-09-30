# Reviewing a policy change

A change to a project's assumptions can invalidate decisions made throughout
the system. Review the full range of consequences, then scope execution to the
areas affected. This is a manual starting point that can grow from experience.

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
Do not delete tests, migration history or retained data merely because a profile
label became lighter. Deliberately authorize and assess those changes separately
when they fall outside the requested policy work.

Carry out in-scope authorized work, in dependency order. Run checks appropriate
to the changed behavior and consequence. A policy-only edit cannot prove a restore,
safe migration, access boundary or deployed state. Leave out-of-scope actions as
concrete follow-ups, and continue unaffected work under its existing policy.

## Record the outcome

Record date, old/new requirements, assessed areas, linked work and evidence,
remaining gaps and the gate for the changed use. Adopted policy, implementation
and verified compliance are separate states. Report which one was reached.

For now, this review and linked queue are the mechanism. Broader automation can
later detect policy changes, find consumers or select checks. Add it from actual
transitions rather than inventing a universal suite before the project needs one.
