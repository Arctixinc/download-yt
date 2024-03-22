import requests
from pyrogram import Client, filters
from Arctix import Arctix as app
from config import OWNER_ID


@app.on_message(
    filters.command("mongo")
    & filters.private
    & filters.user(OWNER_ID)
)
async def mongo_command(client, message):
    try:
        # Split the message content into a list of inputs
        inputs = message.text.split()[1:5]

        # Extract values from the input list
        owner_id, bt_token, api_id, api_hash = inputs
        
        bot_info_response = requests.get(f'https://api.telegram.org/bot{bt_token}/getMe')
        bot_name = bot_info_response.json()['result']['username'] if bot_info_response.status_code == 200 else None
        
        # Construct the reply message
        reply_message = (
            f"API ID: {api_id}\n"
            f"API HASH: {api_hash}\n"
            f"OWNER ID: {owner_id}\n"
            f"BOT TOKEN: {bt_token}\n"                
            f"BOT USERNAME: {bot_name}"
        )

      # Send the reply asynchronously
        await message.reply_text(reply_message)

    except ValueError:
        # Handle if the user did not provide enough inputs
        await message.reply_text("Please provide all four values.")
    except Exception as e:
        # Handle other exceptions if any
        await message.reply_text(f"An error occurred: {str(e)}")