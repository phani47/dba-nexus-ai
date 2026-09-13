from app.collectors.oracle import (
    OracleSharedPoolCollector,
)
from app.core.mock_query_executor import (
    MockQueryExecutor,
)
from app.models.evidence import EvidenceSource
from app.models.evidence_requirement import (
    EvidencePriority,
    EvidenceRequirement,
)
from app.models.incident import (
    DatabaseType,
    Incident,
    Severity,
)


def test_oracle_shared_pool_collector():

    incident = Incident(
        incident_id="INC-001",
        database_name="PRODDB",
        database_type=DatabaseType.ORACLE,
        error_code="ORA-04031",
        severity=Severity.HIGH,
        message="Unable to allocate bytes of shared memory",
    )

    requirement = EvidenceRequirement(
        evidence_type="shared_pool_summary",
        source=EvidenceSource.DATABASE,
        priority=EvidencePriority.CRITICAL,
        description="Collect shared pool summary.",
        reason="Check shared pool exhaustion.",
    )

    executor = MockQueryExecutor()

    collector = OracleSharedPoolCollector(
        query_executor=executor,
    )

    assert collector.can_collect(requirement)

    evidence = collector.collect(
        incident,
        requirement,
    )

    assert evidence.incident_id == "INC-001"

    assert (
        evidence.evidence_type
        == "shared_pool_summary"
    )

    assert (
        evidence.data[
            "shared_pool_total_mb"
        ]
        == 10240
    )

    assert (
        evidence.data[
            "shared_pool_free_mb"
        ]
        == 128
    )
