import discord
from discord.ext import tasks
from discord import File
from twitch_request import *

client = discord.Client()


@client.event
async def on_ready():
    activity = discord.Game(name="waiting for clips...", type=1)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print('We have logged in as {0.user}'.format(client))
    global clip_link_old
    clip_link_old = None
    request_loop.start()


@tasks.loop(minutes=5)
async def request_loop():
    global clip_link
    global clip_link_old


    clip_link = stream_request("schlauster")
    if clip_link != None:
        if clip_link != clip_link_old:
            channel = client.get_channel(961274327205048403)
            await channel.send(clip_link)
            await channel.send(f"@everyone ein neuer clip von {name()}")
            clip_link_old = clip_link


client.run("OTU3MDIyNTIxNDY1NjM0ODQ2.Yj4urQ.VSsZgCE67pAbCoQ1EXp9H7IAjnI")
