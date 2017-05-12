import discord
from discord.ext.commands import Bot
import asyncio


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
    global LIL_WOLF_STATUS
    if message.content.startswith('>>howl'):
        await client.send_message(message.channel, 'AWOOOOOO')
    if message.content.startswith('>>close'):
        await client.close()
    if message.content.startswith('>>Status'):
        spl = message.content.split(' ')
        if len(spl) > 1:
            newStatus = spl[2]
            for word in range(3,len(spl)):
                newStatus+=spl[word]+' '
            await client.send_message(message.channel, newStatus)
            LIL_WOLF_STATUS = newStatus
        else:

            if 'LIL_WOLF_STATUS' not in locals():
                await client.send_message(message.channel, "No status as of yet")
            else:
                await client.send_message(message.channel, LIL_WOLF_STATUS)
    else:
        pass


if __name__=="__main__":
    client.run('MzEyNDUwNDY4Njc4NzI5NzM5.C_bvcw.wWl0hNlkVBADqu3se_9YP3u7e3o')

    client.accept_invite('https://discord.gg/ZCFjeCF')

    client.close()


