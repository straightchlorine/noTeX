class NoTeXNoSubjectPathException(Exception):
    """Exception raised in case there is no subject path.

    Attributes:
        message - explanation
    """
    def __init__(self, message):
        super().__init__(message)
