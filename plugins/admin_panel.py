from pyrogram import Client, filters
from pyrogram.types import *
from config import ADMINS

@Client.on_message(filters.command("admin"))
async def admin(client, message):

    if message.from_user.id not in ADMINS:
        return

    kb = ReplyKeyboardMarkup(
        [
            ["📢 Broadcast", "👥 Users"],
            ["➕ Force Sub", "➖ Remove"],
            ["💰 Payments", "📊 Stats"]
        ],
        resize_keyboard=True
    )

    await message.reply("ADMIN PANEL", reply_markup=kb)
