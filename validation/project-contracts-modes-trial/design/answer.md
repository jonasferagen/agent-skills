# Publication handoff — proposed revision 2

Date: 2026-10-03. Proposal for adoption in `exchange.md`; revision 1 remains authoritative. This synthetic design authorizes no distribution or partner contact.

## Purpose and participants

Editorial decides whether a package matches the article revision. Publishing assembles and retains packages and coordinates delivery. Photograph owners control their independent permissions. A designated rights coordinator records permission and withdrawals; assignment of this role remains open. Distribution partners must agree to downstream obligations before participation under the proposal.

Example: package P contains article A and photographs X and Y. Editorial can accept P while a later withdrawal of X makes future distribution impermissible. Earlier lawful deliveries remain lawful. The agreement must preserve both facts.

## Proposed terms

1. **Identity and retained results.** Each candidate records its request identifier, article revision, agreement revision and exact attachment identities and versions. Publishing preserves its acceptance or rejection. Repeating the same request with identical input returns its existing candidate; conflicting input under that identifier is refused. Changed input uses a new request. A rejected candidate never replaces an accepted package.

2. **Separate acceptance and permission.** Editorial acceptance means content matches the specified revision and all specified attachments are present. Publishing reports this as “content accepted.” It does not establish distribution permission. The rights coordinator must record permission for every photograph covering the intended recipient, use and time, with its source and effective period. Missing or disputed permission blocks readiness. Publishing must check current eligibility before each delivery; partners must check before further distribution, including from caches.

3. **Delivery evidence and completion.** Publishing records intended recipients, exact package, delivery identifier, attempts and per-partner outcomes. Receipt acknowledgment is separate from permission or a promise to distribute. Report partial and unknown outcomes explicitly. “Distribution complete” requires an agreed recipient scope and completion rule, still open. Editorial acceptance alone cannot establish that milestone. Retained packages may remain accepted for content while blocked for future distribution.

4. **Withdrawal propagation.** The rights coordinator records authenticated withdrawals, affected photographs, scope and effective time. Publishing identifies affected packages, stops affected future deliveries and sends restrictions to all recorded partners. Partners stop future distribution from their caches and propagate restrictions to downstream recipients they supplied. They acknowledge receipt of the notice separately from confirmation of enforcement. Publishing tracks missing confirmations and escalates them to the designated business decision owner. A sent notice does not prove that a partner has stopped distribution.

5. **Historical copies.** A withdrawal does not reverse historical content acceptance or make previously lawful deliveries unlawful. Possession of a lawful historical copy does not by itself authorize sending another copy. The parties must define how public cache access, downloads and redelivery count as future distribution. Pending resolution, the proposed default is suspension of ambiguous future delivery actions. No deletion of lawful historical copies is implied. Duration and permitted access for retained packages and evidence remain open.

6. **Races and failures.** A withdrawal effective before dispatch prevents affected dispatch. Preserve timing and permission evidence to assess deliveries near the effective time. Uncertain ordering remains unresolved and blocks further affected delivery pending reconciliation. A timeout means unknown outcome, not confirmed failure: consult partner delivery evidence before retrying. Use the same delivery identifier for retries where the partner supports duplicate detection; otherwise resolve duplicate risk before resending. Withdrawal does not prove cancellation of in-flight delivery. Reconcile its outcome under the agreed effective-time rule. A failed notice or unreachable partner remains an open enforcement failure, with an owner and escalation; do not claim universal withdrawal compliance.

7. **Replacement.** Removing or replacing a photograph creates a new candidate, request identifier and explicit attachment list. Editorial accepts the new package against the intended article revision; rights readiness is checked separately. Neither a replacement nor its failure restores permission for the old package. Partners receive explicit replacement identity and the old package’s restriction status.

## Business decisions required

- **Business owner and photograph owners:** nominate the rights coordinator and agree proof of permission, withdrawal authenticity, scope and effective time. This blocks authoritative eligibility decisions.
- **Business owner, rights coordinator and partners:** define future distribution, cache access, in-flight deliveries, uncertain timing and downstream reach. This blocks precise enforcement and dispute resolution.
- **Publishing and partner owners:** agree how eligibility is checked, maximum propagation delay, acknowledgment deadlines, evidence, escalation and remedies when a partner cannot stop distribution. This blocks admission of such partners and claims of complete enforcement.
- **Editorial and Publishing leads:** define intended recipients, partial completion, service targets and who accepts unresolved failures. This blocks an overall distribution-completion claim.
- **Business owner with Publishing:** decide retention duration, access and permitted archival use for packages, permissions and delivery evidence. Revision 1’s retention obligation remains effective meanwhile.

These are proposed decision owners; no partner commitments have been verified or adopted.

## Transition and readiness

Revision 1 reports completion after Editorial acceptance. Revision 2 tightens obligations by adding separate rights and distribution decisions. Editorial and Publishing must adopt the new milestone meanings, and partners must explicitly accept their applicable obligations. Preserve old records and their agreement revision; old acceptance is not proof of current rights or downstream completion.

Before activation, Publishing inventories retained packages and known recipients, links photographs to permission history, identifies missing evidence and establishes partner restriction and acknowledgment procedures. The business owner resolves the open decisions. Required readiness evidence covers a valid delivery, withdrawal through a partner cache, replacement and an uncertain delivery outcome. Packages with incomplete evidence remain unverified for future distribution.

The affected areas are responsibility, retained records, partner interfaces, authority, recovery, documentation and verification. No implementation, deployment or live-account work is authorized here; their capabilities remain uninspected. Keep final adopted terms in exchange.md, with procedures owned by participants. This proposal does not modify the adopted agreement.

## Synthetic exercises

**Valid:** Editorial requests article A with X and Y. Publishing returns P and its attachment identities. Editorial accepts content. The rights coordinator confirms permission for partner B’s intended use; Publishing checks eligibility and records B’s receipt. Both milestones are visible. Overall completion still depends on the selected recipient and completion rule.

**Withdrawal after delivery:** B lawfully receives P; X is then withdrawn effective at T. Publishing blocks future delivery and notifies B. B stops new distribution from its cache and confirms enforcement. P’s historical acceptance and lawful delivery remain recorded. If B does not respond, downstream enforcement remains unresolved and is escalated. A replacement with Z needs a new request, acceptance and rights decision.

**Timeout and rejected replacement:** Delivery times out while withdrawal becomes effective. Publishing marks its outcome unknown, reconciles partner evidence and does not resend P. A replacement missing Z is rejected without replacing the accepted package. The retained accepted package nevertheless remains blocked for future distribution.

These examples establish design consistency, not operational compliance.
