"""Docx Ingestor module."""
from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Docx Ingestor Class object."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Class Method to parse Docx file type.

        Method to check file type and then 
        parse file into list of Quote objects.
        """
        if not cls.can_ingest(path):
            raise 'Cannot ingest exeption'

        quotes = []
        doc = docx.Document(path)
        
        for para in doc.paragraphs:
            if para.text != '':
                parse = para.text.split('-')
                quote = QuoteModel(parse[0], parse[1])
                quotes.append(quote)
        return quotes
