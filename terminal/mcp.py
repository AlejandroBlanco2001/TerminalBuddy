from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import SseConnectionParams


context_7_mcp = SseConnectionParams(
    url="https://mcp.context7.com/mcp",
)

mcps = McpToolset(
    connection_params=context_7_mcp,
)
