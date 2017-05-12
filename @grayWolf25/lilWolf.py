import discord
from discord.ext.commands import Bot
import asyncio

def versionInfo():
    info = ""
    info += "**wolfBot 0.0.1 (Alpha)**\n"
    info += "Author: Discord User @the_gray\n"
    info += "For help, send ```\">>help\"```\n\n"

    return info

client = discord.Client(description="Test bot for the project!", command_prefix='>>')
global LIL_WOLF_STATUS
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    Prog_Proj1 = discord.utils.find(lambda c: c.name == 'Programming Project 1', client.get_all_channels())
    print('---------')
@client.event
async def on_message(message):

    if(message.content == ">>Info"):
        await client.send_message(message.channel, versionInfo())
    if message.content.startswith('!howl'):
        await client.send_message(message.channel, 'AWOOOOOO')
    if message.content.startswith('!close'):
        await client.close()

if __name__=="__main__":
    client.run('MzEyNDUwNDY4Njc4NzI5NzM5.C_bvcw.wWl0hNlkVBADqu3se_9YP3u7e3o')

    client.accept_invite('https://discord.gg/ZCFjeCF')

    client.close()


