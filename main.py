from app.models.incident import (
    DatabaseType,
    Incident,
    Severity,
)
from app.services.playbook_service import select_playbook


def main():
    incident = Incident(
        incident_id="INC-001",
        database_name="PRODDB",
        database_type=DatabaseType.ORACLE,
        error_code="ORA-04031",
        severity=Severity.HIGH,
        message="Unable to allocate bytes of shared memory",
    )

    print("\n=== DBA NEXUS AI ===")

    print("\n--- INCIDENT ---")
    print(f"Incident ID: {incident.incident_id}")
    print(f"Database: {incident.database_name}")
    print(f"Database Type: {incident.database_type.value}")
    print(f"Error Code: {incident.error_code}")
    print(f"Severity: {incident.severity.value}")

    playbook = select_playbook(incident)

    if playbook is None:
        print("\nNo investigation playbook found.")
        return

    print("\n--- PLAYBOOK SELECTED ---")
    print(f"Name: {playbook.name}")
    print(f"Category: {playbook.incident_category}")
    print(f"Description: {playbook.description}")

    print("\n--- INITIAL EVIDENCE PLAN ---")

    for index, evidence in enumerate(
        playbook.initial_evidence,
        start=1,
    ):
        print(f"{index}. {evidence}")

    print("\n--- INITIAL HYPOTHESES ---")

    for index, hypothesis in enumerate(
        playbook.hypotheses,
        start=1,
    ):
        print(f"{index}. {hypothesis.name}")
        print(f"   {hypothesis.description}")

    print("\n--- INVESTIGATION PHASES ---")

    for index, phase in enumerate(
        playbook.phases,
        start=1,
    ):
        print(f"{index}. {phase.name}")
        print(f"   {phase.description}")


if __name__ == "__main__":
    main()
