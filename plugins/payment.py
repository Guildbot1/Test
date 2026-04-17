from pyrogram import Client, filters
from pyrogram.types import *
from database import payments
from utils.qr import generate_qr
from config import UPI_ID

ADMIN = 123456789

@Client.on_message(filters.regex("👑 Premium"))
async def premium(client, message):

    btn = InlineKeyboardMarkup([
        [InlineKeyboardButton("Weekly ₹49", callback_data="pay_week")],
        [InlineKeyboardButton("Monthly ₹99", callback_data="pay_month")]
    ])

    await message.reply("Choose Plan", reply_markup=btn)

@Client.on_callback_query(filters.regex("pay_"))
async def pay(client, q):

    upi = f"upi://pay?pa={UPI_ID}&pn=Bot&am=99"
    qr = generate_qr(upi)

    await q.message.reply_photo(qr, caption="Pay & send screenshot + UTR")

@Client.on_message(filters.photo)
async def receive(client, message):

    await payments.insert_one({
        "user": message.from_user.id,
        "status": "pending"
    })

    await client.send_photo(ADMIN, message.photo.file_id,
                            caption=f"Payment from {message.from_user.id}")

    await message.reply("Waiting for approval")