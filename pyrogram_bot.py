import os
from pyrogram import Client, filters
from pyrogram.types import Message
import logging

logging.basicConfig(level=logging.INFO)

API_ID = int(os.environ.get("API_ID", 12345))
API_HASH = os.environ.get("API_HASH", "your_api_hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token")

app = Client("mink_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message: Message)
   await message.reply("""🌟 Welcome to MinkBot V2
This bot can download music from Spotify and YouTube!Enjoy 🎧""")
    
@app.on_message(filters.audio | filters.voice)
async def handle_audio(client, message: Message):
    if message.audio or message.voice:
        file = await message.download()
        await message.reply("🎶 Got your file! (music recognition logic goes here)")
        os.remove(file)

app.run()
