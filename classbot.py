import discord
from discord.ext import commands, tasks
import requests
import asyncio
import json
import datetime

f = open('class.json')
class_data = json.load(f)
f.close()

name = class_data['name']
size = class_data['size']

# Create an instance of Intents
intents = discord.Intents.default()
intents.members = True  # Enable member-related events

# Create a bot instance with a command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    # Start the background task to check the API every hour
    check_api.start()

@tasks.loop(minutes=15)  # Set the loop to run every hour
async def check_api():
    # Make the API call

    data = requests.get("https://banana.hyperschedule.io/v4/sections").json()
    classIndex = class_data['indices']['class_index']
    # Filter sections for the class name
    class_sections = data[classIndex]
    seatFill = class_sections['seatsFilled']
    CHANNEL_ID = class_data['keys']['channel_id']
    channel = bot.get_channel(CHANNEL_ID)
    if(seatFill < size):
        message = "@everyone" + name+ ' is open!'
        if channel:
            await channel.send(message)
            await channel.send(message)
            await channel.send(message)
            await channel.send(message)
            await channel.send(message)
            await channel.send(message)
            await channel.send(message)
            await channel.send(message)
            await channel.send(message)
        else:
            print(f"Error: Channel with ID {CHANNEL_ID} not found")
    else:
        current_time = datetime.datetime.now().time()
        if current_time.minute % 15 == 0:
            if channel:
                await channel.send(name + ' is still closed :(, but bot is still working :)')
            else:
                print(f"Error: Channel with ID {CHANNEL_ID} not found")
        

# Run the bot with the token you obtained from the Discord Developer Portal
discord_token = class_data['keys']['bot_token']
bot.run(discord_token)
