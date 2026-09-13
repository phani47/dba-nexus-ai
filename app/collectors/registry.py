from app.collectors.base import BaseCollector
from app.collectors.oracle import (
    OracleSharedPoolCollector,
)
from app.core.mock_query_executor import (
    MockQueryExecutor,
)
from app.models.evidence_requirement import (
    EvidenceRequirement,
)


def get_collectors() -> list[BaseCollector]:
    """
    Create and return the available evidence collectors.

    MockQueryExecutor is currently used for local
    development and automated testing.
    """

    query_executor = MockQueryExecutor()

    return [
        OracleSharedPoolCollector(
            query_executor=query_executor,
        ),
    ]


def get_collector(
    requirement: EvidenceRequirement,
) -> BaseCollector | None:
    """
    Return a collector capable of collecting
    the requested evidence.
    """

    for collector in get_collectors():

        if collector.can_collect(requirement):
            return collector

    return None
