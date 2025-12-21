import asyncio
from agno.agent import Agent
from agno.models.openai import OpenAIChat

from cognee import prune
from tools import CogneeTools
from utils import get_db_config
from constants import INSTRUCTIONS, MY_PREFERENCE

from dotenv import load_dotenv
load_dotenv()

async def main():
    """
    Integrate your OpenAI LLM Agent with Memory tools to add and fetch from memory
    """
    await get_db_config()
    
    await prune.prune_data()
    await prune.prune_system(metadata=True)

    cognee_tools = CogneeTools()
    llm = OpenAIChat(id="gpt-5-mini")

    agent = Agent(
        model=llm,
        tools=[cognee_tools],
        instructions=INSTRUCTIONS
    )

    await agent.aprint_response(f"Remember: {MY_PREFERENCE}", stream=True)
    print("\n")
    await agent.aprint_response("who is Tarun and does he watch Formula 1?", stream=True)
    
if __name__ == "__main__":
    asyncio.run(main())