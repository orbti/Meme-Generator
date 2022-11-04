"""PDF Ingester module."""
from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """PDF Ingester Class object."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Class Method to parse PDF file type.

        Method to check file type and then 
        parse file into list of Quote objects.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        tmp = f'./tmp/{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        quotes = []
        # Open file parse each line into a QuoteModel object.
        with open(tmp, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split('-')
                    quote = QuoteModel(parse[0], parse[1])
                    quotes.append(quote)
        os.remove(tmp)

        return quotes
