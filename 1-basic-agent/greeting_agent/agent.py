from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    description="An agent that greets the user",
    model="gemini-3.1-flash-lite",
    instruction="""
    You are a helpful assistant that greets the user.
    Ask the user their name and greet them by name.
    """,    
)