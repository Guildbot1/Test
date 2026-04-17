from pyrogram import Client, filters
from database import users, premium

@Client.on_message(filters.regex("📊 Stats"))
async def stats(client, message):

    u = await users.count_documents({})
    p = await premium.count_documents({})

    await message.reply(f"Users: {u}\nPremium: {p}")