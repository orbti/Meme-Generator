"""Quote Model module."""

class QuoteModel():
    """Quote Model class object."""

    def __init__(self, body, author):
        """Initialize QuoteModel object.
        
        :param info: Body of a quote and associated author.
        """
        self.body = body
        self.author = author

    def __str__(self):
        """Return `str(self)`."""
        return f'{self.body} - {self.author}'

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f'QuoteModel(body={self.body}, author={self.author})'
