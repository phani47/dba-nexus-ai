from app.models.evidence import EvidenceSource
from app.models.evidence_requirement import (
    EvidencePriority,
    EvidenceRequirement,
)
from app.models.incident import DatabaseType, Severity
from app.models.playbook import (
    Hypothesis,
    InvestigationPhase,
    Playbook,
)


ORA_04031_PLAYBOOK = Playbook(
    playbook_id="oracle-ora-04031",

    name="ORA-04031 Shared Memory Investigation",

    database_type=DatabaseType.ORACLE,

    error_code="ORA-04031",

    incident_category="MEMORY",

    severity=Severity.HIGH,

    description=(
        "Investigation workflow for Oracle ORA-04031 "
        "unable to allocate shared memory errors."
    ),

    initial_evidence=[
        "Database Status",
        "Memory Configuration",
        "Shared Pool Summary",
        "ORA-04031 Error Details",
        "OS Memory Summary",
    ],

    evidence_requirements=[
        EvidenceRequirement(
            evidence_type="shared_pool_summary",
            source=EvidenceSource.DATABASE,
            priority=EvidencePriority.CRITICAL,
            description=(
                "Collect shared pool usage, free memory, "
                "and allocation failure information."
            ),
            reason=(
                "Determine whether shared pool exhaustion "
                "or memory pressure caused ORA-04031."
            ),
        ),

        EvidenceRequirement(
            evidence_type="memory_configuration",
            source=EvidenceSource.DATABASE,
            priority=EvidencePriority.HIGH,
            description=(
                "Collect SGA, shared pool, and memory "
                "configuration parameters."
            ),
            reason=(
                "Determine whether memory configuration "
                "contributed to the allocation failure."
            ),
        ),

        EvidenceRequirement(
            evidence_type="os_memory_summary",
            source=EvidenceSource.OS,
            priority=EvidencePriority.HIGH,
            description=(
                "Collect host memory usage, available memory, "
                "and swap activity."
            ),
            reason=(
                "Determine whether operating system memory "
                "pressure contributed to the incident."
            ),
        ),

        EvidenceRequirement(
            evidence_type="sql_parse_metrics",
            source=EvidenceSource.DATABASE,
            priority=EvidencePriority.HIGH,
            description=(
                "Collect hard parse activity, library cache "
                "statistics, and parse-related metrics."
            ),
            reason=(
                "Determine whether excessive hard parsing "
                "is creating shared pool pressure."
            ),
        ),

        EvidenceRequirement(
            evidence_type="error_timeline",
            source=EvidenceSource.LOG,
            priority=EvidencePriority.MEDIUM,
            description=(
                "Collect ORA-04031 events and related errors "
                "around the incident timestamp."
            ),
            reason=(
                "Identify related database events and establish "
                "an incident timeline."
            ),
        ),
    ],

    hypotheses=[
        Hypothesis(
            name="Shared Pool Exhaustion",
            description=(
                "Shared pool memory is exhausted due to "
                "high memory usage."
            ),
        ),

        Hypothesis(
            name="Memory Fragmentation",
            description=(
                "Shared pool memory is fragmented and cannot "
                "allocate a sufficiently large contiguous chunk."
            ),
        ),

        Hypothesis(
            name="Excessive Hard Parsing",
            description=(
                "High hard parsing activity is creating excessive "
                "pressure on the shared pool."
            ),
        ),

        Hypothesis(
            name="Cursor Explosion",
            description=(
                "Excessive cursor usage is consuming shared pool memory."
            ),
        ),
    ],

    phases=[
        InvestigationPhase(
            name="Initial Triage",
            description=(
                "Collect minimum evidence required to understand "
                "the memory incident."
            ),
            evidence_items=[
                "Database Status",
                "Memory Configuration",
                "Shared Pool Summary",
                "OS Memory Summary",
            ],
        ),

        InvestigationPhase(
            name="Memory Investigation",
            description=(
                "Investigate shared pool pressure and memory allocation."
            ),
            evidence_items=[
                "Shared Pool Usage",
                "Library Cache Metrics",
                "Memory Allocation Failures",
            ],
        ),

        InvestigationPhase(
            name="SQL Investigation",
            description=(
                "Investigate SQL parsing and cursor behavior."
            ),
            evidence_items=[
                "Hard Parse Rate",
                "Cursor Usage",
                "Top SQL by Parse Activity",
            ],
        ),
    ],
)
