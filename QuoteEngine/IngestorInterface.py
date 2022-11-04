"""Ingester Interface Module."""
from abc import ABC, abstractmethod

from .QuoteModel import QuoteModel
from typing import List


class IngestorInterface(ABC):
    """Abstract class Ingestor Interface.
    
    Interface to pass to specific Ingestor classes.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Class method to check if file extension is in allowed list."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method to pass to other Ingestor classes."""
        pass
