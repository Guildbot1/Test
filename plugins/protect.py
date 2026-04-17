from database import users

async def is_protect(uid):
    d = await users.find_one({"_id": uid})
    return d.get("protect", False) if d else False