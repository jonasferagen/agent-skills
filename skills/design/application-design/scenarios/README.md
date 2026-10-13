# Application design scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Cases

| Request and context | Expected behavior |
| --- | --- |
| Design one external generation operation against a provider API | Reach the integration guidance. Keep a retained local submission marker distinct from proof that the provider received the request; treat the submission outcome as unknown after a lost response, resubmit nothing automatically, retain the returned bytes, and leave acceptance of the result to its separate owner. Lookup, cancellation, idempotency and recovery of lost output stay unverified until exercised. |
| Design a local candidate-receipt operation over the filesystem | Own publication and acknowledgement without provider mechanics or creative acceptance: verify the complete set, publish bytes with receipt metadata before acknowledging, handle a repeat receipt and a conflict, and exclude a competing local writer. Storage and durability choices are proposals until runtime evidence exists. |
| Change one sentence of an application's README literally | Make the edit without an application-design pass. |
| A proposed identity pairing interprets a handoff term | Marked as a proposed interpretation needing confirmation, not a newly adopted meaning. |
| A path-resolution example stands in for an implementation contract | Named as an example; the exact resolver contract is still owed before it is relied on. |

## Limits

- The cases are document trials in isolated fixtures. They cannot establish
  working adapters, storage durability, provider retry guarantees or native host
  discovery.
- Not exercised: a pure read-only application operation, an HTTP or MCP
  adapter, a second provider, or a language-specific implementation.
