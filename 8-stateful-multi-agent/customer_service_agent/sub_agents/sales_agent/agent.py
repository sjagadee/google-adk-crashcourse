from google.adk.agents.llm_agent import Agent

sales_agent = Agent(
    model="gemini-3.1-flash-lite",
    name='sales_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)
