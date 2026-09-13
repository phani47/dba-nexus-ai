from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class EvidenceSource(str, Enum):
    DATABASE = "database"
    OS = "os"
    LOG = "log"
    MONITORING = "monitoring"


class EvidenceStatus(str, Enum):
    COLLECTED = "collected"
    FAILED = "failed"
    PARTIAL = "partial"


class Evidence(BaseModel):
    """
    Standard evidence contract for DBA Nexus AI.
    """

    evidence_id: str

    incident_id: str

    source: EvidenceSource

    evidence_type: str

    collected_at: datetime = Field(
        default_factory=datetime.now,
    )

    status: EvidenceStatus = EvidenceStatus.COLLECTED

    data: dict[str, Any] = Field(
        default_factory=dict,
    )

    error_message: str | None = None
