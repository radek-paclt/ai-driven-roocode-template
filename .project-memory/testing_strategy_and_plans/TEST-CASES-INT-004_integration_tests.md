---
title: "Integration Test Cases for Console Calculator"
version: "0.1.0"
status: "Draft"
created_by: "tdd"
created_date: "2025-05-14T05:22:25Z"
last_modified_by: "tdd"
last_modified_date: "2025-05-14T05:22:25Z"
related_tasks: ["TEST-INT-004"]
relevant_links: [
  ".project-memory/specifications/SPEC-MAIN-001_console_calculator_main_specification.md",
  "src/calculator/main.py"
]
tags: ["integration-test", "calculator", "python"]
project_type_tags: ["cli-app"]
visibility: "internal"
---

# Integration Test Cases: Console Calculator

This document outlines the integration test cases for the Python Console Calculator. These tests verify the end-to-end functionality by simulating user interaction through the `main.py` script.

**Note**: The exact wording of prompts, error messages, and exit messages used in these test cases are based on common practices. They should be verified against the `SPEC-MAIN-001_console_calculator_main_specification.md` document and updated if necessary. The assumed prompt is `> ` and the assumed exit message is `Exiting calculator.`. Results of calculations are assumed to be floats (e.g., `10 + 5` results in `15.0`).

## Test Environment Setup
- Python environment with all project dependencies installed.
- The calculator application is run, and its input/output is captured.

## Test Case Format
- **ID**: Unique identifier for the test case.
- **Description**: Brief explanation of the test's purpose.
- **Preconditions**: Application is running.
- **Input Sequence**: Sequence of user inputs provided to the application.
- **Expected Console Interaction**: The sequence of prompts printed by the application and the application's responses (results/errors). User input itself is shown for clarity but is provided by the test framework.

## Test Cases

### 1. Valid Calculations

#### TC-INT-CALC-001: Integer Addition
- **ID**: TC-INT-CALC-001
- **Description**: Test addition of two positive integers.
- **Input Sequence**:
  1. `10 + 5`
- **Expected Console Interaction**:
  ```
  > 15.0
  > 
  ```
  *(Assuming the app prints the prompt, then the result, then the next prompt)*

#### TC-INT-CALC-002: Integer Subtraction
- **ID**: TC-INT-CALC-002
- **Description**: Test subtraction of two positive integers.
- **Input Sequence**:
  1. `10 - 5`
- **Expected Console Interaction**:
  ```
  > 5.0
  > 
  ```

#### TC-INT-CALC-003: Integer Multiplication
- **ID**: TC-INT-CALC-003
- **Description**: Test multiplication of two positive integers.
- **Input Sequence**:
  1. `10 * 5`
- **Expected Console Interaction**:
  ```
  > 50.0
  > 
  ```

#### TC-INT-CALC-004: Integer Division
- **ID**: TC-INT-CALC-004
- **Description**: Test division of two positive integers.
- **Input Sequence**:
  1. `10 / 5`
- **Expected Console Interaction**:
  ```
  > 2.0
  > 
  ```

#### TC-INT-CALC-005: Float Addition
- **ID**: TC-INT-CALC-005
- **Description**: Test addition of two positive floats.
- **Input Sequence**:
  1. `10.5 + 5.2`
- **Expected Console Interaction**:
  ```
  > 15.7
  > 
  ```

#### TC-INT-CALC-006: Float Subtraction
- **ID**: TC-INT-CALC-006
- **Description**: Test subtraction of two positive floats.
- **Input Sequence**:
  1. `10.5 - 5.2`
- **Expected Console Interaction**:
  ```
  > 5.3
  > 
  ```
  *(Note: Floating point precision might lead to results like 5.299999999999999. Test should account for this if necessary, e.g. by checking for approximate equality or if the spec defines specific formatting.)*

#### TC-INT-CALC-007: Float Multiplication
- **ID**: TC-INT-CALC-007
- **Description**: Test multiplication of two positive floats.
- **Input Sequence**:
  1. `2.5 * 2.0`
- **Expected Console Interaction**:
  ```
  > 5.0
  > 
  ```

#### TC-INT-CALC-008: Float Division
- **ID**: TC-INT-CALC-008
- **Description**: Test division of two positive floats.
- **Input Sequence**:
  1. `10.0 / 2.5`
- **Expected Console Interaction**:
  ```
  > 4.0
  > 
  ```

#### TC-INT-CALC-009: Mixed Integer/Float Calculation
- **ID**: TC-INT-CALC-009
- **Description**: Test calculation with mixed integer and float operands.
- **Input Sequence**:
  1. `5 + 2.5`
- **Expected Console Interaction**:
  ```
  > 7.5
  > 
  ```

#### TC-INT-CALC-010: Calculation with Negative Numbers
- **ID**: TC-INT-CALC-010
- **Description**: Test calculation involving negative numbers.
- **Input Sequence**:
  1. `-10 + 5`
- **Expected Console Interaction**:
  ```
  > -5.0
  > 
  ```

#### TC-INT-CALC-011: Calculation resulting in Negative Number
- **ID**: TC-INT-CALC-011
- **Description**: Test calculation that results in a negative number.
- **Input Sequence**:
  1. `5 - 10.5`
- **Expected Console Interaction**:
  ```
  > -5.5
  > 
  ```

#### TC-INT-CALC-012: Calculation with Zero
- **ID**: TC-INT-CALC-012
- **Description**: Test calculation involving zero.
- **Input Sequence**:
  1. `0 * 10`
- **Expected Console Interaction**:
  ```
  > 0.0
  > 
  ```

#### TC-INT-CALC-013: Calculation with Multiple Spaces
- **ID**: TC-INT-CALC-013
- **Description**: Test calculation with extra spaces between operands and operator.
- **Input Sequence**:
  1. `10  +    5`
- **Expected Console Interaction**:
  ```
  > 15.0
  > 
  ```

### 2. Exit Commands

#### TC-INT-EXIT-001: `exit` command (lowercase)
- **ID**: TC-INT-EXIT-001
- **Description**: Test exiting the calculator with the `exit` command.
- **Input Sequence**:
  1. `exit`
- **Expected Console Interaction**:
  ```
  > Exiting calculator.
  ```

#### TC-INT-EXIT-002: `quit` command (lowercase)
- **ID**: TC-INT-EXIT-002
- **Description**: Test exiting the calculator with the `quit` command.
- **Input Sequence**:
  1. `quit`
- **Expected Console Interaction**:
  ```
  > Exiting calculator.
  ```

#### TC-INT-EXIT-003: `EXIT` command (uppercase)
- **ID**: TC-INT-EXIT-003
- **Description**: Test exiting the calculator with the `EXIT` command (case-insensitivity).
- **Input Sequence**:
  1. `EXIT`
- **Expected Console Interaction**:
  ```
  > Exiting calculator.
  ```

#### TC-INT-EXIT-004: `QUIT` command (uppercase)
- **ID**: TC-INT-EXIT-004
- **Description**: Test exiting the calculator with the `QUIT` command (case-insensitivity).
- **Input Sequence**:
  1. `QUIT`
- **Expected Console Interaction**:
  ```
  > Exiting calculator.
  ```

#### TC-INT-EXIT-005: `ExIt` command (mixed case)
- **ID**: TC-INT-EXIT-005
- **Description**: Test exiting the calculator with a mixed-case `ExIt` command.
- **Input Sequence**:
  1. `ExIt`
- **Expected Console Interaction**:
  ```
  > Exiting calculator.
  ```

### 3. Error Handling
*(Assumed error messages. Verify with specifications.)*

#### TC-INT-ERR-001: Division by Zero
- **ID**: TC-INT-ERR-001
- **Description**: Test error handling for division by zero.
- **Input Sequence**:
  1. `10 / 0`
- **Expected Console Interaction**:
  ```
  > Error: Division by zero.
  > 
  ```

#### TC-INT-ERR-002: Invalid Input Format - Too Few Parts
- **ID**: TC-INT-ERR-002
- **Description**: Test error handling for input with too few parts.
- **Input Sequence**:
  1. `10 +`
- **Expected Console Interaction**:
  ```
  > Error: Invalid input format. Expected: number operator number
  > 
  ```

#### TC-INT-ERR-003: Invalid Input Format - Too Many Parts
- **ID**: TC-INT-ERR-003
- **Description**: Test error handling for input with too many parts.
- **Input Sequence**:
  1. `10 + 5 + 3`
- **Expected Console Interaction**:
  ```
  > Error: Invalid input format. Expected: number operator number
  > 
  ```

#### TC-INT-ERR-004: Invalid Input Format - Gibberish
- **ID**: TC-INT-ERR-004
- **Description**: Test error handling for non-parseable input.
- **Input Sequence**:
  1. `abc`
- **Expected Console Interaction**:
  ```
  > Error: Invalid input format. Expected: number operator number
  > 
  ```

#### TC-INT-ERR-005: Invalid Number - First Operand
- **ID**: TC-INT-ERR-005
- **Description**: Test error handling for an invalid first number.
- **Input Sequence**:
  1. `1.2.3 + 5`
- **Expected Console Interaction**:
  ```
  > Error: Invalid number '1.2.3'.
  > 
  ```

#### TC-INT-ERR-006: Invalid Number - Second Operand
- **ID**: TC-INT-ERR-006
- **Description**: Test error handling for an invalid second number.
- **Input Sequence**:
  1. `5 + 1.2.3`
- **Expected Console Interaction**:
  ```
  > Error: Invalid number '1.2.3'.
  > 
  ```

#### TC-INT-ERR-007: Invalid Operator
- **ID**: TC-INT-ERR-007
- **Description**: Test error handling for an invalid operator.
- **Input Sequence**:
  1. `10 # 5`
- **Expected Console Interaction**:
  ```
  > Error: Invalid operator '#'. Supported operators: +, -, *, /
  > 
  ```

#### TC-INT-ERR-008: Empty Input
- **ID**: TC-INT-ERR-008
- **Description**: Test handling of empty input (user just presses Enter).
- **Input Sequence**:
  1. `` (empty string)
- **Expected Console Interaction**:
  ```
  > > 
  ```
  *(Assuming it just re-prompts without an error. If an error is expected, this should be updated.)*

### 4. Sequential Operations

#### TC-INT-SEQ-001: Multiple Valid Calculations
- **ID**: TC-INT-SEQ-001
- **Description**: Test performing multiple valid calculations in sequence.
- **Input Sequence**:
  1. `10 + 5`
  2. `2 * 3`
  3. `100 / 4`
- **Expected Console Interaction**:
  ```
  > 15.0
  > 6.0
  > 25.0
  > 
  ```

#### TC-INT-SEQ-002: Valid, Error, Valid
- **ID**: TC-INT-SEQ-002
- **Description**: Test sequence of a valid calculation, an erroneous one, then another valid one.
- **Input Sequence**:
  1. `10 + 5`
  2. `1 / 0`
  3. `2 * 3`
- **Expected Console Interaction**:
  ```
  > 15.0
  > Error: Division by zero.
  > 6.0
  > 
  ```

#### TC-INT-SEQ-003: Valid Calculation then Exit
- **ID**: TC-INT-SEQ-003
- **Description**: Test a valid calculation followed by an exit command.
- **Input Sequence**:
  1. `7 - 2`
  2. `exit`
- **Expected Console Interaction**:
  ```
  > 5.0
  > Exiting calculator.