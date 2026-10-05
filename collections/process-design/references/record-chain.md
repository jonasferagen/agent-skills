# The work-record chain

Six records carry a bounded assignment from intent to a scoped decision. Each
answers one reader question and has one owner. Use a short section or a linked
record when that is sufficient; several of these can share one page when their
meanings stay distinguishable.

A brief says what should be achieved and how it will be assessed. A work item
names the change or investigation intended to meet it. A review subject is the
exact content assessed. A review context is the conditions under which it was
assessed. A finding is an observation with its limits. A decision says what the
findings mean for the intended use and what happens next.

## What connects to what

This is a relationship view. Arrows name relationships between records, not
execution order. One brief can lead to several work items and reviews.

```mermaid
flowchart TB
    brief["Brief revision<br/>Intent and criteria"]
    work["Work item<br/>Question and owner"]
    subject["Review subject<br/>Exact content assessed"]
    context["Review context<br/>Conditions and method"]
    finding["Finding<br/>Observation and limits"]
    decision["Decision<br/>Disposition and next action"]

    brief -->|"Guides"| work
    work -->|"Identifies"| subject
    subject -->|"Assessed by"| finding
    context -->|"Frames"| finding
    brief -->|"Criteria assessed in"| finding
    finding -->|"Informs"| decision
```

A decision can finish a scoped question, ask for more evidence, request work or
revise the brief. A new decision keeps its links to earlier evidence; it does not
rewrite that evidence to match the latest intent.

## What each record keeps explicit

| Record | Keep explicit | Typical owner |
| --- | --- | --- |
| Brief revision | Stable name and revision; intended use; applicable source revisions; constraints, defaults and local choices; criterion identifiers; adopted choices separated from proposed tests and open questions | The commissioning owner |
| Work item | Brief revision and criteria addressed; bounded question or change; responsible repository; dependencies and completion evidence | The project's planning owner, with technical detail in the performing repository |
| Review subject | Exact files and revision with relevant dependencies; what was included or excluded | The owner of the assessed content |
| Review context | Method, relevant settings and conditions; acting reviewer; run identity when executed | The repository performing the review |
| Finding | Criterion assessed; observation or measurement; evidence location; uncertainty and limits | The repository performing the review |
| Decision | Findings considered; disposition for the named use; acting decision-maker and authority; next owner or completion | The owner of the decision being made |

For Markdown records, the record identifier, human revision and commit identify
the reviewed content together. Record the commit when performing the review.
Changed intent or criteria take a new revision with the reason in the work
record. Editorial clarification can retain the revision; exact content is still
identified by its commit. Findings stay attached to the version actually assessed.

## Keep the assignment input separate from its output

The brief is the assignment input: intent, constraints, criteria, current
coordination state and next action. Execution observations, comparative
recommendations, design returns and dispositions belong in a linked record, not
appended to the brief as a results section. Identify the brief revision actually
assessed in that record and link it from the brief without copying the findings
back. A brief may link historical results without making them inputs to a new run.

Do not create a second authoritative status. The brief's coordination state and
next action live in the brief; dated findings and decisions live in the record.
Where a project already has an adequate work record, use it rather than adding
another.

## Criteria state what evidence would answer them

A criterion names an observable question and the evidence that would settle it.
Distinguish measurable geometry, reproducibility conditions and perceptual or
subjective judgement. "The target is three metres from the camera" is a
geometric claim; "it looks three metres away to this observer" is a finding
under a particular viewing setup. Neither is proof of the other.

If a success threshold is still open, record that and collect observations
without claiming acceptance against an invented limit. Inconclusive evidence can
close a deliberately bounded investigation when its decision owner records that
outcome; missing required work alone does not satisfy completion.

## Route feedback to the thing that changed

| Finding or proposed change | Decision and follow-up | Preserve |
| --- | --- | --- |
| The result differs from a specified measurement | The performing owner corrects or explains the subject, then repeats the affected measurements | The earlier subject identity and its findings |
| The conditions differ, or the observation changes with them | Record a new review context; assess it against the same criterion | The fixed subject and each comparison's settings |
| Intended use or a success criterion changes | The commissioning owner revises the brief and identifies which findings remain applicable | The earlier brief, decisions and the scope of existing evidence |
| Evidence is incomplete or contradictory | The reviewing owner records the unresolved question and the smallest useful follow-up | The uncertainty; no assumed acceptance |

A new subject or review basis may need a separate brief rather than reopening a
completed one. Shared subjects and parent briefs are ordinary explicit links,
not inferred progress dependencies.

## Authority stays where the project put it

These records organize work; they grant no authority. The person or role who
directs intent still directs it, and existing delegation still applies. Each
consequential review or decision records its acting person or agent. This does
not require repeating permission already given, and it does not make a recorded
disposition into acceptance by an owner who did not give it.

A completed assignment is not adoption of its subject. State the disposition for
the named use and link the actual adoption decision where one exists.
