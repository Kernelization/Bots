import discord
import random
from discord.ext.commands import Bot
import asyncio

global LOG
global LOGFILE
global SETSTATUS
def versionInfo():
    info = ""
    info += "**wolfBot 0.0.1 (Alpha)**\n"
    info += "Author: Discord User @the_gray\n"
    info += "For help, send ```\">>help\"```\n\n"

    return info

def commands():
    ret = discord.Embed()
    ret.add_field(name='wolfBot Commands',value='COMMAND\nSYNTAX   DESCRIPTION',inline=False)
    ret.add_field(name='Info',value='>>Info   Displays info about the wolfBot',inline=False)
    ret.add_field(name='Commands',value='>>Commands or >>Help  Displays this text info',inline=False)
    ret.add_field(name='Howl',value='>>howl   Howls at you',inline=False)
    ret.add_field(name='Stats',value='>>stats   Displays some basic stats about the server',inline=False)
    ret.add_field(name='Log Status',value='>>log status   Displays the status of the logging software',inline=False)
    ret.add_field(name='Log On/Off',value='>>log ON / >>log OFF   Turns the logging on and off',inline=False)
    ret.add_field(name='User History',value='userHistory-<displayName>   Shows the last timestamp of the last message sent by the user',inline=False)
    ret.add_field(name='Rekt',value='>>rekt   self.getRekt()',inline=False)
    ret.add_field(name='Rekt add',value='>>rekt <url-to-image>   Adds image from url to the rekt database',inline=False)

    ret.set_footer(text='WOOF WOOF --@the_gray')

    return ret
def stats():
    channels = 0
    members = 0
    ret = ""
    for channel in client.get_all_channels():
        channels += 1
    for member in client.get_all_members():
        members += 1


    ret+="Number of channels: "+str(channels)+"\n"
    ret+="Number of members: "+str(members)+"\n"
    return ret

def userHistory(username=""):
    tempLOGFILE = open('./resources/log.txt', 'r')
    lines = tempLOGFILE.readlines()
    br = False
    user = discord.utils.find(lambda m: m.display_name.startswith(username), client.get_all_members())
    ret = ""
    for line in lines:
        if not br:
            linesplit = line.split('\t')
            ID = linesplit[0]
            try:
                if (ID.startswith(user.id)):
                    br = True
                    ret += "HISTORY of " + user.display_name + '\n'
                    ret+= 'Last message: ' + linesplit[1] + '\n'
            except(TypeError,AttributeError):
                ret = "ERROR: User not found!"
    tempLOGFILE.close()
    return ret
client = discord.Client(description="Test bot for the project!", command_prefix='>>')

@client.event
async def on_ready():
    global SETSTATUS
    global LOG
    global LOGFILE
    LOG = False
    SETSTATUS = False
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('---------')


@client.event
async def on_message(message):
    global LOG
    global LOGFILE
    global SETSTATUS
    if(not SETSTATUS):
        game = discord.Game()
        game.name = '>>Commands for help'
        game.url = '>>Commands for help'
        status = discord.Status.online

        await client.change_presence(game=game, status=status, afk=False)
        SETSTATUS = True
    if(message.content == ">>Info"):
        await client.send_message(message.channel, versionInfo())
    if(message.content == ">>Commands") or (message.content == ">>Help"):
        await client.send_message(message.channel,embed=commands())
    if message.content.startswith('>>howl'):
        await client.send_message(message.channel, message.author.mention+' AWOOOOOO')

    if message.content.startswith('>>stats'):
        await client.send_message(message.channel,stats())
    if message.content.startswith("good boy") or message.content.startswith("good boi") or message.content.startswith('>>good boy') or message.content.startswith('>>good boi'):
        await client.send_message(message.channel, "*pants*\n WOOF\n *licks "+message.author.mention+"'s face*")
    if message.content.startswith('>>log'):
        spl = message.content.split(' ')
        onOff = spl[1]
        if(onOff.startswith("ON")):
            LOG = True
            await client.send_message(message.channel, "Logging is on")
        elif(onOff.startswith("OFF")):
            LOG = False
            await client.send_message(message.channel, "Logging is off")
        if(onOff.startswith("status")):
            if(LOG == True):
                await client.send_message(message.channel, "Logging is on")
            else:
                await client.send_message(message.channel, "Logging is off")
    if message.content.startswith('>>userHistory'):
        spl = message.content.split("-")
        if len(spl) == 1:
            await client.send_message(message.channel, "No User!\nUsage: ```>>userHistory-<displayName>```\n")
        elif len(spl) == 2:
            await client.send_message(message.channel, userHistory(spl[1]))
    if message.content.startswith('>>rekt'):
        spl = message.content.split(" ")
        if(len(spl) == 1):
            rektFile = open('./resources/rekt.txt', 'r')
            rektLines = rektFile.readlines()

            rektArr = []
            for line in rektLines:
                print("TEST\n")
                rektArr.append(line)
            rektRand = random.randint(0,len(rektArr)-1)
            await client.send_message(message.channel, rektArr[rektRand])
        else:
            rektFile = open('./resources/rekt.txt','a+')
            rektFile.write(spl[1]+'\n')
        rektFile.close()



    if(LOG):
        LOGFILE = open('./resources/log.txt', 'a+')
        LOGFILE.truncate()
        LOGFILE.write(message.author.id+'\t'+str(message.timestamp)+'\t'+message.content+'\n')
        LOGFILE.close()
        print(message.channel.name+'\t'+message.author.name+'\t'+str(message.timestamp)+'\t'+message.content)
if __name__=="__main__":
    client.run('MzEyNDUwNDY4Njc4NzI5NzM5.C_bvcw.wWl0hNlkVBADqu3se_9YP3u7e3o')

    client.accept_invite('https://discord.gg/ZCFjeCF')

    client.close()


