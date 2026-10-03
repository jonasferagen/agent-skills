# Proposed replacement candidate agreement

This draft replaces the proposal in [handoff.md](handoff.md), the existing handoff document. Archive owns acceptance and retained revisions; Production owns execution. Coordination continues to own briefs, and Display selects revisions to adopt. These responsibilities and retention requirements come from [foundation.md](foundation.md). This draft is proposed, not adopted or implemented.

## Production → Archive

1. **Request.** Archive supplies the requested operation, an identifier for the request, and references to the exact Coordination brief and input revisions. The request records the existing authority to execute and review. Missing inputs or authority prevent execution. Changed inputs or brief require a new request identity; reuse of an identity with different content is a conflict, not a retry.
2. **Delivery.** Production returns a candidate identity, the request and attempt identities, the exact input references, and a location from which Archive can obtain the candidate bytes. It supplies a content hash with its algorithm. Execution success means a candidate was produced; it does not mean acceptance. Production must keep the delivered bytes available and unchanged until Archive acknowledges retaining them, or report that delivery failed.
3. **Acceptance.** Archive retains and checks the delivered bytes against the hash, request, inputs and brief's acceptance criteria. An authorized reviewing agent may perform this review under existing delegation. Archive records either rejection with a reason or acceptance with a distinct revision identity linked to the verified bytes and review evidence. Missing criteria block acceptance. Archive keeps originals and previously accepted bytes; it never replaces them with a new candidate.
4. **Repeat and interruption.** A repeated request with identical content returns its recorded outcome when known. A new execution attempt requires a separate attempt identity. Timeout means the outcome is unknown. Production reconciles its attempt evidence and any available execution status before another execution is authorized; Archive does not blindly resubmit. If the outcome cannot be resolved without provider capabilities that are unknown here, the request stays unresolved and potentially duplicating work is blocked. Withdrawal is recorded separately from confirmed cancellation.
5. **Completion and adoption.** Archive's retained acceptance or rejection record completes review and is available to Production. A rejected or incomplete candidate leaves earlier accepted revisions valid. Display adoption is a separate decision selecting an accepted revision. If a brief changes while work is pending, Archive assesses the result against the new brief explicitly; the prior request and review history remain intact.

## Existing Display compatibility

Adding revision and hash fields is insufficient. Display currently saves only a path and reads it later. If that path changes bytes, Display silently changes what it shows, even if Archive's record contains the old revision and hash. There is no evidence that Display reads or checks the new fields.

A proposed transition is to provide a permanent, unique path for each accepted revision, never replacing its bytes. A path-only Display could then remain pinned to those bytes, provided its actual path handling supports this. Before rollout, verify old and new records with Display and reconcile every retained legacy path to known bytes. Where the earlier bytes cannot be established, mark that history unresolved rather than assigning a fabricated revision. Alternatively, changing Display to resolve and verify revision references requires its own implementation and migration. Neither transition is proven here.

## Paper walkthrough and open work

**Valid example:** request Q1 references brief B1 and input I1. Attempt A1 delivers C1 and hash H1. Archive copies and verifies C1, reviews it, and accepts R1. Display subsequently chooses R1. These are synthetic identifiers, not observed execution.

**Interruption example:** A2 times out while producing C2. Archive records an unknown outcome and keeps R1. If reconciliation finds C2, Archive verifies and reviews it once. A hash mismatch causes rejection, preserves R1, and returns the issue to Production. If reconciliation is unavailable, no duplicate execution is presumed safe.

Implementation still needs evidence for retained-byte protection, request/attempt reconciliation and Display compatibility. Hash algorithm, exchange representation, retention acknowledgement and status retrieval remain implementation terms to settle before use. No provider, runtime or deployment is selected.
