# Read record

All paths below are relative to `/tmp/application-foundation-trial-vq7ilgo3/provider`. Work was limited to this fixture. Counts are whitespace words from `wc -w`; punctuation and Markdown tokens count as words. A content read means the complete file was displayed to the model, distinct from a byte-level mechanical word count.

## Instruction and context reads

| File | Words | Content reads | Classification and reason |
| --- | ---: | ---: | --- |
| `AGENTS.md` | 87 | 1 | Required: requested first read; defines fixture isolation, local context and available routes. |
| `project.md` | 129 | 1 | Required: AGENTS directs this read; supplies Tools/Assets/Game ownership, first environment, explicit roots and execution limits. |
| `.agents/collections/application-foundation/COLLECTION.md` | 157 | 1 | Required for the selected route: identifies application design and its external integration reference as the route for this operation. |
| `.agents/collections/application-foundation/skills/application-design/SKILL.md` | 748 | 1 | Required by that route: operation rules, collaborators, construction, durable state, recovery and a smallest increment directly answer the request. |
| `.agents/collections/application-foundation/skills/application-design/references/external-integrations.md` | 580 | 1 | Required by the skill for an external provider: constrains paid submission, uncertain outcomes, response retention and effectful retries. |

Instruction/context total: 1,701 words. No instruction file actually read was classified irrelevant. The useful material was required by the chosen route; no additional optional guidance was read.

## Supplied task and artifact reads

| File | Words | Content reads | Use |
| --- | ---: | ---: | --- |
| `request.md` | 52 | 1 | Read immediately after AGENTS; requested design scope, interruption trace, output filename and prohibition on generation. |
| `brief.md` | 96 | 1 | Exact synthetic text, request identity/revision, duration, MP3/count/hash requirements and unselected settings. |
| `provider-evidence.md` | 118 | 1 | Dated bounded provider facts and explicit unknowns; used instead of accessing its external link. |
| `handoff.md` | 131 | 1 | Candidate manifest, durable receipt, duplicate delivery, custody and cleanup obligations. |

Supplied artifact total: 397 words. Total distinct supplied content read: 2,098 words across nine files.

## Generated artifact read and mechanical checks

| File or check | Size/read count | What actually happened |
| --- | --- | --- |
| `design.md` | 2,012 words; 1 complete content read after creation | Read back for scope, consistency and coverage. Its drafted text was already present in generation context, so this was a verification reread of generated material, not new source evidence. |
| All nine supplied files above | One additional mechanical pass each; 2,098 words collectively | One `wc -w` command counted bytes/tokens without redisplaying their contents. |
| `design.md` | One additional mechanical pass; 2,012 words | `wc -w` counted the generated design after read-back. |
| `reads.md` | One mechanical word-count pass; no subsequent complete content display | Counted after writing this record. The draft itself was already in generation context. |

No tests, provider probes, filesystem durability experiments or implementation execution were performed. No directory listing or search read additional fixture files. File creation used `apply_patch` only for the two requested output files.

## Repetition, truncation and reused context

Every supplied file had one full semantic read and the single count-only pass noted above. Tool output was not truncated. `project.md` and `brief.md` shared one `cat` invocation; `provider-evidence.md` and `handoff.md` shared another. All other semantic file reads were individual. Tool output limits did not omit material.

Previously displayed source contents were reused from conversation context throughout drafting; they were not reread semantically. The delegated task and inherited conversation instructions were also available as context, including fixture-only/offline scope and the requirement for this read record. They are not filesystem reads, so no invented file/word count is assigned to them. No previous design, source-authoring repository, other trial fixture or network content was used.

## Routing, limits and constraints

The application collection, its design skill and its provider reference were present. No required guidance dependency was missing. Language/runtime/testing packages are deliberately absent according to AGENTS; no language-specific implementation was attempted. The project-foundation collection was not opened because existing ownership and handoff were supplied and preserved, with no project-wide responsibility or contract change proposed. Installation and source-maintenance routes were not relevant to the requested design.

Preserved constraints: offline work; design only; no generation, credentials or paid calls; exact synthetic text and two-second/one-MP3 intent; explicit future storage roots; no writes to original sources or accepted revisions; separate execution, custody and creative acceptance; no invented provider recovery features. The supplied dated evidence governed this offline proposal even though live execution would require current official verification. No supplied input or installed guidance was modified. No task-constraint violation was observed.

Only `design.md` and this read record were created. The design includes proposed local modules, preparation/submission separation, state/publication rules, interruption recovery, handoff bookkeeping and a local-only first implementation step. Unresolved real brief, exact encoding/model/duration policy, runtime, storage configuration, data/access/spending authority and live-provider behavior remain visible prerequisites. Observable output is a proposal, not validated production behavior.
