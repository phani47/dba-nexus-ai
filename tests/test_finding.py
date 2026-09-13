from app.models.finding import (
    Finding,
    FindingConfidence,
    FindingSeverity,
)


def test_create_finding():

    finding = Finding(
        finding_id="FIND-001",
        incident_id="INC-001",
        title="Shared Pool Memory Pressure",
        description=(
            "Shared pool free memory is "
            "critically low."
        ),
        severity=FindingSeverity.HIGH,
        confidence=FindingConfidence.HIGH,
        evidence_ids=[
            "INC-001-shared_pool_summary",
        ],
    )

    assert finding.incident_id == "INC-001"

    assert (
        finding.severity
        == FindingSeverity.HIGH
    )

    assert (
        finding.confidence
        == FindingConfidence.HIGH
    )
