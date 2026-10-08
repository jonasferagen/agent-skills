# One owner for a shared value

Give a value used in several places one authoritative declaration. A consumer
reads that declaration, receives its value through an explicit input, or derives
its copy from it. When direct use or derivation is impractical, a required check
compares the current declaration with the copy and fails on disagreement. A
recorded relationship alone does not check that their values agree.

Start with the owner that already decides the value. For a runtime setting,
use the configuration or environment declaration the program actually consumes.
Keep its precedence, interpretation and requiredness with that owner. A document
can name the setting and link its declaration without repeating its current
value or becoming another source of configuration.

For an external identifier the project chooses to use in several places, such
as a plugin namespace or a repository location, reuse an existing settings owner.
If none exists, establish one project-owned lookup declaration. Give the value a
stable key and have readers resolve that key through the declaration. The
project's conventions select its location and format; this rule requires no
particular document or companion installation.

When a machine needs a literal, pass the resolved value through its supported
interface or generate its input from the declaration. A placeholder is not
derivation unless its loader actually resolves it. Do not teach an unrelated
runtime to discover configuration by searching documentation. If several
consumers intentionally share a file format, define and check that interface.

Keep current bindings distinct from observations. Historical pins, citations,
execution evidence and dated assessments retain the values they actually used.
Examples state their assumed values. These answer different questions from
current configuration and must not be rewritten to look current. Two similar
values with different owners or meanings need not be unified.

Report which declaration owns the value, how each consumer obtains it and what
the check actually covers. A selected resource that is unavailable is a missing
dependency, not evidence that its declared value is wrong. Establishing a route
does not grant access, provision the resource or prove its readiness.
