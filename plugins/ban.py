from database import banned

async def is_banned(uid):
    return await banned.find_one({"_id": uid})