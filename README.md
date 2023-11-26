# discord_bots

To run a bot, follow the instructions in the discord developer portal (https://discord.com/developers/applications) to make a bot. Get the bot token and the channel id you want to use the bot in, and make the appropriate json file. Then, run "python3 [bot.py]" where bot.py is the python file with the discord bot.

For all json files, you can get channel_id and bot_token from the discord API.

Spotify Bot: (spotbot.py)

Notifies if a spotify artist has released a new song/album.

spot.json has the structure 
{
  {keys: {channel_id, bot_token}},
  {spotify: {client_id, client_secret, artist_url}}
}

You can use the spotify API to get client_id and client_secret and the url of an artist's profile to get artist_url.

Class Bot: (classbot.py)

Notifies if a class is open at the 5Cs (using hyperschedule.io). Checks every minute, sending many messages when class is open, and every 15 minutes, sends a message notifying that the bot is still running.

class.json has the structure
{
  {keys: {channel_id, bot_token}},
  {indices: {class_index}},
  name,
  class_size
}

The name of the class is "name," the max class size is "class_size," and the index of the class in hyperschedule is "class_index."

