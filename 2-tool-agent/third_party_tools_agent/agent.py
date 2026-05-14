from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.crewai_tool import CrewaiTool
from crewai_tools import SerperDevTool
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

serper_crewai_tool = SerperDevTool(
    country='us',
    locale='en-US',
    location='Dallas, TX',
    n_results=10
)

adk_crewai_tool = CrewaiTool(
    tool=serper_crewai_tool,
    name='InternetNewsSearch',
    description='Useful for when you need to answer questions about current events or news articles and other general information.',
)


def get_current_time():
    """
    Returns the current time in the format "YYYY-MM-DD HH:MM:SS".
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


root_agent = LlmAgent(
    model="gemini-3.1-flash-lite",
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge, make sure to use tools when appropriate.',
    tools=[get_current_time, adk_crewai_tool]
)
