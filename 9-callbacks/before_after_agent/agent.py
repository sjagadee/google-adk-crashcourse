from datetime import datetime
from typing import Optional

from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.callback_context import CallbackContext
from google.genai import types

"""
Before and After Agent Callback example

This example demonstrates how to use the before_agent_callback and after_agent_callback for logging purposes.
"""


def before_agent_callback(callback_context: CallbackContext) -> Optional[types.Content]:
    """
    Simple callback that logs when the agent starts processing a request.
    
    Args:
        callback_context (CallbackContext): The context of the callback.
    
    Returns:
        Optional[types.Content]: None to continue processing.
    """
    print("Before Agent Callback Called!")
    
    # Get the session state
    state = callback_context.state
    
    # Record timestamp
    timestamp = datetime.now()
    
    # Set agent name if not present
    if "agent_name" not in state:
        state["agent_name"] = "Simple Chat Agent"
        
    # Initialize request counter
    if "request_counter" not in state:
        state["request_counter"] = 0
        
    # Increment request counter
    state["request_counter"] += 1
    
    # To Calculate the time taken to execute the agent
    state["request_start_time"] = timestamp.isoformat()
    
    # Log the request
    print("--- AGENT EXECUTION STARTED ---")
    print(f"Request Number: {state['request_counter']}")
    print(f"Agent Name: {state['agent_name']}")
    print(f"Request Timestamp: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Print to console
    print(f"[BEFORE CALLBACK] Agent processing request number: {state["request_counter"]}")
    
    return None
    
    
def after_agent_callback(callback_context: CallbackContext) -> Optional[types.Content]:
    """
    Simple callback that logs when the agent completes processing a request.
    
    Args:
        callback_context (CallbackContext): The context of the callback.
    
    Returns:
        Optional[types.Content]: None to continue processing.
    """
    print("After Agent Callback Called!")
    
    # Get the session state
    state = callback_context.state
    
    # Record timestamp to calculate time taken
    timestamp = datetime.now()
    duration = None
    if "request_start_time" in state:
        duration = (timestamp - datetime.fromisoformat(state["request_start_time"])).total_seconds()
        
    # Log the request
    # Log the completion
    print("=== AGENT EXECUTION COMPLETED ===")
    print(f"Request #: {state.get('request_counter', 'Unknown')}")
    print(f"Agent Name: {state.get('agent_name', 'Unknown')}")
    if duration is not None:
        print(f"Duration: {duration:.2f} seconds")

    # Print to console
    print(
        f"[AFTER CALLBACK] Agent completed request #{state.get('request_counter', 'Unknown')}"
    )
    if duration is not None:
        print(f"[AFTER CALLBACK] Processing took {duration:.2f} seconds")

    return None
    
    
root_agent = LlmAgent(
    model="gemini-3.1-flash-lite",
    name='root_agent',
    description='A basic agent to demonstrate before and after agent callbacks.',
    instruction="""
    You are a friendly greetings assistant, your name is {agent_name}.
    
    Your job is to:
    - Greet the user politely
    - Respond to user's basic questions
    - Keep the responses friendly and concise
    """,
    before_agent_callback=before_agent_callback,
    after_agent_callback=after_agent_callback
)
