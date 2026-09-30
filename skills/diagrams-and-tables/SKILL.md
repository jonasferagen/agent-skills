---
name: diagrams-and-tables
description: "Choose, draw or review diagrams and tables for relationships, flows, schemas and comparisons. Use when structure is hard to follow in prose or an existing visual needs simplification, grounding or readability checks."
metadata:
  version: "0.2.1"
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

- **How to draw it** — direction, subgraphs, `erDiagram`, table mechanics, and
  portable syntax — is in [references/drawing.md](references/drawing.md). Read
  it before writing a Mermaid block.
- **Models to copy** — overview/detail splits (one detail, several details,
  a staged lifecycle), before/after and layered lanes, a schema change, an
  aggregate-cluster ER split, a whole-schema overview raised to its owning
  documents, and coverage and decision matrices — are in
  [references/worked-examples.md](references/worked-examples.md). Read it once
  the form is chosen.

Two steps bracket the drawing itself: [ground every edge in its
source](references/verification.md#ground-every-edge-in-its-source) before drawing, and [verify that it
reads](references/verification.md#verify-that-it-reads) in the renderer its readers use afterwards. A
diagram that parses is not yet a diagram that works.

A repository-specific _diagram catalog_ is different again: it indexes the
diagrams a repository owns and points at their canonical docs. This skill holds
the conventions; the catalog holds the inventory.

## Read for the visual task

- For form choice, tables, reuse, scope, or splitting a large view, read
  [composition](references/composition.md).
- Before asserting relationships or reviewing a render, read
  [verification](references/verification.md).
- Before writing Mermaid, read [drawing](references/drawing.md).
- Open [worked examples](references/worked-examples.md) when a chosen form needs
  an example; do not load every reference for an ordinary prose edit.
