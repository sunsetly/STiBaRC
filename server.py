import discord
from urllib.request import Request, urlopen

client = discord.Client()
token = 'NDM4MDU1MjIyMjA4ODg4ODMz.Db_CPw.BGU0iFNCiuL4XfIO6e_28aoajKE'

# BOT STUFF #
prefix = 'v! '
admin = '219506234401751041'

@client.event
async def on_message(message):
    global json
    
    if message.author == client.user:
        return
            
    messagecontent = message.content.lower()
    messagecontent = messagecontent.replace('[', '')
    messagecontent = messagecontent.replace(']', '')
    
    if messagecontent.startswith(prefix):
        
        parser = messagecontent.split(prefix, 1)[1]
        print(parser)
        
        if ('help' in parser) and ('memory' not in parser) and ('news' not in parser) and ('scratch' not in parser) and ('weather' not in parser) and ('conversation' not in parser) and ('math' not in parser) and ('discord' not in parser) and ('currency' not in parser) and ('conversions' not in parser) and ('team' not in parser) and ('music' not in parser) and ('chat' not in parser):
            embed = discord.Embed(title="Vorseta:", description="Remember the prefix, `v!`", color=2123412)
            embed.add_field(name="Scratch", value="`scratch help`", inline=False)
            embed.add_field(name="Weather", value="`weather help`", inline=False)
            embed.add_field(name="Conversation", value="`conversation help`", inline=False)
            embed.add_field(name="Math", value="`math help`", inline=False)
            embed.add_field(name="Discord", value="`discord help`", inline=False)
            embed.add_field(name="Currency", value="`currency help`", inline=False)
            embed.add_field(name="Team", value="`team help`", inline=False)
            embed.add_field(name="Music", value="`music help`", inline=False)
            embed.add_field(name="Vorseta Chat (Cross-Server Communication)", value="`chat help`", inline=False)
            embed.add_field(name="Memory", value="`memory help`", inline=False)
            embed.add_field(name="News", value="`news help`", inline=False)
            await client.send_message(message.channel, embed=embed)
        
        if ('session' in parser):
            u = message.content.split()[2]
            p = message.content.split()[3]
            s = stibarc.create_session(u,p)
            


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------')     
                                  
client.run(token)
app.run() 