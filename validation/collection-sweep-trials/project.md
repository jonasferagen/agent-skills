# Project-foundation consumer trials — 2026-10-04

These are bounded cross-evaluation trials, not blind fresh-context trials. The
evaluator had previously reviewed and revised verification-foundation and
application-foundation. That history included source-repository maintenance
rules, Skill Creator, Clear Writing and its instruction reference, and Diagrams
and Tables. It therefore supplied reused authoring and evidence context even
though the evaluator did not author project-foundation. The three cases also ran
in one shared evaluator context: the identical collection entrypoint was read
separately for install and workflow, and the later cases could reuse earlier
context. No source-repository file or prior validation report was read during
these trials.

Entry was each fixture's `AGENTS.md` and `request.txt`. Each raw response is
captured as `ANSWER.md` in that fixture. These are evaluator records, explicitly
requested by the trial coordinator; they are the only additions to the
read-only/design-in-chat fixtures and are not installed project documentation.

## Outcomes

| Case | Outcome | Scope |
| --- | --- | --- |
| `project-install` | Explained staging, selected-source checker comparison, local-modification preservation, full replacement, provenance/routes, retained working agreements and rollback. Distinguished exact import from documented exceptions and self-check from source-pin proof. | No installation or project change performed; only raw answer captured. |
| `project-workflow` | Proposed author, intake and reviewer responsibilities. Kept technical receipt/check outcome separate from acceptance of the exact candidate revision. Placed workflow in a named process README and exchange obligations in a contract topic, with their indexes and architecture links. Walked normal completion and review rejection after successful intake. | Proposal in chat-form answer only; no project docs, diagram, implementation or migration. Unspecified criteria remained open. |
| `project-wording` | Corrected only `establised` to `established` in README. | No skill body was read; the entire README matched the expected single-word replacement. Raw answer captured separately. |

## Actual reads

Counts are approximate whitespace-delimited words from the files displayed to
the evaluator. Each listed file was displayed once in its fixture, without
truncated output. Required means the current route or task needed it; useful
means it assisted judgment without being necessary for the narrow deliverable.
No listed file was classified as irrelevant as a whole. Some broader sections in
loaded entrypoints/maps were outside the requested slice, as described below.

### Installation

Paths below are relative to `project-install/`.

| File read | Words | Classification and reason |
| --- | ---: | --- |
| `AGENTS.md` | 13 | Required: local route and read-only boundary. |
| `request.txt` | 44 | Required: exact upgrade explanation and preservation constraints. |
| `.agents/collections/project-foundation/COLLECTION.md` | 420 | Required: project-instruction discovery entry, selecting installation. |
| `.agents/collections/project-foundation/references/installation.md` | 452 | Required: selected-source comparison, complete replacement, provenance and retained working agreements. |

Displayed input subtotal: **929 words**, of which **872** were installed guidance.
The template, foundation-format, bootstrap and multi-repository links did not
apply to this requested existing-installation explanation; none were opened.
The selected-source checker command was explained, not run.

### Workflow

Paths below are relative to `project-workflow/`.

| File read | Words | Classification and reason |
| --- | ---: | --- |
| `AGENTS.md` | 31 | Required: design in chat, no files or diagrams, default document homes. |
| `request.txt` | 50 | Required: actors, documentation placement and receipt/acceptance distinction. |
| `.agents/collections/project-foundation/COLLECTION.md` | 420 | Required: selects design, contracts, document homes and authored-output route. |
| `.agents/collections/project-foundation/skills/project-design/SKILL.md` | 1,078 | Required: responsibility ownership and workflow-reference route. |
| `.agents/collections/project-foundation/skills/project-contracts/SKILL.md` | 459 | Useful: bounds handoff obligations versus architecture and leaves unspecified terms open; a full contract was not requested. |
| `.agents/collections/project-foundation/references/document-homes.md` | 1,472 | Required: exact default process, contract, index and architecture homes. |
| `.agents/collections/project-foundation/references/authoring.md` | 250 | Required by the authored-sketch route: scoped prose, uncertainty and no unnecessary visual construction. |
| `.agents/collections/project-foundation/skills/project-design/references/workflows.md` | 510 | Required: author/intake/reviewer decisions, technical completion versus acceptance, interruption and document ownership. |
| `.agents/collections/project-foundation/references/status-and-evidence.md` | 590 | Required: proposal status, unknown terms and design walkthrough limits. |
| `.agents/collections/project-foundation/skills/clear-writing/SKILL.md` | 569 | Required by the selected authoring route; its general principles were also present in inherited reviewer context. |

Displayed input subtotal: **5,429 words**, of which **5,348** were installed
guidance. The document-home map's migration, validator and shared-project details
were not needed for this narrow proposal; the full map was read to locate its
authoritative defaults. Project-design's runtime/content material was likewise
outside this slice. These are reading-cost observations, not proof of a routing
defect or a controlled efficiency comparison.

Needed deeper workflow and document-home guidance was reached. Detailed contract
design/review, models, provider selection, planning, implementation, installation,
templates and diagram construction were not needed and were not opened. No
existing local foundation, architecture, policy or contract was supplied outside
the installation. The explicit design-only task scope was sufficient for a
proposed sketch; it did not establish project phase, adopted obligations or
acceptance criteria. No policy reconciliation or adoption is claimed.

### Wording

Paths below are relative to `project-wording/`.

| File read | Words | Classification and reason |
| --- | ---: | --- |
| `AGENTS.md` | 12 | Required: literal edits preserve meaning. |
| `request.txt` | 5 | Required: fixes only one spelling error. |
| `README.md` | 8 | Required: exact source and replacement context. |

Displayed input subtotal: **25 words**, with **zero installed skill-guidance
words**. No deeper guidance was needed or missed for the requested correction.

## Verification, reuse and limits

A mechanical check compared each installed collection's 82 file hashes with its
own local manifest; all matched. This verifies fixture preservation against the
local recorded inventory, not authenticity of a source pin or behavioral quality.
The wording README was compared as a complete string with its exact expected
one-word correction and matched. Mechanical file reads for counts and hashes were
not displayed as guidance and are excluded from the displayed-input subtotals.

There were no repeated content reads within a fixture and no truncated content
read. The entrypoint was read once in each of two fixtures, so it was repeated
across cases. Earlier authoring/evidence knowledge and case context were reused;
these subtotals are neither total model context nor token use and do not measure
the cost of a fresh evaluator.

All requested distinctions appeared in the raw responses, and no material scope
violation was observed apart from the explicitly authorized evaluator capture
files. This is one evaluator run per case. It does not establish reliable native
discovery, successful adoption, correct detailed contracts, working intake,
crash recovery, live acceptance, or effectiveness across models.

## Retained requests and raw answers

The original report names temporary runtime paths. The original requests and
answers are retained below for source review.

### project-install

Request:

We want to update an existing project-foundation installation that may have local edits. Explain how to validate a staged replacement against the selected source, preserve the local changes and working agreements, update provenance/routes and keep rollback possible. Do not install anything or change files.

Raw answer:

Stage the complete replacement from one selected source revision in a separate
directory. Before replacing anything, compare the current installation with its
recorded pin and review the changed guidance and membership. Preserve local edits
and adopted working agreements: move project-specific choices to their existing
project-owned homes, or record necessary imported modifications explicitly in
provenance. Do not discard them to make the copy look clean.

Run the checker from the selected source against the staged copy:

```sh
python3 /selected/source/project-foundation/scripts/check_installation.py /staged/project-foundation
```

The checker compares the manifest and file hashes with the trusted selected
source and rejects missing, changed or extra files, undeclared members, absent
member routes and symlinks. An installed checker's self-check detects drift; it
does not independently prove the recorded source pin. Do not use `--write` to
approve consumer drift. If preserved local modifications must remain in the
import, document the exception and do not claim an exact import.

Once the staged copy is checked and local changes are preserved, replace the
whole old directory rather than overlaying it. Keep the prior pin and preserved
copy or patch available for rollback. Update `.agents/collections/UPSTREAM.md`
with the source repository, source directory, full SHA, collection version and
any release tag, and update affected project routes together. Identify an
uncommitted source as a draft with its base revision and local changes.

Remove routes to retired members such as `git-worktrees`, while retaining
adopted project worktree agreements. Run the project's link and guidance checks
after adoption. An upgrade does not itself migrate document homes, change
inherited decisions or register native client discovery. No installation or
project changes were performed here.

### project-workflow

Request:

Sketch the ownership and document homes for a workflow where an author supplies a candidate, an intake tool checks it, and a reviewer accepts it for downstream use. Say where the workflow explanation and exchange obligations should belong; keep technical receipt distinct from acceptance. No implementation or migration is requested.

Raw answer:

This is a proposed ownership sketch; it does not adopt terms or establish an
implementation.

- The author owns the candidate and its revision. They supply it with the
  information the intake agreement requires, and own any replacement after a
  correction request.
- The intake tool owns technical checking and its receipt/check outcome. It
  reports which candidate revision was received and whether the declared checks
  passed. It does not decide that the candidate is acceptable for downstream use.
- The reviewer owns the acceptance decision for that exact revision and intended
  use. Downstream users rely on the accepted revision and the applicable exchange
  terms, rather than treating a successful intake status as approval.

The workflow explanation belongs in
`project-docs/processes/candidate-intake/README.md`, linked from
`project-docs/processes/README.md` and the relevant architecture route. It describes
the trigger, participants, checking, review decision, correction loop and
completion. The architecture owner describes how these responsibilities relate;
it should link to the process rather than repeat its steps.

Exchange obligations belong in `project-docs/contracts/candidate-exchange.md`,
linked from `project-docs/contracts/README.md` and the process. They cover the
candidate's identity and revision, required submission, technical receipt,
acceptance authority and criteria, downstream eligibility, failure or rejection,
repetition and retention. One compact page can cover these exchanges; distinct
owners or independently changing terms may later justify separate contracts.
The process links these terms rather than defining another version of them.

For a normal case, the author supplies a candidate, intake records successful
checks, the reviewer accepts that revision for the intended use, and downstream
work uses that accepted revision. In an exception, intake can successfully receive
and check a candidate that the reviewer rejects. The receipt remains true;
acceptance was not granted. A changed candidate needs its own assessment rather
than inheriting the earlier decision.

No checking or acceptance criteria were supplied, so their exact terms remain
open with the exchange owner. Commands and implementation details would stay in
the responsible repository's operating documentation; actual checks and reviews
would stay in its declared work-record home. No implementation, migration,
diagram or project document was created by this sketch.

### project-wording

Request:

Fix only establised in README.md.

Raw answer:

Fixed `establised` to `established` in `README.md`. No other README content changed.
