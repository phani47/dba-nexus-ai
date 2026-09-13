from app.models.evidence_requirement import (
    EvidencePriority,
    EvidenceRequirement,
)
from app.models.playbook import Playbook


PRIORITY_ORDER = {
    EvidencePriority.CRITICAL: 1,
    EvidencePriority.HIGH: 2,
    EvidencePriority.MEDIUM: 3,
    EvidencePriority.LOW: 4,
}


def create_evidence_plan(
    playbook: Playbook,
) -> list[EvidenceRequirement]:
    """
    Create an ordered evidence collection plan
    based on evidence priority.
    """

    return sorted(
        playbook.evidence_requirements,
        key=lambda requirement: PRIORITY_ORDER[
            requirement.priority
        ],
    )
