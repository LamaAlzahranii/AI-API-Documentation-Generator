from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

system_prompt = """
You are a Senior .NET API Documentation Expert.

Analyze the provided ASP.NET Core Controller and generate a clean, professional API documentation document in Markdown.

Requirements:
- Use professional headings.
- Use Markdown tables whenever appropriate.
- Explain the endpoint clearly.
- Generate realistic request and response examples.
- Do not mention assumptions.
- Format the document so it is ready to publish.

Sections:

# API Documentation

## API Name

## Overview

## Endpoint

| Property | Value |

## Request Parameters

## Request Body

## Response Codes

| Status | Description |

## Authentication

## Sample Request

## Sample Response

## Notes
"""

controller = """
[ApiController]
[Route("api/employees")]
public class EmployeesController : ControllerBase
{
    [HttpPost]
    public async Task<IActionResult> Create(CreateEmployeeDto dto)
    {
        return Ok();
    }
}
"""

response = client.chat.completions.create(
    model="llama3.2",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": controller}
    ]
)

documentation = response.choices[0].message.content

import os

# Create output folder if it doesn't exist
os.makedirs("output", exist_ok=True)

# Save the documentation
file_path = "output/API_Documentation.md"

with open(file_path, "w", encoding="utf-8") as file:
    file.write(documentation)

print(f"✅ API documentation saved successfully!")
print(f"📄 File location: {file_path}")