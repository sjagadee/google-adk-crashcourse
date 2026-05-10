import asyncio
import uuid

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from question_answering_agent import question_answering_agent

load_dotenv()

# Create a session service to store state
session_service_stateful = InMemorySessionService()

initial_state = {
    "user_name": "Srini Jagadeesh",
    "user_preferences": """
        I like to eat pizza and watch movies.
        I like to play video games and listen to music.
        I am a stock market enthusiast, I look for different types of strategies.
    """
}

# Create a new session
APP_NAME = "Srini bot"
USER_ID = "srinivas_jagadeesh"
SESSION_ID = str(uuid.uuid4())

stateful_session = asyncio.run(session_service_stateful.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state,
))
print(f"New Session Created")
print(f"Session ID: {SESSION_ID}")

runner = Runner(
    agent=question_answering_agent,
    app_name=APP_NAME,
    session_service=session_service_stateful
)

# create a new message
new_message = types.Content(
    role="user",
    parts=[types.Part(text="What does Srinivas's likes to do ?")]
)

for event in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_message
):
    if event.is_final_response():
        if event.content and event.content.parts:
            print(f"Final response: {event.content.parts[0].text}")
            
print("---Session Event Exploration---")
session = asyncio.run(session_service_stateful.get_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID
))

# log final session state
print("---Final Session State---")
for key, value in session.state.items():
    print(f"{key}: {value}")