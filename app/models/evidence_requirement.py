from enum import Enum

from pydantic import BaseModel

from app.models.evidence import EvidenceSource


class EvidencePriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class EvidenceRequirement(BaseModel):
    """
    Defines evidence required for an investigation.
    """

    evidence_type: str

    source: EvidenceSource

    priority: EvidencePriority = EvidencePriority.MEDIUM

    description: str

    reason: str
