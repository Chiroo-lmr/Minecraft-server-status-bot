import discord
from discord import Intents
import mcstatus
from mcstatus import JavaServer
import asyncio

intents = Intents.default()
intents.guilds = True
intents.members = True
intents.messages = True

client = discord.Client(intents=intents)

servers = {
    "Server name         |":"IP:port"
}

count = 0
message_id = 0

@client.event
async def on_ready():
    print('Bot is ready!')
    while True:
        await check_servers()
        await asyncio.sleep(5)

async def check_servers():
    global message
    message = "**# Minecraft servers status :\n"
    for name, address in servers.items():
        server = JavaServer.lookup(address)
        try:
            status = server.status()
        except:
            status = "Offline"
        if status and status != "Offline":
            message += f"🟢  {name}  UP :\n"
            message += f"   **{status.players.online} / {status.players.max} players**\n\n"
        if status == "Offline":
            message += f"🔴  {name}  DOWN.\n\n"
    await delete_and_send_message()

async def delete_and_send_message():
    global count
    global message_id
    global message
    channel = client.get_channel("channel id")
    if count == 0:
        first_message = await channel.send("[searching for the status]")
        message_id = first_message.id
        count = 1
    old_message = await channel.fetch_message(message_id)
    message += "**"
    print(message)
    new_message = await old_message.edit(content=message)
    message_id = new_message.id
    print(message_id)
    pass

client.run('TOKEN BOT')
