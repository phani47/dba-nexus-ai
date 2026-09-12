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

    print("\n--- INCIDENT ---")
    print(incident.model_dump_json(indent=2))


if __name__ == "__main__":
    test_create_oracle_incident()
