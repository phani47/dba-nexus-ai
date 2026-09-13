from app.models.finding import (
    Finding,
    FindingConfidence,
    FindingSeverity,
)

from app.models.root_cause import (
    RootCauseConfidence,
)

from app.root_cause.shared_pool import (
    analyze_shared_pool_root_cause,
)


def test_detect_shared_pool_root_cause():

    finding = Finding(

        finding_id=(
            "INC-001-shared-pool-pressure"
        ),

        incident_id="INC-001",

        title=(
            "Shared Pool Memory Pressure"
        ),

        description=(
            "Shared pool free memory is low."
        ),

        severity=FindingSeverity.CRITICAL,

        confidence=FindingConfidence.HIGH,

        evidence_ids=[
            "INC-001-shared_pool_summary",
        ],

    )

    root_cause = (
        analyze_shared_pool_root_cause(
            [finding]
        )
    )

    assert root_cause is not None

    assert (
        root_cause.title
        == "Shared Pool Exhaustion"
    )

    assert (
        root_cause.confidence
        == RootCauseConfidence.HIGH
    )

def test_no_shared_pool_root_cause():

    root_cause = (
        analyze_shared_pool_root_cause([])
    )

    assert root_cause is None
