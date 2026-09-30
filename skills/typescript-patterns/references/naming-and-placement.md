# Naming And Placement

## Contents

- [File naming and moods](#file-naming)
- [Role dictionary](#role-dictionary)
- [Obligation names](#name-the-obligation-not-the-property)
- [Representation prefixes](#representation-prefixes)
- [Export shape and type placement](#export-shape)

## File Naming

Name a class or primary type file after its primary export. Use the shape
`{Domain?}{Topic}{Role?}.ts` for class-oriented code.

- **Domain** is context not already supplied by the package or directory. Keep
  it when the public identity depends on it; drop it when it repeats the path.
  See
  [directory patterns](directories.md#directory-carries-the-prefix).
- **Topic** is the noun or concept the file owns.
- **Role** names the unit's contract: `Parser`, `Resolver`, `Builder`,
  `Compiler`, `Adapter`, `Registry`, and similar words carry meaning when they
  tell callers what to expect.

Reserve a bare noun for the primary concept, such as `Order`, `DateRange`, or
`GridCoordinate`. Avoid `Utils`, `Helpers`, and `Common`. Use `Manager` only for
a long-lived shell or lifecycle, not a bucket of unrelated operations.

A sibling contract file takes the `Types` role suffix, such as
`DeliveryTypes.ts`. Inside a contract directory such as `types/`, the directory
supplies the namespace, so a module may use a lowercase domain noun, such as
`types/delivery.ts`. Runtime classes take their PascalCase class name.
Class-free runtime modules, such as constants, data records and tokens, use
camelCase names.

A repository may enforce filename/export parity mechanically. Its command,
entry-point exceptions, and any temporary baseline remain local facts. The
check can prove that a name matches an export; it cannot decide whether the
name expresses the right domain, topic, or role.

## File Moods

Most production files have one dominant mood:

| Mood            | Name shape                                 | Test                     | Examples                     |
| --------------- | ------------------------------------------ | ------------------------ | ---------------------------- |
| Value/model     | Bare domain noun                           | Owns data and invariants | `Order`, `DateRange`         |
| Operation       | Agent noun or `{Topic}{Role}`              | Performs a verb on data  | `OrderParser`, `TaxResolver` |
| Policy/strategy | `{Topic}Policy`, `…Limit`, `…Strategy`     | Encodes a decision rule  | `RetryPolicy`                |
| Contract        | Named contract surface or sibling `XTypes` | Passive types only       | `DeliveryTypes`              |

An operation is a class—static or stateful—under [class
shape](class-shape.md#classes-and-managers), except for the narrow cases listed
there.

A folder is dominated by one mood or explicitly splits a functional core from
an imperative shell. A role-named folder mixing values, operations, and policies
usually should be split by concept first.

## Role Dictionary

A role suffix names a recurring contract, not an implementation shape. The
vocabulary is open; coin a new role when its promise is specific and reusable.

| Role        | Promise                                                                            | Neutral examples                |
| ----------- | ---------------------------------------------------------------------------------- | ------------------------------- |
| `Parser`    | Validates external text/data into a domain value; throws on malformed input        | `OrderParser`, `RouteParser`    |
| `Decoder`   | Converts an encoded representation into a domain value                             | `TokenDecoder`, `ImageDecoder`  |
| `Codec`     | Owns both encode and decode directions                                             | `CursorCodec`                   |
| `Resolver`  | Applies precedence or policy to produce one decisive value                         | `LocaleResolver`, `TaxResolver` |
| `Builder`   | Assembles a composite result over ordered steps                                    | `ReportBuilder`                 |
| `Compiler`  | Lowers one whole representation into another final form                            | `TemplateCompiler`              |
| `Emitter`   | Produces canonical low-level units for a downstream stage                          | `TokenEmitter`                  |
| `Factory`   | Mints members of a family from descriptors; owns no lifecycle                      | `TransportFactory`              |
| `Loader`    | Fetches and decodes an external resource, often asynchronously                     | `ProfileLoader`                 |
| `Validator` | Checks an already-parsed value and returns/throws diagnostics without transforming | `OrderValidator`                |
| `Sampler`   | Reads a value from a field or structure at a query point                           | `GridSampler`                   |
| `Registry`  | Owns a keyed store over its lifetime                                               | `HandlerRegistry`               |
| `Disposer`  | Releases one subsystem's resources in defined order                                | `SessionDisposer`               |
| `Manager`   | Owns a long-lived shell or lifecycle                                               | `ConnectionManager`             |
| `Boot`      | Composes and starts one application profile                                        | `AdminBoot`                     |

`Types` names a passive sibling contract surface. `Context` names a mutable
parameter bundle threaded through pipeline steps and usually stays local to the
pipeline rather than earning its own module.

### Name The Obligation, Not The Property

If adding an entry to a registry transfers responsibility or disables a
fallback, name that obligation. `SUPPORTED_FIELDS` sounds like an inventory;
`SERIALIZER_OWNED_FIELDS` says that adding a member makes the serializer
responsible for carrying it.

The name reduces the risk but does not guard against it. If omitting an entry
from the registry is unsafe, the registry must also be fail-closed through an
exhaustive record, an owner-derived schema, or a durable ratchet. See
[Fail-Closed Mirrors](typescript.md#fail-closed-mirrors).

## Representation Prefixes

A role suffix says what a class does. A prefix on a type says which
representation of the concept it is. Name the stage that produced the type and
leave the canonical carried form unmarked.

| Prefix                  | Meaning                                                       | Example            |
| ----------------------- | ------------------------------------------------------------- | ------------------ |
| _(none)_                | Canonical representation carried by the domain                | `Order`            |
| `Input*` or `Authored*` | External or author-supplied form before processing            | `InputOrder`       |
| `Parsed*`               | Validated parser output when distinct from the canonical form | `ParsedOrder`      |
| `Compiled*`             | Whole representation lowered for a later stage                | `CompiledTemplate` |
| `*Json` / `Serialized*` | Serialized mirror of a carried value                          | `OrderJson`        |
| `Resolved*`             | A decision made and consumed at a boundary                    | `ResolvedLocale`   |

One concept's ordinary sequence of representations is therefore:

```text
InputOrder -> Order -> OrderJson
```

Removing the serialization marker from a mirror's name should leave the
canonical type's name. A mismatch is evidence that one representation is
misnamed.

### `Resolved*` Promises A Decision

`Resolved*` does not mean every field is required. It means each absence was
classified: defaulted, rejected, intentionally absent, or carried as a decisive
result. Two questions decide whether the prefix fits:

1. Was deciding precedence or absence the producing step's purpose? Whole-form
   lowering is compilation, even if it applies defaults.
2. Is the result consumed where it was made? A carried or serialized domain
   value normally takes the unmarked name.

A view model may legitimately be `Resolved*` when it is built and consumed at a
view boundary. The rule follows the value's lifecycle, not the producer class's
suffix.

## Export Shape

Keep production modules narrow: one primary runtime symbol per file. A class may
ship with its canonical singleton as a secondary export; the class remains the
primary name. Group related interfaces and aliases only in an explicit contract
surface. Keep helper types private until they escape their owner.

Barrels aggregate owning modules and contract files. They do not excuse mixed
responsibilities inside implementation files.

### Type Placement: Three Tiers

Start at the lowest tier and promote when the type escapes its scope:

1. **Inline with the class** — intrinsic to one class's surface.
2. **Sibling `XTypes.ts`** — shared by nearby callers inside the same boundary.
3. **Named contract module or directory** — crosses a folder or package
   boundary; the directory name communicates the domain contract.

Escape of scope, not raw importer count, triggers promotion. A private helper
type used by many methods remains inline; a public type imported from another
package does not stay in a sibling types file beside the implementation.
