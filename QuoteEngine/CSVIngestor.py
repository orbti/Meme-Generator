"""CSV Ingestor module."""
from typing import List
import pandas as pd

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """CSV Ingestor Class object."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Class Method to parse CSV file type.

        Method to check file type and then 
        parse file into list of Quote objects.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quotes = []
        df = pd.read_csv(path, header=0)

        for index, row in df.iterrows():
            quote = QuoteModel(row.body, row.author)
            quotes.append(quote)

        return quotes
