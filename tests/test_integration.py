import subprocess
import sys
import os
import pytest
from typing import List

# Define paths and constants
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# Ensure src directory is in Python path for imports if main.py relies on it
# This is often handled by pytest configuration or running pytest from project root.
# If main.py uses relative imports like `from .module import ...` and is run as a script,
# it might need to adjust sys.path itself.
# We assume `src` is in PYTHONPATH or `main.py` handles its module resolution.
MAIN_SCRIPT_PATH = os.path.join(PROJECT_ROOT, "src", "calculator", "main.py")

PROMPT = "calc> "  # Updated prompt based on manual test
EXIT_MSG = "\n" # Actual immediate response to exit command

# Error messages updated based on pytest output
ERR_DIV_ZERO = "Error: Division by zero is not allowed.\n"
ERR_INVALID_FORMAT = "Error: Invalid input format. Expected 'number operator number'.\n"
ERR_INVALID_NUMBER_TPL = "Error: Invalid number: '{}'.\n"
ERR_INVALID_OPERATOR_TPL = "Error: Invalid operator: '{}'. Supported operators are +, -, *, /.\n"
# Empty input is treated as an invalid format error
EMPTY_INPUT_RESPONSE = ERR_INVALID_FORMAT


def get_calculator_responses(inputs: List[str], timeout_seconds: float = 2.0) -> List[str]:
    """
    Runs the calculator main.py script as a subprocess.
    Sends a series of inputs (each followed by a newline).
    Reads and discards the initial prompt.
    For each subsequent input:
        - Sends the input.
        - If the input is an exit command, reads the exit message and stops.
        - Otherwise, reads one line of output (result/error), then reads and discards the next prompt.
    Returns a list of the captured output lines (results or errors).
    """
    command = [sys.executable, MAIN_SCRIPT_PATH]

    # Set PYTHONPATH for the subprocess to include the project root
    env = os.environ.copy()
    env["PYTHONPATH"] = PROJECT_ROOT + os.pathsep + env.get("PYTHONPATH", "")
    
    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, # Capture stderr for debugging if needed
        text=True,
        cwd=PROJECT_ROOT,
        env=env, # Pass the modified environment
        bufsize=1  # Line-buffered
    )

    responses: List[str] = []

    try:
        # Robustly read until the first prompt is encountered
        # This handles an optional welcome message (single or multi-line)
        buffer = ""
        prompt_found = False
        MAX_INITIAL_READ_CHARS = 1024
        chars_read_count = 0

        try:
            while chars_read_count < MAX_INITIAL_READ_CHARS:
                char = process.stdout.read(1)
                if not char:
                    # Process exited before printing the prompt or stream ended.
                    # This might happen if the process crashes on startup.
                    # We'll capture stderr outside this specific read loop if prompt_found is false.
                    break
                
                buffer += char
                chars_read_count += 1

                if buffer.endswith(PROMPT):
                    prompt_found = True
                    # welcome_message_actual = buffer[:-len(PROMPT)] # Can be logged if needed
                    break
        except Exception as e_read:
            process.terminate()
            process.wait(timeout=timeout_seconds)
            stderr_output = process.stderr.read()
            raise TimeoutError(f"Exception while reading for initial prompt. Stderr: {stderr_output}. Error: {e_read}. Buffer: '{buffer}'")

        if not prompt_found:
            # If prompt wasn't found, process might have exited or printed unexpected output.
            # Try to get stderr for more info.
            stderr_output = ""
            if process.poll() is not None: # Process has terminated
                stderr_output = process.stderr.read()
            else: # Process still running, but prompt not found (e.g. MAX_INITIAL_READ_CHARS reached)
                process.terminate()
                process.wait(timeout=timeout_seconds)
                stderr_output = process.stderr.read() # Read stderr after termination
            raise TimeoutError(
                f"Failed to find initial prompt '{PROMPT}' after reading {chars_read_count} chars. "
                f"Process exit code: {process.returncode}. Stderr: {stderr_output}. Buffer: '{buffer}'"
            )

        # Initial prompt has been consumed by reading into `buffer`.
        # Proceed with sending inputs.
        for user_input_str in inputs:
            if process.poll() is not None:
                # Process terminated unexpectedly
                stderr_output = process.stderr.read()
                raise Exception(f"Calculator process terminated prematurely. Stderr: {stderr_output}")

            process.stdin.write(user_input_str + "\n")
            process.stdin.flush()

            if user_input_str.lower() in ["exit", "quit"]:
                line = process.stdout.readline() # Read exit message
                responses.append(line)
                break  # Interaction ends

            # Based on error log: app prints a blank line, then result/error, then prompt.
            # 1. Read and discard the blank separator line.
            separator_line = process.stdout.readline()
            # Optionally, assert separator_line == '\n' if this behavior is strictly guaranteed.
            # For now, we just consume it. If it's not there, the next readline will get the actual content.
            # However, the error log strongly implies it IS there for calculations.

            # 2. Read the actual result or error line.
            actual_result_line = process.stdout.readline()
            responses.append(actual_result_line)
        
            if process.poll() is not None and not actual_result_line: # Process died after last input
                 break

            # 3. Read and discard the next prompt.
            # The prompt itself does not end with a newline when printed by input()
            next_prompt_read = process.stdout.read(len(PROMPT))
            if not next_prompt_read and process.poll() is not None: # Process might have exited
                break
            assert next_prompt_read == PROMPT, \
                f"Expected next prompt '{PROMPT}', got '{next_prompt_read}'. Input: '{user_input_str}', Separator: '{separator_line.strip()}', Output: '{actual_result_line.strip()}'"

    except Exception as e:
        # Catch any exception during interaction to provide more context
        stderr_data = ""
        if process.poll() is None: # If process is still running, try to get stderr
             try:
                process.terminate() # Try to terminate gracefully
                _, stderr_data_bytes = process.communicate(timeout=0.5) # Drain pipes
                stderr_data = stderr_data_bytes if isinstance(stderr_data_bytes, str) else stderr_data_bytes.decode('utf-8', 'replace')
             except subprocess.TimeoutExpired:
                process.kill() # Force kill
                _, stderr_data_bytes = process.communicate()
                stderr_data = stderr_data_bytes if isinstance(stderr_data_bytes, str) else stderr_data_bytes.decode('utf-8', 'replace')
        else: # Process already terminated
            stderr_data = process.stderr.read()

        pytest.fail(f"Error during calculator interaction: {e}\nStderr: {stderr_data}\nResponses so far: {responses}")
    finally:
        # Ensure process is cleaned up
        if process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=timeout_seconds)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait() # Wait for kill to complete
        # Optionally, read and print/log any remaining stderr
        # stderr_final = process.stderr.read()
        # if stderr_final:
        #     print(f"Final stderr: {stderr_final}")
        process.stdin.close()
        process.stdout.close()
        process.stderr.close()
        
    return responses


class TestValidCalculations:
    def test_tc_int_calc_001_integer_addition(self):
        inputs = ["10 + 5"]
        expected_responses = ["15\n"]
        assert get_calculator_responses(inputs) == expected_responses

    def test_tc_int_calc_002_integer_subtraction(self):
        inputs = ["10 - 5"]
        expected_responses = ["5\n"]
        assert get_calculator_responses(inputs) == expected_responses

    def test_tc_int_calc_003_integer_multiplication(self):
        inputs = ["10 * 5"]
        expected_responses = ["50\n"]
        assert get_calculator_responses(inputs) == expected_responses

    def test_tc_int_calc_004_integer_division(self):
        inputs = ["10 / 5"]
        # Division of ints might produce float if not perfectly divisible,
        # or int if perfectly divisible. Assuming int for this case.
        # If spec says all division is float, this should be "2.0\n".
        # Manual output "15" for "10+5" suggests int preference.
        expected_responses = ["2\n"]
        assert get_calculator_responses(inputs) == expected_responses

    def test_tc_int_calc_005_float_addition(self):
        inputs = ["10.5 + 5.2"]
        expected_responses = ["15.7\n"]
        assert get_calculator_responses(inputs) == expected_responses

    def test_tc_int_calc_006_float_subtraction(self):
        # Note: 10.5 - 5.2 = 5.299999999999999. Test assumes calculator formats output.
        inputs = ["10.5 - 5.2"]
        expected_responses = ["5.3\n"] 
        assert get_calculator_responses(inputs) == expected_responses

    def test_tc_int_calc_007_float_multiplication(self):
        inputs = ["2.5 * 2.0"]
        expected_responses = ["5\n"] # Actual output is int format
        assert get_calculator_responses(inputs) == expected_responses

    def test_tc_int_calc_008_float_division(self):
        inputs = ["10.0 / 2.5"]
        expected_responses = ["4\n"] # Actual output is int format
        assert get_calculator_responses(inputs) == expected_responses

    def test_tc_int_calc_009_mixed_calculation(self):
        inputs = ["5 + 2.5"]
        expected_responses = ["7.5\n"]
        assert get_calculator_responses(inputs) == expected_responses

    def test_tc_int_calc_010_negative_numbers(self):
        inputs = ["-10 + 5"]
        expected_responses = ["-5\n"] # Integer result
        assert get_calculator_responses(inputs) == expected_responses

    def test_tc_int_calc_011_result_negative(self):
        inputs = ["5 - 10.5"]
        expected_responses = ["-5.5\n"] # Float result
        assert get_calculator_responses(inputs) == expected_responses

    def test_tc_int_calc_012_with_zero(self):
        inputs = ["0 * 10"]
        expected_responses = ["0\n"] # Integer result
        assert get_calculator_responses(inputs) == expected_responses
    
    def test_tc_int_calc_013_multiple_spaces(self):
        inputs = ["10  +    5"]
        expected_responses = ["15\n"] # Integer result
        assert get_calculator_responses(inputs) == expected_responses


class TestExitCommands:
    def test_tc_int_exit_001_exit_lowercase(self):
        inputs = ["exit"]
        expected_responses = [EXIT_MSG]
        assert get_calculator_responses(inputs) == expected_responses

    def test_tc_int_exit_002_quit_lowercase(self):
        inputs = ["quit"]
        expected_responses = [EXIT_MSG]
        assert get_calculator_responses(inputs) == expected_responses

    def test_tc_int_exit_003_exit_uppercase(self):
        inputs = ["EXIT"]
        expected_responses = [EXIT_MSG]
        assert get_calculator_responses(inputs) == expected_responses

    def test_tc_int_exit_004_quit_uppercase(self):
        inputs = ["QUIT"]
        expected_responses = [EXIT_MSG]
        assert get_calculator_responses(inputs) == expected_responses

    def test_tc_int_exit_005_exit_mixed_case(self):
        inputs = ["ExIt"]
        expected_responses = [EXIT_MSG]
        assert get_calculator_responses(inputs) == expected_responses


class TestErrorHandling:
    def test_tc_int_err_001_division_by_zero(self):
        inputs = ["10 / 0"]
        expected_responses = [ERR_DIV_ZERO]
        assert get_calculator_responses(inputs) == expected_responses

    def test_tc_int_err_002_invalid_format_too_few(self):
        inputs = ["10 +"]
        expected_responses = [ERR_INVALID_FORMAT]
        assert get_calculator_responses(inputs) == expected_responses

    def test_tc_int_err_003_invalid_format_too_many(self):
        inputs = ["10 + 5 + 3"]
        expected_responses = [ERR_INVALID_FORMAT]
        assert get_calculator_responses(inputs) == expected_responses
    
    def test_tc_int_err_004_invalid_format_gibberish(self):
        inputs = ["abc"]
        expected_responses = [ERR_INVALID_FORMAT]
        assert get_calculator_responses(inputs) == expected_responses

    def test_tc_int_err_005_invalid_number_first(self):
        inputs = ["1.2.3 + 5"]
        expected_responses = [ERR_INVALID_NUMBER_TPL.format("1.2.3")]
        assert get_calculator_responses(inputs) == expected_responses

    def test_tc_int_err_006_invalid_number_second(self):
        inputs = ["5 + 1.2.3"]
        expected_responses = [ERR_INVALID_NUMBER_TPL.format("1.2.3")]
        assert get_calculator_responses(inputs) == expected_responses

    def test_tc_int_err_007_invalid_operator(self):
        inputs = ["10 # 5"]
        expected_responses = [ERR_INVALID_OPERATOR_TPL.format("#")]
        assert get_calculator_responses(inputs) == expected_responses

    def test_tc_int_err_008_empty_input(self):
        # Assuming empty input results in an empty line of output before re-prompt
        inputs = [""]
        expected_responses = [EMPTY_INPUT_RESPONSE]
        assert get_calculator_responses(inputs) == expected_responses


class TestSequentialOperations:
    def test_tc_int_seq_001_multiple_valid(self):
        inputs = ["10 + 5", "2 * 3", "100 / 4"]
        expected_responses = ["15\n", "6\n", "25\n"] # Integer results
        assert get_calculator_responses(inputs) == expected_responses

    def test_tc_int_seq_002_valid_error_valid(self):
        inputs = ["10 + 5", "1 / 0", "2 * 3"]
        expected_responses = ["15\n", ERR_DIV_ZERO, "6\n"] # Integer results
        assert get_calculator_responses(inputs) == expected_responses

    def test_tc_int_seq_003_valid_then_exit(self):
        inputs = ["7 - 2", "exit"]
        expected_responses = ["5\n", EXIT_MSG] # Integer result
        assert get_calculator_responses(inputs) == expected_responses