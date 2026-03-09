from google.adk.agents.llm_agent import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from .prompts import GENERAL_INSTRUCTIONS

model = LiteLlm(
    model='openai/gpt-4o',
) 

root_agent = LlmAgent(
    model=model,
    name='root_agent',
    description='A helpful assistant for terminal command outputs.',
    static_instruction=GENERAL_INSTRUCTIONS,
    instruction="Default: Be concise and to the point.",
)

