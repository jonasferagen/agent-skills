# Prose styles

Draft. Named registers of writing that are worth reusing, each with an example.
It is not a skill yet; one may grow out of it once a style has been used in a
few places. A project's own writing guide still decides how that project's docs
are written.

| Style | Use it for |
| --- | --- |
| [Short and effective](#short-and-effective) | Labels and one-liners: repository descriptions, commit subjects, table cells, confirmations |

## Short and effective

Say what the thing is, in words that stay true as it changes.

- Name the category and the owner. Leave out the members; lists of contents go
  stale and belong in the README.
- One qualifier at most, and only if it distinguishes. *Project-agnostic* earns
  its place because it rules things out.
- No hedging, no restated context, no trailing summary.
- Stop when the reader can act or decide.

Not for reference documentation, runbooks or anything a reader follows step by
step. Those need completeness more than brevity.

### Example: a repository description

The `jonasferagen/skills` description on GitHub, as revised on 2026-09-24.

| Version | Text | Verdict |
| --- | --- | --- |
| Original | Reusable skill for repository documentation, glossaries, diagrams, and project guidance | Stale: describes the one skill the repository first held |
| First revision | Jonas's reusable, project-agnostic agent skills: project-docs (repository documentation) and my-email-style (email drafting) | Accurate, but stale again when a skill is added |
| Final | Jonas's reusable, project-agnostic agent skills | Says what the repository is and survives new skills |

The example stands even if the live description changes later.

## Related

[my-email-style](../skills/my-email-style/SKILL.md) is a personal voice rather
than a general style: how Jonas writes email, derived from his sent mail. It
shares the same instinct: short, no introductions, no closing paragraphs.
