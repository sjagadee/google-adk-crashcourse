import asyncio
import uuid

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions.database_session_service import DatabaseSessionService
from google.genai import types
from utils import call_agent_async
from memory_agent.agent import memory_agent

load_dotenv()

# --- SESSION MANAGEMENT INIT: Persistent Session Storage ---
# Setup SQLite database and session service to store state
database_url = "sqlite+aiosqlite:///./my_agent_data.db"
session_service = DatabaseSessionService(db_url=database_url)

# --- INITIALIZE: initial state ---
initial_state = {
    "user_name": "Srini Jagadeesh",
    "reminders": [],
}


async def main_async():
    # Setup constrains
    APP_NAME = "Memory Agent"
    USER_ID = "aiwithsrini"

    # --- SESSION MANAGEMENT: Find or Create Session ---
    # check if there is a existing session
    exisiting_session = await session_service.list_sessions(
        app_name=APP_NAME,
        user_id=USER_ID,
    )

    # if existing session found, use it, otherwise create a new session
    if exisiting_session and len(exisiting_session.sessions) > 0:
        SESSION_ID = exisiting_session.sessions[0].id
        print(f"Found existing session: {SESSION_ID}")
    else:
        new_session = await session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            state=initial_state,
        )
        SESSION_ID = new_session.id

        print(f"Created new session: {SESSION_ID}")

    # --- AGENT RUNNER SETUP ---
    # create a runner to run the memory_agent
    runner = Runner(
        session_service=session_service,
        app_name=APP_NAME,
        agent=memory_agent,
    )

    # -- INTERACTIVE AGENT RUN ---
    # run the agent in a loop
    print("\nWelcome to the Memory Agent!")
    print("Your reminders will be remembered accross sessions.")
    print("Type 'quit' or 'exit' to end the conversation.\n")

    while True:
        # get user input
        input_text = input("You: ")

        # if user inputs 'quit' or 'exit', end the conversation
        if input_text.lower() in ["quit", "exit"]:
            print("Goodbye! Your reminders will be remembered accross sessions.")
            break

        # run the agent
        await call_agent_async(runner, USER_ID, SESSION_ID, input_text)


if __name__ == "__main__":
    asyncio.run(main_async())
