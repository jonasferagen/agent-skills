# Service-foundation consumer trials — 2026-10-04

These are design-only cross-evaluation trials using the two supplied installed
fixtures. The evaluator did not author service-foundation, but reused prior
verification/application reviewer context, source-repository maintenance and
authoring knowledge, and a preceding project-foundation cross-evaluation context.
The coordinator also named the expected scope constraints before the fixtures
were read. These are therefore neither blind nor fresh-context trials. No other
trial answer, source-repository file, live service or provider documentation was
consulted during these cases.

Each entry started with its `AGENTS.md`. The requested `request.md` did not exist
in either fixture; the failed reads returned no request content. A local file
listing found `request.txt`, which supplied the actual request. This was a
corrected input-path mismatch, not an installation or service failure. Raw
responses are captured in each fixture's `ANSWER.md`.

## Outcomes and scope

| Fixture | Observed result | Scope preserved |
| --- | --- | --- |
| `service-profile` | Rejected as-is reuse of the Supabase-bound helper for ordinary local PostgreSQL. Distinguished the reusable encrypted export/check/restore/publication method from the helper's endpoint, credential, client image and restore-startup assumptions. Proposed a reviewed project binding around those hooks, rather than changing provider or weakening target validation. | Existing provider and database credentials retained. No backup, restore, credential lookup, provider command, source modification or new framework. Proposed acceptance checks remained unexecuted. |
| `service-transition` | Used both service-boundaries and runtime-operations. Retained the existing HTTP adapter and application handler, local storage and its ownership. Defined lifecycle, maintained ownership, retention/recovery decisions and acceptance evidence. Kept the process-manager choice open and identified serviceControl as a systemd-specific implementation. | No MCP adapter, service split, deployment, container, new database or process-manager adoption. No implementation or runtime guarantee claimed. |

No material design-scope violation was observed. Only the coordinator-requested
answer captures and this evaluator record were written. The fixtures' installed
guidance and request sources were not modified.

## Actual guidance reads

Counts are approximate whitespace words from displayed input. Each listed
content file was displayed once within its fixture. Repeated mechanical reads
for counts/hashes are excluded. No displayed content was truncated. File listings,
tool errors, evaluator instructions and generated answers are not included in
these input subtotals.

### Provider-profile fit

Paths below are relative to `service-profile/`.

| File or excerpt | Words | Classification and reason |
| --- | ---: | --- |
| `AGENTS.md` | 36 | Required: chosen ordinary PostgreSQL, existing credentials and design-only limit. |
| `request.txt` | 44 | Required: as-is helper fit, smallest adaptation and no backup/source change. |
| `.agents/collections/service-foundation/COLLECTION.md` | 275 | Required: runtime route and preservation of selected provider/operating choices. |
| `.agents/collections/service-foundation/skills/runtime-operations/SKILL.md` | 1,704 | Required: backup method, explicit Supabase implementation limitation, configured scope and isolated restore guarantees. |
| `.agents/collections/service-foundation/skills/runtime-operations/scripts/databaseBackup.py`, selected excerpts | 1,037 | Required supporting code: actual credential-profile validation, configuration fields, fixed image/client boundary and disposable startup mechanics. The count includes displayed line prefixes; 212 output lines were shown. |

Displayed input subtotal: **3,096 words**. Installed guidance/code subtotal:
**3,016 words**. The helper excerpts were selected by searching configuration,
provider/pooler, credential and restore identifiers with context, rather than
loading its entire implementation. The code confirmed that configuration alone
cannot make the Supabase-bound implementation an ordinary-local-PostgreSQL helper.

The runtime entrypoint's service-control material was outside this backup-fit
question but appeared in the full skill read. Credential and child-process
constraints were relevant to preserving the existing target safely. No service
boundary, installation or companion workflow was needed.

### Maintained local-service transition

Paths below are relative to `service-transition/`.

| File read | Words | Classification and reason |
| --- | ---: | --- |
| `AGENTS.md` | 53 | Required: HTTP handler/storage baseline, continued local use and unadopted infrastructure. |
| `request.txt` | 36 | Required: maintenance ownership, lifecycle and acceptance plan without infrastructure selection. |
| `.agents/collections/service-foundation/COLLECTION.md` | 275 | Required: promotion route explicitly selects both service and runtime members. |
| `.agents/collections/service-foundation/skills/service-boundaries/SKILL.md` | 377 | Required: existing transport and application rules, caller identity, storage ownership and public-path evidence. |
| `.agents/collections/service-foundation/skills/runtime-operations/SKILL.md` | 1,704 | Required: startup/readiness/shutdown, process ownership, retained state and limits of the supplied systemd helper. |

Displayed input subtotal: **2,445 words**, of which **2,356** were installed
guidance. The collection's two-member route was followed; stopping at runtime
alone would miss public HTTP/handler and ownership obligations. The runtime
entrypoint's backup implementation details were outside this lifecycle plan.
The plan identified the helper's platform-specific fit without loading or running
serviceControl. No installation, provider selection, additional adapter or live
status-check route was activated.

## Integrity observation and limits

A mechanical comparison with each fixture's own `collection.json` failed.
Both supplied 12-file inventories have the same seven mismatching paths:

- `COLLECTION.md`
- `scripts/check_installation.py`
- `skills/runtime-operations/SKILL.md`
- `skills/runtime-operations/scripts/credentialStore.py`
- `skills/runtime-operations/scripts/databaseBackup.py`
- `skills/runtime-operations/scripts/serviceControl.py`
- `skills/runtime-operations/tests/test_runtime.py`

The evaluator did not change these files or regenerate their inventories. The
design routes used the supplied collection version `0.2.0` and runtime member
version `1.3.0`; source-pin or complete-copy integrity was not established.
The hash check is a static fixture observation, not an executed backup/helper
test or evidence of runtime failure. The coordinator was notified for final
inventory synchronization and fixture provenance.

Collection and runtime guidance were displayed separately in both cases, so
those reads repeat across the shared evaluator context. No content was reread
within a fixture; the code-excerpt search was rerun mechanically to count its
output, without redisplaying that content. Prior authoring/evidence knowledge
was reused. The reported input subtotals are neither total model context nor
token use and have no fresh-context/no-skill efficiency baseline.

No local policy, operational guide, live database profile, HTTP implementation
or adopted detailed retention/replay contract was supplied beyond the instructions
and requests. The answers retained those limits instead of inventing adoption or
verified behavior. The helper-fit answer is code-backed design advice; its
proposed adapter has not been implemented or tested. The transition answer has
not established HTTP authorization, readiness, process cleanup, persistent
storage or recovery by execution. One constrained run per case shows the observed
route only, not broad discovery or behavioral reliability.

Both entrypoint reads included sections outside the task. If repeated consumer
use shows meaningful cost, a conditional reference for backup-provider binding
or lifecycle-helper adoption could make that detail cheaper to reach. These two
trials alone do not establish a need to restructure the skill or a universal
reading budget.

## Second pass: reconciled final copies

The coordinator preserved the draft fixtures and supplied
`service-profile-final/` and `service-transition-final/` after reconciling their
inventories with the selected source. The coordinator reports both final copies
passed the trusted-source checker for 12 files and two members. The evaluator
independently compared all 12 file hashes with each final local manifest; both
matched. No source-repository read or manifest regeneration was performed by the
evaluator.

The original drift record above remains evidence about the intentionally earlier
drafts; it is not an unresolved integrity finding in these final copies. The
runtime entrypoint still declares `1.3.0`, and now explicitly covers cleanup of
the selected service unit after launch/readiness timeout, with a failed cleanup
reported separately from the primary error. Its backup cleanup description now
covers both client and rehearsal attempts, including an attached-command timeout.
Provider fit and collection routing remain as described in the initial pass.

Each final case was completed after rereading its own `AGENTS.md`, `request.txt`,
collection entrypoint and required member guidance. Raw new responses are in
`service-profile-final/ANSWER.md` and `service-transition-final/ANSWER.md`.
The final profile case also reread targeted excerpts of its own installed
databaseBackup helper rather than relying only on the prior draft's code.

### Final reads and counts

Installed paths below are relative to each final fixture's
`.agents/collections/service-foundation/`; `AGENTS.md` and `request.txt` remain
at the fixture root. Each displayed file/excerpt was read once in that fixture,
without truncation. Classification is unchanged from the corresponding first
case, and the new cleanup paragraphs were relevant to the proposed failure and
acceptance checks.

| File or excerpt | Profile words | Transition words | Classification |
| --- | ---: | ---: | --- |
| `AGENTS.md` | 36 | 53 | Required local scope and operating baseline |
| `request.txt` | 44 | 36 | Required task and permitted outcome |
| `COLLECTION.md` | 275 | 275 | Required discovery route and preservation of project choices |
| `skills/runtime-operations/SKILL.md` | 1,740 | 1,740 | Required backup-fit or lifecycle guidance |
| `skills/service-boundaries/SKILL.md` | Not read | 377 | Required only for the maintained-service ownership/public-path plan |
| `skills/runtime-operations/scripts/databaseBackup.py`, selected excerpts | 1,026 | Not read | Required supporting code only for as-is fit and binding limits; 208 output lines, including counted line prefixes |

Final profile displayed-input subtotal: **3,121 words**, of which **3,041** were
installed guidance/code. Final transition displayed-input subtotal: **2,481
words**, of which **2,392** were installed guidance. Mechanical count/hash reads
are excluded, and no source-maintenance, installation or companion catalog was
opened. These are displayed-input subtotals, not total model context or tokens.

### Final outcomes and remaining limits

The final profile answer again preserved ordinary local PostgreSQL and existing
database credentials, rejected as-is use of the Supabase-specific helper and
proposed the smallest reviewed project binding around its target/credential and
client/restore boundaries. It explicitly retained attempt-owned cleanup for both
client and rehearsal containers after timeout, without running either path.

The final transition answer again retained the HTTP adapter, application handler
and local retained state, and selected no process manager, additional transport
or deployment infrastructure. It now explicitly makes failed/timed-out
launch/readiness cleanup part of the proposed acceptance evidence and keeps a
cleanup failure distinct from the primary failure. Neither final answer claims
implemented or verified operational behavior.

Only new `ANSWER.md` captures were written in the final fixtures; their installed
files and input sources were unchanged. There were no live operations, provider
commands, installations, helper executions or source modifications. Needed member
routes and supporting provider-binding code were reached; no relevant deeper
guidance was identified as missed for these bounded design explanations.

This second pass reused both prior draft answers and all earlier reviewer context.
It is a repeated evaluation by the same evaluator, not two additional independent
or fresh cases. The coordinator's explanation of the changes was also known
before rereading. The new responses demonstrate consumption of the final supplied
bytes within the stated scope; they do not independently establish reliability
or the behavior of timeout cleanup, backup restoration, HTTP mapping, retention
or recovery. The smaller excerpt-selection pattern differs between passes, so
their totals are not a controlled reading-efficiency comparison.

## Retained requests and raw answers

The temporary fixture paths above describe the actual evaluation. The inputs
and answers below retain that evidence in the repository. Draft and final passes
are two iterations of the same cases, not four independent cases.


### service-profile


#### AGENTS.md

``````text
We use ordinary self-hosted PostgreSQL on localhost, not a hosted pooler. Preserve that selected provider and our existing credentials. Work is a design explanation only, with no commands or external actions. Use .agents/collections/service-foundation/COLLECTION.md for runtime/service work.
``````


#### request.txt

``````text
We need encrypted backups and isolated restore checks for our chosen PostgreSQL deployment. Can we reuse this collection's bundled database backup helper as-is? Explain its fit and the smallest useful adaptation while preserving our chosen provider; do not run a backup or change source.
``````


#### ANSWER.md

``````text
The bundled backup helper does not fit this deployment as-is. Keep the selected
ordinary self-hosted PostgreSQL deployment and existing database credentials.

The reusable method fits: an encrypted export, integrity and decryption checks,
an isolated full restore, project-specific snapshot/access validation, and
publication only after the checks succeed. Keys remain separate from archives;
archives, metadata and receipts stay outside Git and do not overwrite retained
files. A schema-scoped archive must not be described as a whole-system backup.

The bundled implementation has concrete provider assumptions. Its
`database_environment` requires a Supabase pooler hostname, a project-suffixed
login, port 5432 and database `postgres`. It obtains credentials and the encryption
key through the bundled 1Password item reader. Its client and restore paths use
the pinned Supabase PostgreSQL image; the restore startup also assumes that
image's user IDs and initialization layout. Changing only the hostname or image
would not establish a compatible binding.

The smallest useful adaptation is a reviewed project-owned binding around the
existing capture/check/publication method:

- Resolve the approved local endpoint, database and login through the project's
  existing credential mechanism. Validate that exact configured target; do not
  remove target checks, broaden the credentials or accept an arbitrary endpoint
  from caller input.
- Bind the client and disposable restore runtime to the selected PostgreSQL
  version and required extensions. The source client must actually reach the
  host's selected database; passing `localhost` into a separate container does
  not make it the host database. Existing native client tools may be the smaller
  binding. A restore container, if used, needs reviewed initialization and
  permissions rather than an unexamined image-name substitution.
- Configure explicit schema scope, required prerequisite roles, ownership
  preservation, snapshot/access checks, encryption-key custody and a finite
  command timeout appropriate to the archive size. Preserve isolated rehearsal:
  no production passwords, network, published port or persistent data volume,
  with cleanup restricted to the current attempt even after failed startup.

The current configuration fields alone do not replace these provider/runtime
assumptions. Adapt the specific boundary hooks or a small project wrapper rather
than creating a new provider framework or migrating the deployment to fit the
helper. Keep the selected database and existing operational credentials intact.

Before adoption, local synthetic tests should show that wrong targets and
credentials, encryption or integrity failures, restore/validation failure and
cleanup failure prevent a false success or premature publication. A disposable
restore must verify the project's actual selected schema, ownership and access
contract. Missing dependencies must be reported as missing, not as a successful
restore. These are proposed checks; no backup, restore, credential lookup,
provider command or source change was performed.
``````


### service-transition


#### AGENTS.md

``````text
Use .agents/collections/service-foundation/COLLECTION.md for service boundary and runtime lifecycle design. Work is a plan only. Existing HTTP intake calls one application handler, owns its local storage and has no MCP adapter. We now want continued local use, explicit startup/readiness/shutdown, and preservation of retained intake results. No deployment or process manager has yet been adopted.
``````


#### request.txt

``````text
Review the small intake spike before treating it as maintained local service. Give the concrete service ownership, lifecycle and acceptance decisions needed; preserve the existing transport and avoid selecting deployment infrastructure merely to finish the plan.
``````


#### ANSWER.md

``````text
Treat this as a proposed maintenance plan for the existing local intake service.
Retain HTTP intake, its application handler and service-owned local storage.
Continued use does not require adding MCP, splitting services, changing the
database or choosing deployment infrastructure.

First name the maintaining owner and the supported local operating context. Keep
the HTTP adapter responsible for request parsing, caller identity and result/error
mapping; keep the application rules and storage changes in the existing handler.
Identify which retained results and metadata are authoritative, who may release
them, and how repeat or interrupted intake is handled under the existing contract.
Unknown replay or retention terms need an explicit decision; the plan cannot
invent a guarantee that the spike has not established.

Define these lifecycle behaviors for the named intake service:

- Startup selects the intended checkout/version, configuration and retained
  storage, validates prerequisites and rejects an occupied port without killing
  its owner. An ordinary start does not enable, install or upgrade infrastructure.
- Readiness comes from this intended instance after its startup validation. A
  response from any listener on the port is insufficient. Status should identify
  the running instance and selected checkout, while logs omit secret values and
  prohibited record content.
- Shutdown stops only the owned instance and its child processes, closes active
  resources under the chosen interruption policy, and preserves retained intake
  results. An unsuccessful startup cleans up its own processes without deleting
  prior results.
- Restart deliberately applies a chosen code/configuration change and reopens
  the same retained state. Define how active intake is drained or interrupted and
  reconciled. Preserve existing execution identities and external-action gates.
  Provide explicit start, stop, restart, status and logs controls.

Do not give retained results the lifetime of a disposable preview. No process
manager has been adopted: select a lifecycle mechanism only after checking what
these local controls require. The bundled `serviceControl.py` is specifically a
Linux user-systemd implementation, with its own PID/health and cgroup contract;
using it would be a separate reviewed choice, not a prerequisite for finishing
this plan. No hosting, container, deployment or additional transport is selected.

Maintenance acceptance needs evidence for the changed reliance:

1. Trace the existing public HTTP path through identity, validation, the shared
   handler and result mapping. Cover the valid operation and relevant invalid,
   unauthorized and failure cases; preserve any established retry identity.
2. Show successful startup/readiness for the intended instance and honest failure
   for missing prerequisites, bad configuration and an unrelated port owner.
3. Show shutdown and restart preserve previously retained results, handle an
   interrupted intake according to its contract, and leave no owned stray process.
4. Identify the owner and procedure for configuration/release changes, diagnosing
   failures and recovering retained state. Record the supported environment and
   unresolved prerequisites in the project's existing operational/design owners.

Handler tests alone cannot prove HTTP mapping or lifecycle behavior. These checks
are proposed acceptance evidence; no running service, implementation, migration,
process-manager adoption or verified recovery is claimed.
``````


### service-profile-final


#### AGENTS.md

``````text
We use ordinary self-hosted PostgreSQL on localhost, not a hosted pooler. Preserve that selected provider and our existing credentials. Work is a design explanation only, with no commands or external actions. Use .agents/collections/service-foundation/COLLECTION.md for runtime/service work.
``````


#### request.txt

``````text
We need encrypted backups and isolated restore checks for our chosen PostgreSQL deployment. Can we reuse this collection's bundled database backup helper as-is? Explain its fit and the smallest useful adaptation while preserving our chosen provider; do not run a backup or change source.
``````


#### ANSWER.md

``````text
Keep the ordinary local PostgreSQL deployment and existing database credentials.
The bundled backup helper is not reusable as-is for that target.

Its general method is useful: encrypted schema export, integrity/decryption
checks, a full isolated restore with project-specific validation, then publication
without overwriting retained archives. It keeps keys separate from archives and
does not equate an archive of selected schemas with a complete deployment backup.

The implementation enforces a Supabase pooler endpoint and project-suffixed
login, obtains credentials and the key through 1Password item fields, and fixes
both client and rehearsal execution to a Supabase PostgreSQL image. The rehearsal
also fixes user IDs and initialization paths. `BackupConfig` provides schema,
validation and timeout choices; it does not replace those provider bindings.

The smallest useful adaptation is a reviewed project-owned binding at those
boundaries, retaining the capture/check/publication routine:

1. Resolve and validate the exact selected local endpoint, database and login
   through the existing approved credential mechanism. Preserve existing database
   credentials and privilege scope. Do not bypass target checks or accept an
   arbitrary connection target from caller input.
2. Bind the client and disposable rehearsal runtime to the selected PostgreSQL
   version, extensions and initialization needs. A client must reach the actual
   host database; `localhost` in a separate container is not the host endpoint.
   Existing native client tools may be the smaller binding. Do not assume that
   changing only the pinned image establishes compatibility.
3. Configure explicit schemas, prerequisite roles, required ownership, snapshot
   and access checks, encryption-key custody and a suitable finite timeout.
   Preserve rehearsal isolation: no production passwords, network, published
   port or persistent data volume. Preserve attempt-owned cleanup for both client
   and rehearsal containers, including when startup or an attached command times
   out, with cleanup errors reported separately from the original failure.

Before adoption, use synthetic failure cases to check target validation,
credential/environment isolation, encryption/integrity failure, unsuccessful
restore/validation and timeout cleanup. Then verify actual restoration and
permissions against a disposable compatible database. Missing prerequisites
remain unrun checks; a passing report must name what it exercised.

This is a binding proposal, not a new provider framework or a reason to migrate
the deployment. No backup, restore, credential lookup, provider command, source
change or operational verification was performed.
``````


### service-transition-final


#### AGENTS.md

``````text
Use .agents/collections/service-foundation/COLLECTION.md for service boundary and runtime lifecycle design. Work is a plan only. Existing HTTP intake calls one application handler, owns its local storage and has no MCP adapter. We now want continued local use, explicit startup/readiness/shutdown, and preservation of retained intake results. No deployment or process manager has yet been adopted.
``````


#### request.txt

``````text
Review the small intake spike before treating it as maintained local service. Give the concrete service ownership, lifecycle and acceptance decisions needed; preserve the existing transport and avoid selecting deployment infrastructure merely to finish the plan.
``````


#### ANSWER.md

``````text
Maintain the existing local intake service with its HTTP adapter, application
handler and service-owned storage. This proposed plan adds no MCP transport,
service split, deployment or process manager.

Name the maintaining owner, supported local environment, operating identity and
change/recovery responsibilities. Keep parsing, caller identity and result/error
mapping in the HTTP adapter; application rules and storage effects stay in the
existing handler. Identify the retained results and metadata that are
authoritative, who may release them, and the established behavior for duplicate
or interrupted intake. Leave missing retention/replay terms as decisions rather
than claims about the spike.

Define explicit start, stop, restart, status and logs controls:

- Start chooses the intended checkout/version, configuration and retained storage,
  validates prerequisites and refuses an occupied port without killing its owner.
  Readiness must come from the intended running instance after validation, not
  from any successful HTTP response on that port. Status identifies the instance
  and checkout; logs exclude secrets and prohibited record content.
- Stop acts only on the owned instance and process group, closes resources under
  a defined drain/interruption policy and preserves retained results. Failed or
  timed-out launch/readiness must clean up only that attempt's processes. Report a
  cleanup failure separately without hiding the primary startup/readiness failure.
- Restart deliberately applies the chosen code/configuration change and reopens
  retained state. Preserve established credentials, pinned settings and external
  action gates; restarting intake must not implicitly enable unrelated work.

Retained intake results do not acquire a disposable preview's lifetime. Choose a
lifecycle mechanism only after assessing these requirements. The supplied
`serviceControl.py` implements Linux user-systemd and requires its own PID/health
and cgroup identity contract. Using that helper would be a reviewed implementation
choice, not evidence that systemd has already been adopted or a requirement for
finishing this plan.

Acceptance for maintained use should establish:

1. The existing public HTTP path still carries input, caller identity, validation
   and any established retry identity to the same handler, and maps valid,
   unauthorized, invalid and failure results correctly.
2. Intended-instance startup/readiness works; missing prerequisites, bad
   configuration and unrelated port ownership fail honestly without touching
   unrelated processes.
3. Shutdown and restart preserve prior retained results and reconcile interrupted
   intake according to its contract. Timeout cleanup leaves no owned stray
   process, or reports its failure without a false successful verdict.
4. The named owner has the existing project homes for operating instructions,
   release/configuration changes, diagnosis and recovery, with unresolved
   prerequisites recorded explicitly.

Handler tests alone cannot establish HTTP mapping or lifecycle correctness.
These are proposed decisions and checks; no service was run, infrastructure
selected, storage migrated or recovery guarantee verified.
``````


## Final selected-source inventory

Both final fixtures were compared against this source inventory by the source
checker before the repeated design evaluations. The inventory identifies the
artifact and does not constitute a behavioral golden.

``````json

{
  "name": "service-foundation",
  "version": "0.2.0",
  "members": [
    "service-boundaries",
    "runtime-operations"
  ],
  "files": {
    "COLLECTION.md": "66429931f14557baf154e7ffcac3ceecdbaf0b105bdb727d2c5a369d3095352a",
    "references/installation.md": "26c041702194099c989a7d6f9b03d0ce26e04c5aad099c439875287dd419c632",
    "scripts/check_installation.py": "ab1dd5c66b2cce5d53a4d52f56f6005f5926d1118f0f457518afe74cb83b4594",
    "skills/runtime-operations/SKILL.md": "5a703c689550b1cb079643126b8d5f517ddb6b4df65c456deeed1e8942459809",
    "skills/runtime-operations/agents/openai.yaml": "58b1af26167369e5853e790b9e66fabb0c29219da14e09eb0f2ca0add8045a1e",
    "skills/runtime-operations/scripts/credentialStore.py": "4587d90a84606ae870e187ed5cad9c88e4041cbb3f3071538e49daf4b846d0b9",
    "skills/runtime-operations/scripts/databaseBackup.py": "5777907424f299f3e8dea8ea33670c26e48fdb194799e63fdc1f7660e6b6a6bd",
    "skills/runtime-operations/scripts/serviceControl.py": "c78b6c59409e7240ad8f6a31f274c84b437726559a69bac6a188b06af7157ab1",
    "skills/runtime-operations/tests/test_runtime.py": "8527227e9fef7b6e1b44a9b82b30ffe1e59e6b3365f0f2a730b196c399029989",
    "skills/service-boundaries/SKILL.md": "a7118527217c0c9481a60ea5f5eddac2f2bb06d0c3f50f1dd37b214a3eb75a85",
    "skills/service-boundaries/agents/openai.yaml": "d015c7108bf4f9784e9a3fd153faa03f077f061272a69303343ad692323d22fa",
    "tests/test_installation.py": "9b122c3655e1034b934cbe100697141edb23c6ff4278417c8aa5ff5accc2a2ec"
  }
}

``````
