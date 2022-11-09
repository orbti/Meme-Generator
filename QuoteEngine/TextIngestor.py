"""Text Ingester module."""
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Text Ingester Class object."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Class Method to parse Text file type.

        Method to check file type and then 
        parse file into list of Quote objects.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quotes = []
        # Open file parse each line into a QuoteModel object.
        with open(path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip('\n\r').strip().strip('ï»¿')
                if len(line) > 0:
                    parse = line.split('-')
                    quote = QuoteModel(parse[0], parse[1])
                    quotes.append(quote)

        return quotes
