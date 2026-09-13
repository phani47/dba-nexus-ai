from app.collectors.oracle import (
    OracleSharedPoolCollector,
)
from app.collectors.registry import get_collector
from app.models.evidence import EvidenceSource
from app.models.evidence_requirement import (
    EvidencePriority,
    EvidenceRequirement,
)


def test_find_oracle_shared_pool_collector():
    requirement = EvidenceRequirement(
        evidence_type="shared_pool_summary",
        source=EvidenceSource.DATABASE,
        priority=EvidencePriority.CRITICAL,
        description="Collect shared pool summary.",
        reason="Check shared pool exhaustion.",
    )

    collector = get_collector(requirement)

    assert collector is not None

    assert isinstance(
        collector,
        OracleSharedPoolCollector,
    )


def test_unknown_collector_returns_none():
    requirement = EvidenceRequirement(
        evidence_type="unknown_metric",
        source=EvidenceSource.DATABASE,
        priority=EvidencePriority.HIGH,
        description="Unknown metric.",
        reason="Test unknown collector.",
    )

    collector = get_collector(requirement)

    assert collector is None
