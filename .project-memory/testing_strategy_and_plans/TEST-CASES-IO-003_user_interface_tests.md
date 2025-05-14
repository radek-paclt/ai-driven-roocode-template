---
title: "Test Cases - User Interface (ConsoleUI) Module"
version: "0.1.0"
status: "Draft"
created_by: "tdd"
created_date: "2025-05-14T04:35:00Z"
last_modified_by: "tdd"
last_modified_date: "2025-05-14T04:35:00Z"
related_tasks: ["TEST-CASES-IO-003"]
relevant_links:
  - "../lld/LLD-IO-002_user_interface.md"
  - "../specifications/SPEC-MAIN-001_console_calculator_main_specification.md"
  - "../lld/LLD-ERR-003_error_handling.md"
tags: ["test-cases", "ui", "console", "python", "calculator"]
parent_document: "./TEST-PLAN-001_overall_test_plan.md"
child_documents: []
related_concepts: ["REPL", "user_interaction", "error_display", "input_handling", "unit_testing", "integration_testing"]
project_type_tags: ["cli-app", "python"]
visibility: "internal"
---

# Test Cases - User Interface (ConsoleUI) Module

## 1. Introduction

This document outlines the unit and integration test cases for the User Interface (ConsoleUI) module of the Python Console Calculator. These test cases are derived from the following documents:
- [LLD-IO-002_user_interface.md](../lld/LLD-IO-002_user_interface.md)
- [SPEC-MAIN-001_console_calculator_main_specification.md](../specifications/SPEC-MAIN-001_console_calculator_main_specification.md)
- [LLD-ERR-003_error_handling.md](../lld/LLD-ERR-003_error_handling.md)

The ConsoleUI module is responsible for the Read-Eval-Print Loop (REPL), handling user input, invoking the parser and calculation engine, and displaying results or errors.

**Note on `_format_error`**: The [LLD-ERR-003_error_handling.md](../lld/LLD-ERR-003_error_handling.md) suggests that custom exceptions will be initialized with the full user-facing error message, including the "Error: " prefix. If this approach is implemented, the `_format_error` helper function (defined in [LLD-IO-002_user_interface.md](../lld/LLD-IO-002_user_interface.md)) might become redundant. These test cases assume exceptions provide the full message, and thus, unit tests for `_format_error` are not included here.

**Note on "help" command**: The "help" command was mentioned as an example in the task context but is not specified in the current LLDs or the main specification. Therefore, test cases for "help" functionality are not included.

## 2. Test Case Structure

Each test case will include the following fields:
- **Test Case ID**: A unique identifier for the test case.
- **Test Type**: Unit or Integration.
- **Component/Function Tested**: The specific part of the UI module being tested.
- **Description**: A brief description of the test objective.
- **Preconditions**: Any conditions that must be met before executing the test.
- **Input/Steps**: The input data or sequence of actions for the test.
- **Expected Output/Behavior**: The expected result or behavior of the system.
- **Postconditions**: The state of the system after the test execution.
- **Notes**: Any additional relevant information.

## 3. Unit Test Cases

### 3.1. Helper Function: `_format_result(result_value: float) -> str`

| Field                     | Value                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------|
| **Test Case ID**          | UTC_UI_FR_001                                                                                        |
| **Test Type**             | Unit                                                                                                 |
| **Component/Function Tested** | `_format_result`                                                                                     |
| **Description**           | Verify that a positive integer float is correctly converted to a string.                             |
| **Preconditions**         | None.                                                                                                |
| **Input/Steps**           | Call `_format_result(15.0)`.                                                                         |
| **Expected Output/Behavior** | Returns the string `"15.0"`.                                                                         |
| **Postconditions**        | None.                                                                                                |
| **Notes**                 | Based on LLD: "simple string conversion is sufficient".                                              |

| Field                     | Value                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------|
| **Test Case ID**          | UTC_UI_FR_002                                                                                        |
| **Test Type**             | Unit                                                                                                 |
| **Component/Function Tested** | `_format_result`                                                                                     |
| **Description**           | Verify that a floating-point number with decimal places is correctly converted to a string.          |
| **Preconditions**         | None.                                                                                                |
| **Input/Steps**           | Call `_format_result(7.5)`.                                                                          |
| **Expected Output/Behavior** | Returns the string `"7.5"`.                                                                          |
| **Postconditions**        | None.                                                                                                |
| **Notes**                 |                                                                                                      |

| Field                     | Value                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------|
| **Test Case ID**          | UTC_UI_FR_003                                                                                        |
| **Test Type**             | Unit                                                                                                 |
| **Component/Function Tested** | `_format_result`                                                                                     |
| **Description**           | Verify that zero is correctly converted to a string.                                                 |
| **Preconditions**         | None.                                                                                                |
| **Input/Steps**           | Call `_format_result(0.0)`.                                                                          |
| **Expected Output/Behavior** | Returns the string `"0.0"`.                                                                          |
| **Postconditions**        | None.                                                                                                |
| **Notes**                 |                                                                                                      |

| Field                     | Value                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------|
| **Test Case ID**          | UTC_UI_FR_004                                                                                        |
| **Test Type**             | Unit                                                                                                 |
| **Component/Function Tested** | `_format_result`                                                                                     |
| **Description**           | Verify that a negative floating-point number is correctly converted to a string.                     |
| **Preconditions**         | None.                                                                                                |
| **Input/Steps**           | Call `_format_result(-5.25)`.                                                                        |
| **Expected Output/Behavior** | Returns the string `"-5.25"`.                                                                         |
| **Postconditions**        | None.                                                                                                |
| **Notes**                 |                                                                                                      |

### 3.2. Helper Function: `_process_user_command(input_str: str) -> bool`

| Field                     | Value                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------|
| **Test Case ID**          | UTC_UI_PUC_001                                                                                       |
| **Test Type**             | Unit                                                                                                 |
| **Component/Function Tested** | `_process_user_command`                                                                              |
| **Description**           | Verify that "exit" command (lowercase) is recognized.                                                |
| **Preconditions**         | None.                                                                                                |
| **Input/Steps**           | Call `_process_user_command("exit")`.                                                                |
| **Expected Output/Behavior** | Returns `True`.                                                                                      |
| **Postconditions**        | None.                                                                                                |
| **Notes**                 |                                                                                                      |

| Field                     | Value                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------|
| **Test Case ID**          | UTC_UI_PUC_002                                                                                       |
| **Test Type**             | Unit                                                                                                 |
| **Component/Function Tested** | `_process_user_command`                                                                              |
| **Description**           | Verify that "quit" command (lowercase) is recognized.                                                |
| **Preconditions**         | None.                                                                                                |
| **Input/Steps**           | Call `_process_user_command("quit")`.                                                                |
| **Expected Output/Behavior** | Returns `True`.                                                                                      |
| **Postconditions**        | None.                                                                                                |
| **Notes**                 |                                                                                                      |

| Field                     | Value                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------|
| **Test Case ID**          | UTC_UI_PUC_003                                                                                       |
| **Test Type**             | Unit                                                                                                 |
| **Component/Function Tested** | `_process_user_command`                                                                              |
| **Description**           | Verify that "EXIT" command (uppercase) is recognized (case-insensitivity).                           |
| **Preconditions**         | None.                                                                                                |
| **Input/Steps**           | Call `_process_user_command("EXIT")`.                                                                |
| **Expected Output/Behavior** | Returns `True`.                                                                                      |
| **Postconditions**        | None.                                                                                                |
| **Notes**                 |                                                                                                      |

| Field                     | Value                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------|
| **Test Case ID**          | UTC_UI_PUC_004                                                                                       |
| **Test Type**             | Unit                                                                                                 |
| **Component/Function Tested** | `_process_user_command`                                                                              |
| **Description**           | Verify that "QuIt" command (mixed case) is recognized (case-insensitivity).                          |
| **Preconditions**         | None.                                                                                                |
| **Input/Steps**           | Call `_process_user_command("QuIt")`.                                                                |
| **Expected Output/Behavior** | Returns `True`.                                                                                      |
| **Postconditions**        | None.                                                                                                |
| **Notes**                 |                                                                                                      |

| Field                     | Value                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------|
| **Test Case ID**          | UTC_UI_PUC_005                                                                                       |
| **Test Type**             | Unit                                                                                                 |
| **Component/Function Tested** | `_process_user_command`                                                                              |
| **Description**           | Verify that a non-exit command (e.g., a calculation string) is not recognized as an exit command.    |
| **Preconditions**         | None.                                                                                                |
| **Input/Steps**           | Call `_process_user_command("5 + 3")`.                                                               |
| **Expected Output/Behavior** | Returns `False`.                                                                                     |
| **Postconditions**        | None.                                                                                                |
| **Notes**                 |                                                                                                      |

| Field                     | Value                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------|
| **Test Case ID**          | UTC_UI_PUC_006                                                                                       |
| **Test Type**             | Unit                                                                                                 |
| **Component/Function Tested** | `_process_user_command`                                                                              |
| **Description**           | Verify that an empty string is not recognized as an exit command.                                    |
| **Preconditions**         | None.                                                                                                |
| **Input/Steps**           | Call `_process_user_command("")`.                                                                    |
| **Expected Output/Behavior** | Returns `False`.                                                                                     |
| **Postconditions**        | None.                                                                                                |
| **Notes**                 |                                                                                                      |

| Field                     | Value                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------|
| **Test Case ID**          | UTC_UI_PUC_007                                                                                       |
| **Test Type**             | Unit                                                                                                 |
| **Component/Function Tested** | `_process_user_command`                                                                              |
| **Description**           | Verify that a partial exit command (e.g., "exi") is not recognized.                                  |
| **Preconditions**         | None.                                                                                                |
| **Input/Steps**           | Call `_process_user_command("exi")`.                                                                 |
| **Expected Output/Behavior** | Returns `False`.                                                                                     |
| **Postconditions**        | None.                                                                                                |
| **Notes**                 |                                                                                                      |

## 4. Integration Test Cases (`run_calculator_loop`)

**Common Preconditions for Integration Tests:**
- `run_calculator_loop` is called with mocked `InputParser` and `CalculationEngine`.
- `_get_user_input` is mocked to provide a sequence of inputs.
- `_display_output` is mocked to capture displayed messages.

### 4.1. Successful Calculation and Display

| Field                     | Value                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------|
| **Test Case ID**          | ITC_UI_REPL_CALC_001                                                                                 |
| **Test Type**             | Integration                                                                                          |
| **Component/Function Tested** | `run_calculator_loop`                                                                                |
| **Description**           | Verify a simple valid addition is processed and the result displayed.                                |
| **Preconditions**         | - `_get_user_input` mock returns "5 + 3", then "exit". <br> - `InputParser` mock for "5 + 3" returns `{"operand1": 5.0, "operator": "+", "operand2": 3.0}`. <br> - `CalculationEngine` mock for `(5.0, "+", 3.0)` returns `8.0`. |
| **Input/Steps**           | 1. Run `run_calculator_loop`.                                                                        |
| **Expected Output/Behavior** | 1. `_display_output` called with "calc> ". <br> 2. `InputParser.parse("5 + 3")` called. <br> 3. `CalculationEngine.calculate(5.0, "+", 3.0)` called. <br> 4. `_display_output` called with "8.0" (result of `_format_result(8.0)`). <br> 5. `_display_output` called with "calc> ". <br> 6. `_display_output` called with "Exiting calculator. Goodbye!". |
| **Postconditions**        | Loop terminates.                                                                                     |
| **Notes**                 | Assumes `_format_result` works as per its unit tests.                                                |

| Field                     | Value                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------|
| **Test Case ID**          | ITC_UI_REPL_CALC_002                                                                                 |
| **Test Type**             | Integration                                                                                          |
| **Component/Function Tested** | `run_calculator_loop`                                                                                |
| **Description**           | Verify a calculation with floating point numbers.                                                    |
| **Preconditions**         | - `_get_user_input` mock returns "2.5 * 2", then "exit". <br> - `InputParser` mock for "2.5 * 2" returns `{"operand1": 2.5, "operator": "*", "operand2": 2.0}`. <br> - `CalculationEngine` mock for `(2.5, "*", 2.0)` returns `5.0`. |
| **Input/Steps**           | 1. Run `run_calculator_loop`.                                                                        |
| **Expected Output/Behavior** | 1. `_display_output` called with "calc> ". <br> 2. `InputParser.parse("2.5 * 2")` called. <br> 3. `CalculationEngine.calculate(2.5, "*", 2.0)` called. <br> 4. `_display_output` called with "5.0". <br> 5. `_display_output` called with "calc> ". <br> 6. `_display_output` called with "Exiting calculator. Goodbye!". |
| **Postconditions**        | Loop terminates.                                                                                     |
| **Notes**                 |                                                                                                      |

| Field                     | Value                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------|
| **Test Case ID**          | ITC_UI_REPL_CALC_003                                                                                 |
| **Test Type**             | Integration                                                                                          |
| **Component/Function Tested** | `run_calculator_loop`                                                                                |
| **Description**           | Verify multiple calculations in sequence before exiting.                                             |
| **Preconditions**         | - `_get_user_input` mock returns "10 / 2", then "3 - 1", then "quit". <br> - `InputParser` mock for "10 / 2" returns `{"operand1": 10.0, "operator": "/", "operand2": 2.0}`. `CalculationEngine` mock returns `5.0`. <br> - `InputParser` mock for "3 - 1" returns `{"operand1": 3.0, "operator": "-", "operand2": 1.0}`. `CalculationEngine` mock returns `2.0`. |
| **Input/Steps**           | 1. Run `run_calculator_loop`.                                                                        |
| **Expected Output/Behavior** | 1. `_display_output` called with "calc> ". <br> 2. `_display_output` called with "5.0". <br> 3. `_display_output` called with "calc> ". <br> 4. `_display_output` called with "2.0". <br> 5. `_display_output` called with "calc> ". <br> 6. `_display_output` called with "Exiting calculator. Goodbye!". |
| **Postconditions**        | Loop terminates.                                                                                     |
| **Notes**                 |                                                                                                      |

### 4.2. Exit Command Handling

| Field                     | Value                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------|
| **Test Case ID**          | ITC_UI_REPL_EXIT_001                                                                                 |
| **Test Type**             | Integration                                                                                          |
| **Component/Function Tested** | `run_calculator_loop`                                                                                |
| **Description**           | Verify that "exit" command terminates the loop immediately.                                          |
| **Preconditions**         | - `_get_user_input` mock returns "exit".                                                             |
| **Input/Steps**           | 1. Run `run_calculator_loop`.                                                                        |
| **Expected Output/Behavior** | 1. `_display_output` called with "calc> ". <br> 2. `_process_user_command("exit")` is called and returns `True`. <br> 3. `_display_output` called with "Exiting calculator. Goodbye!". <br> 4. `InputParser.parse` and `CalculationEngine.calculate` are NOT called. |
| **Postconditions**        | Loop terminates.                                                                                     |
| **Notes**                 |                                                                                                      |

| Field                     | Value                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------|
| **Test Case ID**          | ITC_UI_REPL_EXIT_002                                                                                 |
| **Test Type**             | Integration                                                                                          |
| **Component/Function Tested** | `run_calculator_loop`                                                                                |
| **Description**           | Verify that "QUIT" (uppercase) command terminates the loop.                                          |
| **Preconditions**         | - `_get_user_input` mock returns "QUIT".                                                             |
| **Input/Steps**           | 1. Run `run_calculator_loop`.                                                                        |
| **Expected Output/Behavior** | 1. `_display_output` called with "calc> ". <br> 2. `_process_user_command("QUIT")` is called and returns `True`. <br> 3. `_display_output` called with "Exiting calculator. Goodbye!". |
| **Postconditions**        | Loop terminates.                                                                                     |
| **Notes**                 | Tests case-insensitivity of exit commands.                                                           |

| Field                     | Value                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------|
| **Test Case ID**          | ITC_UI_REPL_EXIT_003                                                                                 |
| **Test Type**             | Integration                                                                                          |
| **Component/Function Tested** | `run_calculator_loop`                                                                                |
| **Description**           | Verify exit command with leading/trailing whitespace.                                                |
| **Preconditions**         | - `_get_user_input` mock returns "  exit  ".                                                         |
| **Input/Steps**           | 1. Run `run_calculator_loop`.                                                                        |
| **Expected Output/Behavior** | 1. `_display_output` called with "calc> ". <br> 2. Input is trimmed to "exit". <br> 3. `_process_user_command("exit")` is called and returns `True`. <br> 4. `_display_output` called with "Exiting calculator. Goodbye!". |
| **Postconditions**        | Loop terminates.                                                                                     |
| **Notes**                 | Tests input trimming before command processing.                                                      |

### 4.3. Error Handling - Parser Errors

| Field                     | Value                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------|
| **Test Case ID**          | ITC_UI_REPL_ERR_PARSE_001                                                                            |
| **Test Type**             | Integration                                                                                          |
| **Component/Function Tested** | `run_calculator_loop`                                                                                |
| **Description**           | Verify display of `InvalidFormatError` from parser (e.g. too few parts).                             |
| **Preconditions**         | - `_get_user_input` mock returns "5 +", then "exit". <br> - `InputParser` mock for "5 +" raises `InvalidFormatError("Error: Invalid input format. Expected 'number operator number'.")`. |
| **Input/Steps**           | 1. Run `run_calculator_loop`.                                                                        |
| **Expected Output/Behavior** | 1. `_display_output` called with "calc> ". <br> 2. `InputParser.parse("5 +")` called. <br> 3. `_display_output` called with "Error: Invalid input format. Expected 'number operator number'.". <br> 4. `CalculationEngine.calculate` is NOT called. <br> 5. `_display_output` called with "calc> " (loop continues). <br> 6. `_display_output` called with "Exiting calculator. Goodbye!". |
| **Postconditions**        | Loop terminates after "exit".                                                                        |
| **Notes**                 |                                                                                                      |

| Field                     | Value                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------|
| **Test Case ID**          | ITC_UI_REPL_ERR_PARSE_002                                                                            |
| **Test Type**             | Integration                                                                                          |
| **Component/Function Tested** | `run_calculator_loop`                                                                                |
| **Description**           | Verify display of `InvalidNumberError` from parser (e.g. non-numeric operand1).                      |
| **Preconditions**         | - `_get_user_input` mock returns "abc + 5", then "exit". <br> - `InputParser` mock for "abc + 5" raises `InvalidNumberError("Error: Invalid number: 'abc'.")`. |
| **Input/Steps**           | 1. Run `run_calculator_loop`.                                                                        |
| **Expected Output/Behavior** | 1. `_display_output` called with "calc> ". <br> 2. `InputParser.parse("abc + 5")` called. <br> 3. `_display_output` called with "Error: Invalid number: 'abc'.". <br> 4. `CalculationEngine.calculate` is NOT called. <br> 5. `_display_output` called with "calc> ". <br> 6. `_display_output` called with "Exiting calculator. Goodbye!". |
| **Postconditions**        | Loop terminates after "exit".                                                                        |
| **Notes**                 |                                                                                                      |

| Field                     | Value                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------|
| **Test Case ID**          | ITC_UI_REPL_ERR_PARSE_003                                                                            |
| **Test Type**             | Integration                                                                                          |
| **Component/Function Tested** | `run_calculator_loop`                                                                                |
| **Description**           | Verify display of `InvalidOperatorError` from parser.                                                |
| **Preconditions**         | - `_get_user_input` mock returns "5 % 2", then "exit". <br> - `InputParser` mock for "5 % 2" raises `InvalidOperatorError("Error: Invalid operator: '%'. Supported operators are +, -, *, /.")`. |
| **Input/Steps**           | 1. Run `run_calculator_loop`.                                                                        |
| **Expected Output/Behavior** | 1. `_display_output` called with "calc> ". <br> 2. `InputParser.parse("5 % 2")` called. <br> 3. `_display_output` called with "Error: Invalid operator: '%'. Supported operators are +, -, *, /.". <br> 4. `CalculationEngine.calculate` is NOT called. <br> 5. `_display_output` called with "calc> ". <br> 6. `_display_output` called with "Exiting calculator. Goodbye!". |
| **Postconditions**        | Loop terminates after "exit".                                                                        |
| **Notes**                 |                                                                                                      |

| Field                     | Value                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------|
| **Test Case ID**          | ITC_UI_REPL_ERR_PARSE_004                                                                            |
| **Test Type**             | Integration                                                                                          |
| **Component/Function Tested** | `run_calculator_loop`                                                                                |
| **Description**           | Verify display of `InvalidFormatError` for empty input.                                              |
| **Preconditions**         | - `_get_user_input` mock returns "", then "exit". <br> - `InputParser` mock for "" raises `InvalidFormatError("Error: Invalid input format. Expected 'number operator number'.")`. |
| **Input/Steps**           | 1. Run `run_calculator_loop`.                                                                        |
| **Expected Output/Behavior** | 1. `_display_output` called with "calc> ". <br> 2. `InputParser.parse("")` called. <br> 3. `_display_output` called with "Error: Invalid input format. Expected 'number operator number'.". <br> 4. `_display_output` called with "calc> ". <br> 5. `_display_output` called with "Exiting calculator. Goodbye!". |
| **Postconditions**        | Loop terminates after "exit".                                                                        |
| **Notes**                 |                                                                                                      |

### 4.4. Error Handling - Engine Errors

| Field                     | Value                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------|
| **Test Case ID**          | ITC_UI_REPL_ERR_ENGINE_001                                                                           |
| **Test Type**             | Integration                                                                                          |
| **Component/Function Tested** | `run_calculator_loop`                                                                                |
| **Description**           | Verify display of `DivisionByZeroError` from calculation engine.                                     |
| **Preconditions**         | - `_get_user_input` mock returns "10 / 0", then "exit". <br> - `InputParser` mock for "10 / 0" returns `{"operand1": 10.0, "operator": "/", "operand2": 0.0}`. <br> - `CalculationEngine` mock for `(10.0, "/", 0.0)` raises `DivisionByZeroError("Error: Division by zero is not allowed.")`. |
| **Input/Steps**           | 1. Run `run_calculator_loop`.                                                                        |
| **Expected Output/Behavior** | 1. `_display_output` called with "calc> ". <br> 2. `InputParser.parse("10 / 0")` called. <br> 3. `CalculationEngine.calculate(10.0, "/", 0.0)` called. <br> 4. `_display_output` called with "Error: Division by zero is not allowed.". <br> 5. `_display_output` called with "calc> ". <br> 6. `_display_output` called with "Exiting calculator. Goodbye!". |
| **Postconditions**        | Loop terminates after "exit".                                                                        |
| **Notes**                 |                                                                                                      |

### 4.5. Input Variations

| Field                     | Value                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------|
| **Test Case ID**          | ITC_UI_REPL_INPUT_001                                                                                |
| **Test Type**             | Integration                                                                                          |
| **Component/Function Tested** | `run_calculator_loop`                                                                                |
| **Description**           | Verify input with leading/trailing whitespace is handled correctly for calculation.                  |
| **Preconditions**         | - `_get_user_input` mock returns "  7 * 2  ", then "exit". <br> - `InputParser` mock for "7 * 2" (after trimming) returns `{"operand1": 7.0, "operator": "*", "operand2": 2.0}`. <br> - `CalculationEngine` mock for `(7.0, "*", 2.0)` returns `14.0`. |
| **Input/Steps**           | 1. Run `run_calculator_loop`.                                                                        |
| **Expected Output/Behavior** | 1. `_display_output` called with "calc> ". <br> 2. `InputParser.parse("7 * 2")` called (input was trimmed). <br> 3. `CalculationEngine.calculate(7.0, "*", 2.0)` called. <br> 4. `_display_output` called with "14.0". <br> 5. `_display_output` called with "calc> ". <br> 6. `_display_output` called with "Exiting calculator. Goodbye!". |
| **Postconditions**        | Loop terminates.                                                                                     |
| **Notes**                 | Tests trimming of input before parsing.                                                              |
