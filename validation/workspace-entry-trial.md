# Fresh workspace entry consumer trial

Date: 2026-10-03. Isolated fixture: `/tmp/workspace-entry-trial-eubvnyhh`.

## Outcome

Starting at exposed `AGENTS.md` was sufficient to find Primary, the installed collection, and Tools instructions. For a future change to Tools operating circumstances, the appropriate workflow is `forge/.agents/collections/project-foundation/skills/project-policy/SKILL.md`. Primary owns shared policy; Tools declares inheritance for Boundaries, Overview and Policy and supplies local role, integration and data facts. Local facts do not automatically override shared decisions. A real change would review affected facts and downstream requirements, record its impact in owning work notes, and keep implementation/readiness evidence distinct. No actual policy change was requested or performed.

For a task confined to `unrelated/`, Forge policy does not apply merely through filesystem ancestry. Root instructions explicitly exclude unrelated directories; `unrelated/AGENTS.md` independently confirms no adoption. Root AGENTS plus that local file are sufficient for this scenario (about 207 words).

## Actual content reads

Paths are relative to the fixture. Counts are whitespace-delimited words, approximately indicating reading cost; repeated automated inspection is excluded from this unique-content total.

| Path | Words |
| --- | ---: |
| AGENTS.md | 189 |
| forge/AGENTS.md | 48 |
| forge/.agents/collections/project-foundation/COLLECTION.md | 523 |
| forge-tools/AGENTS.md | 99 |
| forge/docs/foundation.md | 417 |
| forge-tools/docs/foundation.md | 173 |
| forge/.agents/collections/project-foundation/references/foundation-format.md | 803 |
| forge/docs/working-agreements.md | 439 |
| forge/.agents/collections/project-foundation/references/multi-repository.md | 684 |
| forge/.agents/collections/project-foundation/references/foundation-authority.md | 440 |
| forge/.agents/collections/project-foundation/skills/project-policy/SKILL.md | 1219 |
| unrelated/AGENTS.md | 18 |
| README.md | 193 |
| forge/docs/architecture/README.md | 465 |
| **Total unique content** | **5710** |

The symlink targets `forge/workspace-entry/AGENTS.md` and `forge/workspace-entry/README.md` were also read programmatically to verify byte identity and extract routes. Their content duplicates root reads (382 words). During collection absence, root and member AGENTS were reread programmatically (288 words). Total content accessed including these checks was approximately 6380 words. Directory listings and path discovery did not read further document bodies.

No real repository or source skill repository was read. No bootstrap, authoring, worktree, source-of-truth, policy-changes, archived README, planning, or setup document body was loaded. Those workflows were unnecessary for finding the future workflow. The collection and policy skill contain some installation/establishment material irrelevant to this consultation; no action followed that material. Architecture was useful for checking role authority. No required guidance was missed for the requested routing decision. Future substantive work would need the conditional policy-change guidance and affected owners, which this trial intentionally did not assess.

## Filesystem checks

- Root `AGENTS.md` is a symlink to `forge/workspace-entry/AGENTS.md`; root `README.md` points to `forge/workspace-entry/README.md`. Both targets existed and had identical bytes through exposed and tracked paths.
- All three Markdown routes in root AGENTS and all twelve in root README resolved to existing paths when based at the workspace root. This includes archive and setup paths; existence checks did not read their bodies.
- Both tracked source files explicitly specify workspace-root resolution, including when read directly. Applying that stated base works. Naive Markdown resolution relative to `forge/workspace-entry/` fails for all prefixed routes (the README link to AGENTS is the one exception). This is a documented consumer convention, not native source-directory Markdown link portability.
- Tools References binds `forge` to this fixture's Primary. Appending the foundation-format route reaches the same installed guidance read above. Shared foundation inheritance is explicit.

## Missing dependencies, simulated and restored

Temporarily renamed only `forge/.agents/collections/project-foundation` to `project-foundation.trial-hidden`, then restored it in a `finally` block. Root and member missing-guidance hooks remained readable; unrelated instructions remained available. A fresh consumer must report the missing collection, defer workflow-dependent decisions and preserve known constraints while continuing unrelated authorized work. The experiment did not substitute cached guidance or historical documents as authority.

Temporarily renamed the entire fixture `forge/` to `forge.trial-hidden`, then restored it in a `finally` block. Root AGENTS and README remained symlinks but became unreadable because both targets are inside Primary. Therefore the root missing-owner hook cannot be discovered by a new consumer through that broken entry. Tools AGENTS and unrelated AGENTS remained readable, so direct member entry still supplies a missing-authority hook. This is an actual limitation of locating both exposed entry targets inside the unavailable Primary. An already-informed consumer retains known constraints; the archived README is not a fallback and was not read.

Final checks confirmed restored Primary, restored collection, readable root AGENTS, and no leftover temporary hidden directories.

## Limits

This checked filesystem routing and a human/agent interpretation of explicit instructions. It did not test automatic client instruction discovery, browser rendering, containers, actual Git task-worktree entry, runtime readiness, or policy implementation compliance. No live actions, repo edits, or new architecture were performed. The only lasting write is this report. An initial shell launch failed before any read; explicit `/bin/bash` with fixture workdir succeeded.
