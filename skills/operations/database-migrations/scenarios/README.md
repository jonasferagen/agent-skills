# Database migrations scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Cases

| Request and context | Expected behavior |
| --- | --- |
| Review a migration runner without containers | Inspect order, ledger, checksums, atomicity, bounded locking and failure behavior without requiring container tooling. |
| An applied migration was edited | Reject the unexplained history mismatch; do not mark later migrations successful. |
| A migration fails after changing a table | Roll back transactional work and its ledger entry, or use documented recovery for a nontransactional step; do not mark success. |
| Two runners start together | Verify serialization through independent sessions and bounded failure. |
| Platform objects are unavailable locally | Declare bootstrap prerequisites or a reviewed baseline with provenance; retain the original history. |
| A baseline is used to mark all original migrations successful | Reject the fabricated history; record the baseline and the history it replaces explicitly. |
| An empty database test passes | Do not claim a supported upgrade preserves existing rows without exercising that state. |
| Embedded tests pass under a privileged connection | Keep actual login, contention and unsupported server features unverified. |
| An embedded engine lacks a required extension | Select compatible native tests or disclose the gap; do not transform SQL silently. |
| Establish a development database before a full test suite exists | Checked-in setup, canonical migrations and a repeatable synthetic seed; normal migration and seed operations stay separate from destructive reset, and whether repeated seeding is idempotent is declared. |
| A reset is requested for retained development data | Retained development data is not a reset target; the data's disposability is established first. |
| Change one migration | Select evidence for the migration and affected starting states; do not automatically run every runner test. |
| Change only a container image | Container tooling is the relevant task; do not redesign migration history. |

## Limits

- All cases are author-reviewed; no independent agent trial or live database
  test has run for this package.
