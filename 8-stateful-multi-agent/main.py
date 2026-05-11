import asyncio

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from customer_service_agent.agent import customer_service_agent
from utils import call_agent_async, add_user_query_to_history

load_dotenv()

# --- SESSION MANAGEMENT INIT: In-Memory Session Service ---
session_service = InMemorySessionService()

# --- INITIALIZE: initial state ---
initial_state = {
    "user_name": "Srini Jagadeesh",
    "purchased_courses": [],
    "interaction_history": [],
}


async def main_async():
    # Setup constrains
    APP_NAME = "Customer Service Agent"
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
        agent=customer_service_agent,
    )

    # --- INTERACTIVE AGENT RUN ---
    # run the agent in a loop
    print("\nWelcome to the Customer Service Agent!")
    print(
        "Your Customer Service Agent is ready to help you in your journey with our courses."
    )
    print("Type 'quit' or 'exit' to end the conversation.\n")

    while True:
        user_query = input("User: ")

        # check if the user wants to end the conversation
        if user_query.lower() in ["quit", "exit"]:
            print("Goodbye! Your conversation has ended.")
            break
        
        # Update interaction history with the user's query
        add_user_query_to_history(
            session_service, APP_NAME, USER_ID, SESSION_ID, user_query
        )

        # run the agent
        await call_agent_async(runner, USER_ID, SESSION_ID, user_query)

    # --- State Examination ---
    # Show final session state
    final_session = session_service.get_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )
    print("\nFinal Session State:")
    for key, value in final_session.state.items():
        print(f"{key}: {value}")


def main():
    """Entry point for the application."""
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
