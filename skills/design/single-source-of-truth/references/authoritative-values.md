# One owner for a shared value

Give a shared value one authoritative declaration. A consumer reads it through
an allowed dependency, receives its resolved value as an explicit input, or
adopts a publication derived from it. When a maintained copy remains, compare it
with the declaration at the selected revision. A recorded relationship alone
does not establish agreement.

Start with the owner that decides the value. For a runtime setting, use the
configuration or environment declaration the program consumes. Keep precedence,
interpretation and requiredness with that owner. A document can name the setting
and point to its declaration without repeating its current value or becoming
another source of configuration.

For an external identifier such as a package name, service URL or repository
location, reuse its existing declaration. If none exists, select a declaration
that fits the project's configuration conventions and state the choice. Similar
values with different owners or meanings need not be unified: a publisher's
latest release and a consumer's selected dependency answer different questions.

Across independently released repositories, the publisher owns the rule and its
publication; each consumer owns which immutable revision it adopts. A lock or
equivalent declaration records source identity, selected revision and artifact
integrity, plus any local transformation or modification. An imported file or
pinned package with that provenance is valid derivation. It need not track the
publisher's moving head or read the publisher's private checkout or database.
Upgrades change the consumer's adoption through its own review process.

Separate the evidence for each responsibility. The publisher checks a generated
artifact against its selected source. The consumer checks its adopted artifact
and behavior against that contract. Integration checks explicitly select the
participants and test their compatibility. Derivation reduces independent
maintenance; it does not by itself prove that the rule, generator or resulting
behavior is correct. Preserve independent examples or behavioral oracles where
those consequences matter.

When a machine needs a literal, pass the resolved value through its supported
interface or generate its input from the declaration. A placeholder is not
derivation unless its loader resolves it. Do not teach a runtime to discover
configuration by searching documentation. If consumers share a format, define
and check that interface. Another service's private tables are not a shared
format unless the owner explicitly publishes them as a supported interface.

Distinguish an adopted contract from both current configuration and historical
observations. A pin can govern current behavior even when upstream has newer
revisions. Execution evidence and dated assessments retain the values they used.
Examples state their assumptions. Do not rewrite these records to appear current.

A current-reference link can resolve through the owning declaration. A citation
used as reproducible evidence names an immutable revision. A link to a moving
branch can help readers browse current material, but cannot identify the bytes
adopted or assessed; do not use it as adoption provenance or historical evidence.

Report which declaration owns the value, which revision each consumer adopts,
how it obtains the value and what any check covers. Distinguish missing
access from disagreement. Declaring a resource does not grant access to it or
prove readiness, and a missing live upstream is not a defect in a consumer
whose contract requires only its available pinned publication.
