from app.models.finding import (
    Finding,
    FindingConfidence,
    FindingSeverity,
)

from app.services.root_cause_service import (
    analyze_root_causes,
)


def test_analyze_root_causes():

    finding = Finding(

        finding_id=(
            "INC-001-shared-pool-pressure"
        ),

        incident_id="INC-001",

        title=(
            "Shared Pool Memory Pressure"
        ),

        description=(
            "Critical shared pool pressure."
        ),

        severity=FindingSeverity.CRITICAL,

        confidence=FindingConfidence.HIGH,

        evidence_ids=[
            "INC-001-shared_pool_summary",
        ],

    )

    root_causes = analyze_root_causes(
        [finding]
    )

    assert len(root_causes) == 1

    assert (
        root_causes[0].title
        == "Shared Pool Exhaustion"
    )
