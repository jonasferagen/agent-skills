# Large conceptual ER documentation task

Create docs/database/model.md explaining this supplied model with canonical ER
views and useful navigation. All facts below are given for this synthetic trial.
No new domain decisions, SQL or implementation are needed.

There are three ownership roots: ORGANISATION, AGREEMENT and SERVICE.
Each agreement belongs to exactly one organisation; each organisation has zero
or more agreements. Each agreement covers exactly one service; each service has
zero or more agreements.

ORGANISATION owns ADDRESS, CONTACT, IDENTIFIER, MEMBERSHIP and NOTE.
AGREEMENT owns CLAUSE, AMENDMENT, ATTACHMENT, MILESTONE and SIGNATURE.
SERVICE owns CATEGORY_ASSIGNMENT, OFFERING, REGION_ASSIGNMENT, SERVICE_NOTE and
SERVICE_IDENTIFIER. Every child belongs to exactly one of its named roots, and
each root may have zero or more of each child type. There are no other links.

Readers need to see how the roots relate and to inspect each root’s owned detail.
Use established guidance to organize the views. No network, installation, runtime
or schema execution; use any existing renderer if available and report limits.
