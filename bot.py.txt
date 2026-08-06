import discord
import os

TOKEN = os.environ["TOKEN"]
CHANNEL_ID = 123456789  # 채널 ID 넣기

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"로그인됨: {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id != CHANNEL_ID:
        return

    text = message.content.lower()

    if "xxl" in text:
        await message.channel.send(f"✅ 발견!\n{message.content}")

client.run(TOKEN)
