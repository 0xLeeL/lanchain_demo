import asyncio

from agents import Agent, Runner, function_tool, set_trace_processors
from langsmith.wrappers import OpenAIAgentsTracingProcessor


@function_tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


async def main():
    agent = Agent(
        name="Weather Agent",
        instructions="You are a helpful assistant.",
        tools=[get_weather],
    )

    question = "What is the weather in San Francisco?"
    result = await Runner.run(agent, question)
    print(result.final_output)


if __name__ == "__main__":
    set_trace_processors([OpenAIAgentsTracingProcessor()])
    asyncio.run(main())