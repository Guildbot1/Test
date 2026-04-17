from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client["file_store_bot"]

users = db.users
channels = db.channels
files = db.files
batches = db.batches
premium = db.premium
banned = db.banned
payments = db.payments
settings = db.settings