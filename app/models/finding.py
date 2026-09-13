from enum import Enum

from pydantic import BaseModel


class FindingSeverity(str, Enum):

    LOW = "low"

    MEDIUM = "medium"

    HIGH = "high"

    CRITICAL = "critical"


class FindingConfidence(str, Enum):

    LOW = "low"

    MEDIUM = "medium"

    HIGH = "high"


class Finding(BaseModel):
    """
    Standard finding generated from
    evidence correlation.
    """

    finding_id: str

    incident_id: str

    title: str

    description: str

    severity: FindingSeverity

    confidence: FindingConfidence

    evidence_ids: list[str]
