from google.adk.agents.llm_agent import LlmAgent
from google.adk.apps.app import App
from google.adk.apps.app import ResumabilityConfig
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.function_tool import FunctionTool
from .mcp import context7_mcp, filesystem_mcp
from .prompts import GENERAL_INSTRUCTIONS
from .tools import run_command, read_output

model = LiteLlm(
    model="openai/gpt-4o",
)

root_agent = LlmAgent(
    model=model,
    name="root_agent",
    description="A senior software engineer specialized in debugging and troubleshooting software projects through terminal-based investigation.",
    static_instruction=GENERAL_INSTRUCTIONS,
    instruction="Default: Be concise and to the point.",
    tools=[
        FunctionTool(run_command, require_confirmation=True),
        read_output,
        context7_mcp,
        filesystem_mcp,
    ],
)

app = App(
    name="terminal",
    root_agent=root_agent,
    resumability_config=ResumabilityConfig(is_resumable=True),
)
