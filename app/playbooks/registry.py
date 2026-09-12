from app.models.incident import DatabaseType
from app.models.playbook import Playbook
from app.playbooks.oracle import ORA_04031_PLAYBOOK


PLAYBOOKS: list[Playbook] = [
    ORA_04031_PLAYBOOK,
]


def get_playbook(
    database_type: DatabaseType,
    error_code: str,
) -> Playbook | None:
    """
    Return the matching investigation playbook.
    """

    normalized_error_code = error_code.upper().strip()

    for playbook in PLAYBOOKS:
        if (
            playbook.database_type == database_type
            and playbook.error_code == normalized_error_code
        ):
            return playbook

    return None
