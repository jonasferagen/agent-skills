---
name: project-contracts
description: "Read, apply, design or review handoff obligations between people, agents, files or services. Use for missing terms, acceptance and compatibility; not for legal agreements or overall system architecture."
metadata:
  version: "0.2.0"
---

# Project contracts

Make clear what participants can rely on at a handoff. Start with the user's
question, the written agreement and its applicable revision (its version if it
has one, otherwise the commit hash or date of the copy in force). A **contract**
here is any written agreement about a handoff: an interface description, a README
section, a schema with its notes, or a brief. Distinguish proposed terms, adopted
obligations and observed behavior. When no written agreement exists, say so,
infer the current expectations from the code, tests and records on each side,
label them as inferred, and ask the user before treating them as adopted. When
resolving conflicts or changing obligations, follow the project's process for
agreeing such changes, or ask the user when there is none.

## Select the task

- **Read or explain:** Answer from relevant terms and linked definitions. Cite
  what supports the answer and distinguish explicit obligations, interpretation
  and ambiguity. Missing terms remain unresolved; a reading task needs no redesign.
  Output: the answer, the terms cited, and the open points.
- **Apply:** Compare a request, result or action with applicable terms. Report
  satisfied, violated or unverified conditions. Missing terms supply no acceptance
  criteria; applying an agreement grants no execution or adoption permission.
  Output: one line per condition (satisfied, violated or unverified) with the
  evidence, plus the exact input and agreement revisions judged.
- **Design or change:** Use [contract design](references/design.md) to discover
  obligations, propose terms and assess changes to existing agreements.
  Output: the proposed or changed terms, marked proposed or adopted, with the
  unresolved terms and the work they block.
- **Review:** Use [contract review](references/review.md) to assess the agreement
  for the requested purpose and report findings. Output: findings, each with the
  term or omission, a concrete case, its consequence and the decision needed.

Load only the reference the task needs. A wording correction needs no contract
work. If the question is which responsibilities should exist at all, that is a
system-design question outside this skill; settle it first, then define the
handoff. A document handoff needs neither an API nor a machine-readable schema.

## Handle gaps and finish

For a missing term, name the unresolved decision, consequence, responsible owner
and dependent work. When the project names no owner, use the maintainer of the
side the term binds (from the code owners file or recent history), or the user.
During reading or application, report the limit without
silently supplying a rule. During design, propose or establish terms within the
scope the user has given and known constraints. Ask only when the current task needs the
answer; continue unaffected work.

Keep an agreement where it already lives. Put a new one where the project keeps
such documents, or beside the interface it describes if no convention exists,
and say which you chose. If the project has a template for agreements, use it;
filled headings do not establish completeness. Implementation procedures,
formats and records of actual exchanges stay in their own places. Link exact
input and agreement revisions when judging a particular result.

Report to the user the conclusions, relevant cases and evidence limits. A schema
check or tool success cannot prove fulfillment of every obligation. Follow the
project's writing conventions for authored changes. When the project has not
decided a term, record the gap in the report and ask the user whether to decide
it now.
