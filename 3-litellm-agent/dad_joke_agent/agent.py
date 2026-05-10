import random

from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from dotenv import load_dotenv

load_dotenv()

model = LiteLlm(
    model="openrouter/x-ai/grok-4.3"
)


def dad_joke_tool():
    dad_jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a bear with no teeth? A gummy bear!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised."
    ]
    
    return random.choice(dad_jokes)


root_agent = Agent(
    model=model,
    name='dad_joke_agent',
    description='Dad Joke Agent.',
    instruction='A helpful assistant that tells dad jokes, using a tool called dad_joke_tool.',
    tools=[dad_joke_tool]
)
