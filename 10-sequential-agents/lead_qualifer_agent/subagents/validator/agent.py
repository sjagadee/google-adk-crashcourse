from google.adk.agents.llm_agent import LlmAgent

"""
Lead Validator Agent

This agent is responsible for validating if a lead has all the necessary information
for qualification.
"""

# --- Constants ---
GEMINI_MODEL = "gemini-3.1-flash-lite"

# Create the validator agent
lead_validator_agent = LlmAgent(
    name="LeadValidatorAgent",
    model=GEMINI_MODEL,
    instruction="""You are a Lead Validation AI.
    
    Examine the lead information provided by the user and determine if it's complete enough for qualification.
    A complete lead should include:
    - Contact information (name, email or phone)
    - Some indication of interest or need
    - Company or context information if applicable
    
    Output ONLY 'valid' or 'invalid' with a single reason if invalid.
    
    Example valid output: 'valid'
    Example invalid output: 'invalid: missing contact information'
    """,
    description="Validates lead information for completeness.",
    output_key="validation_status",
)