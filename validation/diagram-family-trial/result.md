# Selected view

Use a data-flow view: the question concerns information sources, transformations, retained content and destinations. This is a prose outline of the supplied description, not a verified implementation model.

For this outline, put generation, review and retained revisions inside the system boundary; treat the coordinator and consumer as external participants. This boundary is an explanatory choice, not evidence of a network or trust boundary.

Nodes are the coordinator (source), generation process, review process, retained accepted revisions (store), and consumer (recipient). Keep generation and review atomic because their internal steps do not answer the information-flow question.

The coordinator supplies the generation process with an arrow labeled “exact brief.” Generation supplies review with “candidate file bytes” and “provenance,” kept distinct so metadata cannot be mistaken for retained bytes. Review writes “accepted revision” to the retained store. The description does not specify whether that record retains the complete file bytes and provenance; leave its contents unresolved.

The consumer receives “selected bytes.” The description does not identify the process that selects and reads those bytes or explicitly establish their source. Record this as an unresolved incoming flow to the consumer. If the store is its source, the completed view needs the responsible read/selection process and the store-to-process and process-to-consumer data flows. Do not present that candidate completion as established behavior or make the store perform selection itself.

All arrows describe carried information. The outline adds no timing, network links, hosts or access rules.

# Reading the existing ER

The separate ER reading task needs `skills/diagrams-and-tables/references/er/guide.md`, especially its endpoint notation, rather than data-flow construction guidance. No redraw or renderer is needed. Preserve `ORDER ||--o{ LINE : contains` as supplied.

The `||` beside ORDER means each LINE belongs to exactly one ORDER. The `o{` beside LINE means an ORDER contains zero or more LINE entities. “contains” is the relationship label. This does not by itself establish implemented foreign keys or any additional business rules.
