from pyrogram import Client, filters
from pyrogram.types import *
from database import users, premium

@Client.on_message(filters.regex("⚙️ Settings"))
async def settings(client, message):

    u = await users.count_documents({})
    p = await premium.count_documents({})

    text = f"""
🔧 **Settings**

Customize your settings as your need

📊 **Bot Stats**
Total Users: `{u}`
Premium: `{p}`
"""

    btn = InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 F-SUB SETTINGS ⚙️", callback_data="fsub")],
        [InlineKeyboardButton("🔗 LINK SHORTENER 🔗", callback_data="short")],
        [InlineKeyboardButton("☂️ PROTECT CONTENT", callback_data="protect")],
        [InlineKeyboardButton("⏱ AUTO DELETE", callback_data="autodel")],
        [InlineKeyboardButton("🔄 REFRESH", callback_data="refresh")]
    ])

    await message.reply(text, reply_markup=btn)