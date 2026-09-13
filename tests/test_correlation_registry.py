from app.correlation.registry import (
    get_matching_rules,
)

from app.models.evidence import (
    Evidence,
    EvidenceSource,
)


def test_find_shared_pool_rule():

    evidence = Evidence(

        evidence_id=(
            "INC-001-shared_pool_summary"
        ),

        incident_id="INC-001",

        source=EvidenceSource.DATABASE,

        evidence_type=(
            "shared_pool_summary"
        ),

        data={},

    )

    rules = get_matching_rules(
        evidence
    )

    assert len(rules) == 1
def test_unknown_evidence_returns_no_rules():

    evidence = Evidence(

        evidence_id=(
            "INC-001-unknown"
        ),

        incident_id="INC-001",

        source=EvidenceSource.DATABASE,

        evidence_type="unknown_evidence",

        data={},

    )

    rules = get_matching_rules(
        evidence
    )

    assert rules == []
