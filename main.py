import asyncio
from agno.agent import Agent
from agno.models.openai import OpenAIChat

from cognee import prune
from tools import CogneeTools
from constants import MY_PREFERENCE, INSTRUCTIONS

from dotenv import load_dotenv
load_dotenv()

async def main():
    """
    Integrate your OpenAI LLM Agent with Memory tools to add and fetch from memory
    """
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
    await agent.aprint_response("plan 3 days Itinerary for Rome", stream=True)
    
if __name__ == "__main__":
    asyncio.run(main())

