import subprocess
import shlex
import os

# Re-evaluating the run_command for better error handling, still dangerous
def run_command(user_input: str) -> tuple[bool, str, str, int]:
    """
    **WARNING: This function executes arbitrary commands from user input.**
    It uses shlex.split and shell=False to mitigate shell injection risks,
    but it does NOT prevent execution of malicious commands themselves.
    Only use with highly trusted and sanitized input.

    Returns (success: bool, stdout: str, stderr: str, returncode: int).
    """
    args = shlex.split(user_input)
    if not args:
        return False, "", "No command provided.", 0

    try:
        # Using subprocess.run for more modern control
        # capture_output=True: captures stdout and stderr
        # text=True: decodes stdout/stderr as strings using default encoding
        # check=True: raises CalledProcessError if the command returns a non-zero exit code
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return True, result.stdout, result.stderr, result.returncode
    except FileNotFoundError:
        return False, "", f"Error: Command '{args[0]}' not found.", 127 # Common exit code for command not found
    except subprocess.CalledProcessError as e:
        # Command ran, but returned a non-zero exit code (e.g., 'grep' not finding a pattern)
        return False, e.stdout, e.stderr, e.returncode
    except Exception as e:
        # Catch other potential exceptions during subprocess execution
        return False, "", f"An unexpected error occurred: {e}", -1