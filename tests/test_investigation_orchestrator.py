from app.models.incident import (
    DatabaseType,
    Incident,
    Severity,
)

from app.orchestrators.investigation_orchestrator import (
    InvestigationOrchestrator,
)


def test_orchestrate_oracle_ora_04031():

    incident = Incident(
        incident_id="INC-100",
        database_name="PRODDB",
        database_type=DatabaseType.ORACLE,
        error_code="ORA-04031",
        severity=Severity.HIGH,
        message=(
            "Unable to allocate bytes "
            "of shared memory"
        ),
    )

    orchestrator = InvestigationOrchestrator()

    result = orchestrator.investigate(
        incident,
    )

    assert result.status == "completed"

    assert result.playbook is not None

    assert result.playbook.error_code == (
        "ORA-04031"
    )

    assert len(result.evidence) > 0
