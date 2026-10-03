# Assets context

Assets owns receipt of candidate bytes and the later creative review. Tools owns
execution and retains its delivered candidates until verified receipt. This fixture
opens only Assets' local receipt operation. General asset revision machinery,
selection, database storage and Game adoption remain deferred. No implementation
language has been selected. No external provider is called by this operation.

The fixture has one local host and explicit input and retained-output roots. There
is no existing lock or record store. Agents can invoke the command from different
shells; decide how the first implementation handles that circumstance. Keep the
proposal scoped to receipt of one output set.

Use handoff.md and delivery.json. Bytes and identifiers in this fixture are made
up; they are not real project assets or evidence of an implemented handoff.
