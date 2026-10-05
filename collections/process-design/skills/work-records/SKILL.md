---
name: work-records
description: "Commission bounded work as a brief, retain its evidence and close it with a scoped disposition. Use when framing an assignment for another owner, recording what a run actually showed, or deciding what findings mean; routine fixes and plan items need no brief."
metadata:
  version: "0.2.0"
---

# Work records

Make a bounded assignment, its evidence and its disposition separately readable.
Read the existing intent, the source basis actually available and the project's
current owners first. Preserve what the project already records; this guidance
adds no approval gate and migrates nothing.

Five questions decide what you are writing:

| The question in front of you | Write | Shape |
| --- | --- | --- |
| What should this achieve, and how will we know? | A brief | [brief template](../../templates/repository-docs/work-records/brief.md) |
| What happened as work progressed? | A worklog entry | [worklog template](../../templates/repository-docs/work-records/worklog.md) |
| What did this assignment establish against its brief? | A report | [report template](../../templates/repository-docs/work-records/report.md) |
| What do these candidates tell us about an open choice? | A study | [study template](../../templates/repository-docs/work-records/study.md) |
| What is being transferred, and what must the receiver be able to rely on? | A handoff record | [handoff template](../../templates/repository-docs/work-records/handoff-record.md) |

Reading or correcting an existing record needs none of these. A small task can
stay one item in the active plan with a short result; it does not need a brief,
a worklog and a decision record. Use the existing work record when the project
already has an adequate one.

The [record chain](../../references/record-chain.md) owns what each record means
and who keeps it. The [record format](../../references/record-format.md) owns
the optional metadata and its checker.

## Frame the question

When defining assignment boundaries or preparing work for an agent starting
without the conversation, use the [assignment contract](../../references/assignment-contract.md).
It owns split decisions, required inputs, discovery routes and the requested
return. A brief can reference discoverable context without copying it all.

State the intended use and its boundary before the method. Name the bounded
question this work should resolve, the evidence that would let the owner judge
it, and the recorded outcome that closes the assignment. Without a completion
condition, the work has no way to finish except by exhaustion.

Pin the source basis actually used, with revisions and commits. Where a shared
input is unselected or open, name the local hypothesis you are working under
instead of inventing a shared requirement to justify the work. Mark adopted
choices separately from proposed tests and open questions.

Write criteria as observable questions with the evidence that settles them and
the owner who decides. Distinguish a measurement from a judgement; do not let
one stand in for the other. If a threshold is undecided, say so and collect
observations rather than asserting acceptance against an invented limit.

A living specification can support several bounded assignments with their own
completion. Say explicitly when no single completion boundary is selected.

## Perform and retain evidence

Start at project instructions, resolve the brief's required inputs and use the
relevant method owners. Record the actual basis used. If a missing input or
conflicting obligation prevents a sound result, identify the affected work and
continue independent work; use the assignment contract's interruption guidance.

Identify the exact subject: files, revision and relevant dependencies, and what
was included or excluded. Record the conditions, method, settings and acting
reviewer. A result without its conditions cannot be compared with another.

Retain what the run produced, what you observed and what the observation does
not cover. Keep the gaps visible: an unavailable tool, an unverified engine, an
unknown viewing setup and a fabricated input are limits on the evidence, not
details to tidy away. Where a prerequisite was missing, say which conclusion it
blocks.

Put this in the linked record, not in the brief. The brief keeps intent,
criteria, coordination state and next action; appending results to it creates a
second authoritative status and loses which revision was actually assessed.

## Review and decide

Assess findings against the criteria the brief stated, naming the criterion each
observation answers. Keep technical execution, observed behaviour and acceptance
separate: a reproducible run proves the run, not that the result is good enough
for the intended use.

Record the disposition for the named use, the acting decision-maker and the next
owner or completion. A decision can finish the question, ask for more evidence,
request work or revise the brief. An explicitly inconclusive outcome can close a
deliberately bounded investigation; missing required work cannot.

Route feedback to the thing that changed, using the
[feedback table](../../references/record-chain.md#route-feedback-to-the-thing-that-changed).
Changed intent or criteria go back to the commissioning owner as a new revision;
missing evidence goes back to the performing owner. Preserve the earlier record,
its findings and the scope of what they established.

## Keep boundaries

A record organizes work. It grants no authority, authorizes no spending, and
does not make a disposition into acceptance by an owner who did not give it.
Existing delegation still applies; this adds no permission request where
permission was already given.

Do not expand a brief into a second home for policy, architecture,
responsibilities, contracts or the active work queue. Link those owners. When a
record and an authoritative owner disagree, the owner governs and the
disagreement is reported, not silently resolved.

When intent, criteria or scope change, take a new revision and say what changed
and why. Editorial clarification keeps the revision; the commit still identifies
exact content. Do not rewrite retained evidence to match current intent.
