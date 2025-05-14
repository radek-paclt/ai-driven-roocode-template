# src/calculator/main.py

from src.calculator.engine import CalculationEngine
from src.calculator.parser import InputParser
from src.calculator.ui import run_calculator_loop
# Custom exceptions might be imported if specific top-level handling is needed,
# but run_calculator_loop is expected to manage its operational exceptions.
# from src.calculator.exceptions import CalculatorError 

def start_calculator_app():
    """
    Initializes the CalculationEngine and InputParser,
    then starts the calculator's user interface loop.
    """
    # Instantiate the core components
    engine = CalculationEngine()
    parser = InputParser()

    # Start the user interface loop
    # The run_calculator_loop function is expected to handle the REPL,
    # including user input, parsing, calculation, and displaying results.
    # It should also handle internal operational errors gracefully.
    print("Welcome to the Console Calculator!")
    print("You can type expressions like '1 + 1', or 'quit'/'exit' to leave.")
    
    try:
        run_calculator_loop(parser, engine)
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully for a clean exit from the console
        print("\nCalculator exited by user. Goodbye!")
    except Exception as e:
        # Catch any other unexpected errors that might occur outside run_calculator_loop
        # or if run_calculator_loop re-raises an unhandled exception.
        print(f"\nAn unexpected error occurred at the top level: {e}")
        print("Calculator shutting down.")
    finally:
        print("Thank you for using the calculator.")


if __name__ == "__main__":
    # This makes the script executable.
    # When run directly, it will call the start_calculator_app function.
    start_calculator_app()