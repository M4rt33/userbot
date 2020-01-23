from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
import asyncio

@command(outgoing=True, pattern=r"^.mute ?(\d+)?", allow_sudo=True)
async def startmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("**Attenzione utente mutato! xD**")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("**Perpiacere tagga con la @ del utente che vuoi mutare dopo .mute!**")
    chat_id = event.chat_id
    chat = await event.get_chat()
    if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None: 
        if chat.admin_rights.delete_messages is True:
            pass
        else:
            return await event.edit("Mado")
    elif "creator" in vars(chat):
        pass
    elif private == True:
        pass
    else:
        return await event.edit("**Down non puoi mutare una persona senza l'admin**")
    if is_muted(userid, chat_id):
        return await event.edit("**Madoooo che coglione sto utente è già mutato in questa chat!**")
    try:
        mute(userid, chat_id)
    except Exception as e:
        await event.edit("Errore dio cane porcino\nl'errore è" + str(e))
    else:
        await event.edit("**HAHHAHAH quel coglione è stato mutato!**")

@command(outgoing=True, pattern=r"^.unmute ?(\d+)?", allow_sudo=True)
async def endmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("**Attenzione utente mutato! xD**")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("Perpiacere tagga con la @ del utente che vuoi mutare dopo .mute!")
    chat_id = event.chat_id
    if not is_muted(userid, chat_id):
        return await event.edit("**Madoooo che coglione sto utente è già mutato in questa chat!**")
    try:
        unmute(userid, chat_id)
    except Exception as e:
        await event.edit("Errore dio cane porcino\nl'errore è" + str(e))
    else:
        await event.edit("**HAHHAHAH quel coglione è stato mutato!**")

@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, event.chat_id):
        await event.delete()

from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
import asyncio

@command(outgoing=True, pattern=r"^.mute ?(\d+)?")
async def startmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Unexpected issues or ugly errors may occur!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("Perpiacere tagga con la @ del utente che vuoi mutare dopo .mute!")
    chat_id = event.chat_id
    chat = await event.get_chat()
    if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None: 
        if chat.admin_rights.delete_messages is True:
            pass
        else:
            return await event.edit("Non puoi mutare se non hai i permessi di delete")
    elif "creator" in vars(chat):
        pass
    elif private == True:
        pass
    else:
        return await event.edit("**Down non puoi mutare una persona senza l'admin**")
    if is_muted(userid, chat_id):
        return await event.edit("**Madoooo che coglione sto utente è già mutato in questa chat!**")
    try:
        mute(userid, chat_id)
    except Exception as e:
        await event.edit("Errore dio cane porcino\nl'errore è" + str(e))
    else:
        await event.edit("**HAHHAHAH quel coglione è stato mutato!**")

@command(outgoing=True, pattern=r"^.unmute ?(\d+)?")
async def endmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Unexpected issues or ugly errors may occur!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("Perpiacere tagga con la @ del utente che vuoi mutare dopo .mute!")
    chat_id = event.chat_id
    if not is_muted(userid, chat_id):
        return await event.edit("**L'utente non è mutato deficente**")
    try:
        unmute(userid, chat_id)
    except Exception as e:
        await event.edit("Errore dio cane porcino\nl'errore è" + str(e))
    else:
        await event.edit("**Cazzo perchè lo hai smutato rompeva le palle...**")

@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, event.chat_id):
        await event.delete()
