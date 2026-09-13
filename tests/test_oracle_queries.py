from app.core.oracle_queries import (
    CURSOR_USAGE_QUERY,
    LIBRARY_CACHE_QUERY,
    MEMORY_CONFIGURATION_QUERY,
    PARSE_STATISTICS_QUERY,
    SHARED_POOL_SUMMARY_QUERY,
)


def test_oracle_queries_are_defined():

    queries = [
        SHARED_POOL_SUMMARY_QUERY,
        MEMORY_CONFIGURATION_QUERY,
        LIBRARY_CACHE_QUERY,
        PARSE_STATISTICS_QUERY,
        CURSOR_USAGE_QUERY,
    ]

    assert len(queries) == 5

    for query in queries:
        assert query.strip()
        assert query.strip().upper().startswith(
            "SELECT"
        )


def test_shared_pool_query_uses_sgastat():

    assert "v$sgastat" in (
        SHARED_POOL_SUMMARY_QUERY.lower()
    )
