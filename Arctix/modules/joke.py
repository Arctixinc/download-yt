from pyrogram import Client, filters
from Arctix import Arctix as app
import asyncio
import requests


JOKE_API_ENDPOINT = 'https://v2.jokeapi.dev/joke/Dark?format=txt&amount=3'

@app.on_message(filters.command("joke"))
async def joke(_, message):
    response = requests.get(JOKE_API_ENDPOINT)
    joke_text = response.text
    await message.reply_text(joke_text)