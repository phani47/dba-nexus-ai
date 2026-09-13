from app.correlation.base import (
    BaseCorrelationRule,
)

from app.correlation.shared_pool import (
    analyze_shared_pool,
)

from app.models.evidence import Evidence

from app.models.finding import Finding


class SharedPoolCorrelationRule(
    BaseCorrelationRule,
):

    """
    Correlation rule for Oracle
    shared pool memory pressure.
    """

    EVIDENCE_TYPE = "shared_pool_summary"

    def can_analyze(
        self,
        evidence: Evidence,
    ) -> bool:

        return (
            evidence.evidence_type
            == self.EVIDENCE_TYPE
        )

    def analyze(
        self,
        evidence: Evidence,
    ) -> Finding | None:

        return analyze_shared_pool(
            evidence
        )
