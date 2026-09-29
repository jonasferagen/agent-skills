# Enforcement

Which of this canon's rules a machine should check, and which stay with a
reviewer. The repository owns its toolchain, its command names, and its gate;
this page owns the decision behind them.

## Contents

- [Compiler strictness](#compiler-strictness)
- [Reading a strictness finding](#reading-a-strictness-finding)
- [Enforce or review](#enforce-or-review)
- [When a rule cannot express its exemption](#when-a-rule-cannot-express-its-exemption)

## Compiler strictness

The type-checker is the cheapest enforcement available, and the only one that
costs nothing per diff. Turn it up before reaching for a lint rule that
approximates the same guarantee.

Flags divide by **adoption cost**, not by value, and the division is what makes
a baseline usable. Measure before adopting: run the flag against the tree and
count, rather than reasoning from how strict it sounds.

| Class | Character | Adopt |
| --- | --- | --- |
| Free | Reports nothing on a codebase already written in ordinary style | Everywhere, immediately |
| Bounded | Reports a countable set a session can clear | Everywhere, as its own change |
| Structural | Reports at a rate proportional to a whole idiom in the codebase | Its own plan, per repository, on evidence |

`strict` itself, plus unused-binding, override, and casing checks, are normally
free or bounded. A flag that changes how **every indexed read** is typed is
structural: it does not find a bug list, it proposes a different way of writing
lookups, and adopting it is that decision rather than a cleanup. Treat one that
accounts for the large majority of a tree's total findings as structural on that
evidence alone, whatever its reputation elsewhere.

A repository may legitimately differ. What is not legitimate is differing
silently — record the flag, the class it fell into when measured, and the
decision, so the next reader does not re-derive it or assume drift.

## Reading a strictness finding

**A compiler finding is evidence, not an instruction.** The flag proves a
binding is unread; it cannot tell you why it exists.

The case that catches people is a **binding whose only job is to exist**. A
nominal marker is unread by construction — that is what makes it a marker — so
an unused-locals check reports it exactly as it reports dead weight. Deleting it
compiles, passes the suite, and quietly removes a type-level guarantee that had
no runtime behavior to fail. See
[nominal class instances](typescript.md#nominal-class-instances) for the shape
that keeps the guarantee and satisfies the flag.

So: delete what the flag finds, once you have said what each finding *was for*.
A finding you cannot explain is a finding you have not finished reading.

## Enforce or review

A rule earns a machine when the machine can decide it. Work down this list and
stop at the first that fits:

1. **Make it unrepresentable.** A shape the compiler rejects, or a boundary the
   module system cannot resolve across, needs no check and no exception list.
2. **A compiler flag**, when the rule is about types.
3. **A lint rule**, when the rule is syntactic or type-aware but not something
   the compiler decides — and when its violations are mechanically identifiable
   rather than a matter of judgement.
4. **Review**, when applying the rule requires knowing what the code is for.

Most of this canon sits at 4 and belongs there. A pattern about *when* a shape
is appropriate — when a value earns promotion, when a barrel earns its place,
when a port should be narrowed — cannot be checked, because the trigger is
intent. A checker for it will be wrong in both directions, and its exception
list becomes the real policy.

Two things follow:

- **A rule you cannot state as a machine-decidable predicate is not ready to be
  enforced.** Write it as guidance, or narrow it until a predicate exists.
- **A rule whose exceptions are unbounded is guidance wearing a gate's
  clothing.** One or two named exemptions are a rule with edges. Under the
  **Forge Project Policy** a growing list is a defect in the classifier, so
  narrow the predicate instead of extending the list.

An advisory report is a real third option between a gate and silence. A rule
worth surfacing but not worth blocking on emits a warning that the gate does not
fail on — an accretion threshold, a complexity ceiling — so growth stays visible
in ordinary output rather than only to an audit nobody schedules. Say in the
configuration that it is advisory, because a warning with no stated status reads
as a gate that someone forgot to fix.

Before adding a custom check, ratchet, or self-test of your own, establish that
the guard survives structural change. Follow the general remedy order — change
the shape before adding a guard, and name what would retire it; this page
decides which TypeScript mechanism fits once a machine check is the answer.

## When a rule cannot express its exemption

A rule sometimes catches a real defect class **and** an idiom that is correct by
construction, with no configuration that separates them. Framework registration
calls, generated code, and platform callbacks all produce this.

Establish it rather than assuming it. Try the rule's own exemption mechanism in
both directions against a probe carrying a genuine defect and the idiom side by
side. Two outcomes are common and mean opposite things:

- The exemption **does not match the idiom at all**, because the idiom's type is
  an ordinary platform type the rule cannot distinguish.
- The exemption **matches, and takes the defect class with it** — silencing the
  idiom and the bug in one move. This is the dangerous one, because the
  configuration looks like it worked.

When neither direction works, the answer is a **scope decision, not a
suppression decision**:

- **Narrow the one rule**, never the whole lane. The other rules still apply to
  those files, and excluding the directory to solve one rule's problem gives up
  everything else for free.
- **State the limit where the gate is**, in the configuration and in the
  repository's own guidance. An unexplained absence reads as an oversight, and
  the next reader either re-derives the investigation or "fixes" it.
- **Say what the gate no longer claims.** The **Forge Project Policy** requires
  a check to name what it measured; a gate believed to cover something it does
  not is worse than a gate known not to.
- **Record the revisit condition** — the upstream change that would make the
  exemption expressible.

Suppressing the idiom site by site is not the alternative it appears to be. At
any real scale it buries the defect class in the same noise, and the
suppressions outlive whoever understood them.
