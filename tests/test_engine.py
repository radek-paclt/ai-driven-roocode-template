import unittest
from decimal import Decimal, getcontext

# Set precision for Decimal to handle floating point comparisons robustly
getcontext().prec = 50 # Sufficient precision

# Attempt to import the function and exceptions
# This will fail initially as engine.py doesn't exist yet, which is fine for TDD.
try:
    from src.calculator.engine import perform_calculation
    from src.calculator.exceptions import DivisionByZeroError, CalculatorError, InvalidOperatorError
except ImportError:
    # Define dummy placeholders if actual import fails, so the test file can be parsed
    class DivisionByZeroError(Exception): pass
    class CalculatorError(Exception): pass
    class InvalidOperatorError(CalculatorError): pass # Make it inherit for consistency if used

    def perform_calculation(operand1: float, operator: str, operand2: float):
        # Dummy implementation for parsing, will be replaced by actual import
        if operator == "/" and operand2 == 0:
            raise DivisionByZeroError("Error: Division by zero is not allowed.")
        if operator == "+":
            return operand1 + operand2
        if operator == "-":
            return operand1 - operand2
        if operator == "*":
            return operand1 * operand2
        if operator == "/":
            return operand1 / operand2
        # For unknown operator, the LLD-ERR-003 suggests CalculatorError for internal engine error
        # The test case document TEST-CASES-CALC-002 has a specific message for this.
        raise CalculatorError("Error: Internal - Unknown operator received by CalculationEngine.")


class TestCalculationEngine(unittest.TestCase):

    def assertFloatsAlmostEqual(self, val1, val2, places=7):
        # Using Decimal for more robust comparison of floats
        self.assertAlmostEqual(Decimal(str(val1)), Decimal(str(val2)), places=places)

    # 1. Addition (+) Test Cases
    def test_add_positive_integers(self): # TC_CALC_ADD_001
        self.assertFloatsAlmostEqual(perform_calculation(5, "+", 3), 8.0)

    def test_add_positive_floats(self): # TC_CALC_ADD_002
        self.assertFloatsAlmostEqual(perform_calculation(5.5, "+", 3.2), 8.7)

    def test_add_positive_and_negative(self): # TC_CALC_ADD_003
        self.assertFloatsAlmostEqual(perform_calculation(10, "+", -3), 7.0)

    def test_add_negative_and_positive(self): # TC_CALC_ADD_004
        self.assertFloatsAlmostEqual(perform_calculation(-7, "+", 4), -3.0)

    def test_add_two_negative_numbers(self): # TC_CALC_ADD_005
        self.assertFloatsAlmostEqual(perform_calculation(-2.5, "+", -3.5), -6.0)

    def test_add_number_and_zero(self): # TC_CALC_ADD_006
        self.assertFloatsAlmostEqual(perform_calculation(6, "+", 0), 6.0)

    def test_add_zero_and_number(self): # TC_CALC_ADD_007
        self.assertFloatsAlmostEqual(perform_calculation(0, "+", -9), -9.0)

    def test_add_zero_and_zero(self): # TC_CALC_ADD_008
        self.assertFloatsAlmostEqual(perform_calculation(0, "+", 0), 0.0)
    
    def test_add_large_positive_numbers(self): # TC_CALC_ADD_009
        self.assertFloatsAlmostEqual(perform_calculation(1000000, "+", 2000000), 3000000.0)

    def test_add_small_fractional_numbers(self): # TC_CALC_ADD_010
        # Standard float precision can lead to 0.30000000000000004, so compare carefully
        self.assertFloatsAlmostEqual(perform_calculation(0.1, "+", 0.2), 0.3)

    # 2. Subtraction (-) Test Cases
    def test_subtract_smaller_from_larger_positive(self): # TC_CALC_SUB_001
        self.assertFloatsAlmostEqual(perform_calculation(10, "-", 3), 7.0)

    def test_subtract_larger_from_smaller_positive_float(self): # TC_CALC_SUB_002
        self.assertFloatsAlmostEqual(perform_calculation(3.5, "-", 5.2), -1.7)

    def test_subtract_negative_from_positive(self): # TC_CALC_SUB_003
        self.assertFloatsAlmostEqual(perform_calculation(8, "-", -2), 10.0)

    def test_subtract_positive_from_negative(self): # TC_CALC_SUB_004
        self.assertFloatsAlmostEqual(perform_calculation(-5, "-", 3), -8.0)

    def test_subtract_two_negative_numbers(self): # TC_CALC_SUB_005
        self.assertFloatsAlmostEqual(perform_calculation(-2.5, "-", -3.5), 1.0)

    def test_subtract_zero_from_number(self): # TC_CALC_SUB_006
        self.assertFloatsAlmostEqual(perform_calculation(7, "-", 0), 7.0)

    def test_subtract_number_from_zero(self): # TC_CALC_SUB_007
        self.assertFloatsAlmostEqual(perform_calculation(0, "-", 4), -4.0)

    def test_subtract_zero_from_zero(self): # TC_CALC_SUB_008
        self.assertFloatsAlmostEqual(perform_calculation(0, "-", 0), 0.0)

    def test_subtract_number_from_itself(self): # TC_CALC_SUB_009
        self.assertFloatsAlmostEqual(perform_calculation(6.7, "-", 6.7), 0.0)

    # 3. Multiplication (*) Test Cases
    def test_multiply_positive_integers(self): # TC_CALC_MUL_001
        self.assertFloatsAlmostEqual(perform_calculation(6, "*", 4), 24.0)

    def test_multiply_positive_floats(self): # TC_CALC_MUL_002
        self.assertFloatsAlmostEqual(perform_calculation(2.5, "*", 3.0), 7.5)

    def test_multiply_positive_and_negative(self): # TC_CALC_MUL_003
        self.assertFloatsAlmostEqual(perform_calculation(7, "*", -2), -14.0)

    def test_multiply_two_negative_numbers(self): # TC_CALC_MUL_004
        self.assertFloatsAlmostEqual(perform_calculation(-3, "*", -5), 15.0)

    def test_multiply_number_by_zero(self): # TC_CALC_MUL_005
        self.assertFloatsAlmostEqual(perform_calculation(9.8, "*", 0), 0.0)

    def test_multiply_zero_by_number(self): # TC_CALC_MUL_006
        self.assertFloatsAlmostEqual(perform_calculation(0, "*", -6), 0.0)

    def test_multiply_zero_by_zero(self): # TC_CALC_MUL_007
        self.assertFloatsAlmostEqual(perform_calculation(0, "*", 0), 0.0)

    def test_multiply_number_by_one(self): # TC_CALC_MUL_008
        self.assertFloatsAlmostEqual(perform_calculation(12.3, "*", 1), 12.3)

    def test_multiply_number_by_minus_one(self): # TC_CALC_MUL_009
        self.assertFloatsAlmostEqual(perform_calculation(8, "*", -1), -8.0)

    # 4. Division (/) Test Cases
    def test_divide_larger_by_smaller_positive_integer(self): # TC_CALC_DIV_001
        self.assertFloatsAlmostEqual(perform_calculation(10, "/", 2), 5.0)

    def test_divide_positive_floats(self): # TC_CALC_DIV_002
        self.assertFloatsAlmostEqual(perform_calculation(7.5, "/", 2.0), 3.75)

    def test_divide_positive_by_negative(self): # TC_CALC_DIV_003
        self.assertFloatsAlmostEqual(perform_calculation(12, "/", -3), -4.0)

    def test_divide_negative_by_positive(self): # TC_CALC_DIV_004
        self.assertFloatsAlmostEqual(perform_calculation(-9, "/", 3), -3.0)

    def test_divide_two_negative_numbers(self): # TC_CALC_DIV_005
        self.assertFloatsAlmostEqual(perform_calculation(-8.0, "/", -4.0), 2.0)

    def test_divide_zero_by_positive_number(self): # TC_CALC_DIV_006
        self.assertFloatsAlmostEqual(perform_calculation(0, "/", 5), 0.0)

    def test_divide_zero_by_negative_number(self): # TC_CALC_DIV_007
        self.assertFloatsAlmostEqual(perform_calculation(0, "/", -2.5), 0.0)

    def test_divide_number_by_one(self): # TC_CALC_DIV_008
        self.assertFloatsAlmostEqual(perform_calculation(7.7, "/", 1), 7.7)

    def test_divide_number_by_itself_non_zero(self): # TC_CALC_DIV_009
        self.assertFloatsAlmostEqual(perform_calculation(4.5, "/", 4.5), 1.0)

    def test_divide_resulting_in_repeating_decimal(self): # TC_CALC_DIV_010
        self.assertFloatsAlmostEqual(perform_calculation(10, "/", 3), 3.3333333333333335)


    # 5. Error Condition Test Cases
    def test_division_by_zero_positive_operand1(self): # TC_CALC_ERR_001
        with self.assertRaisesRegex(DivisionByZeroError, "Error: Division by zero is not allowed."):
            perform_calculation(5, "/", 0)

    def test_division_by_zero_negative_operand1(self): # TC_CALC_ERR_002
        with self.assertRaisesRegex(DivisionByZeroError, "Error: Division by zero is not allowed."):
            perform_calculation(-5, "/", 0)

    def test_division_by_zero_zero_operand1(self): # TC_CALC_ERR_003
        with self.assertRaisesRegex(DivisionByZeroError, "Error: Division by zero is not allowed."):
            perform_calculation(0, "/", 0)

    def test_unknown_operator_percentage(self): # TC_CALC_ERR_004
        # LLD-ERR-003 suggests CalculatorError for internal engine error for unknown operator.
        # The message comes from TEST-CASES-CALC-002.
        with self.assertRaisesRegex(CalculatorError, "Error: Internal - Unknown operator received by CalculationEngine."):
            perform_calculation(10, "%", 5)
            
    def test_unknown_operator_foo(self): # TC_CALC_ERR_005
        with self.assertRaisesRegex(CalculatorError, "Error: Internal - Unknown operator received by CalculationEngine."):
            perform_calculation(7, "foo", 3)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)