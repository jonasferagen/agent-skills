# External references

Give each current external reference one declaration in the consuming repository.
Reuse an existing resolver or configuration where it fits. Only declare references
the repository uses; it does not need a copy of the entire project's member map.

## Separate identity, selection and location

A local alias identifies the dependency's role. Selection records the publication
or interface the consumer accepts. Location says where to obtain or invoke it in
this environment. Readiness establishes whether that selected dependency can serve
the current operation. Resolving one does not establish the others.

For example, `@brief-contract` can identify the schema needed for incoming briefs;
`@primary` can identify project orientation. Choose aliases meaningful to the local
reader. A provider-oriented alias also fits when the provider itself matters.
Neither syntax is a universal naming requirement; adopt the project's convention.

For each reference, keep enough information to resolve its public entrypoint and
understand when it is needed. Use a readable discovery table for human readers.
When tools also consume it, derive that table from a structured declaration, or
make it point to the authoritative manifest rather than copying its values.

This synthetic table illustrates three different dependency roles:

| Reference | Needed for | Public entrypoint | Selection authority |
| --- | --- | --- | --- |
| `@orientation` | Project ownership guidance | Published guide | Adopted guide revision |
| `@brief-contract` | Brief admission | Schema artifact | Package lock |
| `@store-resolver` | Shared storage operations | Installed command | Accepted JSON interface |

The real declaration also supplies a resolvable artifact, command or document
location. Do not invent a second package lock, credential store or global registry.
An environment override may select an installation, while the committed declaration
retains the accepted interface. Define precedence, relative-path base and missing
or invalid selection behavior wherever the existing resolver contract lives.
Do not store credentials in the discovery table.

## Reference external owners in prose

Current maintained prose uses the declared alias when naming an external dependency
or directing a reader to it. Keep concrete external repository names, checkout
paths, URLs and selected versions in the declaration or owning native manifest.
Write, for example, “Validate incoming briefs with `@brief-contract`.” Describe the
purpose beside the alias so the reader need not resolve it merely to understand
the sentence. Public subresources may be referenced only with syntax the resolver
or documentation convention actually supports.

Preserve exact identifiers in dated evidence, source provenance and explicitly
labelled examples: they record what was observed or assumed. Protocol literals and
package import names required by an external interface also remain exact; connect
them to their owning declaration rather than disguising them as executable aliases.
Generated documentation may render concrete links from the declaration, provided
the source and regeneration route are clear. An unknown reference is an unresolved
dependency, never an invitation to search sibling folders for a plausible match.

## Resolve through an actual mechanism

Document how a human or agent expands a prose alias to the declaration and public
entrypoint. Markdown does not automatically make `@orientation` a link. If clickable
links are needed, use an existing renderer or generate them. A small repository
can use a documented table lookup without building a custom documentation engine.

Programs receive resolved paths, commands or values through their existing inputs
or a defined resolver. They do not scrape explanatory Markdown or assume aliases
work in shells, imports or container manifests. Generated machine files must be
checked against the declaration that produced them. A public command may be found
through an explicit executable setting or installed package; requiring a particular
sibling checkout needs an explicit development-use contract.

Changing a location must not silently select a different interface or bypass
integrity checks. Test relocation, missing aliases and incompatible selections
where those failures matter. A linter for raw prose references must respect the
historical, generated and protocol cases above; filename matching alone cannot
prove a public boundary is sound.
