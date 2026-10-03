# Existing candidate handoff

Proposal: Production returns a file path to Archive. If the request times out,
Archive submits the request again. Archive marks the returned file accepted when
Production reports success. The file path may later hold updated bytes.

An existing Display consumer stores only the file path and reads it on demand.
A proposed new handoff adds a revision identifier and a content hash.
