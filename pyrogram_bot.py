import os
from pyrogram import Client, filters
from pyrogram.types import Message
import logging

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token")

# ✅ Run in BOT MODE only
app = Client("mink_bot", bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply("👋 Welcome to MinkBot V2 with Pyrogram!")

@app.on_message(filters.audio | filters.voice)
async def handle_audio(client, message: Message):
    if message.audio or message.voice:
        file = await message.download()
        await message.reply("🎶 Got your file! (music recognition logic goes here)")
        os.remove(file)

app.run()
