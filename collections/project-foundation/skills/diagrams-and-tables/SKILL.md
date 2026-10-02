---
name: diagrams-and-tables
description: "Choose, draw or review diagrams and tables for relationships, flows, schemas and comparisons. Use when structure is hard to follow in prose or an existing visual needs simplification, grounding or readability checks."
metadata:
  version: "0.3.0"
---

# Diagrams and tables

Apply these conventions wherever a task authors or revises prose, a diagram, or
an overview table — docs, skills, plans, issue bodies, durable comments, design
records, prompts, and review feedback alike. **Before drafting or rewriting a
substantive artifact, ask whether its central facts have a smallest useful
structured form; keep simple claims, why, gotchas, decisions, and conventions as
brief prose.** When the detail would outgrow the artifact, link one canonical
detail owner rather than copying it; in a skill, that owner is normally a
bundled `references/` document.

This skill owns **form choice**: which form carries a subject, at what altitude,
and how it is drawn. The owning surface decides where a form lives. For a
documentation set, that owner decides the form's placement, discoverability,
freshness review against its source, catalog entry, and when an index hands its
detail to the owning document; it also decides that a system document opens with
a brief overview. This skill decides only whether that overview wants a diagram
or a table, and which one. Concise prose is the right overview when there is no
relationship, flow or ownership shape to show. Where a project documentation
skill is available, it owns those placement rules.

Ground every edge in its source before drawing, then verify that the result
reads in the renderer its readers use. A successful parse does not establish
readability; the verification reference below covers both checks.

A repository-specific _diagram catalog_ is different again: it indexes the
diagrams a repository owns and points at their canonical docs. This skill holds
the conventions; the catalog holds the inventory.

## Choose the form

| Subject | Form to reach for first |
| --- | --- |
| Flow, sequence, lifecycle, component wiring | Flowchart — before/after when it changes |
| Schema, storage, or data-model change | ER diagram, plus a table-and-column overview of the delta |
| Tables, columns, indexes, or migration steps | Table: name, type, nullability, what changes |
| Options, states, tiers, per-surface obligations | Ordinary table, one row per case |
| Why, gotchas, decisions, trade-offs, conventions | Prose — no diagram carries these |

For a simple table, read [tables](references/tables.md) and stop there. Reuse a
suitable existing form; filling the project scaffold does not require inventing
a diagram. Ground table entries in the available facts and preserve unknowns.

## Read for the selected task

- For a selected diagram's reuse, layout, detail or splitting, read
  [composition](references/composition.md).
- Before asserting diagram relationships or reviewing a diagram render, read
  [verification](references/verification.md).
- Before writing Mermaid, read [drawing](references/drawing.md).
- Open [worked examples](references/worked-examples.md) when a chosen form needs
  an example; do not load every reference for an ordinary prose or table edit.
