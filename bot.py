import discord
import os

TOKEN = os.environ["TOKEN"]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ 로그인됨: {client.user}")

@client.event
async def on_message(message):
    # ✅ 웹훅 메시지는 허용, 일반 봇 메시지는 무시
    if message.author.bot and message.webhook_id is None:
        return

    text = ""

    # ✅ 일반 메시지
    if message.content:
        text += message.content.lower()

    # ✅ 임베드까지 포함해서 전부 읽기
    for embed in message.embeds:
        if embed.title:
            text += embed.title.lower()
        if embed.description:
            text += embed.description.lower()

    # ✅ 디버그 (로그에 찍힘)
    print(text)

    # ✅ XXL + SHINY 둘 다 있을 때만 알림 (핵심)
    if "xxl" in text and "shiny" in text:
        await message.channel.send("🔥 XXL + 이로치 발견!")

    # ✅ XXL만
    elif "xxl" in text:
        await message.channel.send("🐘 XXL 발견!")

    # ✅ SHINY만
    elif "shiny" in text:
        await message.channel.send("✨ 이로치 발견!")

