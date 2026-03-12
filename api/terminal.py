import subprocess
import threading
import time


# Module-level singleton — set by the lifespan in main.py
session: "TerminalSession | None" = None

class TerminalSession:

    def __init__(self):
        self._lock = threading.Lock()
        self._output_buffer: list[str] = []
        # Keep the buffer from growing without bound when running long-lived
        # processes like FastAPI/uvicorn.
        self._max_buffer_lines = 10_000

        self.proc = subprocess.Popen(
            ["powershell.exe"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )

        self._reader_thread = threading.Thread(
            target=self._reader_loop, daemon=True
        )
        self._reader_thread.start()

    def _append_output(self, chunk: str) -> None:
        if not chunk:
            return
        self._output_buffer.append(chunk)
        if len(self._output_buffer) > self._max_buffer_lines:
            overflow = len(self._output_buffer) - self._max_buffer_lines
            del self._output_buffer[:overflow]

    def _reader_loop(self):
        """Background thread that continuously drains stdout into the buffer."""
        assert self.proc.stdout is not None
        for line in self.proc.stdout:
            with self._lock:
                self._append_output(line)

    def send(self, command: str, wait_seconds: float = 0.5) -> str:
        """Send a command and return output observed within a short window.

        For long-running commands (for example starting a FastAPI server),
        this returns only the initial output. Further logs can be collected
        via `read_and_clear` or `read_buffer`.
        """
        with self._lock:
            self._output_buffer.clear()

        assert self.proc.stdin is not None
        self.proc.stdin.write(command + "\n")
        self.proc.stdin.flush()

        if wait_seconds <= 0:
            return ""

        time.sleep(wait_seconds)

        with self._lock:
            return "".join(self._output_buffer)

    def read_buffer(self) -> str:
        """Return a snapshot of the current output buffer without clearing it."""
        with self._lock:
            return "".join(self._output_buffer)

    def read_and_clear(self) -> str:
        """Drain and return all currently buffered output."""
        with self._lock:
            data = "".join(self._output_buffer)
            self._output_buffer.clear()
            return data

    def terminate(self):
        self.proc.terminate()
        self.proc.wait()