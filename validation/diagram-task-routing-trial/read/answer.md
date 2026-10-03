`ORDER ||--o{ LINE : contains` says:

- `||` beside `ORDER`: each line belongs to exactly one order.
- `o{` beside `LINE`: an order contains zero or more lines.
- `contains` names the relationship.

Yes, an order can have no lines: the `o` allows zero.

No, this does not prove that a database foreign key exists. As `context.md` states, this is a proposed model with no attributes or implementation specified. The diagram expresses the relationship; database implementation remains unspecified.
