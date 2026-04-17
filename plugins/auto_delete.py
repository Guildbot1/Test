AUTO_DELETE = 300

async def auto_delete(msg):
    await msg.delete(delay=AUTO_DELETE)