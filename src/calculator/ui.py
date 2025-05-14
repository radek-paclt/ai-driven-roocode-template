from typing import Protocol, Dict, Any
from .exceptions import CalculatorError # Changed to relative import

# Define Protocols for dependency injection type hinting
class InputParser(Protocol):
    def parse(self, input_string: str) -> Dict[str, Any]:
        """
        Parses the raw user input string.
        Expected Return on Success:
        {
            "operand1": float,  # The first number
            "operator": str,    # The operator (+, -, *, /)
            "operand2": float   # The second number
        }
        Raises CalculatorError or its children on failure.
        """
        ...

class CalculationEngine(Protocol):
    def calculate(self, operand1: float, operator: str, operand2: float) -> float:
        """
        Performs the arithmetic calculation.
        Returns the calculated result (float) on success.
        Raises CalculatorError or its children on failure (e.g., DivisionByZeroError).
        """
        ...

# Helper Functions (internal to the module)
def _get_user_input() -> str:
    """Reads a line of text from the user."""
    return input()

def _display_output(message: str) -> None:
    """Prints a message to the console."""
    print(message)

def _format_result(result_value: float) -> str:
    """Formats the numerical result for display."""
    # For V1, simple string conversion is sufficient.
    # Ensure .0 for whole numbers for consistency if desired, e.g. 15.0
    if result_value == int(result_value):
        return str(int(result_value)) # As per spec examples, "8" not "8.0"
    return str(result_value)


def _process_user_command(input_str: str) -> bool:
    """
    Checks if the input is an exit command and handles it.
    Returns True if an exit command was processed, False otherwise.
    """
    normalized_input = input_str.lower()
    if normalized_input in ["exit", "quit"]:
        return True
    return False

# Public Function
def run_calculator_loop(parser: InputParser, engine: CalculationEngine) -> None:
    """
    Initializes and runs the main REPL.
    It takes instances of the InputParser and CalculationEngine as dependencies.
    """
    PROMPT_MESSAGE = "calc> "
    
    while True:
        _display_output(PROMPT_MESSAGE)
        raw_input_str = _get_user_input()
        trimmed_input = raw_input_str.strip()
        
        if _process_user_command(trimmed_input):
            break
            
        if not trimmed_input: # Handle empty input after stripping, if not an exit command
            # According to LLD-IO-002, parser handles empty input.
            # If parser is expected to raise InvalidFormatError for empty string,
            # this explicit check might be redundant, but good for clarity.
            # For now, let parser handle it.
            pass

        try:
            parsed_data = parser.parse(trimmed_input)
            
            operand1 = parsed_data["operand1"]
            operator_str = parsed_data["operator"]
            operand2 = parsed_data["operand2"]
            
            calculation_value = engine.calculate(operand1, operator_str, operand2)
            
            formatted_result = _format_result(calculation_value)
            _display_output(formatted_result)
            
        except CalculatorError as e:
            _display_output(str(e)) # Exception message already includes "Error: "
        except Exception as e:
            # Catch any other unexpected errors for robustness
            _display_output(f"Error: An unexpected system error occurred: {str(e)}")
            # Potentially log 'e' for debugging in a real application

    _display_output("Exiting calculator. Goodbye!")