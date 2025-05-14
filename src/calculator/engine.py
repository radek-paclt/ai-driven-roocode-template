from typing import Literal
from src.calculator.exceptions import DivisionByZeroError, CalculatorError

Operator = Literal["+", "-", "*", "/"]

class CalculationEngine:
    """
    A simple calculation engine that performs basic arithmetic operations.
    """
    def calculate(
        self,
        operand1: float,
        operator: Operator,
        operand2: float
    ) -> float:
        """
        Performs a basic arithmetic operation on two operands.

        Args:
            operand1: The first number (float).
            operator: The arithmetic operator ("+", "-", "*", "/").
            operand2: The second number (float).

        Returns:
            The result of the calculation (float).

        Raises:
            DivisionByZeroError: If division by zero is attempted.
            CalculatorError: If an unknown operator is provided.
        """
        if operator == "+":
            return operand1 + operand2
        elif operator == "-":
            return operand1 - operand2
        elif operator == "*":
            return operand1 * operand2
        elif operator == "/":
            if operand2 == 0.0:
                raise DivisionByZeroError("Error: Division by zero is not allowed.")
            return operand1 / operand2
        else:
            # This case should ideally not be reached if the InputParser validates operators.
            # However, as a defensive measure and per LLD-ERR-003 for engine-level unknown operator.
            raise CalculatorError(f"Error: Internal - Unknown operator '{operator}' received by CalculationEngine.")