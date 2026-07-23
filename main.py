import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_prompt = """
You are a Senior .NET API Documentation Expert.

Analyze the provided ASP.NET Core Controller and generate professional API documentation in Markdown.

Include:
- API Name
- Overview
- Endpoint
- Request Parameters
- Request Body
- Response Codes
- Authentication
- Sample Request
- Sample Response
- Notes

Use headings and markdown tables.
"""

def generate_documentation(controller):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": controller}
        ]
    )

    return response.choices[0].message.content


controller = """
ضع هنا أي Controller من .NET
"""

print(generate_documentation(controller))