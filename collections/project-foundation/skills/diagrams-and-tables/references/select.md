# Choose a form

| Reader needs to understand | Start with |
| --- | --- |
| A fact, reason, decision, caveat or convention | Brief prose |
| Cases sharing fields, options, obligations or changes | A table; shared fields matter more than item count |
| Work steps and conditional branches | A flowchart |
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
