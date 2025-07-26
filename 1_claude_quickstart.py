import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-3-5-haiku-20241022",
    max_tokens=8192,
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Whats the weather in Tokyo?"
                }
            ]
        }
    ],
)
print(message.content)