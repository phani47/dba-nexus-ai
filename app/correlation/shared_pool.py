from app.models.evidence import Evidence
from app.models.finding import (
    Finding,
    FindingConfidence,
    FindingSeverity,
)


def analyze_shared_pool(
    evidence: Evidence,
) -> Finding | None:
    """
    Analyze Oracle shared pool evidence and
    generate a finding when memory pressure
    is detected.
    """

    if evidence.evidence_type != "shared_pool_summary":
        return None

    total_mb = evidence.data.get(
        "shared_pool_size_mb"
    )

    free_mb = evidence.data.get(
        "free_memory_mb"
    )

    allocation_failures = evidence.data.get(
        "allocation_failures",
        0,
    )

    if not total_mb or free_mb is None:
        return None

    free_percentage = (
        free_mb / total_mb
    ) * 100

    severity = None

    if (
        free_percentage < 1
        and allocation_failures >= 10
    ):
        severity = FindingSeverity.CRITICAL

    elif (
        free_percentage < 3
        or allocation_failures > 0
    ):
        severity = FindingSeverity.HIGH

    elif free_percentage < 5:
        severity = FindingSeverity.MEDIUM

    if severity is None:
        return None

    return Finding(
        finding_id=(
            f"{evidence.incident_id}"
            "-shared-pool-pressure"
        ),
        incident_id=evidence.incident_id,
        title="Shared Pool Memory Pressure",
        description=(
            f"Shared pool free memory is "
            f"{free_percentage:.2f}% "
            f"({free_mb} MB of {total_mb} MB). "
            f"Allocation failures: "
            f"{allocation_failures}."
        ),
        severity=severity,
        confidence=FindingConfidence.HIGH,
        evidence_ids=[
            evidence.evidence_id,
        ],
    )
