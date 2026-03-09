from google.adk.cli.fast_api import get_fast_api_app
import uvicorn
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
AGENTS_DIR = ROOT_FOLDER

app = get_fast_api_app(
    agents_dir=AGENTS_DIR,
    web=False,
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)