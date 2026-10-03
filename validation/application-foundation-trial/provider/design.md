# Proposed first local Tools application

This is a design proposal for the synthetic `sample-sound-01`, revision 1. No implementation, provider request or generated candidate is claimed. Tools owns execution and candidate evidence; Assets owns verified receipt and creative acceptance; Game adoption remains separate. This proposal implements the supplied handoff terms without changing those responsibilities.

## One concrete operation

`generateSoundEffectCandidate(preparedRequest, explicitExecutionAuthority)` makes at most one ElevenLabs generation submission for one durable attempt, captures one MP3, and publishes a retained candidate manifest. It returns either a candidate ready for delivery or an explicit incomplete/failed/unknown attempt. Returning a retained candidate does not establish Assets custody, creative acceptance or an accepted revision.

Preparation is a separate local operation. It validates the brief, parameters, destinations and authority requirements without contacting ElevenLabs. The initial caller is a local command-line entry point; a service, queue, database and general asset store are unnecessary for this slice.

The exact text is the UTF-8 encoding of the following sentence, without backticks or a trailing newline:

`A single soft stone scrape on a dry floor, no voices or music.`

The proposed request uses `text` above and `duration_seconds: 2`. It requests one candidate containing exactly one MP3. Record the exact text bytes, their digest, supplied parameters, and explicitly omitted optional fields. Neither a model version nor an MP3 encoding is adopted in the inputs: do not invent a `model_id` or `output_format` value. Preparation can describe unresolved settings; live readiness requires an explicit decision about allowed provider defaults or verified parameter values, and how the two-second output requirement will be checked. Requested duration alone is not proof of actual duration.

Required local inputs are the brief identity/revision, exact submission choices, an explicit candidate output root, an explicit execution evidence root and the caller's execution scope. Roots must be outside original sources and accepted asset revisions. Validate resolved paths, permissions and available staging space; reject overlapping roots and escaping paths. These paths are caller configuration, not guessed production destinations. No production roots, access credentials, spending allowance or permitted real input data have been supplied.

## Cohesive responsibilities and construction

| Component | Responsibility and dependency |
| --- | --- |
| Local entry point and startup | Parse arguments; construct the operation, filesystem repository and ElevenLabs adapter; supply roots, timeouts and scoped execution configuration; own resource lifetimes and the single-writer lock. Present operation outcomes without redefining their rules. |
| Sound candidate operation | Own validation, identity rules, preparation versus submission, state transitions, the one-output completeness rule and permission to publish. Use the attempt repository and the provider-specific adapter. |
| Local attempt repository | Own durable records, exact request snapshots, append-only event evidence, staged bytes, publication and restart inspection. Keep persistence details out of the operation's decisions. |
| ElevenLabs sound generation adapter | Map the request to `POST /v1/sound-generation`; return complete response bytes with available provider evidence or distinguish known rejection from uncertain submission/capture. Own HTTP details and credential use. Disable hidden SDK/HTTP generation retries. |
| Delivery bookkeeping | Expose the complete candidate manifest and record Assets' verified receipt or explicit disposition. Delivery transport is unselected; no new receiver protocol is assumed. |

These can be a few modules in the first chosen language. No framework, registry, generic provider-job interface or dependency-injection container is proposed. The provider boundary is justified by paid external effects and its particular recovery limitations. Credentials enter only adapter construction through an approved local mechanism; never serialize them into requests, manifests, logs or raw response evidence.

An input-rule change, such as requiring a model version, belongs in preparation/operation validation and the request record. It should not change delivery ownership. A change to ElevenLabs wire syntax belongs in its adapter and mapping checks. A newly verified retrieval capability would require an explicit recovery-contract change, rather than silently turning an unknown attempt into a retriable one.

## What the provider evidence establishes

The supplied `provider-evidence.md` records an inspection dated 2026-10-03 of <https://elevenlabs.io/docs/api-reference/text-to-sound-effects/convert>. This offline proposal uses only that evidence: required text, optional duration/model/output choices, and a successful direct audio response described as MP3. It does not assume a durable job, lookup, idempotency, cancellation or recovery of lost audio. Those capabilities remain unverified, including whether any returned identifier can support reconciliation. Preserve identifiers if available, but do not assign them unsupported meaning.

Before actual execution, verify the needed current official contract, chosen model/output values, authentication setup, account entitlement, pricing/spending authority and permitted data use. These are live-execution prerequisites, not blockers to this design or local-only implementation. No remote preflight that transmits input or costs money belongs in local preparation.

## Identities, durable state and publication

Keep three identities distinct:

- Request identity: `sample-sound-01`, revision 1, plus a fingerprint of the exact generation specification. Reusing this identity with changed text or settings conflicts and requires a revised request.
- Attempt identity: a new locally generated identifier for each explicitly authorized submission. A repeated invocation with the same attempt reads/resumes local work; it never makes a second submission after the submission boundary.
- Candidate identity: allocated once for that attempt and bound to the final immutable manifest. A new attempt cannot replace earlier candidate bytes. Any provider identity is separate evidence.

Suggested storage, with both roots explicitly configured:

```text
evidence-root/
  application.lock
  requests/<request-key>/request.json
  attempts/<attempt-id>/intent.json
  attempts/<attempt-id>/events/<sequence>.json
  attempts/<attempt-id>/capture.json
  attempts/<attempt-id>/manifest.json
  attempts/<attempt-id>/receipt.json
candidate-root/
  .staging/<attempt-id>/candidate.mp3.part
  candidates/<candidate-id>/candidate.mp3
```

Records include request/attempt/candidate identities, exact wire parameters and omissions, text digest, configured roots, timestamps, execution-scope reference, relevant adapter version, supplied provider evidence/date, observed operation/model details or explicit `unavailable`, response outcome and sanitized failure details. The manifest lists exactly one retrieval location, byte length and SHA-256. Do not fabricate an actual model version from an omitted `model_id`.

The first implementation permits one writer on a local host, enforced by an exclusive process-owned lock on the configured evidence root before state mutation. All callers using a candidate root must share that evidence root; otherwise reject the configuration. Document this as a single-application local layout, not a supported multi-process/shared-storage architecture. The lock must be released by process termination; crash recovery must not delete another live process's lock. Readers consume only a published manifest.

| Durable state/event | Meaning and safe next action |
| --- | --- |
| Prepared | Local inputs recorded; readiness may have unresolved prerequisites. No provider effect. Safe to inspect or revise before freezing an attempt. |
| Intent retained | Exact frozen request and attempt identity committed. No submission marker yet: submission may begin only after readiness and authority checks. |
| Submission started | Marker durably committed before entering the HTTP call. Interruption here means potentially submitted, even if the crash occurred before the first byte left. |
| Rejected / outcome unknown | Record known rejection evidence without overstating charge semantics; timeouts, connection loss after possible transmission and incomplete audio capture are unknown. No automatic generation retry. |
| Capture retained | Complete successful response bytes, length/hash and capture completion evidence are durable. Local validation and publication may resume without a provider call. |
| Candidate ready | Final bytes and manifest are durable and agree; complete deliverable may be offered to Assets. Transfer responsibility remains with Tools. |
| Received / explicitly disposed | Record verified Assets receipt or the explicit disposition. Receipt alone does not authorize cleanup or imply acceptance. |

For each record, write a temporary file in its destination directory, flush it, atomically rename and flush the directory. Establish and verify these filesystem guarantees in the selected runtime. Keep immutable event files as evidence; a status summary is reconstructible from them.

Audio first goes to an exclusive staging path. Only a complete successful response, fully retained and hashed, can create a durable capture-completion record. A plausible-looking partial MP3 is insufficient. Validate MP3 decodability, the required output count and the adopted duration/encoding requirements before readiness; this checks technical delivery, not creative suitability. Promote bytes with a same-filesystem rename within the candidate root, then publish `manifest.json` atomically in the evidence root. Because the roots may be on different filesystems, this is ordered publication, not a cross-root atomic transaction: the manifest is the authoritative visibility point.

If interruption leaves final bytes without a manifest, compare them with durable capture evidence and resume local publication. If no completion evidence exists, retain/quarantine bytes and mark capture uncertain; do not infer success from file size. If a manifest exists but bytes are missing or mismatched, report storage/delivery failure and withhold the candidate. Never report completion before durable final bytes and their manifest agree.

Intents, events, capture evidence, candidate bytes, manifests and receipts are retained evidence. Temporary incomplete files are not deliverables but should remain until the attempt's disposition permits removal. In-memory progress and derived status can be reconstructed. No cleanup runs until a retention policy and retained evidence satisfy the handoff terms in addition to receipt.

## Trace the operation and an interruption

On the successful design path, preparation resolves prerequisites; startup acquires the lock; the operation freezes intent and commits the submission marker. The adapter makes one call, captures a complete successful audio response, and records available evidence. Tools retains and validates bytes, commits the manifest, and returns the candidate identity and complete output descriptor. Assets retains and verifies that exact file, then durably records its receipt. Tools records the receipt after matching identities, hashes and retained location. Creative acceptance remains a later Assets decision.

The consequential interruption is after the provider receives the request and before Tools retains the response. On restart, the submission marker exists but no capture-completion record does. The caller sees `outcome unknown`, the attempt ID and any available evidence; there is no candidate ready for delivery. The operation cannot distinguish never-sent from generated-and-lost using the supplied contract. It cannot recover by guessing a job ID, downloading an assumed result URL or resubmitting automatically.

Without newly verified reconciliation support, an execution owner must explicitly dispose of the uncertainty and authorize any new paid attempt within the agreed scope. Preserve the old attempt as uncertain, state possible duplicate generation/cost, and give the new attempt new identities and paths. A local stop records withdrawal; it does not establish provider cancellation or termination. If the original process still receives late bytes, retain them against its original attempt until disposition resolves their ownership.

A second interruption can occur after Assets writes its durable receipt but before Tools receives the acknowledgement. Tools still owns transfer follow-up. Repeat delivery of the same candidate/attempt and bytes using the agreed exchange, obtaining the existing receipt; do not regenerate. Changed hashes under that identity conflict. Missing or mismatched receiver bytes remain delivery failure. The receiver's durable receipt behavior is a supplied contract requirement, not implemented behavior demonstrated here.

## Smallest useful implementation and verification

Start with a local-only preparation and attempt-repository slice in the language chosen by Tools: parse this brief and explicit roots, preserve exact text/parameter choices, report readiness blockers, freeze identities, and support `inspect` on durable records. Add a fake direct-response adapter to exercise capture/publication and restart without credentials or network access. Keep its bytes and evidence explicitly labelled synthetic. This makes the persistence and decision boundary reviewable before enabling paid submission; do not claim it produces an ElevenLabs candidate.

At that boundary, meaningful checks are: exact UTF-8/no-newline preservation; changed inputs conflicting under an existing request identity; invalid/output-scope paths rejected; competing writers excluded; interruption after the submission marker causing zero automatic resubmissions; incomplete capture never publishing a manifest; local recovery after captured bytes/rename; and manifest length/hash mismatch withholding delivery. Exercise identical receipt repetition and conflicting bytes against a local receiver double, while retaining the external receipt contract as unproven.

No tests were run in this design task. These are proposed checks, not evidence. The fake cannot prove provider MP3 encoding, duration semantics, accepted parameters, authentication, prices, timeout behavior or reconciliation. Enabling the real adapter is a later increment requiring the real brief and exact output requirements, a chosen language/runtime and local durability implementation, permitted data, access and spending authority, explicit storage roots and verified current provider behavior. Delivery transport and retention policy may remain separate work, but Tools cannot claim verified custody transfer or release retained evidence before they are resolved.
