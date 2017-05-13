import discord
import random
from discord.ext.commands import Bot
import asyncio

global LOG
global LOGFILE
global SETSTATUS

def versionInfo():
    info = ""
    info += "**wolfBot 0.1.0 (Alpha2)**\n"
    info += "Author: Discord User @the_gray\n"
    info += "For help, send ```\">>help\"```\n\n"

    return info

def commands():
    ret = discord.Embed()

    ret.add_field(name='Info',value='>>Info',inline=True)
    ret.add_field(name='Commands',value='>>Commands or >>Help',inline=True)
    ret.add_field(name='Howl',value='>>howl',inline=True)
    ret.add_field(name='Stats',value='>>stats',inline=True)
    ret.add_field(name='Log Status',value='>>log status',inline=True)
    ret.add_field(name='Log On/Off',value='>>log ON / >>log OFF',inline=True)
    ret.add_field(name='User History',value='userHistory-<displayName>',inline=True)
    ret.add_field(name='Rekt',value='>>rekt',inline=True)
    ret.add_field(name='Rekt add',value='>>rekt <url-to-image>',inline=True)

    ret.set_footer(text='WOOF WOOF --@the_gray')

    return ret
def stats():
    channels = 0
    members = 0
    bots = 0
    ret = ""
    for channel in client.get_all_channels():
        channels += 1
    for member in client.get_all_members():
        roles = discord.utils.find(lambda r : r.name == 'Bots',member.roles)
        if(roles != None):
            bots+=1
        members += 1


    ret+="Number of channels: "+str(channels)+"\n"
    ret+="Number of members: "+str(members)+"\n"
    ret+="Number of bots: "+str(bots)+"\n"
    return ret

def gif(spl=[]):
    if(len(spl)<=1 or len(spl)>3):
        return 'ERROR: Usage >>gif <command> or >>gif <command-to-add> <url-to-gif>'
    elif(len(spl)==2):
        #The command should be in the file
        f = open('./resources/gifs.txt','r')
        line=f.readline()
        found = False
        while(line not in ['\n','\r\n','END']):
            if(line.startswith(spl[1])):
                found = True
                print('Found!')
                break
            else:
                print('Still not found')
                print(line)
                line = f.readline()
        if(not found):
            f.close()
            return ('Gif command not found')
        else:
            foundsplit = line.split(" ")
            rand = random.randint(1,len(foundsplit)-1)
            return foundsplit[rand]
    elif(len(spl) == 3):
        print('[1] Adding new command!')
        #adding in a new command or adding a new link to an existing one
        f = open('./resources/gifs.txt', 'r')
        lines = f.readlines()
        f.close()
        f = open('./resources/gifs.txt', 'w')
        found = False
        for l in lines:
            if(l.startswith('END')):
                f.write(spl[1]+' '+spl[2]+' \n')
                f.write('END')
                f.close()
                return 'Command added!'
            elif(l.startswith(spl[1])):
                f.write(l.rstrip()+spl[2]+' \n')
                f.write('END')
                f.close()
                return 'Link added to >>'+spl[1]+' command!'
            else:
                f.write(l)
        return 'Key added!\n'






def userHistory(username=""):
    tempLOGFILE = open('./resources/log.txt', 'r')
    lines = tempLOGFILE.readlines()
    br = False
    user = discord.utils.find(lambda m: m.display_name.startswith(username), client.get_all_members())
    ret = ""
    print(user.id)
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
    LOG = True
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
        game.name = '>>Help for help'
        game.url = '>>Help for help'
        status = discord.Status.online

        await client.change_presence(game=game, status=status, afk=False)
        SETSTATUS = True
    if(message.content.lower() == ">>info"):
        await client.send_message(message.channel, versionInfo())
    if(message.content.lower() == ">>commands") or (message.content == ">>help"):
        await client.send_message(message.channel, embed=commands())
    if message.content.lower().startswith('>>howl'):
        await client.send_message(message.channel, message.author.mention+' AWOOOOOO')

    if message.content.lower().startswith('>>stats'):
        await client.send_message(message.channel,stats())
    if message.content.lower().startswith("good boy") or message.content.startswith("good boi") or message.content.startswith('>>good boy') or message.content.startswith('>>good boi'):
        await client.send_message(message.channel, "*pants*\n WOOF\n *licks "+message.author.mention+"'s face*")
    if message.content.lower().startswith('>>log'):
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
    if message.content.lower().startswith('>>userHistory'):
        spl = message.content.split("-")
        if len(spl) == 1:
            await client.send_message(message.channel, "No User!\nUsage: ```>>userHistory-<displayName>```\n")
        elif len(spl) == 2:
            try:
                await client.send_message(message.channel, userHistory(spl[1]))
            except(discord.errors.HTTPException):
                await client.send_message(message.channel, 'No user history in logs!')
                f = open('./resources/log.txt','r')
                firstlinedate = f.readline().split('\t')[1]
                await client.send_message(message.channel, 'First message on '+firstlinedate)
    if message.content.lower().startswith('>>rekt'):
        spl = message.content.split(" ")
        if(len(spl) == 1):
            rektFile = open('./resources/rekt.txt', 'r')
            rektLines = rektFile.readlines()

            rektArr = []
            for line in rektLines:
                rektArr.append(line)
            rektRand = random.randint(0,len(rektArr)-1)
            await client.send_message(message.channel, rektArr[rektRand])
        else:
            rektFile = open('./resources/rekt.txt','a+')
            rektFile.write(spl[1]+'\n')
        rektFile.close()
    if message.content.lower().startswith('>>gif'):
        spl = message.content.split(' ')
        await client.send_message(message.channel, gif(spl))



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


