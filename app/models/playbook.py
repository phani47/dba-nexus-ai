from typing import List

from pydantic import BaseModel, Field

from app.models.incident import DatabaseType, Severity


class InvestigationPhase(BaseModel):
    name: str
    description: str
    evidence_items: List[str] = Field(default_factory=list)


class Hypothesis(BaseModel):
    name: str
    description: str


class Playbook(BaseModel):
    playbook_id: str
    name: str

    database_type: DatabaseType

    error_code: str

    incident_category: str

    severity: Severity

    description: str

    initial_evidence: List[str] = Field(
        default_factory=list
    )

    hypotheses: List[Hypothesis] = Field(
        default_factory=list
    )

    phases: List[InvestigationPhase] = Field(
        default_factory=list
    )
