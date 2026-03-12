import subprocess
import threading
import time

# Module-level singleton — set by the lifespan in main.py
session: "TerminalSession | None" = None

class TerminalSession:

    def __init__(self):
        self.proc = subprocess.Popen(
            ["powershell.exe"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        self._lock = threading.Lock()
        self._output_buffer: list[str] = []
        self._reader_thread = threading.Thread(target=self._reader_loop, daemon=True)
        self._reader_thread.start()

    def _reader_loop(self):
        """Background thread that continuously drains stdout into the buffer."""
        for line in self.proc.stdout:
            with self._lock:
                self._output_buffer.append(line)

    def send(self, command: str) -> str:
        """Send a command and return the output produced within a short window."""
        with self._lock:
            self._output_buffer.clear()

        self.proc.stdin.write(command + "\n")
        self.proc.stdin.flush()

        time.sleep(0.8)

        with self._lock:
            return "".join(self._output_buffer)

    def read_buffer(self) -> str:
        """Return whatever is currently in the output buffer without sending a command."""
        with self._lock:
            return "".join(self._output_buffer)

    def terminate(self):
        self.proc.terminate()
        self.proc.wait()