# Equipment model

This proposal answers which physical item the desk lends and whether it can lend
that item now. Storage and general history tracking remain deferred.

## Evidence

Serial 41 and serial 42 are the same drill model, but can be loaned separately.
Serial 41 returned with a damaged chuck. Its loan closed while the desk still
listed it as available. These observations come from [the design](design.md).

## Proposed meaning

A model describes the kind of equipment. An item is the individual physical unit
that can be lent, returned or assessed independently. Each item has one model;
one model can describe multiple items. An equipment name alone cannot distinguish
serial 41 from serial 42. Their serials identify them in this example; whether
serial numbers uniquely identify every item is unresolved.

An item keeps its identity when its loan ends or its condition changes. A loan
connects one item to a borrower. Proposed constraint: an item has at most one
active loan. Group lending and retention of past loans are outside this slice.

Loan state answers whether the item is currently on loan. Condition answers
whether the workshop considers it fit to lend. These are independent facts.
Availability is the desk's decision that the item can be lent now: it requires
no active loan and workshop confirmation that the item is fit to lend. Damage
or unknown condition prevents availability under this proposal. Other possible
restrictions, such as reservations, have no evidence here and remain outside scope.

## Damaged-return test

Closing serial 41's loan changes its loan state, not its identity or drill model.
The damaged chuck means it fails the proposed fitness requirement, so the desk
must consider it unavailable even after closing the loan. The workshop owns the
condition assessment; the desk owns the lending decision. Serial 42 remains a
separate item: serial 41's damage does not establish serial 42's condition or
availability.

Synthetic continuation: if the workshop later confirms serial 41 is fit to lend,
and it has no active loan, the desk can consider it available. No repair or
clearance was observed. The exact condition handoff remains open in
[planning](planning.md); this walkthrough does not prove implemented behavior.
