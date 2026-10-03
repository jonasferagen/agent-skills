---
name: project-policy
description: "Interpret project engineering obligations, assess evidence against them, or establish and review policy as users, data, exposure, lifetime, compatibility or recovery change. A focused policy question needs only the relevant facts and requirements."
metadata:
  version: "4.2.0"
---

# Project policy

If execution exposes a consequential guidance or routing problem, use
[friction capture and repair](../../references/friction.md). Successful work needs
no capture pass.

Make the project's circumstances determine its engineering requirements. Keep
operating facts, proposed requirements, adopted obligations and evidence of
compliance distinct using [status and evidence](../../references/status-and-evidence.md).

Policy sets minimum guarantees. Existing architecture, abstractions and tests do
not automatically become requirements. Preserve explicit commitments until their
owner deliberately changes them; distinguish those commitments from mechanisms
that may be simplified while preserving required outcomes. Verify the affected
behavior when changing a mechanism.

For establishment, adequacy review or changes to phase and delivery scope, read
[phase and scope](references/phase-and-scope.md) to bound the current outcome
without relaxing existing obligations.

## Select the task

- **Read or interpret:** Answer the question from the applicable policy facts,
  boundaries and derived requirements. Identify the source and scope of the
  obligation. Distinguish explicit requirements, interpretation and unresolved
  facts; do not infer readiness from an adopted policy. Stop when the question is
  answered without loading establishment or transition guidance.
- **Apply or assess compliance:** Compare the supplied behavior and evidence with
  the relevant obligations. State what is met, contradicted or unverified. Missing
  evidence is not proof of failure or compliance. Report the affected claim and
  evidence needed; do not rewrite policy to fit implementation or start a wider
  audit merely to answer the question.
- **Establish:** Use [establishment](references/establish.md) to determine a new
  policy's facts, axes and derived requirements.
- **Assess or make a change:** Use [policy changes](references/policy-changes.md)
  for proposed, adopted or already-observed changes. Assess the affected delta
  and consequences; proposals remain proposals until adopted. Load document
  writing guidance only when the task includes updating policy facts.
- **Review policy adequacy:** Compare the policy with the requested use and
  available facts. Use [requirement discovery](references/requirements.md) to find
  missing decisions. Report omissions and contradictions separately from missing
  implementation evidence. Changed circumstances also need the change workflow.

Infer the task from the request and load only what it needs. If evidence reveals
changed operating circumstances, use the affected change route even when nobody
has edited the policy; keep execution within the task's authorization. A literal
wording edit needs a focused meaning check and a short no-obligation-change assessment,
recorded outside the policy table. It needs no full profile reconstruction.
Reading, assessment and review do not themselves authorize changes or external
execution; carry out work already authorized by the user's task.

## Resolve the applicable obligations

Read policy for current facts and adopted decisions, boundaries for scope and
responsibility, and overview for relevant implementation choices. Read a glossary
only when its meanings matter. A blank cell is unknown, not permission, a default
guarantee or a waiver. Preserve current requirements when evidence is incomplete.

For members of a shared project, use
[multi-repository foundations](../../references/multi-repository.md) to resolve
inherited policy, local facts and exception authority. A closer file does not
silently override shared obligations. Follow
[foundation authority](../../references/foundation-authority.md) when establishing or reconciling
decisions, resolving conflicting authority or assessing changed circumstances.
A focused interpretation or compliance assessment within known constraints needs
only the relevant owners and evidence; reuse current readings. Use
[source-of-truth](../source-of-truth/SKILL.md) when competing definitions or
inconsistent consumers require reconciliation.

Policy facts, derived requirements, procedures, work queues and evidence have
separate owners. Follow their links as the question requires. Reading an existing
policy does not require migrating its document format.

## Handle gaps and finish

A missing fact or decision is a project gap: identify its consequence, owner and
what depends on resolving it. Missing proof of an established requirement is an
evidence gap: identify the claim that remains unverified and the necessary check.
Ask only when the current task depends on an answer; continue unaffected work.

A project or evidence gap alone does not establish a defect in the skill.

For authored or restructured documents, use
[shared authoring guidance](../../references/authoring.md). A focused answer from
existing policy needs no authoring workflow. Report the task's conclusion, sources,
checks actually performed and remaining uncertainty. A document assessment cannot
establish operational compliance without evidence from the relevant behavior.
