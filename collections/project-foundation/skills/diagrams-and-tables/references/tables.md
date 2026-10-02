# Tables and comparisons

## Choose a table

A table is the cheapest structured form there is: it renders everywhere, diffs
line by line, needs no syntax discipline, and survives being quoted into an
issue. **Reach for one earlier than feels natural** — most prose that enumerates
anything is a table that was never drawn.

**The test is shared fields, not item count.** Items carrying the same fields
are a table however few of them there are: three items × three fields is one
scan down a column instead of three sentences to parse. Items sharing no
structure stay prose however many there are — putting unrelated statements in a
table gains the reader nothing. A short parallel set is exactly where a
table pays, so counting rows is the wrong question to ask first.

Five shapes carry most cases:

| Shape | Rows × columns | What it exposes |
| --- | --- | --- |
| **Delta table** | one field or option × before, after, migration | exactly what changes, at field altitude |
| **Decision matrix** | one option × each criterion | why the chosen option wins, and what it costs |
| **Coverage matrix** | one surface × each obligation | the gap nobody had noticed |
| **Registry table** | one term × status, canonical meaning | which name is current, and what replaced the rest |
| **Fan-in table** | one referencing entity or group × what it reaches | who depends on a hub, without drawing the hub |

The coverage matrix is the one to reach for deliberately: prose can describe
every surface in turn and never reveal that one of them answers nothing, whereas
the cell nobody can fill, written as `unknown` or `none`, is visible at a
glance.

The fan-in table is the one that rescues a diagram. **A shared target reached by
many entities belongs in a table rather than as a drawn hub.** A hub is the most
expensive node a graph layout can carry, since its edges cross every other edge
in the block; a table shows the same dependency with no crossing at all. Put the
target in the heading, one referencing entity or group per row, and keep the hub
out of the drawing.

### What choosing a form buys

A structured form buys **scannability, not brevity**, and the two are easy to
confuse when reporting a restructure. Converting wrapped prose into a table
collapses the line count, since one table row holds what four wrapped lines
held. It barely moves the word count, because the words were never what made
the passage slow to read. Measure words before claiming a document got shorter.
A line count after a form change describes cell width more than it describes how
much the reader has to take in, and a reviewer told "150 lines to 115" will
believe it.


For an actual diagram, use [composition](composition.md) for layout and detail.
A table-only task needs no diagram composition or rendering guidance.

## Drawing a table or matrix

- **Fill every cell.** A blank reads as "not applicable" and hides an
  unanswered question — write `none`, `n/a`, or `unknown` on purpose.
- **Keep cells short.** A cell that wants a paragraph means the table is at the
  wrong altitude: shrink the cell to a verdict and link to the prose.
- **Watch the width.** A table that scrolls sideways in a rendered doc has the
  same problem as a diagram that is too wide. Drop a column, or transpose the
  axes.
- **One row per case, and say what the rows are.** A table whose rows mix two
  kinds of thing should be two tables.
- **Put the axis in the header**, not in the surrounding sentence, so the table
  still reads when it is quoted into an issue without its paragraph.
