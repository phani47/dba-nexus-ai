from abc import ABC, abstractmethod

from app.models.evidence import Evidence
from app.models.evidence_requirement import (
    EvidenceRequirement,
)
from app.models.incident import Incident


class BaseCollector(ABC):
    """
    Base contract for all DBA Nexus AI
    evidence collectors.
    """

    @abstractmethod
    def can_collect(
        self,
        requirement: EvidenceRequirement,
    ) -> bool:
        """
        Return True if this collector can
        collect the requested evidence.
        """
        raise NotImplementedError

    @abstractmethod
    def collect(
        self,
        incident: Incident,
        requirement: EvidenceRequirement,
    ) -> Evidence:
        """
        Collect evidence for an incident.
        """
        raise NotImplementedError
