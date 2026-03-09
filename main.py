from google.adk.cli.fast_api import get_fast_api_app
from google.adk.sessions.database_session_service import DatabaseSessionService
import uvicorn
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
AGENTS_DIR = ROOT_FOLDER

session_service = DatabaseSessionService(
    db_url="sqlite:///./session.db"
)

app = get_fast_api_app(
    agents_dir=AGENTS_DIR,
    web=False,
    session_service=session_service,
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)