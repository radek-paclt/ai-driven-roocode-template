from .exceptions import (
    InvalidFormatError,
    InvalidNumberError,
    InvalidOperatorError
)

class InputParser:
    """
    Parses and validates user input strings for the calculator.
    """
    SUPPORTED_OPERATORS = ["+", "-", "*", "/"]

    def __init__(self):
        """
        Initializes the InputParser.
        Currently, no specific initialization state is needed.
        """
        pass

    def parse(self, input_string: str) -> dict:
        """
        Parses the raw input string into operands and an operator.

        Args:
            input_string: The raw string input from the user.

        Returns:
            A dictionary on success:
            {
                "operand1": float,
                "operator": str,
                "operand2": float
            }

        Raises:
            InvalidFormatError: If the input string format is incorrect.
            InvalidNumberError: If an operand cannot be converted to a valid number.
            InvalidOperatorError: If an unrecognized or unsupported operator is provided.
        """
        trimmed_input = input_string.strip()

        if not trimmed_input:
            raise InvalidFormatError("Error: Invalid input format. Expected 'number operator number'.")

        parts = trimmed_input.split() # Splits by any whitespace and removes empty strings

        if len(parts) != 3:
            raise InvalidFormatError("Error: Invalid input format. Expected 'number operator number'.")

        operand1_str, operator_str, operand2_str = parts[0], parts[1], parts[2]

        try:
            operand1_float = float(operand1_str)
        except ValueError:
            raise InvalidNumberError(f"Error: Invalid number: '{operand1_str}'.")

        if operator_str not in self.SUPPORTED_OPERATORS:
            raise InvalidOperatorError(f"Error: Invalid operator: '{operator_str}'. Supported operators are +, -, *, /.")

        try:
            operand2_float = float(operand2_str)
        except ValueError:
            raise InvalidNumberError(f"Error: Invalid number: '{operand2_str}'.")

        return {
            "operand1": operand1_float,
            "operator": operator_str,
            "operand2": operand2_float
        }