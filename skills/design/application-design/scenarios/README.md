# Application design scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Cases

| Request and context | Expected behavior |
| --- | --- |
| Design one operation that submits a job to an external provider API | Reach the integration guidance. Keep a retained local submission marker distinct from proof that the provider received the request; treat the submission outcome as unknown after a lost response, resubmit nothing automatically, retain the returned bytes, and leave acceptance of the result to the receiving side. Lookup, cancellation, idempotency and recovery of lost output stay unverified until exercised. |
| Design an operation that receives uploaded files into a local directory and acknowledges them | Own publication and acknowledgement without provider mechanics or a quality judgment: verify the complete set, publish bytes with their record before acknowledging, handle a repeated upload and a conflicting one under the same name, and exclude a competing local writer. Storage and durability choices are proposals until runtime evidence exists. |
| Change one sentence of an application's README literally | Make the edit without an application-design pass. |
| The design proposes that an order ID and an external payment reference identify the same thing | Marked as a proposed interpretation needing confirmation from the agreement between the two systems, not a newly adopted meaning. |
| A worked example resolves a relative path, and the design cites it as the rule | Named as an example; the exact resolution rule is still owed before code relies on it. |

## Limits

- The cases are paper traces against synthetic fixtures. They cannot establish
  working adapters, storage durability or provider retry guarantees.
- Not exercised: a pure read-only application operation, an HTTP or MCP
  adapter, a second provider, or a language-specific implementation.
