from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Arctix import Arctix as app
from config import BOT_USERNAME, OWNER_ID, LOGGER_ID
import config
from pyrogram.types import InputMediaVideo
import random 
from pyrogram.types import Message
import asyncio

@app.on_message(filters.command("start"))
async def start_command(client: app, message: Message):
    await app.send_message(
        chat_id=message.chat.id,
        text="Hello! Welcome to your bot. You can customize this message for the start command."
    )

@app.on_message(filters.private & filters.incoming)
async def on_pm_s(client: Client, message: Message):
    if not message.from_user.id ==OWNER_ID:
        fwded_mesg = await message.forward(chat_id=OWNER_ID, disable_notification=True)



@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    await edited_message.delete()