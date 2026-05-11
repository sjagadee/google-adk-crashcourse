from google.adk.agents.llm_agent import Agent

policy_agent = Agent(
    model="gemini-3.1-flash-lite",
    name='policy_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)
