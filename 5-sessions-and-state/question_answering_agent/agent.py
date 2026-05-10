from google.adk.agents.llm_agent import Agent

question_answering_agent = Agent(
    model="gemini-3.1-flash-lite",
    name='question_answering_agent',
    description='Question Answering Agent.',
    instruction="""
        You are a helpful assistant that answers user's questions based on the user's preferences.
        
        Here some information about the user:
        - Name: {user_name}
        - Preferences: {user_preferences}
        
        You can use this information to answer user's questions.
    """
)
