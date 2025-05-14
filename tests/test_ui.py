import pytest
from unittest.mock import Mock, patch, call

from src.calculator.ui import (
    _format_result,
    _process_user_command,
    run_calculator_loop,
    InputParser,  # Protocol
    CalculationEngine  # Protocol
)
from src.calculator.exceptions import (
    CalculatorError,
    InvalidFormatError,
    InvalidNumberError,
    InvalidOperatorError,
    DivisionByZeroError
)

# Unit Tests for Helper Functions

class TestFormatResult:
    # Test Case ID: UTC_UI_FR_001 (adapted)
    def test_format_result_positive_integer_float(self):
        assert _format_result(15.0) == "15"

    # Test Case ID: UTC_UI_FR_002
    def test_format_result_float_with_decimals(self):
        assert _format_result(7.5) == "7.5"

    # Test Case ID: UTC_UI_FR_003 (adapted)
    def test_format_result_zero(self):
        assert _format_result(0.0) == "0"

    # Test Case ID: UTC_UI_FR_004
    def test_format_result_negative_float(self):
        assert _format_result(-5.25) == "-5.25"

    def test_format_result_negative_integer_float(self):
        assert _format_result(-10.0) == "-10"

class TestProcessUserCommand:
    # Test Case ID: UTC_UI_PUC_001
    def test_process_user_command_exit_lowercase(self):
        assert _process_user_command("exit") is True

    # Test Case ID: UTC_UI_PUC_002
    def test_process_user_command_quit_lowercase(self):
        assert _process_user_command("quit") is True

    # Test Case ID: UTC_UI_PUC_003
    def test_process_user_command_exit_uppercase(self):
        assert _process_user_command("EXIT") is True

    # Test Case ID: UTC_UI_PUC_004
    def test_process_user_command_quit_mixed_case(self):
        assert _process_user_command("QuIt") is True

    # Test Case ID: UTC_UI_PUC_005
    def test_process_user_command_non_exit_command(self):
        assert _process_user_command("5 + 3") is False

    # Test Case ID: UTC_UI_PUC_006
    def test_process_user_command_empty_string(self):
        assert _process_user_command("") is False

    # Test Case ID: UTC_UI_PUC_007
    def test_process_user_command_partial_exit_command(self):
        assert _process_user_command("exi") is False

# Integration Tests for run_calculator_loop

@patch('src.calculator.ui._get_user_input')
@patch('src.calculator.ui._display_output')
def test_repl_successful_calculation_and_display(mock_display_output, mock_get_user_input):
    # Test Case ID: ITC_UI_REPL_CALC_001 (adapted for direct float result and spec format)
    mock_get_user_input.side_effect = ["5 + 3", "exit"]
    
    mock_parser = Mock(spec=InputParser)
    mock_parser.parse.return_value = {"operand1": 5.0, "operator": "+", "operand2": 3.0}
    
    mock_engine = Mock(spec=CalculationEngine)
    mock_engine.calculate.return_value = 8.0
    
    run_calculator_loop(mock_parser, mock_engine)
    
    expected_calls_display = [
        call("calc> "),
        call("8"),  # Result formatted as "8" not "8.0"
        call("calc> "),
        call("Exiting calculator. Goodbye!")
    ]
    mock_display_output.assert_has_calls(expected_calls_display)
    mock_parser.parse.assert_called_once_with("5 + 3")
    mock_engine.calculate.assert_called_once_with(5.0, "+", 3.0)

@patch('src.calculator.ui._get_user_input')
@patch('src.calculator.ui._display_output')
def test_repl_calculation_float_numbers(mock_display_output, mock_get_user_input):
    # Test Case ID: ITC_UI_REPL_CALC_002 (adapted)
    mock_get_user_input.side_effect = ["2.5 * 2", "exit"]
    mock_parser = Mock(spec=InputParser)
    mock_parser.parse.return_value = {"operand1": 2.5, "operator": "*", "operand2": 2.0}
    mock_engine = Mock(spec=CalculationEngine)
    mock_engine.calculate.return_value = 5.0
    
    run_calculator_loop(mock_parser, mock_engine)
    
    expected_calls_display = [
        call("calc> "),
        call("5"), # Result formatted as "5"
        call("calc> "),
        call("Exiting calculator. Goodbye!")
    ]
    mock_display_output.assert_has_calls(expected_calls_display)
    mock_parser.parse.assert_called_once_with("2.5 * 2")
    mock_engine.calculate.assert_called_once_with(2.5, "*", 2.0)

@patch('src.calculator.ui._get_user_input')
@patch('src.calculator.ui._display_output')
def test_repl_multiple_calculations(mock_display_output, mock_get_user_input):
    # Test Case ID: ITC_UI_REPL_CALC_003 (adapted)
    mock_get_user_input.side_effect = ["10 / 4", "3 - 1", "quit"]
    
    mock_parser = Mock(spec=InputParser)
    # Configure side_effect for multiple calls to parse
    mock_parser.parse.side_effect = [
        {"operand1": 10.0, "operator": "/", "operand2": 4.0}, # For "10 / 4"
        {"operand1": 3.0, "operator": "-", "operand2": 1.0}  # For "3 - 1"
    ]
    
    mock_engine = Mock(spec=CalculationEngine)
    # Configure side_effect for multiple calls to calculate
    mock_engine.calculate.side_effect = [
        2.5, # Result for 10.0 / 4.0
        2.0  # Result for 3.0 - 1.0
    ]
    
    run_calculator_loop(mock_parser, mock_engine)
    
    expected_calls_display = [
        call("calc> "),
        call("2.5"),
        call("calc> "),
        call("2"),
        call("calc> "),
        call("Exiting calculator. Goodbye!")
    ]
    mock_display_output.assert_has_calls(expected_calls_display)
    
    expected_calls_parse = [
        call("10 / 4"),
        call("3 - 1")
    ]
    mock_parser.parse.assert_has_calls(expected_calls_parse)
    
    expected_calls_engine = [
        call(10.0, "/", 4.0),
        call(3.0, "-", 1.0)
    ]
    mock_engine.calculate.assert_has_calls(expected_calls_engine)

@patch('src.calculator.ui._get_user_input')
@patch('src.calculator.ui._display_output')
def test_repl_exit_command_terminates_loop(mock_display_output, mock_get_user_input):
    # Test Case ID: ITC_UI_REPL_EXIT_001
    mock_get_user_input.return_value = "exit"
    mock_parser = Mock(spec=InputParser)
    mock_engine = Mock(spec=CalculationEngine)
    
    run_calculator_loop(mock_parser, mock_engine)
    
    expected_calls_display = [
        call("calc> "),
        call("Exiting calculator. Goodbye!")
    ]
    mock_display_output.assert_has_calls(expected_calls_display)
    mock_parser.parse.assert_not_called()
    mock_engine.calculate.assert_not_called()

@patch('src.calculator.ui._get_user_input')
@patch('src.calculator.ui._display_output')
def test_repl_exit_command_uppercase_terminates_loop(mock_display_output, mock_get_user_input):
    # Test Case ID: ITC_UI_REPL_EXIT_002
    mock_get_user_input.return_value = "QUIT"
    mock_parser = Mock(spec=InputParser)
    mock_engine = Mock(spec=CalculationEngine)

    run_calculator_loop(mock_parser, mock_engine)

    expected_calls_display = [
        call("calc> "),
        call("Exiting calculator. Goodbye!")
    ]
    mock_display_output.assert_has_calls(expected_calls_display)

@patch('src.calculator.ui._get_user_input')
@patch('src.calculator.ui._display_output')
def test_repl_exit_command_with_whitespace(mock_display_output, mock_get_user_input):
    # Test Case ID: ITC_UI_REPL_EXIT_003
    mock_get_user_input.return_value = "  exit  "
    mock_parser = Mock(spec=InputParser)
    mock_engine = Mock(spec=CalculationEngine)

    run_calculator_loop(mock_parser, mock_engine)

    expected_calls_display = [
        call("calc> "),
        call("Exiting calculator. Goodbye!")
    ]
    mock_display_output.assert_has_calls(expected_calls_display)
    # Verify that parse is not called, meaning _process_user_command worked on trimmed input
    mock_parser.parse.assert_not_called()


@patch('src.calculator.ui._get_user_input')
@patch('src.calculator.ui._display_output')
def test_repl_parser_invalid_format_error(mock_display_output, mock_get_user_input):
    # Test Case ID: ITC_UI_REPL_ERR_PARSE_001
    mock_get_user_input.side_effect = ["5 +", "exit"]
    mock_parser = Mock(spec=InputParser)
    error_message = "Error: Invalid input format. Expected 'number operator number'."
    mock_parser.parse.side_effect = InvalidFormatError(error_message)
    mock_engine = Mock(spec=CalculationEngine)
    
    run_calculator_loop(mock_parser, mock_engine)
    
    expected_calls_display = [
        call("calc> "),
        call(error_message),
        call("calc> "),
        call("Exiting calculator. Goodbye!")
    ]
    mock_display_output.assert_has_calls(expected_calls_display)
    mock_parser.parse.assert_called_once_with("5 +")
    mock_engine.calculate.assert_not_called()

@patch('src.calculator.ui._get_user_input')
@patch('src.calculator.ui._display_output')
def test_repl_parser_invalid_number_error(mock_display_output, mock_get_user_input):
    # Test Case ID: ITC_UI_REPL_ERR_PARSE_002
    mock_get_user_input.side_effect = ["abc + 5", "exit"]
    mock_parser = Mock(spec=InputParser)
    error_message = "Error: Invalid number: 'abc'."
    mock_parser.parse.side_effect = InvalidNumberError(error_message)
    mock_engine = Mock(spec=CalculationEngine)

    run_calculator_loop(mock_parser, mock_engine)

    expected_calls_display = [
        call("calc> "),
        call(error_message),
        call("calc> "),
        call("Exiting calculator. Goodbye!")
    ]
    mock_display_output.assert_has_calls(expected_calls_display)
    mock_parser.parse.assert_called_once_with("abc + 5")
    mock_engine.calculate.assert_not_called()

@patch('src.calculator.ui._get_user_input')
@patch('src.calculator.ui._display_output')
def test_repl_parser_invalid_operator_error(mock_display_output, mock_get_user_input):
    # Test Case ID: ITC_UI_REPL_ERR_PARSE_003
    mock_get_user_input.side_effect = ["5 % 2", "exit"]
    mock_parser = Mock(spec=InputParser)
    error_message = "Error: Invalid operator: '%'. Supported operators are +, -, *, /."
    mock_parser.parse.side_effect = InvalidOperatorError(error_message)
    mock_engine = Mock(spec=CalculationEngine)

    run_calculator_loop(mock_parser, mock_engine)

    expected_calls_display = [
        call("calc> "),
        call(error_message),
        call("calc> "),
        call("Exiting calculator. Goodbye!")
    ]
    mock_display_output.assert_has_calls(expected_calls_display)
    mock_parser.parse.assert_called_once_with("5 % 2")
    mock_engine.calculate.assert_not_called()

@patch('src.calculator.ui._get_user_input')
@patch('src.calculator.ui._display_output')
def test_repl_parser_empty_input_error(mock_display_output, mock_get_user_input):
    # Test Case ID: ITC_UI_REPL_ERR_PARSE_004
    # Assumes parser raises InvalidFormatError for empty string
    mock_get_user_input.side_effect = ["", "exit"]
    mock_parser = Mock(spec=InputParser)
    error_message = "Error: Invalid input format. Expected 'number operator number'."
    # Configure mock_parser to raise error for empty string
    def parse_side_effect(input_str):
        if input_str == "":
            raise InvalidFormatError(error_message)
        # Fallback for other inputs if any (though test only provides "" then "exit")
        return {"operand1": 1.0, "operator": "+", "operand2": 1.0} 
    mock_parser.parse.side_effect = parse_side_effect
    mock_engine = Mock(spec=CalculationEngine)

    run_calculator_loop(mock_parser, mock_engine)

    expected_calls_display = [
        call("calc> "),
        call(error_message), # Error for empty input
        call("calc> "),      # Prompt for "exit"
        call("Exiting calculator. Goodbye!")
    ]
    mock_display_output.assert_has_calls(expected_calls_display)
    mock_parser.parse.assert_called_once_with("") # Called with empty string
    mock_engine.calculate.assert_not_called()


@patch('src.calculator.ui._get_user_input')
@patch('src.calculator.ui._display_output')
def test_repl_engine_division_by_zero_error(mock_display_output, mock_get_user_input):
    # Test Case ID: ITC_UI_REPL_ERR_ENGINE_001
    mock_get_user_input.side_effect = ["10 / 0", "exit"]
    mock_parser = Mock(spec=InputParser)
    mock_parser.parse.return_value = {"operand1": 10.0, "operator": "/", "operand2": 0.0}
    mock_engine = Mock(spec=CalculationEngine)
    error_message = "Error: Division by zero is not allowed."
    mock_engine.calculate.side_effect = DivisionByZeroError(error_message)
    
    run_calculator_loop(mock_parser, mock_engine)
    
    expected_calls_display = [
        call("calc> "),
        call(error_message),
        call("calc> "),
        call("Exiting calculator. Goodbye!")
    ]
    mock_display_output.assert_has_calls(expected_calls_display)
    mock_parser.parse.assert_called_once_with("10 / 0")
    mock_engine.calculate.assert_called_once_with(10.0, "/", 0.0)

@patch('src.calculator.ui._get_user_input')
@patch('src.calculator.ui._display_output')
def test_repl_input_with_whitespace_calculation(mock_display_output, mock_get_user_input):
    # Test Case ID: ITC_UI_REPL_INPUT_001 (adapted)
    mock_get_user_input.side_effect = ["  7 * 2  ", "exit"]
    mock_parser = Mock(spec=InputParser)
    mock_parser.parse.return_value = {"operand1": 7.0, "operator": "*", "operand2": 2.0}
    mock_engine = Mock(spec=CalculationEngine)
    mock_engine.calculate.return_value = 14.0
    
    run_calculator_loop(mock_parser, mock_engine)
    
    expected_calls_display = [
        call("calc> "),
        call("14"), # Result formatted as "14"
        call("calc> "),
        call("Exiting calculator. Goodbye!")
    ]
    mock_display_output.assert_has_calls(expected_calls_display)
    # Input to parse should be trimmed
    mock_parser.parse.assert_called_once_with("7 * 2") 
    mock_engine.calculate.assert_called_once_with(7.0, "*", 2.0)

@patch('src.calculator.ui._get_user_input')
@patch('src.calculator.ui._display_output')
def test_repl_unexpected_general_exception(mock_display_output, mock_get_user_input):
    """Test handling of unexpected non-CalculatorError exceptions."""
    mock_get_user_input.side_effect = ["1 + 1", "exit"]
    mock_parser = Mock(spec=InputParser)
    mock_parser.parse.return_value = {"operand1": 1.0, "operator": "+", "operand2": 1.0}
    
    mock_engine = Mock(spec=CalculationEngine)
    unexpected_error_message = "A very unexpected error!"
    mock_engine.calculate.side_effect = RuntimeError(unexpected_error_message) # A generic exception
    
    run_calculator_loop(mock_parser, mock_engine)
    
    expected_calls_display = [
        call("calc> "),
        call(f"Error: An unexpected system error occurred: {unexpected_error_message}"),
        call("calc> "),
        call("Exiting calculator. Goodbye!")
    ]
    mock_display_output.assert_has_calls(expected_calls_display)
    mock_parser.parse.assert_called_once_with("1 + 1")
    mock_engine.calculate.assert_called_once_with(1.0, "+", 1.0)