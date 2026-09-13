from app.models.finding import Finding

from app.models.root_cause import RootCause

from app.root_cause.shared_pool import (
    analyze_shared_pool_root_cause,
)


def analyze_root_causes(
    findings: list[Finding],
) -> list[RootCause]:

    """
    Analyze findings and generate
    probable root causes.
    """

    root_causes: list[RootCause] = []

    shared_pool_root_cause = (
        analyze_shared_pool_root_cause(
            findings
        )
    )

    if shared_pool_root_cause is not None:

        root_causes.append(
            shared_pool_root_cause
        )

    return root_causes
