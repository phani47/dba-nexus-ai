from app.collectors.base import BaseCollector

from app.models.evidence import (
    Evidence,
    EvidenceSource,
)

from app.models.evidence_requirement import (
    EvidenceRequirement,
)

from app.models.incident import Incident


class OSMemoryCollector(BaseCollector):

    """
    Collect operating system memory evidence.

    Currently returns simulated evidence.
    """

    EVIDENCE_TYPE = "os_memory_summary"

    def can_collect(
        self,
        requirement: EvidenceRequirement,
    ) -> bool:

        return (
            requirement.evidence_type
            == self.EVIDENCE_TYPE
            and requirement.source
            == EvidenceSource.OS
        )

    def collect(
        self,
        incident: Incident,
        requirement: EvidenceRequirement,
    ) -> Evidence:

        return Evidence(
            evidence_id=(
                f"{incident.incident_id}-"
                f"{requirement.evidence_type}"
            ),
            incident_id=incident.incident_id,
            source=EvidenceSource.OS,
            evidence_type=requirement.evidence_type,
            data={
                "total_memory_mb": 32768,
                "available_memory_mb": 1024,
                "swap_used_mb": 4096,
                "memory_usage_percent": 96.8,
            },
        )
