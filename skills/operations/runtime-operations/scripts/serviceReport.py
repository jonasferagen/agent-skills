"""One report line per service instance, so a project-wide status stays readable."""
import json
import re

NAME = re.compile(r'[a-z][a-z0-9-]*(:[a-z][a-z0-9-]*)?')


class ServiceReport:
    # Authoritative wire schema and closed vocabularies. Source maintenance checks
    # the standalone dispatcher and service convention against these declarations.
    SCHEMA = 'service-report/v1'
    # A closed vocabulary. A reader learns seven words once, and a controller cannot
    # invent an eighth that every consumer would then have to guess at:
    #   ready      a running instance that answers ready now
    #   scheduled  an installed, active schedule; a run is intended, none is held
    #   stopped    known here and deliberately not running
    #   absent     nothing installed or provisioned here to run
    #   elsewhere  the named unit or instance belongs to another checkout
    #   failed     it ran or was asked to run, and did not succeed
    #   unknown    the controller could not determine the state
    STATES = ('ready', 'scheduled', 'stopped', 'absent', 'elsewhere', 'failed', 'unknown')
    # What the service is, as against what `state` says it is doing now. A state
    # cannot answer this: `absent` is what an unprovisioned environment, an
    # unnamed instance and a never-installed unit all report, so a consumer that
    # composes a project-wide launch cannot tell from the state which of them such
    # a launch may touch. A declaring controller says so once:
    #   maintained   kept running; a project-wide launch starts and stops it
    #   environment  provisioned deliberately, by its own guide's words
    #   scheduled    a schedule, installed once by its own start
    #   on-demand    an instance that cannot be started without a name
    # `scheduled` appears in both vocabularies on purpose: an installed schedule is
    # both what that service is and what it is doing.
    LIFECYCLES = ('maintained', 'environment', 'scheduled', 'on-demand')
    LIMIT = 200

    @staticmethod
    def _text(value, field):
        if value is None:
            return None
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f'A report {field} is a non-empty string or absent')
        if '\n' in value or '\r' in value or len(value) > ServiceReport.LIMIT:
            # The row is the point. Long output -- a journal, a durable receipt, a
            # database probe -- belongs to `status <name>`, which a reader asks for
            # after a row says something is owed.
            raise ValueError(f'A report {field} is one line of at most '
                             f'{ServiceReport.LIMIT} characters')
        return value

    @staticmethod
    def line(service: str, checkout, state: str, *, endpoint: str | None = None,
             unit: str | None = None, detail: str | None = None,
             attention: str | None = None, lifecycle: str | None = None) -> str:
        """Render one instance's report as a single JSON line.

        `service` names the service as the dispatcher discovered it, and
        `service:instance` when one service holds several named instances.
        `attention` is for what a reader must act on, so an aggregate can show the
        rows that are owed something without reading every detail. `lifecycle`
        declares which class the service belongs to; a controller that has not
        declared one reports `null`, which reads as unclassified and is what keeps
        a partial adoption visible rather than wrong.
        """
        if not isinstance(service, str) or not NAME.fullmatch(service):
            raise ValueError('A report names its service, optionally as service:instance')
        if state not in ServiceReport.STATES:
            raise ValueError('A report state is one of: ' + ', '.join(ServiceReport.STATES))
        if lifecycle is not None and lifecycle not in ServiceReport.LIFECYCLES:
            raise ValueError('A report lifecycle is absent or one of: '
                             + ', '.join(ServiceReport.LIFECYCLES))
        return json.dumps({
            'schema': ServiceReport.SCHEMA,
            'service': service,
            'checkout': str(checkout) if checkout is not None else None,
            'state': state,
            'lifecycle': lifecycle,
            'endpoint': ServiceReport._text(endpoint, 'endpoint'),
            'unit': ServiceReport._text(unit, 'unit'),
            'detail': ServiceReport._text(detail, 'detail'),
            'attention': ServiceReport._text(attention, 'attention'),
        })

    @staticmethod
    def reports(output: str) -> list[dict]:
        """The report lines in a controller's output, ignoring whatever else it printed.

        A controller may still print its own text; only well-formed lines of this
        schema are read, so a partial adoption cannot be mistaken for a report.
        """
        found = []
        for line in output.splitlines():
            line = line.strip()
            if not line.startswith('{') or ServiceReport.SCHEMA not in line:
                continue
            try:
                record = json.loads(line)
            except ValueError:
                continue
            if (isinstance(record, dict) and record.get('schema') == ServiceReport.SCHEMA
                    and isinstance(record.get('service'), str)
                    and record.get('state') in ServiceReport.STATES):
                if record.get('lifecycle') not in ServiceReport.LIFECYCLES:
                    # An unrecognized class is dropped to unclassified rather than
                    # dropping the row: a reading must survive a value a consumer
                    # cannot act on, and nothing may act on a class it cannot name.
                    record['lifecycle'] = None
                found.append(record)
        return found
