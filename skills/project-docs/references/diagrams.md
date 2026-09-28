# Diagram conventions

Each diagram answers one reader question. Prefer maintainable text diagrams such
as Mermaid in repositories that render them; follow an established visual format
when one exists. See the [worked example](worked-example.md) for a glossary-led set.

## Choose the view

| Question | Suitable view |
| --- | --- |
| What are the main concepts and relationships? | Conceptual relationship map |
| What is shared across several kinds of item? | Common abstraction and its concrete forms |
| How does work move through decisions? | Process or state diagram |
| What runs where and talks to what? | Runtime architecture |
| How many related rows can exist? | ER diagram with verified cardinalities |

Do not mix a foreign-key map, an approval process and network architecture without
making the differing arrow meanings clear. Split a crowded overview into focused
views linked from the glossary. Keep a useful overview before implementation detail.

## Build from evidence

1. Choose terms already defined in the project and identify the question.
2. Verify each relationship against the appropriate source: schema for stored
   links, implementation for behavior, configuration for deployment, and explicit
   decisions for planned behavior.
3. Mark optionality, uncertainty or proposed behavior when omission would mislead.
   A conceptual map need not show every column or cardinality.
4. Label arrows with relationships or actions: “belongs to,” “supports,” “creates
   after approval.” Distinguish owner, payer, actor, identity and permission when
   the domain does; never collapse them merely to simplify the picture.
5. Add a caption explaining scope and any interpretation the arrows require.

Use the same label for the same concept across views. If several nodes represent
instances of one type, name their roles, such as “parent task” and “subtask.” Avoid
making layout groups look like new domain entities.

## Layout and inspection

Choose direction by shape: a short sequence may read left to right; a branching
relationship map often fits better top to bottom. Use concise labels with line
breaks where needed. Do not rely on color alone to explain meaning.

Render the diagram with available local tooling and inspect it at a normal reading
width. Check clipped text, edge-label collisions, crossings, excessive width and
unreadably small labels. Reflow or split a view instead of shrinking it indefinitely.
A successful parser run is not a readability check.

When the repository has a target preview or publishing renderer, inspect the
diagram there as well. Check the themes readers use: a diagram type may color
text, nodes, rows, labels and edges separately. Give text and its background
compatible colors, and keep renderer-specific overrides in the affected project.

Use temporary output for visual QA unless exported images are requested or needed
by the project's renderer. Keep source diagrams authoritative. Do not add a new
runtime dependency to the application solely to render documentation.
