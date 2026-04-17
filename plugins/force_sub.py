from database import channels

async def check_force_sub(client, user_id):
    async for ch in channels.find({}):
        try:
            member = await client.get_chat_member(ch["id"], user_id)
            if member.status == "left":
                return False
        except:
            return False
    return True