from app.models.finding import FindingSeverity
from app.correlation.shared_pool import (
    analyze_shared_pool,
)

from app.models.evidence import (
    Evidence,
    EvidenceSource,
)


def test_detect_shared_pool_pressure():

    evidence = Evidence(
        evidence_id=(
            "INC-001-shared_pool_summary"
        ),
        incident_id="INC-001",
        source=EvidenceSource.DATABASE,
        evidence_type="shared_pool_summary",
        data={
            "shared_pool_size_mb": 10240,
            "free_memory_mb": 128,
            "allocation_failures": 47,
            "library_cache_hit_ratio": 92.5,
        },
    )

    finding = analyze_shared_pool(
        evidence
    )

    assert finding is not None

    assert (
        finding.title
        == "Shared Pool Memory Pressure"
    )

    assert (
        finding.incident_id
        == "INC-001"
    )

    assert (
        "1.25%"
        in finding.description
    )
def test_detect_critical_shared_pool_pressure():

    evidence = Evidence(
        evidence_id="INC-002-shared_pool_summary",
        incident_id="INC-002",
        source=EvidenceSource.DATABASE,
        evidence_type="shared_pool_summary",
        data={
            "shared_pool_size_mb": 10000,
            "free_memory_mb": 50,
            "allocation_failures": 20,
        },
    )

    finding = analyze_shared_pool(
        evidence
    )

    assert finding is not None

    assert (
        finding.severity
        == FindingSeverity.CRITICAL
    )


def test_detect_medium_shared_pool_pressure():

    evidence = Evidence(
        evidence_id="INC-003-shared_pool_summary",
        incident_id="INC-003",
        source=EvidenceSource.DATABASE,
        evidence_type="shared_pool_summary",
        data={
            "shared_pool_size_mb": 10000,
            "free_memory_mb": 400,
            "allocation_failures": 0,
        },
    )

    finding = analyze_shared_pool(
        evidence
    )

    assert finding is not None

    assert (
        finding.severity
        == FindingSeverity.MEDIUM
    )


def test_no_shared_pool_pressure():

    evidence = Evidence(
        evidence_id="INC-004-shared_pool_summary",
        incident_id="INC-004",
        source=EvidenceSource.DATABASE,
        evidence_type="shared_pool_summary",
        data={
            "shared_pool_size_mb": 10000,
            "free_memory_mb": 1000,
            "allocation_failures": 0,
        },
    )

    finding = analyze_shared_pool(
        evidence
    )

    assert finding is None
