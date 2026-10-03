# Review: timeout followed by retry

The agreement does not establish that retrying the same request after a timeout
is safe. A timeout can leave the transfer incomplete, still running or complete;
the written terms do not distinguish those outcomes or specify how to recover.

## What the current terms establish

- [Delivery](docs/agreement.md#delivery) names the request ID, immutable revision
  and receiving team, and requires the receiving team to check that identity
  before acceptance. Successful-copy evidence establishes transfer only.
- [Acceptance](docs/agreement.md#acceptance) assigns acceptance to Mira, the
  receiving coordinator, when the revision matches the requested revision and
  the receipt states that identity. A different revision remains pending; the
  sending team cannot accept it.

These terms separate transfer from acceptance. They do not describe observed
runtime behavior, and this review supplies no missing guarantee.

## Consequential missing terms

1. **Timeout outcome and reconciliation.** The first copy may complete while its
   response is lost, or remain in progress when the sender retries. Neither
   Delivery nor Acceptance defines a status lookup, retained evidence, the owner
   of reconciliation or a condition for retrying. The sender cannot rely on a
   timeout meaning failure or cancellation, or on resubmission being safe. The
   receiver cannot rely on the earlier attempt having stopped. The team owners
   need to decide how an unknown outcome is resolved and who acts before another
   transfer proceeds.

2. **Request identity across attempts and duplicate handling.** The agreement
   names a request ID but does not distinguish that request from its transfer
   attempts. If the original and retry both arrive with the same identity, the
   receiver could process both or reuse the first result without violating an
   explicit retry term. It is also unclear how conflicting content or revisions
   under one request ID are detected and handled. The sender cannot rely on a
   retry returning the existing result; the receiver cannot rely on one request
   producing only one accepted delivery. The team owners need to define the
   identity relationship and the outcome for duplicates and conflicts.

3. **Observable acceptance and preservation of earlier state.** Mira may accept
   the first delivery while the sender never receives that decision. The terms
   do not say who issues or retains the receipt, whether it records acceptance
   or only identity, how the sender learns Mira's decision, or what a retry does
   to an earlier accepted state. The sender cannot treat copy success or an
   identity-bearing receipt alone as proof that Mira accepted. The receiver
   cannot rely on the sender knowing acceptance occurred or on retries preserving
   that state. Mira and the team owners need to define acceptance evidence,
   retrieval and treatment of an already accepted request.

4. **Interrupted-copy recovery.** A timed-out attempt may leave partial output
   while the retry starts another copy. Delivery does not identify valid retained
   output, the recovery owner, or whether a retry resumes, replaces or separately
   stages that output. The sender cannot rely on a retry cleaning up the first
   attempt; the receiver cannot rely on leftover output being complete or safe
   to combine with the retry. The team owners need to define which output remains
   usable and who completes or removes incomplete attempts before acceptance.

## Evidence and scope

This document review traced incomplete and still-running transfers, a completed
copy with a lost response, duplicate arrivals, conflicting identity content, and
acceptance whose notification is lost. No runtime, provider or implementation
evidence was available. The missing decisions remain unresolved; no proposed
term was adopted, and the agreement was not changed.
