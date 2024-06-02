import anthropic
import os

client = anthropic.Anthropic(
    api_key=os.environ.get('ANTHROPIC_API_KEY'),
)


async def get_context():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the file
    file_path = os.path.join(script_dir, '..', 'character.txt')

    # Print the constructed file path for debugging
    print("File path:", file_path)
    try:
        with open(file_path, 'r') as file:
            context = file.read()
        file.close()
        return context
    except FileNotFoundError:
        print("File not found")


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
