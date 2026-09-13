from app.collectors.registry import get_collector
from app.models.incident import Incident
from app.services.evidence_planner import (
    create_evidence_plan,
)
from app.services.playbook_service import (
    select_playbook,
)


def investigate(
    incident: Incident,
) -> list[dict]:
    """
    Execute the investigation workflow
    for an incoming database incident.
    """

    playbook = select_playbook(
        incident,
    )

    if playbook is None:
        return []

    evidence_plan = create_evidence_plan(
        playbook,
    )

    results = []

    for requirement in evidence_plan:

        collector = get_collector(
            requirement,
        )

        if collector is None:

            results.append(
                {
                    "evidence_type": (
                        requirement.evidence_type
                    ),
                    "priority": (
                        requirement.priority.value
                    ),
                    "status": "NOT_AVAILABLE",
                    "collector": None,
                    "evidence": None,
                }
            )

            continue

        evidence = collector.collect(
            incident,
            requirement,
        )

        results.append(
            {
                "evidence_type": (
                    requirement.evidence_type
                ),
                "priority": (
                    requirement.priority.value
                ),
                "status": "COLLECTED",
                "collector": (
                    collector.__class__.__name__
                ),
                "evidence": evidence,
            }
        )

    return results
