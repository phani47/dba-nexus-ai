from app.correlation.base import (
    BaseCorrelationRule,
)

from app.correlation.shared_pool_rule import (
    SharedPoolCorrelationRule,
)

from app.models.evidence import Evidence


def get_correlation_rules() -> list[
    BaseCorrelationRule
]:

    """
    Return available evidence
    correlation rules.
    """

    return [

        SharedPoolCorrelationRule(),

    ]


def get_matching_rules(
    evidence: Evidence,
) -> list[BaseCorrelationRule]:

    """
    Return correlation rules capable
    of analyzing the given evidence.
    """

    return [

        rule

        for rule in get_correlation_rules()

        if rule.can_analyze(evidence)

    ]
