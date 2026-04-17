from pyrogram import Client, filters
from pyrogram.types import *
from database import users

@Client.on_message(filters.command("start"))
async def start(client, message):

    await users.update_one(
        {"_id": message.from_user.id},
        {"$set": {"user": message.from_user.id}},
        upsert=True
    )

    kb = ReplyKeyboardMarkup(
        [
            ["📂 File Store", "👑 Premium"],
            ["⚙️ Settings", "📊 Stats"]
        ],
        resize_keyboard=True
    )

    await message.reply("🔥 Welcome to File Store Bot", reply_markup=kb)