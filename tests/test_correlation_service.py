from app.models.evidence import (
    Evidence,
    EvidenceSource,
)

from app.services.correlation_service import (
    analyze_evidence,
)


def test_analyze_shared_pool_evidence():

    evidence = Evidence(

        evidence_id=(
            "INC-001-shared_pool_summary"
        ),

        incident_id="INC-001",

        source=EvidenceSource.DATABASE,

        evidence_type=(
            "shared_pool_summary"
        ),

        data={

            "shared_pool_size_mb": 10000,

            "free_memory_mb": 50,

            "allocation_failures": 20,

        },

    )

    findings = analyze_evidence(

        [evidence]

    )

    assert len(findings) == 1

    assert (

        findings[0].title
        == "Shared Pool Memory Pressure"

    )
