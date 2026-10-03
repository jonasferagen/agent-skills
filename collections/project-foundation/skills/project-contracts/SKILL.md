---
name: project-contracts
description: "Read, apply, design or review obligations at a handoff between people, agents, files or services. Use for interpreting terms, assessing an exchange, finding missing obligations or changing compatibility; legal agreements and overall architecture have separate workflows."
metadata:
  version: "0.2.1"
---

# Project contracts

Make clear what participants can rely on at a handoff. Start with the user's
question, the authoritative agreement and the revision applicable to the exchange.
Keep proposed terms, adopted obligations and observed behavior distinct using
[status and evidence](../../references/status-and-evidence.md). Use
[foundation authority](../../references/foundation-authority.md) when establishing
or reconciling obligations, resolving conflicting authority or assessing changed
scope or operating circumstances. Reading or applying known terms within unchanged
constraints needs only their relevant owners; reuse current readings.

## Select the task

- **Read or explain:** Answer from the relevant terms and linked definitions.
  Distinguish explicit obligations, interpretation and ambiguity. Cite the terms
  that support the answer. A missing answer stays unresolved; a reading question
  does not require designing the agreement or reviewing all its terms.
- **Apply:** Compare a particular request, result or action with the applicable
  terms. Identify conditions satisfied, violated or undecidable from available
  evidence. Missing terms cannot supply acceptance criteria. Applying a contract
  does not itself authorize execution or adoption of a result.
- **Design or change:** Use [contract design](references/design.md) to discover
  needed obligations, propose terms and assess changes to existing agreements.
- **Review:** Use [contract review](references/review.md) to assess an existing
  agreement for the requested purpose and report findings.

Infer the task from the request. Load only the relevant reference; reading a
contract does not automatically trigger review. A literal wording correction
uses ordinary editing guidance. If the question is which responsibilities or
components should exist, use [project-design](../project-design/SKILL.md).
A document or file handoff does not require an API or machine-readable schema.

## Handle missing information

When the task exposes a missing term, identify the decision it leaves unresolved,
its consequence and the work that depends on it. During reading or application,
report that limit without silently supplying a rule. During design, propose or
establish terms within the user's authorized scope and existing constraints.
Continue unaffected work; ask only when the current task needs the missing answer.

A missing project term is not automatically a defect in this skill. If guidance
or routing caused an omission, an undocumented workaround or repeated difficulty,
use [friction capture](../../references/friction.md) to record the observation
and candidate improvement at a natural checkpoint. Keep project decisions in
the agreement; reusable guidance follows the collection's capture route.

For authored or restructured explanations, use
[authoring guidance](../../references/authoring.md). A focused answer from existing
terms needs no authoring workflow.
