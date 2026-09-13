SHARED_POOL_SUMMARY_QUERY = """
SELECT
    ROUND(
        SUM(CASE
            WHEN pool = 'shared pool'
            THEN bytes
            ELSE 0
        END) / 1024 / 1024,
        2
    ) AS shared_pool_total_mb,

    ROUND(
        SUM(CASE
            WHEN pool = 'shared pool'
             AND name = 'free memory'
            THEN bytes
            ELSE 0
        END) / 1024 / 1024,
        2
    ) AS shared_pool_free_mb

FROM v$sgastat;
"""


MEMORY_CONFIGURATION_QUERY = """
SELECT
    name,
    value
FROM v$parameter
WHERE name IN (
    'memory_target',
    'memory_max_target',
    'sga_target',
    'sga_max_size',
    'shared_pool_size',
    'pga_aggregate_target'
)
ORDER BY name;
"""


LIBRARY_CACHE_QUERY = """
SELECT
    namespace,
    pins,
    pinhits,
    reloads,
    invalidations
FROM v$librarycache
ORDER BY reloads DESC;
"""


PARSE_STATISTICS_QUERY = """
SELECT
    name,
    value
FROM v$sysstat
WHERE name IN (
    'parse count (total)',
    'parse count (hard)',
    'session cursor cache hits'
);
"""


CURSOR_USAGE_QUERY = """
SELECT
    name,
    value
FROM v$sysstat
WHERE name IN (
    'opened cursors cumulative',
    'opened cursors current'
);
"""
