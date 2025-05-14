---
title: "Input Parser Module - Low-Level Design"
version: "0.1.0"
status: "Draft"
created_by: "architect"
created_date: "2025-05-14T04:57:00Z" # Approximate current UTC time
last_modified_by: "architect"
last_modified_date: "2025-05-14T04:57:00Z"
related_tasks: ["ARCH-LLD-PARSER-004"]
relevant_links:
  - "../hld/HLD-MAIN-001_main_architecture.md"
  - "../specifications/SPEC-MAIN-001_console_calculator_main_specification.md"
  - "./LLD-IO-002_user_interface.md"
  - "./LLD-ERR-003_error_handling.md"
  - "../../project_postulates.md"
tags: ["lld", "parser", "input-validation", "python", "calculator"]
parent_document: "../hld/HLD-MAIN-001_main_architecture.md"
child_documents: []
related_concepts: ["string_manipulation", "type_conversion", "exception_handling", "input_validation"]
project_type_tags: ["cli-app", "python"]
visibility: "internal"
---

# Input Parser Module - Low-Level Design

## 1. Component Overview

### 1.1. Purpose and Scope
This document provides the Low-Level Design (LLD) for the `InputParser` module of the Python Console Calculator application. The `InputParser` is responsible for processing raw string input from the user (via the `ConsoleUI`), validating its format, parsing it into numerical operands and a string operator, and handling various input errors by raising specific custom exceptions.

The scope of this LLD includes:
*   The internal structure of the `InputParser` (e.g., a class with methods).
*   Detailed algorithms for parsing and validating user input.
*   Specification of how custom exceptions (`InvalidFormatError`, `InvalidNumberError`, `InvalidOperatorError`) are used for error reporting, consistent with [LLD-ERR-003_error_handling.md](./LLD-ERR-003_error_handling.md).
*   The public interface the `InputParser` provides to the `ConsoleUI`.

This LLD adheres to the responsibilities outlined in the [HLD-MAIN-001_main_architecture.md](../hld/HLD-MAIN-001_main_architecture.md) (Section 5.2) and the input/error requirements from [SPEC-MAIN-001_console_calculator_main_specification.md](../specifications/SPEC-MAIN-001_console_calculator_main_specification.md).

### 1.2. Relationship to Other Components
*   **`ConsoleUI`**: Consumes the `InputParser` by calling its `parse` method. It expects either a dictionary of parsed components on success or will handle exceptions raised by the parser on failure.
*   **`ErrorHandling` (Custom Exceptions)**: The `InputParser` uses custom exception classes defined in [LLD-ERR-003_error_handling.md](./LLD-ERR-003_error_handling.md) to signal parsing errors.

## 2. Detailed Design

### 2.1. Component Structure
The `InputParser` will be implemented as a Python class.

```python
# Conceptual Python definition of the InputParser class
# Actual exceptions will be imported from the exceptions module.

# from ..exceptions import InvalidFormatError, InvalidNumberError, InvalidOperatorError

class InputParser:
    """
    Parses and validates user input strings for the calculator.
    """

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
        # Detailed logic will be specified in section 2.4 Algorithms and Logic
        pass
```

### 2.2. Supported Operators
The parser will validate the operator against the following list of supported operators:
*   `+` (Addition)
*   `-` (Subtraction)
*   `*` (Multiplication)
*   `/` (Division)

### 2.3. Data Structures
*   **Input**: `input_string: str` - Raw user input.
*   **Intermediate**: `parts: list[str]` - List of strings after splitting the input.
*   **Output (Success)**: `dict` - `{'operand1': float, 'operator': str, 'operand2': float}`
*   **Output (Failure)**: Raises one of the custom exceptions.

### 2.4. Algorithms and Logic

#### 2.4.1. `parse(self, input_string: str) -> dict` Method Logic
1.  **Trim Whitespace**:
    *   Remove leading and trailing whitespace from `input_string`.
    *   Example: `"  10 + 5  "` becomes `"10 + 5"`.

2.  **Handle Empty Input**:
    *   If the trimmed `input_string` is empty, raise `InvalidFormatError("Error: Invalid input format. Expected 'number operator number'.")`. This aligns with the error message for general invalid format as per [SPEC-MAIN-001_console_calculator_main_specification.md#section-8](../specifications/SPEC-MAIN-001_console_calculator_main_specification.md#section-8).

3.  **Split Input String**:
    *   Split the trimmed `input_string` by spaces into a list of parts.
    *   Example: `"10 + 5"` becomes `['10', '+', '5']`.
    *   Example: `"10  +    5"` (multiple spaces) becomes `['10', '', '+', '', '', '5']` if using simple `split(' ')`. A more robust approach is to split by whitespace, which handles multiple spaces better, e.g., `input_string.split()`. This will result in `['10', '+', '5']`.

4.  **Validate Number of Parts**:
    *   Check if the number of parts is exactly 3 (operand1, operator, operand2).
    *   If not 3, raise `InvalidFormatError("Error: Invalid input format. Expected 'number operator number'.")`.

5.  **Extract and Validate Operand 1**:
    *   The first part (`parts[0]`) is `operand1_str`.
    *   Attempt to convert `operand1_str` to a `float`.
    *   If `ValueError` occurs during conversion, raise `InvalidNumberError(f"Error: Invalid number: '{operand1_str}'.")`.

6.  **Extract and Validate Operator**:
    *   The second part (`parts[1]`) is `operator_str`.
    *   Check if `operator_str` is one of the supported operators (`+`, `-`, `*`, `/`).
    *   If not, raise `InvalidOperatorError(f"Error: Invalid operator: '{operator_str}'. Supported operators are +, -, *, /.")`.

7.  **Extract and Validate Operand 2**:
    *   The third part (`parts[2]`) is `operand2_str`.
    *   Attempt to convert `operand2_str` to a `float`.
    *   If `ValueError` occurs during conversion, raise `InvalidNumberError(f"Error: Invalid number: '{operand2_str}'.")`.

8.  **Return Parsed Data**:
    *   If all validations pass, return a dictionary:
      ```python
      {
          "operand1": float_operand1,
          "operator": operator_str,
          "operand2": float_operand2
      }
      ```

## 3. Interface Specifications

### 3.1. Provided Interface

*   **Class**: `InputParser`
*   **Method**: `parse(self, input_string: str) -> dict`
    *   **Description**: Parses a raw user input string into its constituent numerical operands and operator string.
    *   **Parameters**:
        *   `input_string (str)`: The raw string provided by the user.
    *   **Returns (on success)**:
        A dictionary with the following structure:
        ```python
        {
            "operand1": float,  # The first numerical operand
            "operator": str,    # The operator string (+, -, *, /)
            "operand2": float   # The second numerical operand
        }
        ```
    *   **Raises (on failure)**:
        *   `InvalidFormatError`: If the input string does not conform to the "number operator number" structure, or if the input is empty.
        *   `InvalidNumberError`: If either of the operand parts cannot be converted to a valid floating-point number.
        *   `InvalidOperatorError`: If the operator part is not one of the recognized operators.
        The message of the raised exception will be the user-facing error message as defined in [SPEC-MAIN-001_console_calculator_main_specification.md#section-8](../specifications/SPEC-MAIN-001_console_calculator_main_specification.md#section-8) and [LLD-ERR-003_error_handling.md](./LLD-ERR-003_error_handling.md).

## 4. Data Design
(Covered in 2.3 Data Structures)

## 5. Behavior Specifications (Pythonic Pseudocode)

```python
# Assumes custom exceptions are defined and importable
# from ..exceptions import InvalidFormatError, InvalidNumberError, InvalidOperatorError

class InputParser:
    SUPPORTED_OPERATORS = ["+", "-", "*", "/"]

    def parse(self, input_string: str) -> dict:
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

```

## 6. Error Handling
The `InputParser` signals errors by raising specific custom exceptions:
*   `InvalidFormatError`: For issues with the overall structure of the input (e.g., wrong number of components, empty input after trimming).
    *   Message: `"Error: Invalid input format. Expected 'number operator number'."`
*   `InvalidNumberError`: When a part expected to be a number cannot be converted to `float`.
    *   Message: `f"Error: Invalid number: '{value_that_failed}'.`
*   `InvalidOperatorError`: When the operator token is not one of the supported operators.
    *   Message: `f"Error: Invalid operator: '{operator_token}'. Supported operators are +, -, *, /."`

These exceptions and their messages are consistent with [LLD-ERR-003_error_handling.md](./LLD-ERR-003_error_handling.md) and [SPEC-MAIN-001_console_calculator_main_specification.md](../specifications/SPEC-MAIN-001_console_calculator_main_specification.md). The `ConsoleUI` will be responsible for catching these exceptions and displaying their messages.

## 7. Security Considerations
*   The `InputParser`'s primary role in security is input validation. By attempting to convert operands to `float` and strictly checking operators, it prevents arbitrary string data from propagating further into the system (e.g., to a calculation engine that might be vulnerable if it received non-numeric data).
*   The use of `float()` conversion inherently handles many malformed number inputs by raising `ValueError`, which is then caught and translated into a custom `InvalidNumberError`.
*   This design does not involve `eval()` or direct execution of user input, minimizing risks of code injection.

## 8. Testing Considerations
Unit tests for the `InputParser.parse` method should cover:
*   **Valid Inputs**:
    *   Simple integers: `"1 + 2"`
    *   Floating-point numbers: `"3.14 * 2.0"`
    *   Negative numbers: `"-5 - -10"`
    *   Input with leading/trailing/multiple spaces: `"  10  /  2  "`
    *   All supported operators.
*   **Invalid Format Errors**:
    *   Empty string: `""`
    *   String with only spaces: `"   "`
    *   Too few parts: `"1 +"`
    *   Too many parts: `"1 + 2 * 3"`
*   **Invalid Number Errors**:
    *   Non-numeric operand1: `"abc + 5"`
    *   Non-numeric operand2: `"5 * xyz"`
    *   Partially numeric: `"1.2.3 + 4"`
*   **Invalid Operator Errors**:
    *   Unsupported operator: `"10 % 2"`
    *   Missing operator: `"10 2"` (this would be caught as InvalidFormatError due to 2 parts)

Tests should use `pytest.raises` (or equivalent) to assert that the correct exception is raised with the correct message for each error scenario. For success cases, tests should verify the content of the returned dictionary.

## 9. Future Considerations
*   **More Complex Expressions**: If order of operations or functions were introduced, the parsing logic (splitting by space) would need a complete overhaul (e.g., Shunting-yard algorithm, AST generation).
*   **Variable Support**: Would require recognizing variable names and potentially a symbol table.
*   **Different Delimiters**: If delimiters other than space were allowed, the splitting logic would need to be adjusted.