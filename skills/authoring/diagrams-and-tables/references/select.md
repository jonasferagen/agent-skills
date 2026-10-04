# Choose a form

| Reader needs to understand | Start with |
| --- | --- |
| A fact, reason, decision, caveat or convention | Brief prose |
| Cases sharing fields, options, obligations or changes | A table; shared fields matter more than item count |
| Work steps and conditional branches | A flowchart |
| Who performs work, how, and what crosses responsibilities | A [swimlane activity view](swimlane/read.md), including human/agent/tool workflows |
| One object's states and allowed transitions | A state diagram |
| Ordered interactions between participants | A sequence diagram |
| Information sources, transformations, stores and destinations | A data-flow diagram |
| System parts, ownership and dependencies | A component or context view |
| Entities and their relationships | An ER diagram; add a field table only when field details matter |

Choose by the question, not the nouns: a database request can need a sequence
view of callers, an ER view of stored relationships, or a flowchart of validation
steps. A workflow describes work moving; a state diagram describes what one
object may become. Show several views only when they answer distinct questions.

Use a diagram when the relationships are the explanation. Do not add one merely
because the document describes a system. Keep each form on one reader question
and distinguish established facts, proposals and unknowns.

Mermaid's `flowchart` is a rendering syntax that can also draw component/context
views and data-flow views. Select guidance by what the nodes and arrows mean,
not by that keyword. A repository handoff arrow does not by itself state the
order in which work executes.

For agent-led work, choose by the same reader question. A swimlane activity view
can expose responsibility and method without implying that every handoff is an
API. Use a sequence diagram when the exact calls, messages and replies matter.
Use formal BPMN when its defined process/collaboration semantics are needed;
ordinary activity boxes with method labels do not claim BPMN conformance.
