from nemoguardrails import LLMRails, RailsConfig
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/nemo",
    tags=["Nemo"],
)

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