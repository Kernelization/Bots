import discord
from discord.ext.commands import Bot
import asyncio

STATUS = 'Hunting...'
NAME = 'lilWolf'

client = discord.Client(description="Test bot for the project!", command_prefix='>>')

client.accept_invite('https://discord.gg/ZCFjeCF')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('---------')
    client.send_message('programming_project_1','lilWolf is here bitches!')
    print('Made our greeting')
@client.event
async def on_message(message):
    if message.content.startswith('!howl'):
        await client.send_message(message.channel, 'AWOOOOOO')
    if message.content.startswith(''):
    if message.content.startswith('!close'):
        await client.close()


if __name__=="__main__":
    client.run('MzEyNDUwNDY4Njc4NzI5NzM5.C_bg5w.ZG4GVKj4HH5fyHuICKF1n7q_8dE')

    client.close()


