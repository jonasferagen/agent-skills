---
name: documentation-records
description: "Decide what belongs in maintained documentation and what belongs in plans, logs and other records. Use when updating guides after a change, moving history or proposals out of current pages, filing or retiring a record, or keeping a record's time scope; not for wording, README structure or diagrams."
metadata:
  version: "0.1.0"
---

# Documentation and records

Keep each document about the time it serves. Maintained guidance tells readers
how the system works now; records keep what was planned, decided, observed or
done. This skill decides which content belongs where and what happens to it when
the system changes. How the text reads is a writing task; where a project keeps
its records is that project's decision.

## Know what kind of document you are editing

Maintained guidance describes current purpose, behavior, responsibilities,
interfaces and constraints. It includes overviews, READMEs, agent and project
instructions, repository and package documentation, maintained guides and
current indexes. A "History" or "Maintenance" heading does not turn a current
page into a historical record.

Records describe another time: plans and proposals look forward; logs,
handoffs, decision records, implementation summaries and changelogs look back.
A record keeps its intended time scope. Preserve the decisions, evidence
references, dates and assessed conditions it records without adding a migration
story, and do not restate it as current behavior. A verb form a record's own
convention prescribes, such as a changelog's imperative "Add export", is form,
not a claim about the present; keep it. A dated observation states
the conditions assessed, not a promise of current status.

## Keep current guidance about the present

- When work changes the system, update the owning guide to describe the
  resulting state. Do not append an implementation summary, a change narrative
  or a completed plan.
- Keep current limitations, unsupported behavior, uncertainty and the rationale
  for current rules with the guidance they qualify. Their ability to change is
  not a reason to move them out.
- Move proposals, future commitments and accounts of past work into records.
- An instruction for an existing operation, or a conditional rule, describes a
  present capability even when it is phrased in the future tense. This is a
  boundary on meaning, not a ban on future-tense verbs.
- Link a record only when the reader needs its background or next work. A link
  does not make the record authoritative for current behavior.

## Put records where the project keeps them

Keep plans, handoffs and historical records in the consuming project's
designated location, apart from maintained guidance. The project owns that
location, its naming and filing rules, and any exception such as a dedicated,
clearly named changelog. Do not invent a repository path, archive folder or
storage policy. If the project names none, report what would need a home rather
than creating one.

Write a new record only when the task or the project's rules call for one.
Moving existing history or proposals out of current guidance needs no separate
request: keep what is worth keeping in the record location. When
moving a record out of maintained guidance, confirm that the stored copy is
complete before removing the original, and point remaining links at the current
guide or the stored record.

## Retire entries from current indexes

An index keeps the names, alternative names and paths readers look up today,
including the status of retired entries they may still meet. Beyond that, the
reader's current use decides how much retirement detail to keep; a full
inventory of retired paths is not required merely because something was
retired.

## Check the result

Read each changed current page as a reader arriving today: does every claim
describe the present system, and does every limit that affects them remain
visible? Read each record as a reader of its own time: are its dates, evidence
and scope intact? Respect the requested form and explicit project exceptions.
