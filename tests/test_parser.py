import pytest
from calculator.parser import InputParser # This will be created next
from calculator.exceptions import (
    InvalidFormatError,
    InvalidNumberError,
    InvalidOperatorError,
    CalculatorError
)

# Test Cases for Valid Inputs (Section 3.1)

def test_parse_valid_simple_addition_tc_parser_valid_001():
    """TC_PARSER_VALID_001: Test with a simple valid input: two positive integers and the '+' operator."""
    parser = InputParser()
    result = parser.parse("5 + 3")
    assert result == {"operand1": 5.0, "operator": "+", "operand2": 3.0}

def test_parse_valid_floats_multiplication_tc_parser_valid_002():
    """TC_PARSER_VALID_002: Test with floating-point numbers and the '*' operator."""
    parser = InputParser()
    result = parser.parse("3.14 * 2.5")
    assert result == {"operand1": 3.14, "operator": "*", "operand2": 2.5}

def test_parse_valid_negative_numbers_subtraction_tc_parser_valid_003():
    """TC_PARSER_VALID_003: Test with negative numbers and the '-' operator."""
    parser = InputParser()
    result = parser.parse("-7 - -2")
    assert result == {"operand1": -7.0, "operator": "-", "operand2": -2.0}

def test_parse_valid_division_mixed_types_tc_parser_valid_004():
    """TC_PARSER_VALID_004: Test with the '/' operator and mixed integer/float."""
    parser = InputParser()
    result = parser.parse("10 / 2.5")
    assert result == {"operand1": 10.0, "operator": "/", "operand2": 2.5}

def test_parse_valid_leading_trailing_spaces_tc_parser_valid_005():
    """TC_PARSER_VALID_005: Test with leading and trailing spaces."""
    parser = InputParser()
    result = parser.parse("  15 + 5  ")
    assert result == {"operand1": 15.0, "operator": "+", "operand2": 5.0}

def test_parse_valid_multiple_internal_spaces_tc_parser_valid_006():
    """TC_PARSER_VALID_006: Test with multiple spaces between components."""
    parser = InputParser()
    result = parser.parse("20   *    4")
    assert result == {"operand1": 20.0, "operator": "*", "operand2": 4.0}

def test_parse_valid_zero_operand_tc_parser_valid_007():
    """TC_PARSER_VALID_007: Test with zero as an operand."""
    parser = InputParser()
    result = parser.parse("0 - 100")
    assert result == {"operand1": 0.0, "operator": "-", "operand2": 100.0}

def test_parse_valid_leading_decimal_operand_tc_parser_valid_008():
    """TC_PARSER_VALID_008: Test with numbers that could be tricky for float conversion (e.g., '.5')."""
    parser = InputParser()
    result = parser.parse(".5 * 2")
    assert result == {"operand1": 0.5, "operator": "*", "operand2": 2.0}

def test_parse_valid_trailing_zeros_decimal_tc_parser_valid_009():
    """TC_PARSER_VALID_009: Test with numbers that have trailing zeros after decimal point."""
    parser = InputParser()
    result = parser.parse("10.000 + 5.0")
    assert result == {"operand1": 10.0, "operator": "+", "operand2": 5.0}

# Test Cases for Invalid Format Errors (Section 3.2)

def test_parse_invalid_format_empty_string_tc_parser_format_001():
    """TC_PARSER_FORMAT_001: Test with an empty input string."""
    parser = InputParser()
    with pytest.raises(InvalidFormatError, match="Error: Invalid input format. Expected 'number operator number'."):
        parser.parse("")

def test_parse_invalid_format_only_spaces_tc_parser_format_002():
    """TC_PARSER_FORMAT_002: Test with an input string containing only spaces."""
    parser = InputParser()
    with pytest.raises(InvalidFormatError, match="Error: Invalid input format. Expected 'number operator number'."):
        parser.parse("   ")

def test_parse_invalid_format_one_number_only_tc_parser_format_003():
    """TC_PARSER_FORMAT_003: Test with too few parts (one number only)."""
    parser = InputParser()
    with pytest.raises(InvalidFormatError, match="Error: Invalid input format. Expected 'number operator number'."):
        parser.parse("5")

def test_parse_invalid_format_number_and_operator_tc_parser_format_004():
    """TC_PARSER_FORMAT_004: Test with too few parts (number and operator)."""
    parser = InputParser()
    with pytest.raises(InvalidFormatError, match="Error: Invalid input format. Expected 'number operator number'."):
        parser.parse("5 +")

def test_parse_invalid_format_too_many_parts_tc_parser_format_005():
    """TC_PARSER_FORMAT_005: Test with too many parts."""
    parser = InputParser()
    with pytest.raises(InvalidFormatError, match="Error: Invalid input format. Expected 'number operator number'."):
        parser.parse("5 + 3 * 2")

def test_parse_invalid_format_only_operator_tc_parser_format_006():
    """TC_PARSER_FORMAT_006: Test with only an operator."""
    parser = InputParser()
    with pytest.raises(InvalidFormatError, match="Error: Invalid input format. Expected 'number operator number'."):
        parser.parse("+")

def test_parse_invalid_format_two_numbers_no_operator_tc_parser_format_007():
    """TC_PARSER_FORMAT_007: Test with two numbers, no operator."""
    parser = InputParser()
    with pytest.raises(InvalidFormatError, match="Error: Invalid input format. Expected 'number operator number'."):
        parser.parse("10 20")

# Test Cases for Invalid Number Errors (Section 3.3)

def test_parse_invalid_number_non_numeric_first_operand_tc_parser_number_001():
    """TC_PARSER_NUMBER_001: Test with a non-numeric first operand."""
    parser = InputParser()
    with pytest.raises(InvalidNumberError, match="Error: Invalid number: 'abc'."):
        parser.parse("abc + 5")

def test_parse_invalid_number_non_numeric_second_operand_tc_parser_number_002():
    """TC_PARSER_NUMBER_002: Test with a non-numeric second operand."""
    parser = InputParser()
    with pytest.raises(InvalidNumberError, match="Error: Invalid number: 'xyz'."):
        parser.parse("10 * xyz")

def test_parse_invalid_number_malformed_first_operand_tc_parser_number_003():
    """TC_PARSER_NUMBER_003: Test with a malformed number (e.g., multiple decimal points) as the first operand."""
    parser = InputParser()
    with pytest.raises(InvalidNumberError, match="Error: Invalid number: '1.2.3'."):
        parser.parse("1.2.3 + 4")

def test_parse_invalid_number_malformed_second_operand_tc_parser_number_004():
    """TC_PARSER_NUMBER_004: Test with a malformed number as the second operand."""
    parser = InputParser()
    with pytest.raises(InvalidNumberError, match="Error: Invalid number: '1..2'."):
        parser.parse("4 / 1..2")

def test_parse_invalid_number_symbol_operand_tc_parser_number_005():
    """TC_PARSER_NUMBER_005: Test with an operand that is just a symbol (not an operator)."""
    parser = InputParser()
    with pytest.raises(InvalidNumberError, match="Error: Invalid number: '@'."):
        parser.parse("@ + 5")

def test_parse_invalid_number_contains_non_numeric_chars_tc_parser_number_006():
    """TC_PARSER_NUMBER_006: Test with a number containing non-numeric characters."""
    parser = InputParser()
    with pytest.raises(InvalidNumberError, match="Error: Invalid number: '12a3'."):
        parser.parse("12a3 / 3")

# Test Cases for Invalid Operator Errors (Section 3.4)

def test_parse_invalid_operator_unsupported_percent_tc_parser_operator_001():
    """TC_PARSER_OPERATOR_001: Test with an unsupported operator (e.g., '%')."""
    parser = InputParser()
    with pytest.raises(InvalidOperatorError, match="Error: Invalid operator: '%'. Supported operators are \\+, -, \\*, /."):
        parser.parse("10 % 2")

def test_parse_invalid_operator_unsupported_caret_tc_parser_operator_002():
    """TC_PARSER_OPERATOR_002: Test with another unsupported operator (e.g., '^')."""
    parser = InputParser()
    with pytest.raises(InvalidOperatorError, match="Error: Invalid operator: '\\^'. Supported operators are \\+, -, \\*, /."):
        parser.parse("2 ^ 3")

def test_parse_invalid_operator_unsupported_double_star_tc_parser_operator_003():
    """TC_PARSER_OPERATOR_003: Test with a multi-character unsupported operator."""
    parser = InputParser()
    with pytest.raises(InvalidOperatorError, match="Error: Invalid operator: '\\*\\*'. Supported operators are \\+, -, \\*, /."):
        parser.parse("10 ** 2")

def test_parse_invalid_operator_non_symbol_operator_tc_parser_operator_004():
    """TC_PARSER_OPERATOR_004: Test with a non-symbol operator."""
    parser = InputParser()
    with pytest.raises(InvalidOperatorError, match="Error: Invalid operator: 'add'. Supported operators are \\+, -, \\*, /."):
        parser.parse("10 add 5")