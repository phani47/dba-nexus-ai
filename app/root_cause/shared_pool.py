from app.models.finding import Finding
from app.models.root_cause import (
    RootCause,
    RootCauseConfidence,
)


def analyze_shared_pool_root_cause(
    findings: list[Finding],
) -> RootCause | None:

    """
    Determine whether the collected
    findings indicate shared pool
    exhaustion.
    """

    matching_findings = [

        finding

        for finding in findings

        if finding.title
        == "Shared Pool Memory Pressure"

    ]

    if not matching_findings:

        return None

    finding_ids = [

        finding.finding_id

        for finding in matching_findings

    ]

    return RootCause(

        root_cause_id=(
            f"{matching_findings[0].incident_id}"
            "-shared-pool-exhaustion"
        ),

        incident_id=(
            matching_findings[0].incident_id
        ),

        title="Shared Pool Exhaustion",

        description=(
            "Oracle shared pool memory pressure "
            "and allocation failures indicate "
            "probable shared pool exhaustion."
        ),

        confidence=RootCauseConfidence.HIGH,

        supporting_finding_ids=finding_ids,

    )
