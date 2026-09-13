from app.correlation.registry import (
    get_matching_rules,
)

from app.models.evidence import Evidence

from app.models.finding import Finding


def analyze_evidence(
    evidence_items: list[Evidence],
) -> list[Finding]:

    """
    Analyze collected evidence using
    registered correlation rules.
    """

    findings: list[Finding] = []

    for evidence in evidence_items:

        rules = get_matching_rules(
            evidence
        )

        for rule in rules:

            finding = rule.analyze(
                evidence
            )

            if finding is not None:

                findings.append(
                    finding
                )

    return findings
