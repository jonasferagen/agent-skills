---
name: compact-ux
description: "Design or review compact interfaces for familiar users: replace repeated explanations and redundant help controls with recognizable labels, stat badges and contextual details. Use for verbose cards, cluttered inspectors or repeated information icons; not for visual restyling alone or first-use onboarding."
metadata:
  version: "0.1.0"
---

# Compact UX

Optimize the repeated task for someone who knows the application. Keep the
information they compare or act on visible; reveal explanations where they look
for them. Follow the consuming project's audience assumption. When familiarity
is unknown, infer it only from concrete context and state the assumption; do not
apply this default to onboarding or unfamiliar, consequential actions.

## Keep the decision visible

Identify what the user scans, compares, selects or edits in this view. Keep names,
current values, meaningful differences, availability and selection state visible.
Move repeated descriptions, formulas and rule explanations into contextual
details. Keep a restriction, error or consequence visible when it changes whether
the current action is sensible or possible. A tooltip should elaborate a useful
summary, not be required to discover the action or its current state.

Use short labels, established symbols and compact badges for familiar concepts.
Preserve signs, units and distinctions that affect interpretation: a negative
modifier stays negative, and a fixed amount stays distinguishable from a rolled
bonus. Use shape, text or a symbol as well as color. Reuse the application's
vocabulary and visual conventions; a short shared key can help when introducing
a symbol. Avoid inventing a new symbol for every sentence being removed.

## Put the explanation on its subject

Prefer hovering or focusing the existing name, value, badge or relevant region
to adding an information circle beside each fact. Give a stat its specific
explanation; give an item's name or surface its full description. Keep the
relationship between trigger and explanation clear. Remove a dedicated help
control when its subject provides equally usable access.

For example, an equipment card can show its name, timing and compact damage and
parry badges. Hovering the name explains reach and attack behavior; hovering the
parry badge explains that modifier. A small signed circle can carry the parry
value. This is a pattern to adapt, not a required icon set or card layout.

## Preserve interaction paths

Hover is the pointer shortcut, not the only way to read the information. Make
the same explanation available on keyboard focus and through an appropriate
touch interaction. Reuse an existing focusable subject when possible; avoid
adding a tab stop for every decorative span or nesting buttons inside a button.
Give symbolic values accessible names and associate explanations with their
subjects. A native title alone is insufficient for these paths.

Keep the existing primary action predictable. Inspecting a badge should not
accidentally equip, submit or delete something. If a card already selects on tap,
choose a detail path compatible with that action, such as details for the selected
item or a persistent inspector. A separate details control can remain when no
existing subject can expose the explanation without conflicting actions.

Allow details to be dismissed, keep them within the viewport and prevent them
from blocking nearby controls. If a tooltip can be hovered, keep it open while
the pointer crosses to it. Use a disclosure or inspector for long or interactive
content. Familiar users still need keyboard access, readable values and adequate
hit areas; compactness does not require shrinking text or targets.

## Check the repeated task

Review the actual view at a normal working size and a narrow supported size.
Compare a few representative items, including negative, zero and exceptional
values. Check hover, focus, dismissal, touch access, selection and disabled
states. Confirm that explanations remain accurate and the usual action takes
no extra step. Preserve the underlying rules and saved state. Report what was
changed and which interaction paths were exercised; a shorter page alone does
not establish a better interface.
