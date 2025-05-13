---
title: "Console Calculator - LLD - User Interface Module (ConsoleUI/REPL Handler)"
version: "0.1.0"
status: "Draft"
created_by: "architect"
created_date: "2025-05-13T23:08:00Z" # Approximate current time
last_modified_by: "architect"
last_modified_date: "2025-05-13T23:08:00Z" # Approximate current time
related_tasks: ["ARCH-LLD-IO-002"]
relevant_links:
  - "../hld/HLD-MAIN-001_main_architecture.md"
  - "../specifications/SPEC-MAIN-001_console_calculator_main_specification.md"
  - "../../project_postulates.md"
tags: ["lld", "ui", "console", "repl", "python", "calculator"]
parent_document: "../hld/HLD-MAIN-001_main_architecture.md"
child_documents: []
related_concepts: ["REPL", "user_interaction", "console_io", "error_display", "input_handling"]
project_type_tags: ["cli-app", "python"]
visibility: "internal"
---

# Console Calculator - LLD - User Interface Module (ConsoleUI/REPL Handler)

## 1. Component Overview

This document provides the Low-Level Design (LLD) for the User Interface module, also referred to as the ConsoleUI or REPL (Read-Eval-Print Loop) Handler, of the Python Console Calculator application. This component is responsible for all direct user interaction, including managing the main application loop, reading user input, displaying prompts, results, and error messages. It orchestrates the overall flow by interacting with the `InputParser` and `CalculationEngine` components.

This LLD is based on the [High-Level Design (HLD)](../hld/HLD-MAIN-001_main_architecture.md) and the [Main Specification](../specifications/SPEC-MAIN-001_console_calculator_main_specification.md).

## 2. Detailed Design

### 2.1. Component Structure

The User Interface module will be implemented as a Python module containing a main public function `run_calculator_loop()` and several helper functions to manage specific UI tasks.

**Public Functions:**
*   `run_calculator_loop(parser: InputParser, engine: CalculationEngine)`: Initializes and runs the main REPL. It takes instances of the `InputParser` and `CalculationEngine` as dependencies.

**Helper Functions (internal to the module):**
*   `_get_user_input(prompt_message: str) -> str`: Displays a prompt and reads a line of text from the user.
*   `_display_output(message: str)`: Prints a message to the console.
*   `_format_result(result_value: float) -> str`: Formats the numerical result for display.
*   `_format_error(error_message_from_component: str) -> str`: Formats an error message for display, prepending "Error: ".
*   `_process_user_command(input_str: str) -> bool`: Checks if the input is an exit command and handles it. Returns `True` if an exit command was processed, `False` otherwise.

### 2.2. Interfaces and Contracts

#### 2.2.1. Provided Interface (Public Function)

*   **`run_calculator_loop(parser: InputParser, engine: CalculationEngine)`**
    *   **Description**: Starts and manages the main REPL of the calculator.
    *   **Parameters**:
        *   `parser`: An instance of the `InputParser` component. This object is expected to have a method `parse(input_string: str) -> dict`.
        *   `engine`: An instance of the `CalculationEngine` component. This object is expected to have a method `calculate(operand1: float, operator: str, operand2: float) -> dict`.
    *   **Returns**: `None`.
    *   **Side Effects**: Continuously interacts with the user via the console until an exit command is given.

#### 2.2.2. Used Interfaces (Dependencies)

The `ConsoleUI` module depends on the following interfaces from other components:

1.  **`InputParser.parse(input_string: str) -> dict`**
    *   **Description**: Parses the raw user input string.
    *   **Expected Return on Success**:
        ```python
        {
            "has_error": False,
            "operand1": float,  # The first number
            "operator": str,    # The operator (+, -, *, /)
            "operand2": float   # The second number
        }
        ```
    *   **Expected Return on Error**:
        ```python
        {
            "has_error": True,
            "error_message": str  # User-friendly error message from the parser
        }
        ```

2.  **`CalculationEngine.calculate(operand1: float, operator: str, operand2: float) -> dict`**
    *   **Description**: Performs the arithmetic calculation.
    *   **Expected Return on Success**:
        ```python
        {
            "has_error": False,
            "value": float  # The calculated result
        }
        ```
    *   **Expected Return on Error (e.g., division by zero)**:
        ```python
        {
            "has_error": True,
            "error_message": str  # User-friendly error message from the engine
        }
        ```

### 2.3. Data Structures

The `ConsoleUI` module primarily deals with strings for input and output. It interprets the dictionary structures returned by the `InputParser` and `CalculationEngine` as defined in section 2.2.2.

*   **Input Prompt**: `str` (e.g., "calc> ")
*   **User Input**: `str`
*   **Display Messages**: `str`

### 2.4. Algorithms and Logic

The core logic resides in the `run_calculator_loop` function, which implements the REPL.

1.  **Initialization**: Set the input prompt string.
2.  **Main Loop**:
    a.  Display the input prompt using `_display_output()`.
    b.  Get raw user input using `_get_user_input()`.
    c.  Trim leading/trailing whitespace from the input.
    d.  Check for exit commands (e.g., "exit", "quit", case-insensitive) using `_process_user_command()`. If an exit command is detected, terminate the loop.
    e.  If not an exit command, pass the trimmed input string to `parser.parse()`.
    f.  Evaluate the `InputParser`'s response:
        i.  If `parsed_input["has_error"]` is `True`, format the `parsed_input["error_message"]` using `_format_error()` and display it using `_display_output()`. Continue to the next loop iteration.
        ii. If `parsed_input["has_error"]` is `False`, extract `operand1`, `operator`, and `operand2`.
    g.  Pass the extracted `operand1`, `operator`, and `operand2` to `engine.calculate()`.
    h.  Evaluate the `CalculationEngine`'s response:
        i.  If `calculation_result["has_error"]` is `True`, format the `calculation_result["error_message"]` using `_format_error()` and display it using `_display_output()`.
        ii. If `calculation_result["has_error"]` is `False`, format `calculation_result["value"]` using `_format_result()` and display it using `_display_output()`.
    i.  Repeat loop.

## 3. Behavior Specifications (Pseudocode)

### 3.1. `run_calculator_loop(parser, engine)`

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
        
        // Delegate to InputParser
        parsed_data = parser_instance.parse(trimmed_input)
        
        IF parsed_data["has_error"] == TRUE:
            formatted_error = _format_error(parsed_data["error_message"])
            _display_output(formatted_error)
            CONTINUE LOOP
        END IF
        
        operand1 = parsed_data["operand1"]
        operator_str = parsed_data["operator"]
        operand2 = parsed_data["operand2"]
        
        // Delegate to CalculationEngine
        calculation_outcome = engine_instance.calculate(operand1, operator_str, operand2)
        
        IF calculation_outcome["has_error"] == TRUE:
            formatted_error = _format_error(calculation_outcome["error_message"])
            _display_output(formatted_error)
        ELSE:
            formatted_result = _format_result(calculation_outcome["value"])
            _display_output(formatted_result)
        END IF
    END WHILE
    
    _display_output("Exiting calculator. Goodbye!") // Optional exit message
END FUNCTION
```

### 3.2. `_get_user_input()`

```pseudocode
FUNCTION _get_user_input():
    // This function directly uses the built-in input reading capability of Python.
    // Example: return input()
    RETURN READ_CONSOLE_LINE() 
END FUNCTION
```

### 3.3. `_display_output(message: str)`

```pseudocode
FUNCTION _display_output(message):
    // This function directly uses the built-in printing capability of Python.
    // Example: print(message)
    PRINT_TO_CONSOLE(message)
END FUNCTION
```

### 3.4. `_format_result(result_value: float) -> str`

```pseudocode
FUNCTION _format_result(result_value):
    // Converts the float result to a string.
    // For V1, simple string conversion is sufficient.
    // Example: return str(result_value)
    RETURN CONVERT_FLOAT_TO_STRING(result_value)
END FUNCTION
```

### 3.5. `_format_error(error_message_from_component: str) -> str`

```pseudocode
FUNCTION _format_error(error_message_from_component):
    // Prepends "Error: " to the message from the component.
    RETURN "Error: " + error_message_from_component
END FUNCTION
```

### 3.6. `_process_user_command(input_str: str) -> bool`

```pseudocode
FUNCTION _process_user_command(input_str):
    normalized_input = TO_LOWERCASE(input_str)
    IF normalized_input == "exit" OR normalized_input == "quit":
        RETURN TRUE // Indicates an exit command was processed
    END IF
    RETURN FALSE // Not an exit command
END FUNCTION
```

## 4. Error Handling

*   The `ConsoleUI` module itself does not generate logical errors related to parsing or calculation.
*   It receives error information (a dictionary with `has_error: True` and `error_message: str`) from the `InputParser` and `CalculationEngine`.
*   It is responsible for formatting these error messages (e.g., by prepending "Error: ") and displaying them to the user via the console.
*   If `_get_user_input()` encounters an I/O error (e.g., EOF), the behavior will depend on the underlying Python `input()` function, which might raise an `EOFError`. For V1, specific handling of `EOFError` beyond letting the program terminate is not required unless specified.

## 5. Security Considerations

*   The `ConsoleUI` module directly handles user input. However, it passes this input as strings to other components.
*   It does not use `eval()` or any other mechanism that could directly execute user input as code.
*   The primary security measure is the robust parsing and validation performed by the `InputParser` component.

## 6. Testing Considerations

*   **Unit Testing**:
    *   Helper functions like `_format_result`, `_format_error`, and `_process_user_command` can be unit tested directly.
    *   The main `run_calculator_loop` is harder to unit test directly due to its reliance on console I/O and external dependencies.
*   **Integration Testing Strategy for `run_calculator_loop`**:
    *   Mock the `_get_user_input` and `_display_output` functions to simulate console interaction without actual console I/O.
    *   Mock the `InputParser` and `CalculationEngine` dependencies to control their behavior and return values (both success and error cases).
    *   Verify that `run_calculator_loop` calls the mocked parser and engine with correct arguments based on simulated input.
    *   Verify that `_display_output` is called with correctly formatted results or error messages based on the mocked responses from parser/engine.
    *   Test the exit conditions ("exit", "quit").
*   **Testability Design**:
    *   Dependency injection for `parser` and `engine` in `run_calculator_loop` facilitates mocking.
    *   Separation of I/O into helper functions (`_get_user_input`, `_display_output`) allows them to be easily patched or mocked during tests.

## 7. Future Considerations

*   If more complex prompt logic or output formatting is required, the helper functions can be expanded.
*   For a more sophisticated UI (e.g., GUI), this entire module would be replaced.