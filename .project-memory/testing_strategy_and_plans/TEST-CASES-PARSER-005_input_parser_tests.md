---
title: "Unit Test Cases for Input Parser Module"
version: "0.1.0"
status: "Draft"
created_by: "tdd"
created_date: "2025-05-14T07:00:00Z" # Approximate current UTC time
last_modified_by: "tdd"
last_modified_date: "2025-05-14T07:00:00Z"
related_tasks: ["TEST-CASES-PARSER-005"]
relevant_links:
  - "../lld/LLD-PARSER-004_input_parser.md"
  - "../specifications/SPEC-MAIN-001_console_calculator_main_specification.md"
  - "../lld/LLD-ERR-003_error_handling.md"
  - "./TEST-PLAN-001_overall_test_plan.md"
tags: ["test-cases", "unit-test", "parser", "python", "calculator"]
parent_document: "./TEST-PLAN-001_overall_test_plan.md"
child_documents: []
related_concepts: ["input_validation", "exception_testing", "tdd"]
project_type_tags: ["cli-app", "python"]
visibility: "internal"
---

# Unit Test Cases for Input Parser Module

## 1. Introduction

This document outlines the unit test cases for the `InputParser` module of the Python Console Calculator. These tests are designed to verify the functionality of the `parse` method, ensuring it correctly processes valid user inputs and appropriately handles various error conditions by raising the specified custom exceptions with correct messages.

The tests are based on the specifications detailed in:
*   [`LLD-PARSER-004_input_parser.md`](../lld/LLD-PARSER-004_input_parser.md)
*   [`SPEC-MAIN-001_console_calculator_main_specification.md`](../specifications/SPEC-MAIN-001_console_calculator_main_specification.md)
*   [`LLD-ERR-003_error_handling.md`](../lld/LLD-ERR-003_error_handling.md)

## 2. Test Environment and Preconditions

*   An instance of the `InputParser` class is available.
*   Custom exceptions (`InvalidFormatError`, `InvalidNumberError`, `InvalidOperatorError`, and their base `CalculatorError`) are defined and accessible.
*   Tests will typically use a testing framework like `pytest` to assert expected outcomes and raised exceptions.

## 3. Test Cases

### 3.1. Valid Inputs

These tests verify that the `parse` method correctly processes valid input strings and returns the expected dictionary.

---

**Test Case ID**: `TC_PARSER_VALID_001`
**Description**: Test with a simple valid input: two positive integers and the '+' operator.
**Preconditions**: `InputParser` instance available.
**Input**: `"5 + 3"`
**Test Steps**:
    1. Call `parser.parse("5 + 3")`.
**Expected Output/Behavior**:
    Returns `{"operand1": 5.0, "operator": "+", "operand2": 3.0}`.
**Postconditions**: None.

---

**Test Case ID**: `TC_PARSER_VALID_002`
**Description**: Test with floating-point numbers and the '*' operator.
**Preconditions**: `InputParser` instance available.
**Input**: `"3.14 * 2.5"`
**Test Steps**:
    1. Call `parser.parse("3.14 * 2.5")`.
**Expected Output/Behavior**:
    Returns `{"operand1": 3.14, "operator": "*", "operand2": 2.5}`.
**Postconditions**: None.

---

**Test Case ID**: `TC_PARSER_VALID_003`
**Description**: Test with negative numbers and the '-' operator.
**Preconditions**: `InputParser` instance available.
**Input**: `"-7 - -2"`
**Test Steps**:
    1. Call `parser.parse("-7 - -2")`.
**Expected Output/Behavior**:
    Returns `{"operand1": -7.0, "operator": "-", "operand2": -2.0}`.
**Postconditions**: None.

---

**Test Case ID**: `TC_PARSER_VALID_004`
**Description**: Test with the '/' operator and mixed integer/float.
**Preconditions**: `InputParser` instance available.
**Input**: `"10 / 2.5"`
**Test Steps**:
    1. Call `parser.parse("10 / 2.5")`.
**Expected Output/Behavior**:
    Returns `{"operand1": 10.0, "operator": "/", "operand2": 2.5}`.
**Postconditions**: None.

---

**Test Case ID**: `TC_PARSER_VALID_005`
**Description**: Test with leading and trailing spaces.
**Preconditions**: `InputParser` instance available.
**Input**: `"  15 + 5  "`
**Test Steps**:
    1. Call `parser.parse("  15 + 5  ")`.
**Expected Output/Behavior**:
    Returns `{"operand1": 15.0, "operator": "+", "operand2": 5.0}`.
**Postconditions**: None.

---

**Test Case ID**: `TC_PARSER_VALID_006`
**Description**: Test with multiple spaces between components.
**Preconditions**: `InputParser` instance available.
**Input**: `"20   *    4"`
**Test Steps**:
    1. Call `parser.parse("20   *    4")`.
**Expected Output/Behavior**:
    Returns `{"operand1": 20.0, "operator": "*", "operand2": 4.0}`.
**Postconditions**: None.

---

**Test Case ID**: `TC_PARSER_VALID_007`
**Description**: Test with zero as an operand.
**Preconditions**: `InputParser` instance available.
**Input**: `"0 - 100"`
**Test Steps**:
    1. Call `parser.parse("0 - 100")`.
**Expected Output/Behavior**:
    Returns `{"operand1": 0.0, "operator": "-", "operand2": 100.0}`.
**Postconditions**: None.

---

**Test Case ID**: `TC_PARSER_VALID_008`
**Description**: Test with numbers that could be tricky for float conversion (e.g., ".5").
**Preconditions**: `InputParser` instance available.
**Input**: `".5 * 2"`
**Test Steps**:
    1. Call `parser.parse(".5 * 2")`.
**Expected Output/Behavior**:
    Returns `{"operand1": 0.5, "operator": "*", "operand2": 2.0}`.
**Postconditions**: None.

---

**Test Case ID**: `TC_PARSER_VALID_009`
**Description**: Test with numbers that have trailing zeros after decimal point.
**Preconditions**: `InputParser` instance available.
**Input**: `"10.000 + 5.0"`
**Test Steps**:
    1. Call `parser.parse("10.000 + 5.0")`.
**Expected Output/Behavior**:
    Returns `{"operand1": 10.0, "operator": "+", "operand2": 5.0}`.
**Postconditions**: None.

---

### 3.2. Invalid Format Errors (`InvalidFormatError`)

These tests verify that the `parse` method raises `InvalidFormatError` with the correct message for inputs that do not conform to the "number operator number" structure.

---

**Test Case ID**: `TC_PARSER_FORMAT_001`
**Description**: Test with an empty input string.
**Preconditions**: `InputParser` instance available.
**Input**: `""`
**Test Steps**:
    1. Call `parser.parse("")`.
**Expected Output/Behavior**:
    Raises `InvalidFormatError` with message: `"Error: Invalid input format. Expected 'number operator number'."`
**Postconditions**: None.

---

**Test Case ID**: `TC_PARSER_FORMAT_002`
**Description**: Test with an input string containing only spaces.
**Preconditions**: `InputParser` instance available.
**Input**: `"   "`
**Test Steps**:
    1. Call `parser.parse("   ")`.
**Expected Output/Behavior**:
    Raises `InvalidFormatError` with message: `"Error: Invalid input format. Expected 'number operator number'."`
**Postconditions**: None.

---

**Test Case ID**: `TC_PARSER_FORMAT_003`
**Description**: Test with too few parts (one number only).
**Preconditions**: `InputParser` instance available.
**Input**: `"5"`
**Test Steps**:
    1. Call `parser.parse("5")`.
**Expected Output/Behavior**:
    Raises `InvalidFormatError` with message: `"Error: Invalid input format. Expected 'number operator number'."`
**Postconditions**: None.

---

**Test Case ID**: `TC_PARSER_FORMAT_004`
**Description**: Test with too few parts (number and operator).
**Preconditions**: `InputParser` instance available.
**Input**: `"5 +"`
**Test Steps**:
    1. Call `parser.parse("5 +")`.
**Expected Output/Behavior**:
    Raises `InvalidFormatError` with message: `"Error: Invalid input format. Expected 'number operator number'."`
**Postconditions**: None.

---

**Test Case ID**: `TC_PARSER_FORMAT_005`
**Description**: Test with too many parts.
**Preconditions**: `InputParser` instance available.
**Input**: `"5 + 3 * 2"`
**Test Steps**:
    1. Call `parser.parse("5 + 3 * 2")`.
**Expected Output/Behavior**:
    Raises `InvalidFormatError` with message: `"Error: Invalid input format. Expected 'number operator number'."`
**Postconditions**: None.

---

**Test Case ID**: `TC_PARSER_FORMAT_006`
**Description**: Test with only an operator.
**Preconditions**: `InputParser` instance available.
**Input**: `"+"`
**Test Steps**:
    1. Call `parser.parse("+")`.
**Expected Output/Behavior**:
    Raises `InvalidFormatError` with message: `"Error: Invalid input format. Expected 'number operator number'."`
**Postconditions**: None.

---

**Test Case ID**: `TC_PARSER_FORMAT_007`
**Description**: Test with two numbers, no operator.
**Preconditions**: `InputParser` instance available.
**Input**: `"10 20"`
**Test Steps**:
    1. Call `parser.parse("10 20")`.
**Expected Output/Behavior**:
    Raises `InvalidFormatError` with message: `"Error: Invalid input format. Expected 'number operator number'."`
**Postconditions**: None.

---

### 3.3. Invalid Number Errors (`InvalidNumberError`)

These tests verify that the `parse` method raises `InvalidNumberError` with the correct message when an operand cannot be converted to a valid number.

---

**Test Case ID**: `TC_PARSER_NUMBER_001`
**Description**: Test with a non-numeric first operand.
**Preconditions**: `InputParser` instance available.
**Input**: `"abc + 5"`
**Test Steps**:
    1. Call `parser.parse("abc + 5")`.
**Expected Output/Behavior**:
    Raises `InvalidNumberError` with message: `"Error: Invalid number: 'abc'."`
**Postconditions**: None.

---

**Test Case ID**: `TC_PARSER_NUMBER_002`
**Description**: Test with a non-numeric second operand.
**Preconditions**: `InputParser` instance available.
**Input**: `"10 * xyz"`
**Test Steps**:
    1. Call `parser.parse("10 * xyz")`.
**Expected Output/Behavior**:
    Raises `InvalidNumberError` with message: `"Error: Invalid number: 'xyz'."`
**Postconditions**: None.

---

**Test Case ID**: `TC_PARSER_NUMBER_003`
**Description**: Test with a malformed number (e.g., multiple decimal points) as the first operand.
**Preconditions**: `InputParser` instance available.
**Input**: `"1.2.3 + 4"`
**Test Steps**:
    1. Call `parser.parse("1.2.3 + 4")`.
**Expected Output/Behavior**:
    Raises `InvalidNumberError` with message: `"Error: Invalid number: '1.2.3'."`
**Postconditions**: None.

---

**Test Case ID**: `TC_PARSER_NUMBER_004`
**Description**: Test with a malformed number as the second operand.
**Preconditions**: `InputParser` instance available.
**Input**: `"4 / 1..2"`
**Test Steps**:
    1. Call `parser.parse("4 / 1..2")`.
**Expected Output/Behavior**:
    Raises `InvalidNumberError` with message: `"Error: Invalid number: '1..2'."`
**Postconditions**: None.

---

**Test Case ID**: `TC_PARSER_NUMBER_005`
**Description**: Test with an operand that is just a symbol (not an operator).
**Preconditions**: `InputParser` instance available.
**Input**: `"@ + 5"`
**Test Steps**:
    1. Call `parser.parse("@ + 5")`.
**Expected Output/Behavior**:
    Raises `InvalidNumberError` with message: `"Error: Invalid number: '@'."`
**Postconditions**: None.

---

**Test Case ID**: `TC_PARSER_NUMBER_006`
**Description**: Test with a number containing non-numeric characters.
**Preconditions**: `InputParser` instance available.
**Input**: `"12a3 / 3"`
**Test Steps**:
    1. Call `parser.parse("12a3 / 3")`.
**Expected Output/Behavior**:
    Raises `InvalidNumberError` with message: `"Error: Invalid number: '12a3'."`
**Postconditions**: None.

---

### 3.4. Invalid Operator Errors (`InvalidOperatorError`)

These tests verify that the `parse` method raises `InvalidOperatorError` with the correct message when an unrecognized or unsupported operator is provided.

---

**Test Case ID**: `TC_PARSER_OPERATOR_001`
**Description**: Test with an unsupported operator (e.g., '%').
**Preconditions**: `InputParser` instance available.
**Input**: `"10 % 2"`
**Test Steps**:
    1. Call `parser.parse("10 % 2")`.
**Expected Output/Behavior**:
    Raises `InvalidOperatorError` with message: `"Error: Invalid operator: '%'. Supported operators are +, -, *, /."`
**Postconditions**: None.

---

**Test Case ID**: `TC_PARSER_OPERATOR_002`
**Description**: Test with another unsupported operator (e.g., '^').
**Preconditions**: `InputParser` instance available.
**Input**: `"2 ^ 3"`
**Test Steps**:
    1. Call `parser.parse("2 ^ 3")`.
**Expected Output/Behavior**:
    Raises `InvalidOperatorError` with message: `"Error: Invalid operator: '^'. Supported operators are +, -, *, /."`
**Postconditions**: None.

---

**Test Case ID**: `TC_PARSER_OPERATOR_003`
**Description**: Test with a multi-character unsupported operator.
**Preconditions**: `InputParser` instance available.
**Input**: `"10 ** 2"`
**Test Steps**:
    1. Call `parser.parse("10 ** 2")`.
**Expected Output/Behavior**:
    Raises `InvalidOperatorError` with message: `"Error: Invalid operator: '**'. Supported operators are +, -, *, /."`
**Postconditions**: None.

---

**Test Case ID**: `TC_PARSER_OPERATOR_004`
**Description**: Test with a non-symbol operator.
**Preconditions**: `InputParser` instance available.
**Input**: `"10 add 5"`
**Test Steps**:
    1. Call `parser.parse("10 add 5")`.
**Expected Output/Behavior**:
    Raises `InvalidOperatorError` with message: `"Error: Invalid operator: 'add'. Supported operators are +, -, *, /."`
**Postconditions**: None.

---

## 4. Summary of Test Coverage

The test cases above cover:
*   Successful parsing of valid inputs with integers, floats, negative numbers, and various spacing.
*   All supported arithmetic operators (+, -, \*, /).
*   `InvalidFormatError` for:
    *   Empty or whitespace-only input.
    *   Inputs with too few or too many components.
*   `InvalidNumberError` for:
    *   Non-numeric text as operands.
    *   Malformed numerical strings.
*   `InvalidOperatorError` for:
    *   Operators not in the supported set.

These tests aim to provide comprehensive coverage for the `InputParser.parse` method as per the defined requirements and LLDs.