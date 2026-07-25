import json
from prompts import analysis_system_prompt


def analyze_controller(client, controller):

    response = client.chat.completions.create(
        model="llama3.2",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": analysis_system_prompt
            },
            {
                "role": "user",
                "content": controller
            }
        ]
    )

    result = response.choices[0].message.content

    # print("===== LLM RESPONSE =====")
    # print(result)
    # print("========================")

    return json.loads(result)