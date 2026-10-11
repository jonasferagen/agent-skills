# Document claim homes — independent fixture review, 2026-10-11

Clear-writing 0.5.0 and source-of-truth 3.2.0 were tested from the task revision based on `dd506d4d9b03e0e10ed58a5d4d8d0c708fd7ab22`. Complete copies of both packages were installed in an otherwise independent fixture at `/tmp/document-authority-trial`. The evaluator selected omission, existing-answer links, bounded upkeep and preservation of contract/evidence qualifiers before dispatch, using the scenarios on the two skill validation pages.

The agent had no inherited conversation history. Entry was a supplied project-instruction hook and the exact installed metadata below; this was not host discovery or spontaneous activation. The agent received no expected answer and was forbidden to read the authoring repositories or validation records. The exact task was:

> Review the documentation in /tmp/document-authority-trial for clarity and consistency. Start from its AGENTS.md and follow the installed guidance. This is a read-only fixture review: return the revised passages you recommend, preserving useful meaning and assessed evidence; do not edit files or real repositories. Record the files actually read, approximate whitespace words for those reads, repeated/truncated reads and any needed guidance missed. Do not read the authoring repositories or their validation records. Retain your review and read log in /tmp/document-authority-trial-review.md. Return a concise result with the artifact path. You are a fresh agent with no inherited task history.

## Evaluator assessment

The retained replacements omit both incidental “no release” claims, point to the existing listing, and name the keeper's two existing maintained homes and update trigger. They retain the loader's missing hash verification, the consumer refusal obligation and unresolved support as different claims. The dated import-only result and its unattempted cases remain unchanged. No new status owner, release page, consistency gate or authority was introduced. All preselected behavior criteria passed in this fixture.

The reported read set reaches both entrypoints, instruction-writing guidance and source-of-truth definitions. Shared-value, runtime-boundary and check-design references are unnecessary for these removals. The read log is agent testimony, not an independently captured tool trace; read-based conclusions and context savings remain unverified. This single broad case does not prove reliability. A nearby literal-spelling task was reviewed only as an informed author trace: preserve its narrow scope and operational qualifiers without adding ownership or status machinery. No release tag was made.

Source verification passed: `python3 -B scripts/check.py` completed four checks with 45 tests and no skipped suites, and `git diff --check` passed. These checks establish package/helper integrity, not prose freshness or selection reliability.

## Present-content clarification — 2026-10-11

Jonas subsequently requested the present-content principle for generic
documentation, preserving deliberate history/planning records. Clear-writing
0.6.0 supplied that boundary. Project-bootstrap's second independent adoption
of it moved histories from role definitions and implementation entrypoints, but
left the current roles index's adoption/relocation narrative. The distribution's
adoption route named overviews and keeper entrypoints, leaving the index route
implicit. Clear-writing 0.6.1 explicitly names current indexes and registers
within the same intended boundary, preserving keys, aliases, retirement lookup,
required adoption basis and evidence identities. This is a wording clarification;
the distribution owns the expanded adoption review and its fresh trial.

An informed author trace applies the boundary to a roles index: retain current
rows and stable aliases, move migration narrative to an existing dated record,
and keep current maintenance instructions with a pointer. A retired-key row and
a dated decision record remain valid in their own purpose. This trace is not
independent discovery or adoption evidence. The original fixture above tested
claim selection, not this later clarification; the distribution retains its
separate downstream trial assessment.

## Exact fixture input

### `AGENTS.md`

```markdown
# Library documentation fixture

Use the installed clear-writing skill for authored prose. For repeated definitions or changing prose claims, use the installed source-of-truth skill. Read only the references needed for the task. Domain documentation is owned by the Library keeper; its entrypoint is docs/keeper.md. Preserve supported behavior, obligations, unknowns and the assessed conditions of dated evidence. Work here is a read-only review; return revised passages and a read log.

## Installed skill metadata

- clear-writing — Draft or edit explanatory and instructional prose for clarity, including technical explanations, documentation, skills, project instructions and concise labels. Preserve the requested voice, factual meaning and level of certainty. Entry: .agents/skills/clear-writing/SKILL.md
- source-of-truth — Reconcile a rule, vocabulary, shape or changing prose claim defined in several places. Use when copies drift, a change requires coordinated edits, or a consistency check needs to survive restructuring. Entry: .agents/skills/source-of-truth/SKILL.md
```

### `README.md`

```markdown
# Widget library

The library supplies models for application props. No release has been made yet. Start asset work at [the keeper](docs/keeper.md). Read [integration](docs/integration.md) before using a model. Available revisions are listed on the [releases page](docs/releases.md).
```

### `docs/keeper.md`

```markdown
# Library keeper

The keeper publishes models and maintains their integration guide and release listing. No model is released yet. Update docs when models change. Consumers own renderer configuration.
```

### `docs/releases.md`

```markdown
# Releases

The keeper maintains this listing when a revision is published or withdrawn. Published revisions: widget/r1. This page owns availability; integration.md owns supported consumer behavior.
```

### `docs/integration.md`

```markdown
# Integration

Load an exact asset revision. The current loader checks that the model can be imported but does not verify manifest hashes. Consumers are required to refuse a missing manifest or a hash mismatch. Consumer support for that requirement remains unresolved. Renderer configuration belongs to the consuming application.
```

### `result-2026-10-10.md`

```markdown
# Trial result — 2026-10-10

Revision 0123456 loaded widget/r1 successfully. The trial checked model import only; no hash-mismatch or missing-manifest case was attempted.
```

## Retained independent output

# Library documentation fixture review

Reviewed `/tmp/document-authority-trial` as a read-only fixture. The fixture and real repositories were not edited. This review recommends four prose replacements and retains the dated trial record unchanged.

## Findings and authority decisions

The README and keeper page each say that no release exists, while `docs/releases.md` lists `widget/r1`. The release page explicitly owns availability. Remove the two incidental status claims and keep their links to that page; do not replace them with another release snapshot.

The integration guide distinguishes an import check from manifest-hash verification, requires consumers to refuse a missing manifest or hash mismatch, and leaves consumer support unresolved. Those facts answer different questions and must all remain. The successful import in the dated trial does not establish support for either refusal case.

The keeper page also repeats the renderer-configuration rule. Keep that rule in the integration guide and let the keeper page direct readers there. Keep the keeper's publishing and maintenance responsibilities, including the existing model-change trigger, and make the actor explicit.

| Concept | Authoritative home | Evidence and recommended treatment |
| --- | --- | --- |
| Which revisions are available? | `docs/releases.md` | Its `widget/r1` listing conflicts with the two “no release” claims. Stop at source-of-truth rung 1: remove the restatements and link to the listing. |
| Who owns renderer configuration? | `docs/integration.md` | The keeper page repeats the same rule. Stop at rung 1: retain the integration rule and replace the keeper's copy with a reference. |
| What must consumers refuse, and what support is known? | `docs/integration.md`, maintained by the keeper | Preserve the requirement, loader limitation and unresolved consumer support separately. No competing definition needs consolidation. |
| What did the trial assess? | `result-2026-10-10.md` | Preserve the date, revision, model and import-only scope. This is assessed evidence, not a statement of current availability or validation support. |

The prose links share a medium with their homes, so no generation, boundary workaround or consistency check is needed for these recommended removals. Publication or withdrawal triggers updates to the release listing; the keeper's existing model-change instruction governs affected documentation. The revisions do not introduce an additional maintenance requirement.

## Recommended replacements

### `README.md`

```markdown
# Widget library

The library supplies models for application props. Start asset work at [the keeper](docs/keeper.md). Read [integration](docs/integration.md) before using a model. Find available revisions on the [releases page](docs/releases.md).
```

This preserves the entrypoint and the instruction to read integration before use, while removing the stale release snapshot.

### `docs/keeper.md`

```markdown
# Library keeper

The keeper publishes models and maintains their [integration guide](integration.md) and [release listing](releases.md). When models change, the keeper updates the affected documentation.

Use the release listing to find available revisions. Read the integration guide for consumer requirements, supported behavior, unresolved support and renderer responsibilities.
```

This names the maintenance actor and points to each answer's home. It removes the stale release snapshot and the independent renderer-rule copy.

### `docs/integration.md`

```markdown
# Integration

Load an exact asset revision.

The current loader checks whether the model can be imported. It does not verify manifest hashes.

Consumers must refuse assets with a missing manifest or a hash mismatch. Consumer support for this requirement remains unresolved.

The consuming application owns renderer configuration.
```

The paragraph breaks separate use, observed loader behavior, consumer obligations and renderer responsibility. The wording does not imply that the loader checks for a missing manifest or that consumers meet the refusal requirement.

### `docs/releases.md`

```markdown
# Releases

This page owns revision availability. The keeper updates the listing when a revision is published or withdrawn. For consumer requirements and supported behavior, read [Integration](integration.md).

Published revisions:

- `widget/r1`
```

This makes the existing authority and update trigger easier to find, links directly to integration, and retains the published revision.

### `result-2026-10-10.md`: retain unchanged

```markdown
# Trial result — 2026-10-10

Revision 0123456 loaded widget/r1 successfully. The trial checked model import only; no hash-mismatch or missing-manifest case was attempted.
```

There is no concrete clarity defect that warrants rewriting this record. Its assessed conditions and unattempted cases remain explicit.

## Verification and limits

Compared every recommended replacement with the fixture source for actors, conditions, obligations, technical distinctions and certainty. The dated trial remains unchanged. No implementation behavior was tested, and no successful hash-mismatch or missing-manifest refusal is claimed. The fixture declares no project checker. No authoring repositories, their history or their validation records were read.

## Read log

Paths below are relative to `/tmp/document-authority-trial`. Counts approximate whitespace-delimited words and include Markdown syntax. All content reads were complete.

| Order | File actually read | Words | Purpose |
| --- | --- | ---: | --- |
| 1 | `AGENTS.md` | 142 | Fixture scope, entrypoint, evidence preservation and installed skill routes. |
| 2 | `.agents/skills/clear-writing/SKILL.md` | 690 | Selected authoring guidance. |
| 2 | `.agents/skills/source-of-truth/SKILL.md` | 641 | Selected consistency and authority guidance. |
| 3 | `.agents/skills/clear-writing/references/instructions.md` | 506 | Preserve instructional conditions, actors and rule strength. |
| 3 | `.agents/skills/source-of-truth/references/definitions.md` | 1,508 | Select prose claims and homes; choose removal over restatement. |
| 3 | `docs/keeper.md` | 29 | Required domain entrypoint and owner. |
| 4 | `README.md` | 36 | Overview, entrypoint and duplicated release claim. |
| 4 | `docs/integration.md` | 49 | Current behavior, obligations, unknowns and renderer rule. |
| 4 | `docs/releases.md` | 26 | Availability home, published revision and update trigger. |
| 4 | `result-2026-10-10.md` | 23 | Dated import-only evidence and unattempted cases. |
| | **Total** | **3,650** | |

- Repeated content reads: none. The word count for `AGENTS.md` was calculated from its already-returned text, without rereading the file.
- Truncated reads: none.
- Failed attempts: two initial `python` commands failed because that executable was unavailable; neither read a file. The subsequent `python3` reads succeeded.
- Filename inventory: `rg --files` listed the six non-hidden fixture Markdown paths; this was not a content read.
- Needed guidance missed: none identified. The short-text reference was not needed for these explanatory passages. The shared-value, boundary and check-design references were not needed because the review proposes no shared configuration value, cross-runtime derivation or retained check.
- No source content outside the fixture was read. The only file written was this report.
