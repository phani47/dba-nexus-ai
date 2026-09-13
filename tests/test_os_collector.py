from app.collectors.os import (
    OSMemoryCollector,
)

from app.models.evidence import EvidenceSource

from app.models.evidence_requirement import (
    EvidencePriority,
    EvidenceRequirement,
)

from app.models.incident import (
    DatabaseType,
    Incident,
    Severity,
)


def test_os_memory_collector():

    incident = Incident(
        incident_id="INC-OS-001",
        database_name="PRODDB",
        database_type=DatabaseType.ORACLE,
        error_code="ORA-04031",
        severity=Severity.HIGH,
        message="Unable to allocate bytes of shared memory",
    )

    requirement = EvidenceRequirement(
        evidence_type="os_memory_summary",
        source=EvidenceSource.OS,
        priority=EvidencePriority.HIGH,
        description="Collect OS memory summary.",
        reason="Check operating system memory pressure.",
    )

    collector = OSMemoryCollector()

    assert collector.can_collect(
        requirement
    )

    evidence = collector.collect(
        incident,
        requirement,
    )

    assert evidence.source == EvidenceSource.OS

    assert (
        evidence.data[
            "memory_usage_percent"
        ]
        == 96.8
    )

    assert (
        evidence.data[
            "swap_used_mb"
        ]
        == 4096
    )
