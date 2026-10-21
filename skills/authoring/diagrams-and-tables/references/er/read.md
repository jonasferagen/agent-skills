# Read an ER diagram

Identify whether the view is conceptual, proposed or implemented. Use its caption,
legend and model/glossary for entity and relationship meanings. An ER alone does
not prove implemented foreign keys or additional business rules. Unknown
cardinalities remain unknown; do not supply a constraint to complete an answer.

## Mermaid cardinality

Each end’s symbol describes the entity beside it. In
`ORDER ||--o{ ORDER_LINE : contains`, each order line belongs to exactly one
order, and an order contains zero or more order lines.

| Meaning | Left end | Right end |
| --- | --- | --- |
| exactly one | `\|\|` | `\|\|` |
| zero or one | `\|o` | `o\|` |
| zero or more | `}o` | `o{` |
| one or more | `}\|` | `\|{` |


Read the relationship label together with both endpoints. When attributes appear,
PK marks a primary key and FK a foreign key in the represented model; confirm the
model's status before treating either as implemented. Distinct relationships
between the same entities may describe different roles.

[Mermaid's ER documentation](https://mermaid.js.org/syntax/entityRelationshipDiagram.html)
owns syntax and notation. Consult it for unfamiliar symbols needed by the question.
Reading or applying a view requires no layout work, examples or renderer discovery.
For source accuracy use [semantic review](../review.md); for edits use the
[family guide](guide.md).
