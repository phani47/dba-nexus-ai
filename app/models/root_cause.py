from enum import Enum

from pydantic import BaseModel, Field


class RootCauseConfidence(str, Enum):

    LOW = "low"

    MEDIUM = "medium"

    HIGH = "high"


class RootCause(BaseModel):

    """
    Represents a probable root cause
    identified during investigation.
    """

    root_cause_id: str

    incident_id: str

    title: str

    description: str

    confidence: RootCauseConfidence

    supporting_finding_ids: list[str] = Field(
        default_factory=list,
    )
