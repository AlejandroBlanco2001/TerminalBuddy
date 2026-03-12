"""ADK tool functions that wrap the shared TerminalSession singleton."""
import api.terminal as terminal_module


def run_command(command: str) -> str:
    """Run a shell command in the persistent PowerShell session and return its output.

    Args:
        command: The PowerShell command to execute.

    Returns:
        The text output produced by the command.
    """
    if terminal_module.session is None:
        return "Error: terminal session is not initialised."
    return terminal_module.session.send(command)


def read_output() -> str:
    """Read whatever output is currently buffered from the terminal without sending a new command.

    Returns:
        Any pending output from the terminal.
    """
    if terminal_module.session is None:
        return "Error: terminal session is not initialised."
    return terminal_module.session.read_buffer()
