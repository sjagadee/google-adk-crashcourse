from google.adk.agents.llm_agent import LlmAgent

"""
System Report Synthesizer Agent

This agent is responsible for synthesizing information from other agents
to create a comprehensive system health report.
"""

GEMINI_MODEL = "gemini-3.1-flash-lite"


# System Report Synthesizer Agent
synthesizer_agent = LlmAgent(
    name="synthesizer_agent",
    model=GEMINI_MODEL,
    instruction="""You are a System Report Synthesizer.
    
    Your task is to create a comprehensive system health report by combining information from:
    - CPU information: {cpu_info}
    - Memory information: {memory_info}
    - Disk information: {disk_info}
    
    Create a well-formatted report with:
    1. An executive summary at the top with overall system health status
    2. Sections for each component with their respective information
    3. Recommendations based on any concerning metrics
    
    Use markdown formatting to make the report readable and professional.
    Highlight any concerning values and provide practical recommendations.
    """,
    description="Synthesizes all system information into a comprehensive report",
)