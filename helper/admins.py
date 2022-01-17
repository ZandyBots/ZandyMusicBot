import assets.admins
import time 
from typing import List

from pyrogram.types import Chat
from assets.admins import get as gett
from assets.admins import set


async def get_administrators(chat: Chat) -> List[int]:
    get = gett(chat.id)

    if get:
        return get
    else:
        time.sleep(3) #control flood wait 
        administrators = await chat.get_members(filter="administrators")
        to_set = []

        for administrator in administrators:
            if administrator.can_manage_voice_chats:
                to_set.append(administrator.user.id)

        set(chat.id, to_set)
        return await get_administrators(chat)
