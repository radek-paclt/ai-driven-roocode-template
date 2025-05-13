---
title: "Error Handling Module - Low-Level Design"
version: "0.1.0"
status: "Draft"
created_by: "architect"
created_date: "2025-05-13T23:18:00Z"
last_modified_by: "architect"
last_modified_date: "2025-05-13T23:18:00Z"
related_tasks: ["ARCH-LLD-ERR-003"]
relevant_links:
  - "../hld/HLD-MAIN-001_main_architecture.md"
  - "../specifications/SPEC-MAIN-001_console_calculator_main_specification.md"
  - "./LLD-CALC-001_calculator_module.md"
  - "./LLD-IO-002_user_interface.md"
  - "../../project_postulates.md"
tags: ["lld", "error-handling", "exceptions", "python", "calculator"]
parent_document: "../hld/HLD-MAIN-001_main_architecture.md"
child_documents: []
related_concepts: ["custom_exceptions", "exception_propagation", "error_reporting", "try_except"]
project_type_tags: ["cli-app", "python"]
visibility: "internal"
---

# Error Handling Module - Low-Level Design

## 1. Component Overview

### 1.1. Purpose and Scope
This document details the Low-Level Design (LLD) for the error handling mechanism of the Python Console Calculator application. The primary purpose is to establish a robust, clear, and centralized strategy for managing and reporting errors that occur during input parsing, validation, and calculation.

The scope of this LLD includes:
*   Definition of a hierarchy of custom Python exception classes.
*   Specification of how and when these exceptions are raised by components like the `InputParser` and `CalculationEngine`.
*   Description of how the `ConsoleUI` (REPL Handler) will catch these exceptions and present user-friendly error messages.

This design refines the conceptual error handling approach mentioned in the [HLD-MAIN-001_main_architecture.md](../hld/HLD-MAIN-001_main_architecture.md) by formalizing error signaling through custom exceptions, ensuring consistency with the error messages defined in [SPEC-MAIN-001_console_calculator_main_specification.md](../specifications/SPEC-MAIN-001_console_calculator_main_specification.md).

### 1.2. Relationship to Other Components
This error handling design provides a contract that other components will adhere to:
*   **`InputParser`**: Will raise specific input-related exceptions.
*   **`CalculationEngine`**: Will raise specific calculation-related exceptions.
*   **`ConsoleUI`**: Will catch these exceptions to inform the user.

This LLD implicitly suggests updates to the error signaling mechanisms described in [LLD-CALC-001_calculator_module.md](./LLD-CALC-001_calculator_module.md) and the expected error returns in [LLD-IO-002_user_interface.md](./LLD-IO-002_user_interface.md), moving from dictionary-based error returns to raising exceptions.

## 2. Detailed Design

### 2.1. Custom Exception Hierarchy
A hierarchy of custom exception classes will be defined to represent specific error conditions within the application. All custom exceptions will inherit from a base `CalculatorError` class, which itself inherits from Python's built-in `Exception` class.

```python
# Conceptual Python definition of the exception hierarchy

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
```

### 2.2. Exception Raising Strategy

Components responsible for validation or computation will raise these custom exceptions when an error is detected. The message passed to the exception constructor will be the user-friendly message defined in [SPEC-MAIN-001_console_calculator_main_specification.md#section-8](../specifications/SPEC-MAIN-001_console_calculator_main_specification.md#section-8).

#### 2.2.1. `InputParser`
The `InputParser` component will be responsible for raising exceptions related to input format and content.

*   **Invalid Input Format (General)** (e.g., wrong number of parts, empty input):
    *   Raises: `InvalidFormatError("Error: Invalid input format. Expected 'number operator number'.")`
*   **Invalid Number (Operand1 or Operand2)** (e.g., `abc + 5` or `5 + xyz`):
    *   Raises: `InvalidNumberError(f"Error: Invalid number: '{part_causing_error}'.")`
*   **Invalid Operator** (e.g., `5 % 3`):
    *   Raises: `InvalidOperatorError(f"Error: Invalid operator: '{operator_token}'. Supported operators are +, -, *, /.")`

#### 2.2.2. `CalculationEngine`
The `CalculationEngine` component will be responsible for raising exceptions related to arithmetic calculations.

*   **Division by Zero** (e.g., `10 / 0`):
    *   Raises: `DivisionByZeroError("Error: Division by zero is not allowed.")`

### 2.3. Exception Handling Strategy (in `ConsoleUI`)
The main application loop within the `ConsoleUI` module will implement `try-except` blocks to catch the custom exceptions raised by the `InputParser` and `CalculationEngine`.

*   A `try` block will encompass the calls to `parser.parse()` and `engine.calculate()`.
*   `except` blocks will catch `CalculatorError` (or potentially more specific exceptions if different handling logic per exception type is needed, though for V1, catching the base `CalculatorError` and using its message is sufficient).
*   Upon catching an exception, the `ConsoleUI` will extract the message from the exception object (which is the user-friendly message) and display it to the user. The existing `_format_error` helper in `ConsoleUI` (which prepends "Error: ") might be redundant if the exception messages already contain this prefix as per the spec, or it can be adjusted. For consistency with the spec's user messages, the exceptions should be initialized with the full "Error: ..." string.

## 3. Interface Specifications

The primary "interface" for this error handling module is the definition of the custom exception classes themselves:
*   `CalculatorError(Exception)`
*   `InvalidInputError(CalculatorError)`
*   `InvalidFormatError(InvalidInputError)`
*   `InvalidNumberError(InvalidInputError)`
*   `InvalidOperatorError(InvalidInputError)`
*   `DivisionByZeroError(CalculatorError)`

Each exception class is instantiated with a single string argument: the user-facing error message.

## 4. Data Design
The key data element in this design is the **error message string**. This string is:
1.  Defined in the [SPEC-MAIN-001_console_calculator_main_specification.md](../specifications/SPEC-MAIN-001_console_calculator_main_specification.md).
2.  Passed as an argument when instantiating a custom exception.
3.  Stored within the exception object.
4.  Retrieved by the `ConsoleUI` when an exception is caught.
5.  Displayed to the user.

## 5. Behavior Specifications (Pseudocode Examples)

This section illustrates how components would use the exception-based error handling.

### 5.1. `InputParser` (Conceptual Update)

```pseudocode
FUNCTION parse_expression(inputString):
    parts = SPLIT_STRING(inputString, " ")
    
    IF LENGTH(parts) != 3:
        RAISE InvalidFormatError("Error: Invalid input format. Expected 'number operator number'.")
    END IF
    
    TRY:
        operand1 = CONVERT_TO_FLOAT(parts[0])
    CATCH ConversionError: // Assuming CONVERT_TO_FLOAT raises a generic conversion error
        RAISE InvalidNumberError("Error: Invalid number: '" + parts[0] + "'.")
    END TRY
    
    operator_token = parts[1]
    
    TRY:
        operand2 = CONVERT_TO_FLOAT(parts[2])
    CATCH ConversionError:
        RAISE InvalidNumberError("Error: Invalid number: '" + parts[2] + "'.")
    END TRY
    
    IF operator_token NOT IN ["+", "-", "*", "/"]:
        RAISE InvalidOperatorError("Error: Invalid operator: '" + operator_token + "'. Supported operators are +, -, *, /.")
    END IF
    
    RETURN { operand1: operand1, operator: operator_token, operand2: operand2 } // Success case
END FUNCTION
```

### 5.2. `CalculationEngine` (Conceptual Update)

```pseudocode
FUNCTION perform_calculation(operand1: float, operator: string, operand2: float):
    IF operator == "+":
        RETURN operand1 + operand2
    ELSE IF operator == "-":
        RETURN operand1 - operand2
    ELSE IF operator == "*":
        RETURN operand1 * operand2
    ELSE IF operator == "/":
        IF operand2 == 0.0:
            RAISE DivisionByZeroError("Error: Division by zero is not allowed.")
        ELSE:
            RETURN operand1 / operand2
        END IF
    // This else case implies an internal error if parser allowed an invalid operator through
    ELSE: 
        // For robustness, though ideally unreachable if parser is correct
        RAISE CalculatorError("Error: Internal - Unknown operator received by CalculationEngine.") 
    END IF
END FUNCTION
```

### 5.3. `ConsoleUI` (Conceptual Update to `run_calculator_loop`)

```pseudocode
FUNCTION run_calculator_loop(parser_instance, engine_instance):
    CONSTANT PROMPT_MESSAGE = "calc> "
    
    WHILE TRUE:
        _display_output(PROMPT_MESSAGE)
        raw_input = _get_user_input()
        trimmed_input = TRIM_WHITESPACE(raw_input)
        
        IF _process_user_command(trimmed_input) == TRUE: // Exit command handled
            BREAK LOOP
        END IF
        
        TRY:
            // Delegate to InputParser
            parsed_data = parser_instance.parse(trimmed_input) 
            // parsed_data now only contains success values: {operand1, operator, operand2}
            
            operand1 = parsed_data["operand1"]
            operator_str = parsed_data["operator"]
            operand2 = parsed_data["operand2"]
            
            // Delegate to CalculationEngine
            calculation_value = engine_instance.calculate(operand1, operator_str, operand2)
            // calculation_value is the direct float result on success
            
            formatted_result = _format_result(calculation_value)
            _display_output(formatted_result)
            
        CATCH CalculatorError as e: // Catches any of our custom calculator errors
            // The message 'e' already contains "Error: ..." prefix from instantiation
            _display_output(STRING(e)) // Display the exception's message
            // The _format_error helper might no longer be needed if exceptions carry the full message.
            // Or, it could be used if exceptions only carry the core message part.
            // For this LLD, assume exceptions carry the full user-facing message.

        // Optional: Catch other unexpected errors for robustness
        // CATCH Exception as general_e:
        //     _display_output("Error: An unexpected system error occurred.")
        //     // Log general_e for debugging
            
        END TRY
    END WHILE
    
    _display_output("Exiting calculator. Goodbye!")
END FUNCTION
```

## 6. Error Handling (Summary of this LLD's Strategy)
This LLD establishes a formal error handling strategy based on custom Python exceptions:
1.  A defined hierarchy of exceptions (`CalculatorError`, `InvalidInputError`, etc.) provides semantic meaning to error conditions.
2.  Error-producing components (`InputParser`, `CalculationEngine`) signal errors by *raising* these exceptions, initialized with user-friendly messages from the specification.
3.  The main application controller (`ConsoleUI`) uses `try-except` blocks to *catch* these exceptions and display their messages to the user.
4.  This approach separates normal program flow from error handling flow, leading to potentially cleaner code in the components that can now directly return results on success without packaging them in a dictionary with an error flag.

## 7. Security Considerations
*   Using custom exceptions for error handling does not inherently introduce new security vulnerabilities.
*   It contributes to a more robust and predictable error flow, which can indirectly support security by ensuring errors are handled gracefully rather than leading to unexpected states.
*   The actual security of input handling still relies on the `InputParser`'s validation logic, as detailed in its LLD and the HLD.

## 8. Testing Considerations
*   **Unit Tests for `InputParser` and `CalculationEngine`**:
    *   Must be updated/written to assert that the correct custom exceptions are `raised` under specific error conditions (e.g., using `pytest.raises`).
    *   Tests should also verify that the messages of the raised exceptions match those defined in the specification.
*   **Unit/Integration Tests for `ConsoleUI`**:
    *   When testing `run_calculator_loop` (likely with mocked dependencies for parser and engine), configure the mocks to `raise` the defined custom exceptions.
    *   Verify that the `ConsoleUI` correctly catches these exceptions and that the `_display_output` mock is called with the appropriate error message extracted from the exception.

## 9. Impact on Other LLDs
This LLD proposes a change from dictionary-based error reporting to exception-based error handling. This will require conceptual or actual updates to:
*   **[`LLD-CALC-001_calculator_module.md`](./LLD-CALC-001_calculator_module.md)**: The `perform_calculation` function should `raise` exceptions instead of returning an error dictionary.
*   **[`LLD-IO-002_user_interface.md`](./LLD-IO-002_user_interface.md)**: The `run_calculator_loop` function in `ConsoleUI` should use `try-except` blocks to handle exceptions raised by the parser and engine, instead of checking `has_error` in a returned dictionary. The `InputParser` dependency will also change its return signature on success (direct data, not wrapped).

These changes promote a more standard Pythonic error handling approach.