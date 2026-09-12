from app.models.incident import Incident
from app.models.playbook import Playbook
from app.playbooks.registry import get_playbook


def select_playbook(
    incident: Incident,
) -> Playbook | None:
    """
    Select the appropriate investigation playbook
    for an incoming incident.
    """

    return get_playbook(
        database_type=incident.database_type,
        error_code=incident.error_code,
    )
