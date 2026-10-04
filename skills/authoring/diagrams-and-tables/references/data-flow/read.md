# Read a data-flow view

Identify the declared system boundary, scope and observed/proposed status. Follow
its legend. External entities are sources or recipients relative to that boundary;
processes transform information; stores retain it. A person or agent can perform a
process without being a running service.

A flow carries the named information. Its direction does not by itself establish
execution order, permission, network connectivity or organizational ownership.
Distinguish file bytes, metadata and references: a URL does not prove retention.
A store does not itself approve or convert data. If a transfer hides the responsible
process, report the abstraction or ambiguity rather than inventing implementation.

Our illustrative Mermaid convention uses rectangles for external entities, rounded
nodes for processes and cylinders for stores. This is a collection convention,
not a claim of formal Yourdon/DeMarco or Gane–Sarson notation. Other views may use
different symbols; their stated notation takes precedence.

A context view may represent the whole system as one process. Detail opens it while
preserving its external flows. A trust boundary needs an explicit meaning; a folder,
repository or company border alone does not establish enforcement. A data-flow view
alone does not prove security properties.

Reading and prose outlines need no layout, examples or renderer search. Use
[semantic review](../review.md) to assess accuracy or the [family guide](guide.md)
when constructing a view. Official sources are linked from that guide when needed.
