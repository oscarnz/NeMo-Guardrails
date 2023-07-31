from nemoguardrails import LLMRails, RailsConfig
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/nemo",
    tags=["Nemo"],
)

COLANG_CONFIG = """
define user express greeting
  "hi"

define user express insult
  "You are stupid"

# Basic guardrail against insults.
define flow
  user express insult
  bot express calmly willingness to help

"""

YAML_CONFIG = """
models:
  - type: main
    engine: openai
    model: text-davinci-003
"""


# Give the path to the folder containing the rails
config = RailsConfig.from_path("./nemo/config")
rails = LLMRails(
    config,
    verbose=True)

memory = []

@router.post("/chat")
async def chat(
    input: str
):
    
    # Define role and question to be asked
    history = {
        "role": "user",
        "content": input
    }
    memory.append(history)
    
    response = await rails.generate_async(messages=memory)

    memory.append(response)

    return response


@router.post("/chat-stateless")
async def chat_without_file(
    input: str
):
    config_stateless = RailsConfig.from_content(COLANG_CONFIG, YAML_CONFIG)
    app_stateless = LLMRails(config_stateless)
    
    # Define role and question to be asked
    history = {
        "role": "user",
        "content": input
    }
    memory.append(history)
    
    response = await app_stateless.generate_async(messages=memory)

    memory.append(response)

    return response