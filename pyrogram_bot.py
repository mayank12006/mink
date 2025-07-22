import os
from pyrogram import Client, filters
from pyrogram.types import Message
import logging

logging.basicConfig(level=logging.INFO)

API_ID = int(os.environ.get("API_ID", 22080529))
API_HASH = os.environ.get("API_HASH", "8c5ef7fe6857ea7aca95175ed2dcfbaa")

app = Client("minkadi_bot", api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply("🌟 Welcome to MinkBot V2\n"
        "This bot can download music from Spotify and YouTube! Enjoy 🎧")
    

@app.on_message(filters.audio | filters.voice)
async def handle_audio(client, message: Message):
    if message.audio or message.voice:
        file = await message.download()
        await message.reply("🎶 Got your file! (music recognition logic goes here)")
        os.remove(file)

app.run()
