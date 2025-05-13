---
title: "Unit Test Cases - Calculation Engine Logic"
version: "0.1.0"
status: "Draft"
created_by: "tdd"
created_date: "2025-05-13T23:18:00Z"
last_modified_by: "tdd"
last_modified_date: "2025-05-13T23:18:00Z"
related_tasks: ["TEST-CASES-CALC-002"]
relevant_links:
  - "../../lld/LLD-CALC-001_calculator_module.md"
  - "./TEST-PLAN-001_overall_test_plan.md"
  - "../../specifications/SPEC-MAIN-001_console_calculator_main_specification.md"
tags: ["test_cases", "unit_test", "calculation_engine", "python", "calculator", "arithmetic_operations"]
parent_document: "./TEST-PLAN-001_overall_test_plan.md"
child_documents: []
related_concepts: ["arithmetic_operations", "error_handling", "division_by_zero", "unit_testing", "test_driven_development"]
project_type_tags: ["cli-app", "python"]
visibility: "internal"
---

# Unit Test Cases - Calculation Engine (`perform_calculation`)

This document outlines the unit test cases for the `perform_calculation` function within the Calculation Engine module, as specified in [`LLD-CALC-001_calculator_module.md`](../../lld/LLD-CALC-001_calculator_module.md). These tests aim to verify the correctness of arithmetic operations, handling of edge cases, and error conditions.

## Test Case Format

Each test case is defined with the following attributes:
-   **Test Case ID**: A unique identifier for the test case.
-   **Description/Purpose**: A brief explanation of what the test case verifies.
-   **Input `operand1`**: The first numerical input.
-   **Input `operator`**: The arithmetic operator.
-   **Input `operand2`**: The second numerical input.
-   **Expected `has_error`**: The expected boolean value for the `has_error` key in the result dictionary.
-   **Expected `value`**: The expected numerical result if `has_error` is `False`, otherwise `None`.
-   **Expected `error_message`**: The expected error message string if `has_error` is `True`, otherwise `None`.

## 1. Addition (+) Test Cases

| Test Case ID      | Description/Purpose                                  | Input `operand1` | Input `operator` | Input `operand2` | Expected `has_error` | Expected `value` | Expected `error_message` |
|-------------------|------------------------------------------------------|------------------|------------------|------------------|----------------------|------------------|--------------------------|
| TC_CALC_ADD_001   | Add two positive integers.                           | 5                | +                | 3                | False                | 8.0              | None                     |
| TC_CALC_ADD_002   | Add two positive floats.                             | 5.5              | +                | 3.2              | False                | 8.7              | None                     |
| TC_CALC_ADD_003   | Add a positive and a negative number.                | 10               | +                | -3               | False                | 7.0              | None                     |
| TC_CALC_ADD_004   | Add a negative and a positive number.                | -7               | +                | 4                | False                | -3.0             | None                     |
| TC_CALC_ADD_005   | Add two negative numbers.                            | -2.5             | +                | -3.5             | False                | -6.0             | None                     |
| TC_CALC_ADD_006   | Add a number and zero.                               | 6                | +                | 0                | False                | 6.0              | None                     |
| TC_CALC_ADD_007   | Add zero and a number.                               | 0                | +                | -9               | False                | -9.0             | None                     |
| TC_CALC_ADD_008   | Add zero and zero.                                   | 0                | +                | 0                | False                | 0.0              | None                     |
| TC_CALC_ADD_009   | Add large positive numbers.                          | 1000000          | +                | 2000000          | False                | 3000000.0        | None                     |
| TC_CALC_ADD_010   | Add small (fractional) positive numbers.             | 0.1              | +                | 0.2              | False                | 0.3              | None                     |

## 2. Subtraction (-) Test Cases

| Test Case ID      | Description/Purpose                                  | Input `operand1` | Input `operator` | Input `operand2` | Expected `has_error` | Expected `value` | Expected `error_message` |
|-------------------|------------------------------------------------------|------------------|------------------|------------------|----------------------|------------------|--------------------------|
| TC_CALC_SUB_001   | Subtract a smaller positive integer from a larger one. | 10               | -                | 3                | False                | 7.0              | None                     |
| TC_CALC_SUB_002   | Subtract a larger positive float from a smaller one. | 3.5              | -                | 5.2              | False                | -1.7             | None                     |
| TC_CALC_SUB_003   | Subtract a negative number from a positive number.   | 8                | -                | -2               | False                | 10.0             | None                     |
| TC_CALC_SUB_004   | Subtract a positive number from a negative number.   | -5               | -                | 3                | False                | -8.0             | None                     |
| TC_CALC_SUB_005   | Subtract two negative numbers (-a - (-b) = -a + b).  | -2.5             | -                | -3.5             | False                | 1.0              | None                     |
| TC_CALC_SUB_006   | Subtract zero from a number.                         | 7                | -                | 0                | False                | 7.0              | None                     |
| TC_CALC_SUB_007   | Subtract a number from zero.                         | 0                | -                | 4                | False                | -4.0             | None                     |
| TC_CALC_SUB_008   | Subtract zero from zero.                             | 0                | -                | 0                | False                | 0.0              | None                     |
| TC_CALC_SUB_009   | Subtract a number from itself.                       | 6.7              | -                | 6.7              | False                | 0.0              | None                     |

## 3. Multiplication (*) Test Cases

| Test Case ID      | Description/Purpose                                  | Input `operand1` | Input `operator` | Input `operand2` | Expected `has_error` | Expected `value` | Expected `error_message` |
|-------------------|------------------------------------------------------|------------------|------------------|------------------|----------------------|------------------|--------------------------|
| TC_CALC_MUL_001   | Multiply two positive integers.                      | 6                | *                | 4                | False                | 24.0             | None                     |
| TC_CALC_MUL_002   | Multiply two positive floats.                        | 2.5              | *                | 3.0              | False                | 7.5              | None                     |
| TC_CALC_MUL_003   | Multiply a positive and a negative number.           | 7                | *                | -2               | False                | -14.0            | None                     |
| TC_CALC_MUL_004   | Multiply two negative numbers.                       | -3               | *                | -5               | False                | 15.0             | None                     |
| TC_CALC_MUL_005   | Multiply a number by zero.                           | 9.8              | *                | 0                | False                | 0.0              | None                     |
| TC_CALC_MUL_006   | Multiply zero by a number.                           | 0                | *                | -6               | False                | 0.0              | None                     |
| TC_CALC_MUL_007   | Multiply zero by zero.                               | 0                | *                | 0                | False                | 0.0              | None                     |
| TC_CALC_MUL_008   | Multiply a number by 1.                              | 12.3             | *                | 1                | False                | 12.3             | None                     |
| TC_CALC_MUL_009   | Multiply a number by -1.                             | 8                | *                | -1               | False                | -8.0             | None                     |

## 4. Division (/) Test Cases

| Test Case ID      | Description/Purpose                                  | Input `operand1` | Input `operator` | Input `operand2` | Expected `has_error` | Expected `value` | Expected `error_message`                       |
|-------------------|------------------------------------------------------|------------------|------------------|------------------|----------------------|------------------|------------------------------------------------|
| TC_CALC_DIV_001   | Divide a larger positive integer by a smaller one.   | 10               | /                | 2                | False                | 5.0              | None                                           |
| TC_CALC_DIV_002   | Divide a positive float by another, resulting float. | 7.5              | /                | 2.0              | False                | 3.75             | None                                           |
| TC_CALC_DIV_003   | Divide a positive number by a negative number.       | 12               | /                | -3               | False                | -4.0             | None                                           |
| TC_CALC_DIV_004   | Divide a negative number by a positive number.       | -9               | /                | 3                | False                | -3.0             | None                                           |
| TC_CALC_DIV_005   | Divide two negative numbers.                         | -8.0             | /                | -4.0             | False                | 2.0              | None                                           |
| TC_CALC_DIV_006   | Divide zero by a non-zero positive number.           | 0                | /                | 5                | False                | 0.0              | None                                           |
| TC_CALC_DIV_007   | Divide zero by a non-zero negative number.           | 0                | /                | -2.5             | False                | 0.0              | None                                           |
| TC_CALC_DIV_008   | Divide a number by 1.                                | 7.7              | /                | 1                | False                | 7.7              | None                                           |
| TC_CALC_DIV_009   | Divide a number by itself (non-zero).                | 4.5              | /                | 4.5              | False                | 1.0              | None                                           |
| TC_CALC_DIV_010   | Divide resulting in a repeating decimal (approx).    | 10               | /                | 3                | False                | 3.3333333333333335 | None                                           |

## 5. Error Condition Test Cases

| Test Case ID      | Description/Purpose                                  | Input `operand1` | Input `operator` | Input `operand2` | Expected `has_error` | Expected `value` | Expected `error_message`                                       |
|-------------------|------------------------------------------------------|------------------|------------------|------------------|----------------------|------------------|----------------------------------------------------------------|
| TC_CALC_ERR_001   | Division by zero (positive operand1).                | 5                | /                | 0                | True                 | None             | "Error: Division by zero is not allowed."                      |
| TC_CALC_ERR_002   | Division by zero (negative operand1).                | -5               | /                | 0                | True                 | None             | "Error: Division by zero is not allowed."                      |
| TC_CALC_ERR_003   | Division by zero (zero operand1).                    | 0                | /                | 0                | True                 | None             | "Error: Division by zero is not allowed."                      |
| TC_CALC_ERR_004   | Unknown operator (e.g., '%').                        | 10               | %                | 5                | True                 | None             | "Error: Internal - Unknown operator received by CalculationEngine." |
| TC_CALC_ERR_005   | Unknown operator (e.g., 'foo').                      | 7                | foo              | 3                | True                 | None             | "Error: Internal - Unknown operator received by CalculationEngine." |

**Note on Floating Point Precision:** For test cases involving floating-point arithmetic (e.g., `TC_CALC_ADD_010`, `TC_CALC_SUB_002`, `TC_CALC_DIV_010`), the `Expected value` might need to be compared with a certain tolerance during actual test implementation due to the nature of floating-point representation. The values provided are the direct results from standard Python float operations.