"""Context7 MCP for Google ADK — up-to-date library docs for the agent.
"""
import os
from pathlib import Path

from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

_project_root = Path(__file__).resolve().parent.parent

_env = os.environ.copy()
if os.environ.get("CONTEXT7_API_KEY"):
    _env["CONTEXT7_API_KEY"] = os.environ["CONTEXT7_API_KEY"]

context7_params = StdioConnectionParams(
    server_params=StdioServerParameters(
        command="npx",
        args=["-y", "@upstash/context7-mcp"],
        env=_env,
        cwd=_project_root,
    ),
    timeout=30.0,
)

context7_mcp = McpToolset(connection_params=context7_params)

filesystem_params = StdioConnectionParams(
    server_params=StdioServerParameters(
        command="npx",
        args=[
            "-y",
            "@modelcontextprotocol/server-filesystem",
            os.path.abspath(_project_root),
        ],
    ),
    timeout=30.0,
)
filesystem_mcp = McpToolset(connection_params=filesystem_params)

