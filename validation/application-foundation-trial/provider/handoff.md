# Candidate handoff terms for this synthetic design

Tools delivers a candidate identity, attempt identity and the complete expected
output set. Each output has a retrieval location, byte length and SHA-256. An
expiring provider URL alone does not meet Tools' retention obligation.

Assets acknowledges only after retaining and verifying the complete set. A receipt
records the candidate/attempt identities, hashes and retained location. Receipt
must survive loss of the acknowledgement response. Missing bytes or a mismatch is
a delivery failure, not receipt. A repeated delivery with the same identity and
bytes returns the existing receipt; changed bytes under that identity conflict.

Receipt establishes custody, not creative acceptance or a selected revision.
Cleanup requires retention policy and retained evidence in addition to receipt.
Tools keeps transfer responsibility until verified receipt or explicit disposition.
