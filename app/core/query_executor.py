from abc import ABC, abstractmethod
from typing import Any


class QueryExecutor(ABC):
    """
    Base contract for executing database queries.
    """

    @abstractmethod
    def execute(
        self,
        query: str,
    ) -> list[dict[str, Any]]:
        """
        Execute a query and return structured rows.
        """
        raise NotImplementedError
