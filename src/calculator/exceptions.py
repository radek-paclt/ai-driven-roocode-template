class CalculatorError(Exception):
    """Base class for all calculator application specific errors."""
    def __init__(self, message: str):
        super().__init__(message)
        # The message is intended to be the user-facing error message
        # as defined in the specification.

class InvalidInputError(CalculatorError):
    """Base class for errors related to invalid user input."""
    pass

class InvalidFormatError(InvalidInputError):
    """Raised when the input string format is incorrect."""
    pass

class InvalidNumberError(InvalidInputError):
    """Raised when an operand cannot be converted to a valid number."""
    pass

class InvalidOperatorError(InvalidInputError):
    """Raised when an unrecognized or unsupported operator is provided."""
    pass

class DivisionByZeroError(CalculatorError):
    """Raised when an attempt is made to divide by zero."""
    pass