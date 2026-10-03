# Choose the next useful step

Start with the most consequential unresolved question or the smallest useful
behavior the current design can support. Identify its owner, necessary inputs,
expected result and evidence that would resolve it. Explain why this step comes
before another when there is a real dependency.

Use a design exercise when ownership or meaning is unclear, a bounded experiment
when feasibility is uncertain, and implementation when the relevant decisions are
sufficiently settled. A small unknown need not block unrelated authorized work.
Record what a deferred decision blocks and when it needs an answer; avoid choosing
future infrastructure solely to make a plan look complete.

Keep the active sequence in the project's existing planning owner. Local design
pages may explain prerequisites and link to it without creating competing queues.
Preserve deferred work and distinguish a proposed sequence from approved execution.
A plan's existence is not authorization to run paid jobs, migrate sources or deploy.

Choose acceptance evidence for the result claimed. For design, a traced normal case
and a relevant revision or failure case may suffice. For implemented behavior,
name the observable outcome and prerequisites; use the project's verification
workflow when selecting or changing checks. Separate blockers from later decisions.

Keep this scoped to choosing work. Git mechanics, tracker updates, publishing and
release processes remain with their existing owners.
