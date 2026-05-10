from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from datetime import datetime


def get_current_time() -> dict:
    """
    Returns the current time in the format "YYYY-MM-DD HH:MM:SS".
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    

root_agent = Agent(
    model="gemini-3.1-flash-lite",
    name='tool_agent',
    description='Tool Agent',
    instruction="""
    You are a helpful assistant that can use following tools:
    - google_search
    """,
    tools=[google_search], # when using built-in tools, pass them directly to the agent, but one agent can have one built-in tool
    # tools=[get_current_time],
    # tools=[google_search, get_current_time], # wont work
)
