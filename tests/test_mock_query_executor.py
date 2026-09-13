from app.core.mock_query_executor import (
    MockQueryExecutor,
)
from app.core.oracle_queries import (
    SHARED_POOL_SUMMARY_QUERY,
)


def test_mock_executor_returns_shared_pool_data():

    executor = MockQueryExecutor()

    rows = executor.execute(
        SHARED_POOL_SUMMARY_QUERY,
    )

    assert len(rows) == 1

    assert (
        rows[0]["shared_pool_total_mb"]
        == 10240
    )

    assert (
        rows[0]["shared_pool_free_mb"]
        == 128
    )


def test_mock_executor_returns_empty_for_unknown_query():

    executor = MockQueryExecutor()

    rows = executor.execute(
        "SELECT * FROM unknown_table"
    )

    assert rows == []
