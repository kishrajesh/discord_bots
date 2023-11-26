import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import discord
from discord.ext import commands, tasks
import requests
import asyncio
import json

f = open('spot.json')
spot_data = json.load(f)
f.close()

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

@tasks.loop(minutes=1)  # Set the loop to run every hour
async def check_api():
    # Make the API call
    client_id = spot_data['spotify']['client_id']
    client_secret = spot_data['spotify']['client_secret']
    # Set up Spotify API credentials
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    artist_id = spot_data['spotify']['artist_url']
    # Get the total number of tracks by the artist
    # Get the artist's albums
    albums = sp.artist_albums(artist_id, album_type='album,single', limit=50)  # Adjust limit as needed

    total_tracks = 0

    # Sum the number of tracks across all albums
    for album in albums['items']:
        album_info = sp.album(album['id'])
        total_tracks += album_info['total_tracks']


    #print(f"The artist has {total_tracks} songs on Spotify.")
    CHANNEL_ID = spot_data['keys']['channel_id']
    channel = bot.get_channel(CHANNEL_ID)
    if(total_tracks > 0):
        #print("hype")
        if channel:
            await channel.send('@everyone Wolyme is up!')
        else:
            print(f"Error: Channel with ID {CHANNEL_ID} not found")
    else:
        if channel:
            await channel.send('Wolyme is still down :(')
        else:
            print(f"Error: Channel with ID {CHANNEL_ID} not found")
        

# Run the bot with the token you obtained from the Discord Developer Portal
discord_token = spot_data['keys']['bot_token']
bot.run(discord_token)