from google.adk.agents.llm_agent import LlmAgent
from pydantic import BaseModel, Field


# Output schema definition using pydantic
class EmailContent(BaseModel):
    subject: str = Field(..., description="The subject of the email, should be consise and descriptive.")
    body: str = Field(..., description="The body of the email, should be on point and with well-structured and formatted text with greetings, paragraphs, and signature.")


root_agent = LlmAgent(
    model="gemini-3.1-flash-lite",
    name='email_agent',
    description='Generate a professional email with a subject and body.',
    instruction="""
        You are an Email Generation Assistant.
        Your task is to generate a professional email based on the user's request.
        
        GUIDELINES:
            - Create an appropriate subject line (concise and relevant)
            - Write a well-structured email body with:
                * Professional greeting
                * Clear and concise main content
                * Appropriate closing
                * Your name as signature
            - Suggest relevant attachments if applicable (empty list if none needed)
            - Email tone should match the purpose (formal for business, friendly for colleagues)
            - Keep emails concise but complete
            
        IMPORTANT: Your response MUST be valid JSON matching this structure:
        {
            "subject": "Subject line here",
            "body": "Email body here with proper paragraphs and formatting",
        }
        
        DO NOT include any explanations or additional text outside the JSON response.
    """,
    output_schema=EmailContent,
    output_key='email'
)
