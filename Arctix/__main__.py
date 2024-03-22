import asyncio
import importlib
from pyrogram import idle
from Arctix import Arctix
from config import LOGGER_ID
from Arctix.modules import ALL_MODULES


#LOGGER_ID = -1001986522281
loop = asyncio.get_event_loop()

async def Arctixx_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("Arctix.modules." + all_module)
    print("𝖻𝗈𝗍 𝗌𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅 𝗌𝗍𝖺𝗋𝗍")
    await Arctix.send_message(LOGGER_ID, "**𝖨 𝖺𝗆 alive**")
    await idle()
    print("Error Came , check where is erro")
  

if __name__ == "__main__":
    loop.run_until_complete(Arctixx_boot())