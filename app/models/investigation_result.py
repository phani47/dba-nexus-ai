from datetime import datetime

from pydantic import BaseModel, Field

from app.models.evidence import Evidence
from app.models.finding import Finding
from app.models.incident import Incident
from app.models.playbook import Playbook


class InvestigationResult(BaseModel):
    """
    Final result of a DBA Nexus AI investigation.
    """

    incident: Incident

    playbook: Playbook | None = None

    evidence: list[Evidence] = Field(
        default_factory=list,
    )

    findings: list[Finding] = Field(
        default_factory=list,
    )

    started_at: datetime = Field(
        default_factory=datetime.now,
    )

    completed_at: datetime | None = None

    status: str = "completed"
