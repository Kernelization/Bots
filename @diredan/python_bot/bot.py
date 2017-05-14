# our imports
import discord
import configparser
import importlib
# initializing client
client = discord.Client()
# getting our config file, and reading it
config = configparser.ConfigParser()
config.read('config.ini')
# setting our globals from config file
PREFIX = config["Settings"]["prefix"]
OWNER = config["Settings"]["owner"]  # unused but will be needed


# ran when the bot successfully logs in :D
@client.event
async def on_ready():
    print('Logged in as', client.user.name)


# ran every time a message is received
@client.event
async def on_message(message):
    # if message starts with prefix and author is not a bot ( to prevent spam )
    if message.content.startswith(PREFIX) and not message.author.bot:
        # parsing the message to get arguments and the command
        command = message.content.split(" ")[0][len(PREFIX):]
        arguments = message.content.split(" ")[1:]
        # a really awkward way of loading a our command files
        try:
            await importlib.import_module("commands." + command).run(message, client, arguments)
        except ImportError:
            await client.send_message(message.channel, "```That isn't a command!```")
        except discord.Forbidden:
            print("[Error] Forbidden error!")
# logging into our bot
client.run(config["Auth"]["token"])
