import anthropic
import os

client = anthropic.Anthropic(
    api_key=os.environ.get('ANTHROPIC_API_KEY'),
)


async def get_context():
    with open('../character.txt', 'r') as file:
        context = file.read()
    file.close()
    return context


async def get_response(prompt):

    context = await get_context()
    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0.8,
        system=context,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text
