# Prose styles

Draft. A collection of writing styles worth reusing, with real examples. Not a
skill yet; one may grow out of it once a style has been used in a few places.

Each style says where it fits and where it doesn't, because no single style
suits everything. Examples are kept as written at the time, even when the thing
they describe has changed since.

## Short and effective

For text that labels or introduces something: repository descriptions, titles,
status lines, commit subjects, one-line summaries.

- Say what the thing is, not what it currently holds. Contents change; purpose
  rarely does.
- One line. If it needs a second, the first is doing the wrong job.
- Cut what the reader already knows from context or can see one click away.
- No filler, no hedging, no parenthetical inventories.

Not for reference documentation, runbooks or anything a reader follows step by
step. Those need completeness more than brevity.

### Example: a repository description (2026-09-24)

The repository started as a single skill and became the home for several.

1. Before: "Reusable skill for repository documentation, glossaries, diagrams,
   and project guidance". Accurate once, then wrong as soon as a second skill
   arrived.
2. First rewrite: "Jonas's reusable, project-agnostic agent skills: project-docs
   (repository documentation) and my-email-style (email drafting)". Correct, but
   the list goes stale with every new skill, and the README already has it.
3. Final: "Jonas's reusable, project-agnostic agent skills". Says what the
   repository is for, and stays true as it grows.

## Related

[my-email-style](../skills/my-email-style/SKILL.md) is a personal voice rather
than a general style: how Jonas writes email, derived from his sent mail. It
shares the same instinct: short, no introductions, no closing paragraphs.
