---
name: lesson-capture
description: "Capture reusable engineering lessons when a review, bug fix, architectural smell, simplification or user correction reveals a meaningful pattern. Check whether agent-skills already covers it, then improve the right home within the authorized scope."
metadata:
  version: "0.1.0"
---

# Capture reusable lessons

At a natural checkpoint in the current task, consider whether a meaningful
finding would improve future engineering decisions. Keep the original task
moving. An ordinary edit or a speculative smell alone does not call for a
catalog review.

## Decide whether the lesson generalizes

State the mechanism, the conditions where it applies, and a case where it does
not. Distinguish a reproduced defect or demonstrated improvement from a proposed
change. One well-supported mechanism can justify guidance; recurrence adds
confidence but is not a prerequisite. Preserve uncertainty and local tradeoffs.

Ask whether the guidance would change a future decision. Keep project-specific
facts and choices in their project. Do not turn a local convention, an untested
optimization or a user's one-time exception into a universal requirement.

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
stop. Do not start another lesson-capture cycle about the capture process.
