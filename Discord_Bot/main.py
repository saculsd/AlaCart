import discord
from discord import File
from discord.ext import tasks
import random

import os

from messages import ASCHE, FLAMME
from accounts import accounts
from html_request import request


def getsize(file_name, ):
    global bild1_größe
    global größe1_old
    bild1_größe = os.path.getsize("./bilder/" + file_name)


request(True)
getsize("plan_link1.jpg")
größe1_old = bild1_größe

client = discord.Client()

announce_link = False


@client.event
async def on_ready():
    activity = discord.Game(name="!plan", type=1)
    await client.change_presence(status=discord.Status.online,
                                 activity=activity)
    print('We have logged in as {0.user}'.format(client))
    request_loop.start()


@tasks.loop(minutes=5)
async def request_loop():
    request(False)
    getsize("plan_link1.jpg")
    global bild1_größe
    global größe1_old

    if bild1_größe != größe1_old:
        print("Neuer Plan")
        größe1_old = bild1_größe

        channel = client.get_channel(941785576317784185)
        await channel.send(file=File("./bilder/plan_link1.jpg"))

        if request.post_bild1 == False:
            await channel.send(file=File("./bilder/plan_extra1.jpg"))
        if request.post_bild2 == False:
            await channel.send(file=File("./bilder/plan_extra2.jpg"))
        if request.post_bild3 == False:
            await channel.send(file=File("./bilder/plan_extra3.jpg"))
        if request.post_bild4 == False:
            await channel.send(file=File("./bilder/plan_extra4.jpg"))

        await channel.send("@everyone Es gibt einen neuen Vertretungsplan")


@client.event
async def on_message(message):
    if message.content.startswith("!plan"):
        if message.channel.id != 935890486856646677:
            Author = message.author.id
            if Author in accounts:

                await message.channel.send("überprüfe auf Neusten Vertretungsplan...")
                request(False)
                await message.channel.send(file=File("./bilder/plan_link1.jpg"))

                if request.post_bild1 == False:
                    await message.channel.send(file=File("./bilder/plan_extra1.jpg"))
                if request.post_bild2 == False:
                    await message.channel.send(file=File("./bilder/plan_extra2.jpg"))
                if request.post_bild3 == False:
                    await message.channel.send(file=File("./bilder/plan_extra3.jpg"))
                if request.post_bild4 == False:
                    await message.channel.send(file=File("./bilder/plan_extra4.jpg"))

                await message.channel.send("Das ist der Aktuellste Vertretungsplan")

            else:
                await message.channel.send(":lock: Du hast keine Erlaubnis diese Dateien zu sehen :lock:")

        else:
            await message.channel.send(":lock: Falscher Kanal :lock:")

    if message.content.startswith("!splan"):
        if message.channel.id != 935890486856646677:
            Author = message.author.id
            if Author in accounts:
                await message.channel.send(file=File("./bilder/M2.jpg"))
            else:
                await message.channel.send(":lock: Du hast keine Erlaubnis diese Dateien zu sehen :lock:")
        else:
            await message.channel.send(":lock: Falscher Kanal :lock:")

    if message.content.startswith("!asche"):
        await message.channel.send(ASCHE)

    if message.content.startswith("!flamme"):
        await message.channel.send(FLAMME)

    # quatsch:
    if message.content.startswith("!pipi"):
        await message.channel.send("no more pipi")


#client.run("OTM1MTgwMTc3NjU3NDM4MjA5.Ye64aQ.o8XM06NDh9afN0ec8A8r8zMayZ8")

