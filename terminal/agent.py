from google.adk.agents.llm_agent import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from .prompts import GENERAL_INSTRUCTIONS
from .tools import run_command, read_output
from .mcp import context7_mcp, filesystem_mcp

model = LiteLlm(
    model='openai/gpt-4o',
)

root_agent = LlmAgent(
    model=model,
    name='root_agent',
    description='A senior software engineer specialized in debugging and troubleshooting software projects through terminal-based investigation.',
    static_instruction=GENERAL_INSTRUCTIONS,
    instruction="Default: Be concise and to the point.",
    tools=[run_command, read_output, context7_mcp, filesystem_mcp],
)

