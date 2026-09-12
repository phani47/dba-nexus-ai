from app.models.incident import DatabaseType
from app.playbooks.registry import get_playbook


def test_find_oracle_ora_04031_playbook():
    playbook = get_playbook(
        database_type=DatabaseType.ORACLE,
        error_code="ORA-04031",
    )

    assert playbook is not None
    assert playbook.playbook_id == "oracle-ora-04031"
    assert playbook.error_code == "ORA-04031"


def test_error_code_normalization():
    playbook = get_playbook(
        database_type=DatabaseType.ORACLE,
        error_code="ora-04031",
    )

    assert playbook is not None
    assert playbook.name == "ORA-04031 Shared Memory Investigation"


def test_unknown_playbook_returns_none():
    playbook = get_playbook(
        database_type=DatabaseType.ORACLE,
        error_code="ORA-99999",
    )

    assert playbook is None
