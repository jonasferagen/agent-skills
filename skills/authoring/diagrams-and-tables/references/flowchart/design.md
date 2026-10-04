# Construct a flowchart

Read the [reading notes](read.md) for meanings and use shared
[composition](../composition.md) and [verification](../verification.md) guidance.
Add [Mermaid conventions](../mermaid.md) when using Mermaid. The
[example](examples.md) is optional when a branch and loop need illustration.

Ground the steps in the owning procedure, implementation or explicitly proposed
workflow. If actors or behavior need to be designed, use the project's selected
workflow-design guidance; drawing a missing branch must not silently decide it.

Bound the view by its trigger and observable outcomes. Label actions with verbs
and decisions with questions whose outgoing conditions are explicit. Include
relevant rejection, failure or pause outcomes so the happy path does not imply
that every input succeeds. Keep unresolved behavior visible in the caption or
an open question rather than inventing a default path.

For a repeat path, show the correction or event that permits another pass and
the stop or pause condition that matters to this workflow. Preserve source rules
for attempt identity, retry and authority through links to their owner. Avoid
turning rejection into an unconditional rerun.

When responsibilities matter, put the actor in the action label or use labelled
lanes/groups. Use one approach consistently at a useful level of detail. Separate
execution completion from acceptance and adoption. If parallel work or waiting
for several results matters, state the fork/join semantics explicitly or choose
a notation that expresses them; a pair of arrows is insufficient.

Walk a normal case and one consequential alternative before rendering. Check
that branch conditions cover the intended cases, merged paths preserve their
prerequisites, and each relevant path reaches a meaningful outcome or declared
wait. Then render and inspect at the intended reading width and themes. A parse
cannot establish either the workflow's correctness or its readability.
