# Application foundation trial setup

Date: 2026-10-03. Three independent subagents with no forked conversation context
worked in separate consumers under `/tmp/application-foundation-trial-vq7ilgo3/`.
Each fixture had its own complete, unmodified copies of application-foundation
and project-foundation from agent-skills commit
`fa0d3bb537b6dbc51b0cdf943d8cf9c78e700d1f`. No language, runtime or testing packages
were installed. No live Forge repository was changed.

Entry was a project-instruction hook, not explicit skill invocation or native host
discovery. Each evaluator was told to read `AGENTS.md`, then `request.md`, perform
the task using only its fixture, and record actual reads, approximate whitespace
words, repetitions, truncation, reused context and limits. It was not given the
intended route or expected design. Network, source-repository access, other fixture
access and live service effects were excluded. Evaluators could write the requested
output and read log only. The receipt evaluator later received a reminder to keep
the proposal bounded, with no implementation or extra scenario suite; no proposed
answer or finding was supplied.

## Retained artifacts

Each case retains its request, project context, supplied inputs, provenance,
result and read log. `project-instructions.txt` is the exact fixture `AGENTS.md`,
renamed so this archived snapshot does not govern work in the authoring repository.
Its relative installation links describe the original fixture. Installed collection
copies are reconstructed from the pinned commit rather than duplicated in this
archive. The [collection hashes](collection-hashes.json) identify every file of the
application-foundation candidate; final package content matched these hashes.

To reconstruct a case outside this repository, copy its supplied files into a fresh
directory, restore `project-instructions.txt` as `AGENTS.md`, and install both
collections at `.agents/collections/<name>/` from the pinned commit. Restore
`UPSTREAM.md` under `.agents/collections/`. Exclude `design.md` and `reads.md` from
the evaluator's initial fixture. The wording case's original README sentence was
`This tool recieve candidate files.`; its retained README is the corrected result.

| Case | Raw inputs | Result |
| --- | --- | --- |
| Provider execution | [Request](provider/request.md), [context](provider/project.md), [brief](provider/brief.md), [provider evidence](provider/provider-evidence.md), [handoff](provider/handoff.md) | [Design](provider/design.md), [reads](provider/reads.md) |
| Local receipt | [Request](receipt/request.md), [context](receipt/project.md), [delivery](receipt/delivery.json), [handoff](receipt/handoff.md), synthetic bytes in `receipt/inputs/` | [Design](receipt/design.md), [reads](receipt/reads.md) |
| Literal wording | [Request](wording/request.md), [context](wording/project.md), original sentence above | [README](wording/README.md), [reads](wording/reads.md) |

The provider facts are a bounded paraphrase of current official documentation,
with the source and date in the fixture. The input text is synthetic. The receipt
payloads are fabricated text bytes with real computed hashes, not project assets.
Handoff terms are supplied fixture obligations informed by Forge's proposed
exchange, not adoption of that exchange in live repositories.

The parent compared every initial fixture file with its SHA-256 inventory after
the trials. Only the requested README sentence changed. Added files were exactly
the requested designs and read logs; installed guidance remained byte-identical.
The parent inspected both designs and all read records. These checks establish
fixture integrity and bounded design behavior, not execution or provider guarantees.
