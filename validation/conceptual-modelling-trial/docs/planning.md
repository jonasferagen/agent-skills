# Planning

Conceptual clarification complete as a proposal: [the equipment model](equipment-model.md)
separates item identity, model, loan state and condition. Its damaged-return
walkthrough explains why closing serial 41's loan must not make it available.
Implementation and operational validation have not been performed.

Open questions before implementing lending decisions:

- Desk and workshop: agree how the desk receives and accepts a current condition
  assessment, including a return with damage or an unavailable workshop. Use the
  observed return as input; completion means the owners can explain when the
  desk may consider the item available without inferring fitness from loan closure.
  This blocks implementation of reliable availability, not this conceptual proposal.
- Desk: confirm how physical units are distinguished if serial numbers are missing
  or repeated. Review representative inventory before selecting an identifier;
  completion means each independently lent item can be identified unambiguously.

Storage, automation and general history tracking remain deferred until a concrete
operation requires them.
