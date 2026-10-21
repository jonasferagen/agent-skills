# Read a flowchart

Start with its caption, legend, entry condition and scope. Under this skill's
minimal convention, a rectangle is an action, a diamond asks a decision question,
and a rounded terminal marks an entry or outcome. Arrows mean the next step when
the stated condition holds. Follow an existing diagram's declared notation first.

Trace a concrete case from entry to an outcome. Read each branch condition;
missing or overlapping conditions leave the choice ambiguous unless the source
states a priority or that several branches execute. Two outgoing arrows alone
do not prove parallel execution. Converging arrows do not prove synchronization.

For a loop, identify what changes before the repeated step and what lets work
exit or pause. An arrow back to execution does not establish that retry is safe,
authorized or bounded. A missing failure path means the view does not explain
that case; it does not prove failure is impossible.

Actor labels or lanes identify responsibility only as declared. Crossing a lane
does not establish a transport mechanism, permission or completed handoff.
Distinguish operation completion, review acceptance and consumer adoption when
the source distinguishes them. A terminal called "Done" is ambiguous if it does
not identify which of those outcomes has occurred.

When explaining a supplied view, report omissions without inventing missing
steps or decisions. Applying its path is an interpretation task and grants no
permission to execute the depicted actions.
