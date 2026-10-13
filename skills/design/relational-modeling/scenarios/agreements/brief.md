# Agreements fixture

Synthetic inputs for the first two cases in [the scenarios](../README.md).
Everything here is made up.

## Brief

Known entities: organisation, agreement, service.

Retrieval questions:

1. Which agreements involve a given organisation?
2. Which service does each agreement cover?

Participant roles and relationship cardinalities have not been decided. Use a
small provisional model to reason about the questions; identify assumptions and
blocking choices rather than asking an external owner during this bounded
exercise. Names and identifiers in examples must be synthetic. Do not infer an
application stack, interface, schema implementation or operational permission.

Produce a small database model proposal with a canonical ER view, a domain
glossary and retrieval scenarios. Organize the documents so the next reader can
find their owners. This is a design exercise, not adoption for a real project or
a runtime test.

## Correction

Deliver this only after the first model exists:

> An agreement may cover several services. An organisation's participant role
> may differ for each service covered by that agreement.

Expected: coverage becomes an agreement/service association; role meaning
becomes organisation + agreement + service in model and glossary; scenarios keep
distinct results per agreement and prevent role facts leaking across agreements
that share a service. Missing coverage, simultaneous roles and the meaning of a
missing role may remain open, named as such.
