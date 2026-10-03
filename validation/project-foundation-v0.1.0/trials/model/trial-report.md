# Fresh consumer trial report

## Result

Completed the conceptual request in `seed-model.md`, `design.md` and `plan.md`.
The 82 percent observation is scoped to the sample from lot A. Lot B remains
untested. The revised proposal distinguishes cultivar, lot, sample and observation,
and traces hypothetical disagreement from A or B without inventing observed data.
The surrounding responsibility split remains proposed. The plan owns the missing
evidence and claim decision. No storage, general history or automation was designed.

## Actual guidance reads

Word counts are approximate whitespace counts, including headings and front matter.
Paths below are relative to `.agents/collections/project-foundation/` except the
first two project files. Each was read once in full, in this order (files in the
same command share a reading batch). “Required” means an explicit entry or workflow
route for this task; “useful” means chosen for a specific decision; “irrelevant”
means it did not help this request.

1. `AGENTS.md` — 18 words — required entry.
2. `context.md` — 28 — required project scope and owners.
3. `COLLECTION.md` — 344 — required route selection.
4. `skills/project-design/SKILL.md` — 825 — required meaning-changing design workflow.
5. `references/authoring.md` — 250 — required authored explanation guidance.
6. `skills/project-design/references/conceptual-models.md` — 357 — required selected domain meaning route; directly useful for identities, cardinalities and disagreement.
7. `skills/clear-writing/SKILL.md` — 549 — required authoring route; useful for preserving uncertainty.
8. `skills/diagrams-and-tables/SKILL.md` — 526 — required by authoring when choosing how to explain relationships; ultimately prose was sufficient for the claim-scope explanation.
9. `skills/project-planning/SKILL.md` — 645 — required because next steps were updated.
10. `references/status-and-evidence.md` — 590 — required status reporting route; preserved proposed versus observed status.
11. `references/foundation-authority.md` — 442 — useful to check that existing scope and proposed boundaries were preserved; little new task-specific information.
12. `skills/diagrams-and-tables/references/select.md` — 254 — required selected form route; helped choose brief prose rather than constructing a visual.
13. `skills/project-planning/references/next-step.md` — 299 — required next-step route; narrowed work to evidence needed for claims.
14. `references/document-homes.md` — 783 — required link from planning; only its existing-layout rule affected this task. Most canonical-home and migration detail was irrelevant to the fixture.

Total guidance and entry text: approximately 5,910 words. No entire loaded file
was classified irrelevant, but document-homes and foundation-authority had low
marginal value here. No guidance reads were repeated or truncated. A later Python
pass read these files only to count words; it did not print their content again.
Project source documents were read once before edits and once in full afterward.
No provenance, live repository, prior trial output, source-maintenance, policy,
contracts, bootstrap or renderer guidance was read.

## Output checks

- Reread all three updated documents in full and compared them to the supplied facts.
- Traced the observed A/B case: shared cultivar does not merge lots; only A has sample evidence; B's result stays unknown.
- Traced synthetic disagreement within A and across B. Sample observations retain their scope; broader interpretations and affected claims require reconsideration.
- Checked that unknown test details, proposed responsibilities and synthetic percentages were explicitly marked.
- Checked that design links to the model for detailed meanings and to the plan for next actions; the plan does not become a competing domain definition.
- A Python link check confirmed all relative document links resolve.
- Added revision 1 and the current date because the original documents had no revision convention.

These are document consistency checks, not scientific validation, implementation
verification, claim approval or publication. No statistical rule, empirical test,
legal claim standard or customer guarantee was established. No diagrams were
created, so no diagram render check applies. No managed project-docs directory
was changed, so its filename validator did not apply.

## Limits and friction

The fixture provided only a reported percentage and lot attribution; sample size,
raw counts, method, conditions, date and intended sale scope remain unavailable.
The result is a conceptual proposal sufficient to locate those missing facts and
prevent an unsupported cultivar-wide inference.

Every shell command emitted three `Failed to create stream fd: Operation not
permitted` warnings but exited successfully and returned complete requested
content. Writes and subsequent rereads succeeded. All work stayed inside this
fixture; it has no `.git` directory, and no worktree or live repository was used.
