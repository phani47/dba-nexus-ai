from typing import Any

from app.core.query_executor import QueryExecutor


class MockQueryExecutor(QueryExecutor):
    """
    Mock query executor used for
    development and automated testing.
    """

    def execute(
        self,
        query: str,
    ) -> list[dict[str, Any]]:

        if "v$sgastat" in query.lower():

            return [
                {
                    "shared_pool_total_mb": 10240,
                    "shared_pool_free_mb": 128,
                }
            ]

        return []
