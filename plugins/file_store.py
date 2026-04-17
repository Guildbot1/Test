from pyrogram import Client, filters
from database import files

@Client.on_message(filters.command("link"))
async def link(client, message):

    if not message.reply_to_message:
        return await message.reply("Reply to file")

    fid = message.reply_to_message.id

    await files.insert_one({"file_id": fid})

    bot = await client.get_me()
    link = f"https://t.me/{bot.username}?start=file_{fid}"

    await message.reply(link)