# Diagrams in a documentation set

Which diagrams a documentation set owns, where each one lives, and how it stays
true. **Choosing a form and drawing it well is a separate craft** — form choice,
altitude, layout, portable syntax, evidence grounding and readability checking
belong to a diagrams skill where one is available. This page covers only what is
particular to a set of documents.

## Which doc owns which view

| Question the reader arrives with | Doc that owns the view |
| --- | --- |
| What are the main concepts, and how do they relate? | The domain or model doc |
| How many related rows can exist? | The domain doc, from verified cardinalities |
| What runs where, and what talks to what? | The architecture doc |
| How does work move through decisions? | The doc that owns that process |

One view has one home. Other documents link to it rather than redrawing it, so a
correction lands once. An index may name a view and point at the document that
owns it; it does not carry a second copy.

Keep a useful overview ahead of implementation detail in the set as a whole, not
only inside one document. Where a crowded overview has to split, link the focused
views from the glossary or index so a reader can still find the whole shape.

## Terms come from the glossary

Draw with names the glossary already defines, and add the term there in the same
change if the diagram needs a concept the set has not named. A diagram is often
where a missing term first becomes obvious — that is a glossary gap to close, not
a licence to coin a synonym in a picture.

## Freshness is part of doc review

A diagram is a claim about the system, so it goes stale like prose and more
quietly, because nobody rereads a picture. When reviewing a document, check its
diagrams against the same sources as its text, and reconcile both in the same
change.

State whether a view shows current behavior or a proposal, and where a set
deliberately keeps a historical diagram, keep it distinguishable from current
guidance.
