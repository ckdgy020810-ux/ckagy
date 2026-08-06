import discord
import os

TOKEN = os.environ["TOKEN"]
CHANNEL_ID = 123456789  # 너 채널 ID로 바꾸기

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"로그인됨: {client.user}")

@client.event
async def on_message(message):
    # ✅ 다른 채널이면 무시
    if message.channel.id != CHANNEL_ID:
        return

    # ✅ 일반 봇 메시지는 무시하지만, 웹훅은 허용
    if message.author.bot and message.webhook_id is None:
        return

    text = message.content.lower()

    # ✅ 테스트 필터 (xxl 포함)
    if "xxl" in text:
        await message.channel.send(f"✅ 발견!\n{message.content}")

client.run(TOKEN)
