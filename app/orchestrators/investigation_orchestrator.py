from datetime import datetime

from app.collectors.registry import get_collector

from app.models.incident import Incident

from app.models.investigation_result import (
    InvestigationResult,
)

from app.services.evidence_planner import (
    create_evidence_plan,
)

from app.services.playbook_service import (
    select_playbook,
)


class InvestigationOrchestrator:
    """
    Coordinates the complete DBA investigation workflow.
    """

    def investigate(
        self,
        incident: Incident,
    ) -> InvestigationResult:

        result = InvestigationResult(
            incident=incident,
            status="running",
        )

        # Step 1:
        # Select investigation playbook.

        playbook = select_playbook(incident)

        if playbook is None:

            result.status = "no_playbook"

            result.completed_at = datetime.now()

            return result

        result.playbook = playbook

        # Step 2:
        # Create priority ordered evidence plan.

        evidence_plan = create_evidence_plan(
            playbook,
        )

        # Step 3:
        # Find collectors and collect evidence.

        for requirement in evidence_plan:

            collector = get_collector(
                requirement,
            )

            if collector is None:

                continue

            evidence = collector.collect(
                incident,
                requirement,
            )

            result.evidence.append(
                evidence,
            )

        # Step 4:
        # Investigation completed.

        result.status = "completed"

        result.completed_at = datetime.now()

        return result
