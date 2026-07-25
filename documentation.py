from prompts import documentation_system_prompt
def generate_documentation(client, context):

    stream = client.chat.completions.create(
        model="llama3.2",
        messages=[
            {
             "role":"system",
             "content":documentation_system_prompt
            },
            {
             "role":"user",
             "content":context
            }
        ],
        stream=True
    )


    documentation = ""

    for chunk in stream:

        text = chunk.choices[0].delta.content or ""

        print(text, end="", flush=True)

        documentation += text


    return documentation