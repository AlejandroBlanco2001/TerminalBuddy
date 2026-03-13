from google.adk.cli.fast_api import get_fast_api_app
import uvicorn
from pathlib import Path
from contextlib import asynccontextmanager
from fastapi import FastAPI
import api.terminal as terminal_module
from api.terminal import TerminalSession

ROOT_FOLDER = Path(__file__).parent
AGENTS_DIR = ROOT_FOLDER

@asynccontextmanager
async def lifespan(app: FastAPI):
    terminal_module.session = TerminalSession()
    terminal_module.session.send("uv run example/main.py")
    yield
    terminal_module.session.terminate()
    terminal_module.session = None

app = get_fast_api_app(
    agents_dir=AGENTS_DIR,
    web=True,
    session_service_uri="sqlite+aiosqlite:///./session.db",
    lifespan=lifespan
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)