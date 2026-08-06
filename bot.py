import discord
import os

TOKEN = os.environ["TOKEN"]  # ✅ 이걸로 변경

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ 로그인됨: {client.user}")

@client.event
async def on_message(message):
    print("📩 메시지 감지됨")

    if message.author.bot and message.webhook_id is None:
        return

    text = ""

    if message.content:
        text += message.content.lower()

    for embed in message.embeds:
        if embed.title:
            text += embed.title.lower()
        if embed.description:
            text += embed.description.lower()

    print("📄 내용:", text)

    if "xxl" in text:
        await message.channel.send("🐘 XXL 발견!")

client.run(TOKEN)
