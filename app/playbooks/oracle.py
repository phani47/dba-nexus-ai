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
