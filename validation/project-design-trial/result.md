# Fieldnotes boundary review

The repository responsibilities fit the workflow. The current handoff violates archive ownership: ingest replaces accepted bytes before coordination accepts the replacement. A successful import therefore changes the notebook's selected data even when editorial review later rejects it.

## Proposed handoff

Keep coordination responsible for research questions and editorial acceptance, ingest responsible for adapters and execution logs, and archive responsible for retained originals, source identity and accepted dataset revisions. The notebook continues to consume explicitly selected archive revisions. These responsibilities do not require separate services or deployment environments.

Ingest should submit a candidate for review without replacing an accepted revision. Each submission needs enough information to connect its candidate bytes, source identity and retained original revision, transformation settings or version, and ingest job record. An execution record reports whether processing succeeded; it does not grant editorial acceptance. Candidate retention and the representation of these records remain design choices.

Coordination records acceptance or rejection against the exact candidate reviewed. Archive validates that an acceptance names that candidate and creates an accepted revision while preserving previously accepted bytes. Keep notebook selection explicit and separate from candidate production. Archive should own changes to that selection; coordination supplies the editorial decision. Confirm this selection rule in the next walkthrough because the current README does not assign its writer.

If candidate content changes after review, it needs a new identity and review. Repeating a submission or acceptance for the same candidate must not replace bytes or create an ambiguous second acceptance; the handoff should return or reference its existing outcome. An incomplete job must not publish a candidate as complete. Missing originals or unavailable editorial review leave accepted revisions and notebook selection intact, with ingest recording processing failures and coordination resolving editorial questions.

## Representative cases

Normal case: the notebook selects accepted revision A. Ingest processes a retained original into candidate B and records the job. Coordination reviews B and accepts it. Archive records B as a new accepted revision while retaining A. An explicit selection change then lets the notebook consume B; selecting A remains possible.

Rejection case: the notebook selects A while B awaits review. Coordination rejects B. Archive leaves A and its selection unchanged. Ingest can produce candidate C from corrected processing, with its own identity and job record. Repeating B's submission cannot bypass the recorded rejection.

These are proposed local walkthroughs using symbolic identities. No real jobs, approvals, recovery, concurrency behavior or storage isolation have been demonstrated.

## Next useful planning step

Have the coordination owner lead a short local walkthrough with the ingest and archive roles to settle the candidate-to-accepted-revision contract. Use the existing README and the two cases above as inputs. Produce a small example set naming the original, candidate, job, editorial decision, accepted revision and selected revision, plus who may change each. Add one repeated acceptance and one changed-candidate case.

The result is ready for implementation planning when all roles agree that rejection preserves A, acceptance identifies the reviewed bytes, repeated requests have one clear outcome, and the notebook's selected revision has a single writer. Record accepted decisions in the project's existing architecture owner and the follow-up in its planning owner when those owners are available. This fixture exposes neither owner, so this file records a proposal rather than creating a project-wide authority or queue.

This contract comes before storage implementation because storage must preserve the agreed identities and transitions. Python remains an ingest choice. Other toolchains, hosting, containers and database selection remain deferred; none is needed to resolve this boundary. Credentials and real source data remain outside the exercise.

## Separate wording request: skill selection only

For “Correct recieve to receive in a help message,” select no subject or authoring skill. The collection explicitly routes a literal wording change that preserves meaning to a focused edit check. If executed, inspect the target message, replace only the typo and verify the exact change. Project-design, clear-writing, diagrams-and-tables, project-policy and project-docs are unnecessary for that request. No help message was edited here.
