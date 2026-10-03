---
name: project-planning
description: "Create, review or maintain project plans, sequence bounded work, and reconcile shared and local next steps. Use for planning outcomes and dependencies; architecture decisions and execution procedures retain their own owners."
metadata:
  version: "0.2.0"
---

# Project planning

If execution exposes a consequential guidance or routing problem, use
[friction capture and repair](../../references/friction.md). Successful work needs
no capture pass.

Start from the project's current scope, planning owner and relevant design or
implementation evidence. Use [foundation authority](../../references/foundation-authority.md)
for adopted constraints; reuse current readings. A request to review a plan
produces findings; a request to update it authorizes the corresponding edits.

## Choose the task

- To choose what comes next, use [next-step selection](references/next-step.md).
- To create or restructure a plan, use the structure below. The
  [worked example](references/example.md) offers an optional scaffold.
- To update or resume work, reconcile the affected items against actual results.
  Reading a status or correcting wording needs no full replanning pass.

## Structure around outcomes

Keep plans under the managed project directory using
[canonical document homes](../../references/document-homes.md). Follow its
transition rules for an existing layout; do not create a second active queue.

Within the canonical or explicitly transitional home, preserve useful planning
conventions. Distinguish
longer-term outcomes, active bounded work and detailed execution steps when those
levels help the reader. They need not be separate documents. Detail near-term work
enough to act; leave later work at the level its evidence supports. A roadmap's
order does not establish dates, estimates or a commitment to execute.

For an active item, make its intended result, responsible owner, necessary inputs,
next action and completion evidence easy to find. Record a blocker only when it
prevents that result. Deferred questions need a revisit condition and the work
they affect. Use prose, a short list or a table according to the existing plan;
these are useful fields, not a mandatory schema for every small task.

Sequence by real dependencies. Name the prerequisite result rather than relying
on list position. Independent work can proceed when its inputs exist; architectural
levels and repository names do not establish a mandatory order. A small experiment
can resolve uncertainty without committing to the full implementation.

## Keep shared and local work aligned

Give each actionable item one authoritative status and next action. In a project
with several repositories, use its established shared planning owner for work
that coordinates them. Link local implementation detail and acceptance procedures
from that item. If the project delegates local queues, the shared plan links them
and carries only the dependencies or outcomes needed for coordination.

Local design pages explain prerequisites and decisions and link to the owning
work item. Reconcile competing queues by preserving unique tasks and choosing
one owner for each status; do not simply delete the less prominent list. Use
[project-docs](../project-docs/SKILL.md) only when document ownership needs a
decision. Plans link current architecture and contracts without becoming another
home for their definitions.

## Maintain the plan as evidence changes

On completion, record the result and relevant evidence, then update dependent
items. Distinguish design agreement, implemented behavior and verified behavior
([states](../../references/status-and-evidence.md#states)); a completed design task does not complete its implementation task. Partial work
retains its remaining action and any usable evidence.

When a discovery changes scope or dependencies, revise the affected sequence and
explain the consequential change briefly. Preserve useful decisions and outcomes
in the managed records home, linking technical evidence from its owner; keep obsolete instructions out
of the active queue. Cancellation and supersession retain unresolved obligations
and links to replacement work where needed. Do not rewrite unrelated plan areas
for a routine progress update.

## Check and report

Trace one active item from inputs to completion evidence, including its dependent
consumer when relevant. Check that it has one status owner, its next action is
possible or its blocker explicit, and deferred choices have not become accidental
gates. Report proposed sequencing separately from authorized execution. A plan
grants no [authority to act](../../references/status-and-evidence.md#authority-to-act), such as running
paid jobs, migrating or deploying.

For authored plans use [authoring guidance](../../references/authoring.md).
