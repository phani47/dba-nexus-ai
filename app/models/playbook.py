from pydantic import BaseModel, Field

from app.models.evidence_requirement import EvidenceRequirement
from app.models.incident import DatabaseType, Severity


class InvestigationPhase(BaseModel):
    name: str
    description: str
    evidence_items: list[str] = Field(default_factory=list)


class Hypothesis(BaseModel):
    name: str
    description: str


class Playbook(BaseModel):
    """
    Machine-readable investigation playbook.
    """

    playbook_id: str
    name: str

    database_type: DatabaseType
    error_code: str

    incident_category: str
    severity: Severity

    description: str

    initial_evidence: list[str] = Field(
        default_factory=list,
    )

    evidence_requirements: list[EvidenceRequirement] = Field(
        default_factory=list,
    )

    hypotheses: list[Hypothesis] = Field(
        default_factory=list,
    )

    phases: list[InvestigationPhase] = Field(
        default_factory=list,
    )
