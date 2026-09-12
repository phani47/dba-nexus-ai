from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class DatabaseType(str, Enum):
    ORACLE = "oracle"
    POSTGRESQL = "postgresql"
    MONGODB = "mongodb"


class Severity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class Incident(BaseModel):
    """Represents a database incident received by DBA Nexus AI."""

    incident_id: str = Field(
        ...,
        description="Unique identifier for the incident",
    )

    database_name: str = Field(
        ...,
        description="Name of the affected database",
    )

    database_type: DatabaseType = Field(
        ...,
        description="Database technology",
    )

    error_code: str = Field(
        ...,
        description="Database error code",
    )

    timestamp: datetime = Field(
        default_factory=datetime.now,
        description="Time when the incident occurred",
    )

    severity: Severity = Field(
        default=Severity.HIGH,
        description="Incident severity",
    )

    message: str | None = Field(
        default=None,
        description="Full incident message",
    )
