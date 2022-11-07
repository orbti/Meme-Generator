"""PDF Ingester module."""
from typing import List
import subprocess
import os
import random
import re

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

        # Open file parse each line into a QuoteModel object.
        f = open(tmp, 'r')
        quotes = []
        try:
            for text in f.readlines():
                text = text.strip('\n\r\x0c')
                print(text)
                if len(text) > 0:
                    parse = re.split(' \B', text)
                    print(parse)
                    for i in range(0, len(parse)-1, 2):
                        body = parse[i]
                        author = parse[i+1].strip('- ')
                        quote = QuoteModel(body, author)
                        quotes.append(quote)
        except Exception as e:
            print(e)
        finally:
            f.close()
            os.remove(tmp)
            print(quotes)

        return quotes
