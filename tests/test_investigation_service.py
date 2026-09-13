from app.models.incident import (
    DatabaseType,
    Incident,
    Severity,
)
from app.services.investigation_service import (
    investigate,
)


def test_oracle_ora_04031_investigation():

    incident = Incident(
        incident_id="INC-001",
        database_name="PRODDB",
        database_type=DatabaseType.ORACLE,
        error_code="ORA-04031",
        severity=Severity.HIGH,
        message="Unable to allocate bytes of shared memory",
    )

    results = investigate(
        incident,
    )

    assert len(results) == 5

    assert (
        results[0]["evidence_type"]
        == "shared_pool_summary"
    )

    assert (
        results[0]["status"]
        == "COLLECTED"
    )

    assert (
        results[0]["collector"]
        == "OracleSharedPoolCollector"
    )

    assert (
        results[1]["status"]
        == "NOT_AVAILABLE"
    )
