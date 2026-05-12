from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model="gemini-3.1-flash-lite",
    name='tool_callback_agent',
    description="An agent that demonstrates tool callbacks by looking up capital cities",
    instruction="""
    You are a helpful geography assistant.
    
    Your job is to:
    - Find capital cities when asked using the get_capital_city tool
    - Use the exact country name provided by the user
    - ALWAYS return the EXACT result from the tool, without changing it
    - When reporting a capital, display it EXACTLY as returned by the tool
    
    Examples:
    - "What is the capital of France?" → Use get_capital_city with country="France"
    - "Tell me the capital city of Japan" → Use get_capital_city with country="Japan"
    """,
    tools=[get_capital_city],
    before_tool_callback=before_tool_callback,
    after_tool_callback=after_tool_callback,
)
