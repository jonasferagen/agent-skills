# Exhibit-image operating design

Date: 2026-10-03 · Revision: 1 · Status: proposal for review

## Decision and authority

Recommend a manual, local first operation once a real brief, source and suitable local capability are established. Use it to learn the acceptance criteria and handoffs before considering a remote service. This document proposes procedure; it does not adopt policy, select infrastructure or authorize execution.

[Foundation](foundation.md) already assigns Coordination the brief and creative decisions, Imaging execution and candidates, Archive originals, accepted revisions and deliveries, and Display presentation adjustments. It requires retaining originals and prior accepted revisions. Cloud use and spending remain unauthorized. Existing reviewer delegation applies; this proposal adds no mandatory human approval. Storage, serialization and the first real brief/source are unknown.

## Representative request and completion

**Synthetic example only:** request EX-01 asks for an exhibit image from original O-01 revision 1 under brief B-01 revision 1. The proposed brief would identify intended use, permitted changes, visual criteria, dimensions, format and Display constraints. These values must be supplied for real work; none are inferred here. Example IDs indicate linked records, not real assets, approvals or successful jobs.

Completion has three distinct decisions: Imaging establishes that an operation returned a usable candidate; Coordination or its delegated reviewer accepts its creative fit; Display accepts a particular archived delivery for presentation. Archive verifies and records the delivery's identity and fidelity to the accepted revision. A job success or a creative approval alone does not complete consumer review.

## Proposed route through owners

1. **Coordination opens the request.** Record EX-01, exact brief revision, required source identity, intended Display use and authorized scope. Coordination resolves missing creative criteria. Display supplies presentation constraints before execution where known. Agents may prepare these records within existing delegation; their preparation grants no additional authority.
2. **Archive supplies the source.** Resolve O-01/r1 and make the designated input available without overwriting the original. Archive confirms identity and source availability. Imaging verifies it can read the supplied input and meet the requested output contract. Missing permission, source or capability holds the operation at this step.
3. **Imaging prepares and executes.** Identify attempt A-01 against EX-01, B-01/r1 and O-01/r1. Before execution, establish the local tool, actual version and relevant settings, writable candidate destination and how records survive interruption. Imaging writes candidates and execution records; it cannot write creative acceptance or replace Archive's accepted revisions. Record result C-01, settings, completion evidence and any limitations. A partial or corrupt file stays ineligible for review.
4. **Coordination reviews C-01.** Its reviewer records the exact candidate and brief/source revisions, decision and reason. Acceptance applies only to that match. Rejection returns reasons to Imaging or triggers a clarified brief; it does not change accepted archive material.
5. **Archive registers and delivers.** Following recorded creative acceptance, Archive creates accepted revision R-01 linked to C-01 and its review, then delivery D-01 linked to R-01 and the requested output specifications. Archive verifies the delivered bytes/artifact correspond to the accepted result and specification, preserving the original and all earlier accepted revisions. Conversion that materially changes the result returns to creative review.
6. **Display reviews D-01.** Record selected delivery identity, presentation adjustments and consumer outcome. Display owns these adjustments; it does not rewrite R-01 or the creative decision. A suitable delivery is recorded as adopted for the intended presentation. A presentation problem goes to Display; incorrect delivery goes to Archive; a changed creative need goes to Coordination.

These are proposed transitions: brief ready → input ready → operation pending → candidate available → creatively accepted → archived/delivered → consumer adopted. Each arrow requires its owner's evidence above. Rejection and unknown execution outcome are separate branches. “Ready” here remains a design condition, not a claim about available software.

## Smallest useful records and state

Use a short request sheet and linked review/delivery records initially. Record identities and revisions, owner, permitted inputs/writes, attempt and candidate references, actual tool/settings, outcome and reasons. Exact format and paths are deferred until the first operation needs them; a database or universal API is unnecessary.

Coordination is authoritative for briefs and creative reviews. Imaging is authoritative for execution evidence and candidates. Archive is authoritative for originals, accepted revisions and deliveries. Display is authoritative for consumer selection and presentation adjustments. Records link those decisions rather than creating competing copies. Responsibility boundaries do not imply separate repositories, processes or deployments. No owner needs a service merely to keep a record.

Authored briefs, originals, reviews, accepted revisions and delivery/selection records are durable work. Candidate retention and execution-record lifetime are unresolved. For the trial, preserve them through review and recovery; do not authorize their deletion here. Caches and scratch can be disposable only after the responsible owner establishes that no sole output or recovery evidence remains there. Original and prior accepted revision retention is already mandatory.

## Local first versus later remote service

| Decision dimension | Manual/local first | Later remote service |
| --- | --- | --- |
| Quality and artifact fit | Unverified; test a chosen real brief | Unverified; compare representative results |
| Reproducibility | Capture tool, version and settings | Also capture provider operation/model/configuration |
| Review | Existing creative and consumer owners | Same acceptance owners |
| Data exposure and authority | Confirm local input/output scope | Requires explicit cloud/data/spending authorization |
| Recovery | Inspect local outputs and execution record | Requires evidence for job lookup, unknown outcomes and retry effects |
| Cost and effort | Measure operator time and tool costs | Measure charges, latency, support and integration effort |
| Packaging | Manual procedure initially | Direct calls or service only if measured needs justify them |

The local recommendation is a proposed learning sequence, not evidence that local tools can perform the request. Remote use becomes worth evaluating if the local trial shows a concrete quality, throughput or operator-effort gap. A persistent service would additionally need demonstrated coordination or unattended-operation requirements; multiple possible tools alone are insufficient.

## Settle now and gate later choices

For this proposal, settle the owner handoffs, distinct acceptance decisions, revision linkage, retention of adopted material and conservative handling of unknown outcomes. Before treating these new procedural details as adopted, record the relevant decision through the existing project authority. This review does not demand a new human approval role.

**Next proposed task:** Coordination selects a real brief with measurable criteria; Archive identifies its source; Display states intended-use constraints. Imaging then performs an authorized local capability preflight and proposes one bounded candidate operation. Evidence needed: readable input, suitable local tool, known write locations, captured actual version/settings and a result reviewable by Coordination and Display. No commands, capabilities or recovery behavior have yet been verified.

**Remote evaluation gates:** first establish a measured unmet need and authorized data/execution/spending scope. Then Imaging evaluates current authoritative provider documentation and terms for artifact support, quality constraints, model/version configuration, retention/deletion, credentials, cost, lookup, retry/idempotency, cancellation and partial results. Unknown support is a selection blocker when required for safe recovery. Credentials belong in the chosen secure runtime mechanism, never request records or Git; that mechanism is still unselected.

Remote use would change exposure and retained-state/recovery obligations. Before adoption, the project decision authority must resolve those facts and their consequences; Imaging owns execution safeguards, Archive owns retention/delivery effects and Display checks compatibility. Preserve open requirements until evidence exists. A future bounded authorized experiment must demonstrate normal completion, interrupted response reconciliation and the same creative/delivery/consumer checks. Do not infer paid retry safety from a local test. Provider, version, transport, storage and deployment remain unselected.

## Walkthroughs

**Normal example:** B-01/r1 and O-01/r1 reach Imaging as A-01; it returns C-01 with execution evidence. A delegated creative reviewer could accept C-01 for that exact brief/source. Archive would register R-01 and deliver D-01 after verifying correspondence. Display would record its review and selection of D-01. Each action is simulated; no acceptance or adoption actually occurred.

**Rejected candidate:** Coordination rejects C-01 because the hypothetical focal subject is wrong. Imaging diagnoses whether the output diverged from the recorded brief; Coordination diagnoses ambiguous creative instructions. Preserve B-01/r1, O-01/r1, C-01 and rejection evidence for follow-up. If the brief stands, a new A-02 yields a separate C-02 for review. Previous accepted revisions remain valid. Rejection authorizes no new tool scope, spending or cleanup.

**Changed brief:** Coordination issues B-01/r2 with a different intended crop. The earlier approval, if any, remains historical evidence for r1 and does not authorize r2. Coordination and Display assess reuse against r2; Archive retains previous accepted material. Imaging receives a new attempt linked to r2 if changes are needed. Even if C-01 is reusable, record a fresh assessment against r2 before Archive creates the new accepted association/delivery. A late r1 result stays attached to r1 and cannot silently become r2's output.

**Interrupted remote response, hypothetical only:** A future authorized attempt RA-01 is submitted with a stable request reference and available provider job identifier recorded durably. The connection ends without a result. Imaging records “outcome unknown,” retains the exact brief/source/configuration and submission evidence, and stops automatic resubmission. A timeout proves neither failure nor cancellation. Imaging uses documented lookup/reconciliation, within the authorized scope, to find the original operation. A confirmed completed job may supply a candidate; a confirmed failure may permit a new attempt if retry effects and authority are established. If lookup is unavailable or ambiguous, keep the attempt unresolved and obtain evidence before another potentially chargeable/write-producing submission. Do not invent idempotency or cancellation support. Coordination may withdraw interest, but Imaging separately records whether provider cancellation was confirmed. Late or partial outputs remain candidates tied to RA-01; no creative acceptance or archival overwrite follows automatically.

## Review result and limits

The normal, rejection, revised-brief and interruption traces preserve owner boundaries and distinguish execution, creative acceptance, delivery verification and consumer adoption. This establishes internal design consistency only. Feasibility, quality, tool commands, durable writes, isolation, actual recovery, spending behavior and real acceptance all remain unverified. The existing foundation is unchanged; no proposed procedure has been silently promoted into adopted policy.
