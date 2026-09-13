from app.playbooks.oracle import ORA_04031_PLAYBOOK
from app.services.evidence_planner import (
    create_evidence_plan,
)


def test_evidence_plan_is_priority_ordered():
    plan = create_evidence_plan(
        ORA_04031_PLAYBOOK,
    )

    assert len(plan) == 5

    assert plan[0].priority.value == "critical"

    assert plan[0].evidence_type == "shared_pool_summary"

    assert plan[-1].priority.value == "medium"

    assert plan[-1].evidence_type == "error_timeline"
