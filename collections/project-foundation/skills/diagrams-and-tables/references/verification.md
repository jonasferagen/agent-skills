# Grounding and checking a visual

## Ground every edge in its source

A diagram states facts, and a reader treats a drawn edge as verified. Draw from
evidence, not from memory of how the system probably works.

1. Use terms the project has already defined. A diagram that coins a synonym for
   an existing concept adds a second name for it.
2. Verify each relationship against whatever owns it: the schema for a stored
   link, the implementation for behavior, the configuration for what is deployed,
   and an explicit decision for anything planned.
3. Label each edge with its meaning — *belongs to*, *supports*, *creates after
   approval* — not with a column name. Distinguish owner, payer, actor, identity
   and permission wherever the domain distinguishes them, and never collapse them
   to tidy the picture.
4. Mark optionality, uncertainty and proposed behavior where leaving them out
   would mislead. A conceptual map need not carry every column or cardinality,
   but it must not imply a certainty it lacks.
5. Caption the view with its scope and any interpretation its arrows require,
   especially when one diagram's arrows mean a stored link and another's mean a
   process.

Use one label for one concept across every view in a set. Where several nodes are
instances of one type, name their roles — *parent task* and *subtask* — rather
than repeating the type name. Do not let a layout group read as a domain entity it
is not.

## Find the renderer when needed

For diagram construction or visual review, inspect the project’s documented
preview/build command and relevant package scripts or configuration first. Use
that renderer when available. Otherwise check for an existing compatible local
tool. Record the renderer/version used when it affects syntax or layout claims.
A repository containing Mermaid text alone does not establish a render command.

If no renderer is available, report source review separately from unperformed
parse and visual checks. Follow the task’s dependency/network constraints; do not
add an application dependency solely for documentation. Reading a model or
reviewing only its semantics needs no renderer search.

## Verify that it reads

A parse is not a readability check, and neither is your own satisfaction with the
source. Render the diagram with the project's tooling and look at it at the width
a reader gets.

- Check clipped text, colliding edge labels, crossings, runaway width and labels
  shrunk past reading size. Reflow or split the view rather than shrinking it
  further.
- Where the project has a preview or publishing renderer, inspect it there too.
  The source is authoritative, but the reader sees the render.
- Check the themes readers actually use, including dark mode. A diagram type may
  color text, nodes, rows, labels and edges separately, so give text and its
  background compatible colors in each theme, and keep any renderer-specific
  override in the project that needs it.
- Do not rely on color alone to carry meaning.
- Use temporary output for visual checks unless the project's renderer needs a
  committed image. Never add a runtime dependency to an application solely to
  render its documentation.
