# Numbers and identity

## Choose what equality means

Keep identity, display formatting and approximate agreement separate. Formatting
with `:g` or rounding to a few decimals can map distinct values to the same
string. Use explicit domain IDs for entities; use an exact value key only when
exact value equality is the intended grouping rule. When building a mapping
that requires unique keys, detect duplicates before assignment rather than
silently replacing an earlier record.

```python
readings = (1.000001, 1.000002)
assert readings[0] != readings[1]
assert f"{readings[0]:g}" == f"{readings[1]:g}"
```

More display digits do not define durable entity identity. If the domain
intentionally groups values into bins, define the unit, bin width, origin and
boundary/tie rule. Preserve that policy independently of display precision.
Approximate equality is not transitive: A can be close to B and B to C while A
is not close to C. Do not use it as dictionary-key equality or assume it defines
unambiguous deduplication groups; clustering needs an explicit grouping policy.

## Choose tolerances for the decision

Name the quantity, units, expected magnitude and source of error before choosing
a tolerance. Distinguish measurement uncertainty, arithmetic error, conversion
loss and a permitted domain margin. A display precision or machine epsilon alone
does not determine an acceptance threshold.

For approximate scalar agreement, `math.isclose` combines a relative tolerance
with an absolute tolerance. Relative tolerance scales with magnitude; an
absolute tolerance has the quantity's units and is needed for nonzero values
near zero. Set `rel_tol=0.0` when the contract allows only a fixed absolute
difference. Default relative tolerance can otherwise admit a large absolute
difference at large coordinates.

Boundary ownership and one-sided limits need their own rules: decide which side
owns equality and whether a margin tightens or relaxes acceptance. Do not replace
ordered comparisons with `isclose` indiscriminately. A length tolerance cannot
be reused unchanged for squared distances, areas or volumes.

Give each policy an owner and document why related stages share a tolerance or
use different ones. Avoid both a universal epsilon and unexplained per-call
constants. When the contract requires exact decimal or rational arithmetic,
consider scaled integers, `Decimal` or `Fraction`; converting an already rounded
float cannot recover the original exact input.

## Check the representation that leaves the process

Where finite values are required, reject NaN and infinity explicitly with
`math.isfinite`; a range check alone can miss NaN. Finite inputs can overflow
during arithmetic, so check consequential derived results too.

When converting to a lower-precision representation, validate the decoded output
against the required invariants. Distinct values can collapse after float32
packing or decimal rounding. A successful in-memory check does not prove that
serialized values retain ordering, separation or positive size. Report an
unsupported precision/range when needed rather than widening a tolerance until
the check passes.

Exercise values on both sides of a decision boundary, the boundary itself, zero
and representative magnitudes. For conversion-sensitive behavior, include a
round trip through the actual output encoding. Check for missing or merged
records as well as individual numeric error.

Sources: [floating-point representation](https://docs.python.org/3.11/tutorial/floatingpoint.html),
[`math.isclose` and `math.isfinite`](https://docs.python.org/3.11/library/math.html#math.isclose),
[binary packing](https://docs.python.org/3.11/library/struct.html#format-characters).
