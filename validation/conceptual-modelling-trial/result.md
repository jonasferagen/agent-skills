# Lending desk clarification

The proposal distinguishes an equipment model from each independently lent
physical item. It also separates loan state from workshop-owned condition.
The desk may consider an item available only when no loan is active and the
workshop confirms it is fit to lend.

The observed return tests this distinction: serial 41 remains the same drill
item after its loan closes, but its damaged chuck prevents availability.
Serial 42 is independently assessed. A later clearance is a synthetic example,
not an observed repair.

Updated owners:

- [Equipment meaning](docs/equipment-model.md): identities, relationships,
  proposed availability rule and damaged-return walkthrough.
- [Design boundary](docs/design.md): desk decision and workshop assessment.
- [Open work](docs/planning.md): condition handoff and identifier assumptions.

This is a conceptual proposal. It does not establish working software or an
adopted operating contract. Storage, automation and general history remain deferred.
