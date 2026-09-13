from abc import ABC, abstractmethod

from app.models.evidence import Evidence
from app.models.finding import Finding


class BaseCorrelationRule(ABC):

    """
    Base interface for evidence
    correlation rules.
    """

    @abstractmethod
    def can_analyze(
        self,
        evidence: Evidence,
    ) -> bool:
        """
        Return True when this rule
        can analyze the evidence.
        """

        pass

    @abstractmethod
    def analyze(
        self,
        evidence: Evidence,
    ) -> Finding | None:
        """
        Analyze evidence and return
        a finding when applicable.
        """

        pass
