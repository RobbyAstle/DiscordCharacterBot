import discord
import os
import character_behavior


API_KEY = os.environ.get('DISCORD_API_KEY')

# Initialize the bot
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)


message_read_limit = 2


def main():
    client.run(API_KEY)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


@client.event
async def on_message(message):
    if client.user.mentioned_in(message) and not message.author.bot:
        ai_prompt = f'{message.author}: {message.content}'
        ai_response = await character_behavior.get_response(ai_prompt)
        await message.channel.send(ai_response)


def fetch_last_messages(channel, limit):
    messages = []
    message_content = channel.history(before=True, limit=limit)
    for message in message_content:
        messages.append(message)
    return messages


if __name__ == '__main__':
    main()
