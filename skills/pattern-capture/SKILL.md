---
name: pattern-capture
description: "Assess and capture an engineering pattern when explicitly requested, or when a review, fix or user correction reveals a reusable lesson. Check existing guidance, prefer a simple rule, and improve its home within the authorized scope."
metadata:
  version: "0.2.0"
---

# Pattern capture

At a natural checkpoint in the current task, consider whether a meaningful
finding would improve future engineering decisions. Keep the original task
moving. An ordinary edit or a speculative smell alone does not call for a
catalog review.

An explicit capture request also activates this workflow for small ideas that
would not warrant that checkpoint. Use the idea named by the user or evident
in the current discussion; ask only if the intended idea is unclear. In clients
with native skill invocation, use `$pattern-capture`. A project may also map
`/pattern-capture [idea]` to this skill in its instructions; that text shortcut
does not register a native slash command.

## Decide whether the lesson generalizes

State the mechanism, the conditions where it applies, and a case where it does
not. Distinguish a reproduced defect or demonstrated improvement from a proposed
change. One well-supported mechanism can justify guidance; recurrence adds
confidence but is not a prerequisite. Preserve uncertainty and local tradeoffs.

Ask whether the guidance would change a future decision. Keep project-specific
facts and choices in their project. Do not turn a local convention, an untested
optimization or a user's one-time exception into a universal requirement.

## Prefer the simplest adequate rule

Choose the simplest rule that preserves the required behavior and meaningful
distinctions. When exceptions accumulate, reconsider the rule's scope, ownership
or abstraction before adding another exception. A narrower rule or separate
concerns may explain the cases better. Keep exceptions that protect real
invariants; brevity alone is not evidence that they are unnecessary.

Apply this test to the proposed guidance and its existing home. Prefer improving
one clear rule over adding a competing rule or another skill. Skill-authoring
guidance covers how to write the package; this workflow decides what is worth
capturing and where it belongs.

## Find its home without loading the catalog

Find the authoring repository from the project's instructions or imported-skill
provenance. Read its catalog or skill metadata first, then only the likely
owner's instructions and relevant references. Do not assume a machine path or
load every skill. If no source location is available, name the proposed home
and missing location in the task's hand-back.

Prefer, in order:

1. Leave adequate existing guidance as it is and identify it in the result.
2. Correct or extend its owning skill or conditional reference.
3. Refactor overlapping guidance when ownership or activation is unclear.
4. Create a skill when the workflow has its own recognizable trigger and useful
   outcome. Language-neutral decisions belong outside language-specific skills.

## Capture within the task's scope

When skill maintenance is authorized, make the smallest useful source change,
using the authoring repository's conventions and checks. A read-only review can
identify a home and propose exact guidance without editing it. This skill does
not itself authorize changing another repository or installing updated skills.
Avoid editing vendored copies independently of their source and provenance.

Include the relevant conditions, evidence and limits. Put source-specific
observations and uncertain proposals in the repository's validation record;
keep reusable instructions concise. Add a realistic activation case and a
nearby case that should not activate the guidance. When it changes a workflow,
validate behavior as well as package structure, within available authorization.

Finish by reporting what generalized, its existing or changed home, and what
was actually verified. If the existing guidance already covers it, say so and
stop. Do not recursively capture lessons about the capture process.
