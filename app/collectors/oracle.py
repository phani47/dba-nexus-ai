from app.collectors.base import BaseCollector
from app.core.oracle_queries import (
    SHARED_POOL_SUMMARY_QUERY,
)
from app.core.query_executor import QueryExecutor
from app.models.evidence import (
    Evidence,
    EvidenceSource,
)
from app.models.evidence_requirement import (
    EvidenceRequirement,
)
from app.models.incident import Incident


class OracleSharedPoolCollector(BaseCollector):
    """
    Collect Oracle shared pool evidence.
    """

    EVIDENCE_TYPE = "shared_pool_summary"

    def __init__(
        self,
        query_executor: QueryExecutor,
    ) -> None:
        self.query_executor = query_executor

    def can_collect(
        self,
        requirement: EvidenceRequirement,
    ) -> bool:

        return (
            requirement.evidence_type
            == self.EVIDENCE_TYPE
            and requirement.source
            == EvidenceSource.DATABASE
        )

    def collect(
        self,
        incident: Incident,
        requirement: EvidenceRequirement,
    ) -> Evidence:

        rows = self.query_executor.execute(
            SHARED_POOL_SUMMARY_QUERY
        )

        data = rows[0] if rows else {}

        return Evidence(
            evidence_id=(
                f"{incident.incident_id}-"
                f"{requirement.evidence_type}"
            ),
            incident_id=incident.incident_id,
            source=EvidenceSource.DATABASE,
            evidence_type=requirement.evidence_type,
            data=data,
        )
