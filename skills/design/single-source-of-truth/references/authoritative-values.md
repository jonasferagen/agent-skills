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
as a package name, a service URL or a repository location, reuse the setting
that already declares it. If none exists, keep the value in one declaration,
such as a configuration file the project already reads, and have every other
appearance reference it. Follow the project's conventions for where such
declarations live; if there is none, pick the existing configuration file the
most consumers already read and state that choice.

When a machine needs a literal, pass the resolved value through its supported
interface or generate its input from the declaration. A placeholder is not
derivation unless its loader actually resolves it. Do not teach an unrelated
runtime to discover configuration by searching documentation. If several
consumers intentionally share a file format, define and check that interface.

Keep current declarations distinct from observations. Historical pins, citations,
execution evidence and dated assessments retain the values they actually used.
Examples state their assumed values. These answer different questions from
current configuration and must not be rewritten to look current. Two similar
values with different owners or meanings need not be unified.

A citation either resolves through the declaration, which makes it a current
reference, or names a pinned revision, which makes it a historical one. A link
to a moving branch, such as a hosted `blob/main` URL, is neither: its meaning
changes silently when the branch moves. Cite through the declaration or pin the
revision.

Report to the user which declaration owns the value, how each consumer obtains
it and what the check actually covers. A declared resource that is unavailable
is a missing dependency, not evidence that its declared value is wrong.
Declaring a value does not grant access to the resource or prove it is ready.
