from pyrogram import Client, filters
from database import batches

temp = {}

@Client.on_message(filters.command("batch"))
async def batch(client, message):
    temp[message.from_user.id] = []
    await message.reply("Send files then /done")

@Client.on_message(filters.document | filters.video | filters.audio)
async def add_file(client, message):
    uid = message.from_user.id
    if uid in temp:
        temp[uid].append(message.id)
        await message.reply("Added")

@Client.on_message(filters.command("done"))
async def done(client, message):
    uid = message.from_user.id
    if uid not in temp:
        return

    bid = str(uid)
    await batches.insert_one({"batch": bid, "files": temp[uid]})

    bot = await client.get_me()
    link = f"https://t.me/{bot.username}?start=batch_{bid}"

    await message.reply(link)
    del temp[uid]