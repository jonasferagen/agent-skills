# Single source of truth scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use does not read them. Record observed results
with the change that ran them, not here. All examples are synthetic.

## Finding the owner and selecting a revision

| Request and context | Expected behavior |
| --- | --- |
| A vocabulary is enforced by a service's database constraint and mirrored in its application | The service's constraint decides admitted values; derive or check the application representation against the selected schema. No other service's private database becomes a dependency. |
| A consumer pins a published schema at revision A while the publisher releases B | A is an intentional adoption, not automatic drift. Verify the installed artifact and consumer behavior against A; evaluate any support or compatibility policy separately. |
| A generated contract is checked into a consumer with source revision and digest | Recognized as valid derivation. Publisher checks generation against the selected source; consumer checks adopted bytes and behavior. No routine sibling checkout read. |
| The consumer edits an imported contract without recording the change | The adoption is ambiguous; record the local modification and its owner, or restore the selected publication. |
| A source investigation needs to explain a generator defect | Read authorized publisher inputs for that investigation; do not turn that access into a permanent prerequisite for consumer checks. |
| A consumer's gate compares its pin with the publisher's latest branch | Reject the equality gate as a generic SSOT remedy. Preserve adoption independence and name any explicit upgrade or compatibility policy. |
| Two version pins differ across independently released consumers | No forced convergence merely from difference; identify adopted contracts and explicit integration obligations. |
| A list holds every member of an adopted vocabulary | Treat as a mirror that needs derivation or parity, not a policy. |
| A list deliberately treats some vocabulary members differently | Treat as an owned policy with a reason, not a complete mirror. |
| A boundary validates more strictly than storage | Identify a separate narrowing policy and its reason instead of claiming exact parity. |
| Two similar lists answer different questions | Compare their meanings and owners before unifying them. |
| One constant is used several times in one module | No independently maintained duplication. |
| A stable constant has many uses while a growing vocabulary is copied across media | Prioritize the growing concept's silent failure risk over copy count. |
| Neither derivation nor automated agreement is practical | Record copies, owners, update triggers and the consequence of a missed update. |

## Crossing boundaries

| Request and context | Expected behavior |
| --- | --- |
| A rule has different spellings in two languages | Derive from a selected structured source or compare normalized representations; retain independent examples to check conversion meaning. |
| A proposed fix imports server dependencies into a browser | Preserve the boundary; consider a dependency-free publication, generated client artifact or request delivery. |
| Only a type crosses a bundle boundary | Check runtime erasure and declared build dependency; erasure does not erase repository adoption responsibilities. |
| Processes hardcode deployment addresses in shared code | Supply resolved settings through explicit inputs from the deployment or configuration owner. |
| Two deployment declarations must agree and no shared source is in scope | Compare the explicitly selected deployment inputs, or record coordination risk; local checks do not discover private live configs. |
| An application wants another service's private table to mirror a vocabulary | Use that owner's published contract, API, event or export; private-table inspection is not the default SSOT remedy. |
| A vocabulary would become rows read by a PostgreSQL check constraint | Explain the subquery restriction and distinguish a schema redesign from duplication cleanup; follow migration authorization. |
| An integration suite declares two selected service versions | Exercise their public interfaces for compatibility and report selected revisions separately from local package checks. |
| A fallback turns an unknown code into an empty label | Require exhaustiveness or explicit failure where the adopted contract requires completeness. |
| A protocol explicitly permits values unknown to an older consumer | Preserve deliberate tolerance, state its obligation and test the unknown case. |
| A fixed label ignores the stored value | Identify silent false output and prefer an accurate less specific derived answer when available. |

## Shared values, structured contracts and prose

| Request and context | Expected behavior |
| --- | --- |
| A package name appears in docs, generated config and prompts | Identify its owning declaration, derive required literals and retain historical evidence with the value it actually used. |
| A loader does not expand placeholders | Reject a placeholder as derivation; supply or generate a literal, or check maintained agreement. |
| Behavior tests parse a Markdown contract table | Prefer an existing structured contract or validated extraction publication; record source revision and keep consumers on their selected artifact. |
| A document links to a moving branch | Permit it for browsing current material, but reject it as immutable adoption provenance or historical evidence. |
| A document's vocabulary is stale against the revision it describes | Remove an unnecessary copy or reconcile the needed explanation with that selected contract. |
| Overviews repeat incidental release status | Remove snapshots; do not create an inventory merely to relocate them. |
| Release availability determines a reader's next action | Link the authoritative listing directly with enough context. |
| Necessary prose is manually maintained | Identify a bounded scope, owner and update triggers; supporting documents point there. |
| A requirement demands validation the loader does not perform | Preserve the requirement and observed gap as separate facts. |
| An old acceptance report names a passing revision | Preserve its revision and conditions as historical evidence. |

## Checks and independent evidence

| Request and context | Expected behavior |
| --- | --- |
| A parity check states a third literal list | Reject that list as parity evidence; compare the selected representations. |
| A behavior test states a literal expected result | Preserve it as an independent oracle, not a fragile structural golden. |
| A generator deterministically produces the same wrong label as the implementation | Generation parity does not establish meaning; retain an independent behavioral example that can reveal the error. |
| A check compares a fresh file count with a hand-maintained current baseline | Read the selected manifest instead; distinguish such baselines from immutable dependency pins. |
| A publisher is offline but a consumer's required pinned artifact is present | Run local adoption checks; upstream availability is not a new requirement. |
| The pinned artifact required for a local check is missing | Fail that required check with a missing-dependency explanation, not disagreement or success. |
| An optional integration service is unavailable | Report that integration was not measured; a prominent skip is not evidence of compatibility. |
| A relevant check runs only manually or behind an environment variable | Preserve the evidence of a run but report absent gate coverage. |
| A new check has only passed | Introduce a representative disagreement, observe the expected failure and revert it. |
| A shrink-only ledger lists known debt | Accept only a bounded local ledger that rejects new or increased violations and may only shrink. |
| Inventory comes from the caller's working directory | Anchor to the check's owned root or explicit input, scope the query and report the measured root and set. |
| A check copies a build-directory list | Read the selected build declaration rather than maintaining another list. |
| A check's tests require a neighboring checkout or private live database | Fabricate an isolated tree and publication; integration environments remain explicit separate subjects. |
| A report has no stated reader or action | Identify its decision and owner before retaining it; do not claim gate prevention. |
| Unrelated changes can trigger the check's failure | Narrow the inputs or justify the proxy against the missed-defect cost. |
| A scanner hard-codes a workspace's private repositories | Keep local enforcement with each owner and integration selection explicit. |
| Whether a retained check earns its cost | Leave the decision to the project while applying durability requirements to checks kept. |

## Project conventions and limits

| Request and context | Expected behavior |
| --- | --- |
| Applying the skill in an existing project | Existing project conventions take precedence; no rename, schema change or upgrade is implied. |
| A requirement raises the consequence of inconsistent copies | Revisit affected appearances and checks, record unmet obligations and distinguish requirements from observed support. |
| No consequence is stated | Assess how disagreement fails, state the assumption and ask when cost is unclear. |

Document-authoritative extraction is a described design option, not a bundled
worked implementation. These scenarios specify expected behavior; they do not
establish independent routing acceptance or live compatibility.
