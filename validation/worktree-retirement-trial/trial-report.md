# Fresh bootstrap consumer trial

## Scope and result

Project: `/tmp/foundation-retirement-ze2ehjtx/project`.
Collection: `/tmp/foundation-retirement-ze2ehjtx/project-foundation` (existing sibling installation).

Established a minimal documentation foundation for a household equipment inventory. Storage and interface remain undecided. Treated the project as independent because no shared project or parent authority was supplied; the shared collection supplies guidance only.

Outputs:

- `project/AGENTS.md` — preserves British English and notes location, adds operating summary, reference lookup, missing-owner behaviour and task routes.
- `project/docs/foundation.md` — five required sections, collection root bound once, empty inheritance, project purpose, implementation unknowns and six policy axes.
- `project/README.md` — foundation and instruction entry links.

No Git repository, dependencies, application code, source-repository edits or external writes. No worktree was needed because the target is outside Git. No review note was needed: there was no observed obstacle or workaround. This trial report is the requested external evidence record.

## Instruction and template reads

Counts are whitespace-delimited words in complete tool-visible file content, including Markdown. Each file was read once for instructions; none was truncated. Counts below are measured after the trial, using the saved initial AGENTS text for its entry. Counting those files again with Python did not expose their content to the model and is excluded from instruction rereads.

| File, relative to project | Approx. words | Instruction reads | Truncated | Reason |
| --- | ---: | ---: | --- | --- |
| `AGENTS.md` | 21 | 1 | No | Required: task entry and existing working agreements. |
| `../project-foundation/skills/project-bootstrap/SKILL.md` | 1104 | 1 | No | Required: task selected bootstrap and its output rules. |
| `../project-foundation/references/foundation-format.md` | 803 | 1 | No | Required: strict foundation schema and shared reference lookup. |
| `../project-foundation/templates/docs/foundation.md` | 189 | 1 | No | Required: adapt foundation scaffold. |
| `../project-foundation/templates/README.md` | 8 | 1 | No | Required: adapt README scaffold. |
| `../project-foundation/COLLECTION.md` | 313 | 1 | No | Required: bootstrap directs use of complete collection and routes. |
| `../project-foundation/references/authoring.md` | 248 | 1 | No | Required: bootstrap directs authoring guidance. |
| `../project-foundation/skills/project-policy/SKILL.md` | 683 | 1 | No | Required: bootstrap directs initial policy assessment. |
| `../project-foundation/skills/project-docs/SKILL.md` | 838 | 1 | No | Required: bootstrap directs reader routes. |
| `../project-foundation/references/foundation-authority.md` | 458 | 1 | No | Required: bootstrap directs consultation and conflict rules. |
| `../project-foundation/skills/clear-writing/SKILL.md` | 549 | 1 | No | Required by authoring guidance: wording and certainty. |
| `../project-foundation/skills/clear-writing/references/instructions.md` | 506 | 1 | No | Required by authoring guidance: agent instruction wording. |
| `../project-foundation/skills/project-policy/references/establish.md` | 377 | 1 | No | Required by policy establishment route: axes and unknowns. |
| `../project-foundation/skills/project-docs/references/structure.md` | 688 | 1 | No | Required by docs skill: document homes and reader routes. |
| `../project-foundation/skills/project-policy/references/requirements.md` | 217 | 1 | No | Required by establishment reference: identify missing decisions. |
| `../project-foundation/skills/project-policy/references/writing-policy.md` | 352 | 1 | No | Required by establishment reference: policy shape and checks. |

Total instruction/template words: **7354** across **16** files. No repeated model-visible instruction reads. All read files were required by the invoked workflow and useful for its prescribed output; no irrelevant file was intentionally loaded. The instruction load is larger than the resulting project documentation.

## Output checks (separate from instruction reads)

- `git rev-parse --show-toplevel`: failed as expected because this fixture is outside Git. Initial listing found only AGENTS.md.
- Ran the installed `scripts/validate-foundation.py` against `docs/foundation.md`: **format valid**. Script executed; its source was not read as guidance. The validator's internal reads are outside the model-visible instruction log.
- Read all three generated files in full for review: AGENTS.md 330 words, README.md 18 words, foundation.md 213 words (561 words total). No output review was truncated.
- Python checked all Markdown file links and heading anchors, all collection route target files, the format route anchor, absence of template delimiters, trailing whitespace and a local `.git` directory: **passed**.
- These mechanical checks reread generated documents and read heading text from target documents internally without displaying it; those are output checks, not additional instruction consultations.
- Collection file enumeration found 63 files. No collection contents were copied or modified.
- Reviewed claims against the request: no stack, persistence mechanism, interface, deployment, access model or recovery guarantee was selected. Policy uncertainty does not claim compliance.

## Limits and next decision

No Git diff check was available because the project is intentionally outside Git; a direct trailing-whitespace check passed. No application or operational checks apply because no tool was implemented. Link checks establish local accessibility, not policy truth or operational compliance. Collection route targets were checked for existence; unrelated skill bodies and all source-authoring materials remained unread.

Next unresolved choices are storage and interface. Users, data sensitivity and replaceability, exposure, compatibility, expected lifetime and recovery needs remain unknown and must inform later design. No choice blocks this documentation bootstrap.
