from app.models.incident import (
    DatabaseType,
    Incident,
    Severity,
)


def test_create_oracle_incident():
    incident = Incident(
        incident_id="INC-001",
        database_name="PRODDB",
        database_type=DatabaseType.ORACLE,
        error_code="ORA-04031",
        severity=Severity.HIGH,
        message="Unable to allocate bytes of shared memory",
    )

    assert incident.incident_id == "INC-001"
    assert incident.database_name == "PRODDB"
    assert incident.database_type == DatabaseType.ORACLE
    assert incident.error_code == "ORA-04031"
    assert incident.severity == Severity.HIGH


def test_incident_default_severity():
    incident = Incident(
        incident_id="INC-002",
        database_name="TESTDB",
        database_type=DatabaseType.POSTGRESQL,
        error_code="CONNECTION_ERROR",
    )

    assert incident.severity == Severity.HIGH
