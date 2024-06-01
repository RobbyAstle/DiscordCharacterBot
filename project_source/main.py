import discord
import os

# Initialize the bot
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if client.user.mentioned_in(message) and not message.author.bot:
        print(f'Message from {message.author}: {message.content}')

# Run the bot
# Make sure to replace 'YOUR_BOT_TOKEN' with your actual bot token
client.run('YOUR_BOT_TOKEN')
