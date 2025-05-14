# Python Console Calculator User Manual

## 1. Introduction

Welcome to the Python Console Calculator! This simple application allows you to perform basic arithmetic calculations directly from your console or terminal. This guide will walk you through how to run the calculator, input expressions, understand its features, and troubleshoot common issues.

## 2. Getting Started

### Prerequisites
*   Python 3.x installed on your system.

### Running the Calculator
To start the calculator, open your terminal or command prompt, navigate to the root directory of the project, and run the following command:

```bash
python -m src.calculator.main
```
Alternatively, if you are in the `src/calculator` directory, you might be ableto run it with:
```bash
python main.py
```

Upon starting, you will see a welcome message:
```
Welcome to the Console Calculator!
You can type expressions like '1 + 1', or 'quit'/'exit' to leave.
calc> 
```
The `calc> ` prompt indicates that the calculator is ready for your input.

## 3. How to Use

### Input Format
The calculator expects you to enter expressions in the following format:

`number operator number`

Where:
*   `number`: Can be an integer (e.g., `5`, `-10`) or a floating-point number (e.g., `3.14`, `-0.5`).
*   `operator`: One of the supported arithmetic operators.
*   There should be a space between each number and the operator.

**Examples:**
*   `10 + 5`
*   `3.14 * 2`
*   `-7 / 3.5`
*   `100 - 200`

After you type your expression and press Enter, the calculator will display the result on the next line and then show a new `calc> ` prompt for your next calculation.

**Example Interaction:**
```
calc> 10 + 5
15.0
calc> 2.5 * 4
10.0
calc> 
```

### Supported Operations
The calculator supports the following basic arithmetic operations:

| Operator | Operation    | Example     | Result |
| :------- | :----------- | :---------- | :----- |
| `+`      | Addition     | `7 + 3`     | `10.0` |
| `-`      | Subtraction  | `10 - 4.5`  | `5.5`  |
| `*`      | Multiplication | `6 * 7`     | `42.0` |
| `/`      | Division     | `9 / 2`     | `4.5`  |

## 4. Exiting the Calculator

To exit the calculator application, simply type `exit` or `quit` (case-insensitive) at the `calc> ` prompt and press Enter.

**Example:**
```
calc> exit
Thank you for using the calculator.
```
or
```
calc> QUIT
Thank you for using the calculator.
```
You can also exit by pressing `Ctrl+C`. This will display:
```
calc> ^C
Calculator exited by user. Goodbye!
Thank you for using the calculator.
```

## 5. Error Messages

If you enter an expression incorrectly or attempt an invalid operation, the calculator will display an error message. Here are some common error messages and their meanings:

*   **`Error: Division by zero is not allowed.`**
    *   **Meaning**: You attempted to divide a number by zero (e.g., `10 / 0`). Division by zero is undefined in mathematics.
    *   **Solution**: Ensure the second number (divisor) in a division operation is not zero.

*   **`Error: Invalid input format. Expected 'number operator number'.`**
    *   **Meaning**: Your input does not follow the `number operator number` structure. This could be due to too few parts (e.g., `5 +`), too many parts (e.g., `5 + 3 2`), or no input at all.
    *   **Solution**: Check your input and make sure it consists of exactly one number, one operator, and another number, each separated by a single space.

*   **`Error: Invalid number: '[your_input]'.`**
    *   **Meaning**: One of the numbers you entered is not a valid numerical value (e.g., `abc + 5` or `5 + xyz`). The `[your_input]` part will show the specific text that was not recognized as a number.
    *   **Solution**: Ensure that both operands are valid integers or floating-point numbers.

*   **`Error: Invalid operator: '[your_operator]'. Supported operators are +, -, *, /.`**
    *   **Meaning**: The operator you used is not one of the supported operators (`+`, `-`, `*`, `/`). The `[your_operator]` part will show the operator that was not recognized.
    *   **Solution**: Use only the supported operators.

If an unexpected error occurs within the application, you might see a message like:
`An unexpected error occurred at the top level: [error details]`
`Calculator shutting down.`

In such cases, please ensure your Python environment is set up correctly.

---

We hope this user manual helps you use the Python Console Calculator effectively!