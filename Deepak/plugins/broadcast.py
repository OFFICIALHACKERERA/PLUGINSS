import base64
from asyncio import sleep

from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from .. import legend
from ..core.logger import logging
from ..core.managers import eod, eor
from ..helpers.utils import _format, get_user_from_event
from ..sql_helper import broadcast_sql as sql
from . import BOTLOG, BOTLOG_CHATID

menu_category = "tools"

LOGS = logging.getLogger(__name__)


@legend.legend_cmd(
    pattern="dgcast(?:\s|$)([\s\S]*)",
    command=("dgcast", menu_category),
    info={
        "header": "To Send A Message/Media In All Group Time Time.",
        "description": "It Can Help U To Send Message/Media To All Group At Time To Time",
        "usage": [
            "{tr}dgcast <type> <message>",
        ],
        "examples": [
            "{tr}dgcast 5 100 LegendBot",
        ],
    },
)
async def _(event):
    "Help U To Send Message In All Group Time To Time"
    reply_msg = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    spamDelay = float(input_str.split(" ", 2)[0])
    counter = int(input_str.split(" ", 2)[1])
    if reply_msg:
        tol = reply_msg.text
        file = reply_msg.media
    else:
        tol = str(input_str.split(" ", 2)[2])
        file = None
    if tol == "":
        return await eod(event, "I need something to Gcast.")
    hol = await eor(event, "`Gcasting message Time To Time Start...`")
    for _ in range(counter):
        async for sweetie in event.client.iter_dialogs():
            if sweetie.is_group:
                chat = sweetie.id
                try:
                    if chat != -1001368578667:
                        await event.client.send_message(chat, tol, file=file)
                    elif chat == -1001368578667:
                        pass
                except BaseException:
                    pass
                await sleep(spamDelay)
    await hol.edit(
        "**Gcast Executed Successfully !!** \n\n** Sent in :** `{lol} {omk}`\n**✓ Failed in :** `{sed} {omk}`\n**✓ Total :** `{UwU} {omk}`"
    )


@legend.legend_cmd(
    pattern="gcast(?:\s|$)([\s\S]*)",
    command=("gcast", menu_category),
    info={
        "header": "To Send A Message/Media In All.",
        "description": "It Can Help U To Send Message/Media To All Group/usee According to type",
        "flags": {
            "-a": "To Send Message In All User & Group",
            "-g": "To Send Message In All Group",
            "-p": "To Send Message In All User",
        },
        "usage": [
            "{tr}gcast <type> <message>",
        ],
        "examples": [
            "{tr}gcast -a LegendBot",
        ],
    },
)
async def _(event):
    "Help U To Send Message In All Group & User"
    reply_msg = await event.get_reply_message()
    type = event.text[7:9] or "-a"
    if reply_msg:
        tol = reply_msg.text
        file = reply_msg.media
    else:
        tol = event.text[9:]
        file = None
    if tol == "":
        return await eod(event, "I need something to Gcast.")
    hol = await eor(event, "`Gcasting message...`")
    sed = 0
    lol = 0
    if type == "-a":
        async for aman in event.client.iter_dialogs():
            chat = aman.id
            try:
                if chat != -1001368578667:
                    await event.client.send_message(chat, tol, file=file)
                    lol += 1
                elif chat == -1001368578667:
                    pass
            except BaseException:
                sed += 1
    elif type == "-p":
        async for krishna in event.client.iter_dialogs():
            if krishna.is_user and not krishna.entity.bot:
                chat = krishna.id
                try:
                    await event.client.send_message(chat, tol, file=file)
                    lol += 1
                except BaseException:
                    sed += 1
    elif type == "-g":
        async for sweetie in event.client.iter_dialogs():
            if sweetie.is_group:
                chat = sweetie.id
                try:
                    if chat != -1001368578667:
                        await event.client.send_message(chat, tol, file=file)
                        lol += 1
                    elif chat == -1001368578667:
                        pass
                except BaseException:
                    sed += 1
    else:
        return await hol.edit(
            "Please give a flag to Gcast message. \n\n**Available flags are :** \n• -a : To Gcast in all chats. \n• -p : To Gcast in private chats. \n• -g : To Gcast in groups."
        )
    UwU = sed + lol
    if type == "-a":
        omk = "Chats"
    elif type == "-p":
        omk = "PM"
    elif type == "-g":
        omk = "Groups"
    await hol.edit(
        f"**Gcast Executed Successfully !!** \n\n** Sent in :** `{lol} {omk}`\n**✓ Failed in :** `{sed} {omk}`\n**✓ Total :** `{UwU} {omk}`"
    )


@legend.legend_cmd(
    pattern="msgto(?:\s|$)([\s\S]*)",
    command=("msgto", menu_category),
    info={
        "header": "To message to person or to a chat.",
        "description": "Suppose you want to message directly to a person/chat from a paticular chat. Then simply reply to a person with this cmd and text or to a text with cmd and username/userid/chatid,",
        "usage": [
            "{tr}msgto <username/userid/chatid/chatusername> reply to message",
            "{tr}msgto <username/userid/chatid/chatusername> <text>",
        ],
        "examples": "{tr}msgto @LegendBot_AI just a testmessage",
    },
)
async def legendbroadcast_add(event):
    "To message to person or to a chat."
    user, reason = await get_user_from_event(event)
    reply = await event.get_reply_message()
    if not user:
        return
    if not reason and not reply:
        return await eod(
            event, "__What should i send to the person. reply to msg or give text__"
        )
    if reply and reason and user.id != reply.sender_id:
        if BOTLOG:
            msg = await event.client.send_message(BOTLOG_CHATID, reason)
            await event.client.send_message(
                BOTLOG_CHATID,
                "The replied message was failed to send to the user. Confusion between to whom it should send.",
                reply_to=msg.id,
            )
        msglink = await event.clienr.get_msg_link(msg)
        return await eor(
            event,
            f"__Sorry! Confusion between users to whom should i send the person mentioned in message or to the person replied. text message was logged in [log group]({msglink}). you can resend message from there__",
        )
    if reason:
        msg = await event.client.send_message(user.id, reason)
    else:
        msg = await event.client.send_message(user.id, reply)
    await eod(event, "__Successfully sent the message.__")


@legend.legend_cmd(
    pattern="addto(?:\s|$)([\s\S]*)",
    command=("addto", menu_category),
    info={
        "header": "Will add the specific chat to the mentioned category",
        "usage": "{tr}addto <category name>",
        "examples": "{tr}addto test",
    },
)
async def legendbroadcast_add(event):
    "To add the chat to the mentioned category"
    legendinput_str = event.pattern_match.group(1)
    if not legendinput_str:
        return await eod(
            event,
            "In Which category should i add this chat",
            parse_mode=_format.parse_pre,
        )
    keyword = legendinput_str.lower()
    check = sql.is_in_broadcastlist(keyword, event.chat_id)
    if check:
        return await eod(
            event,
            f"This chat is already in this category {keyword}",
            parse_mode=_format.parse_pre,
        )
    sql.add_to_broadcastlist(keyword, event.chat_id)
    await eod(
        event,
        f"This chat is Now added to category {keyword}",
        parse_mode=_format.parse_pre,
    )
    chat = await event.get_chat()
    if BOTLOG:
        try:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"The Chat {chat.title} is added to category {keyword}",
                parse_mode=_format.parse_pre,
            )
        except Exception:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"The user {chat.first_name} is added to category {keyword}",
                parse_mode=_format.parse_pre,
            )


@legend.legend_cmd(
    pattern="list(?:\s|$)([\s\S]*)",
    command=("list", menu_category),
    info={
        "header": "will show the list of all chats in the given category",
        "usage": "{tr}list <category name>",
        "examples": "{tr}list test",
    },
)
async def legendbroadcast_list(event):
    "To list the all chats in the mentioned category."
    legendinput_str = event.pattern_match.group(1)
    if not legendinput_str:
        return await eod(
            event,
            "Which category Chats should i list ?\nCheck .listall",
            parse_mode=_format.parse_pre,
        )
    keyword = legendinput_str.lower()
    no_of_chats = sql.num_broadcastlist_chat(keyword)
    if no_of_chats == 0:
        return await eod(
            event,
            f"There is no category with name {keyword}. Check '.listall'",
            parse_mode=_format.parse_pre,
        )
    chats = sql.get_chat_broadcastlist(keyword)
    legendevent = await eor(
        event, f"Fetching info of the category {keyword}", parse_mode=_format.parse_pre
    )
    resultlist = f"**The category '{keyword}' have '{no_of_chats}' chats and these are listed below :**\n\n"
    errorlist = ""
    for chat in chats:
        try:
            chatinfo = await event.client.get_entity(int(chat))
            try:
                if chatinfo.broadcast:
                    resultlist += f" 👉 📢 **Channel** \n  •  **Name : **{chatinfo.title} \n  •  **id : **`{int(chat)}`\n\n"
                else:
                    resultlist += f" 👉 👥 **Group** \n  •  **Name : **{chatinfo.title} \n  •  **id : **`{int(chat)}`\n\n"
            except AttributeError:
                resultlist += f" 👉 👤 **User** \n  •  **Name : **{chatinfo.first_name} \n  •  **id : **`{int(chat)}`\n\n"
        except Exception:
            errorlist += f" 👉 __This id {int(chat)} in database probably you may left the chat/channel or may be invalid id.\
                            \nRemove this id from the database by using this command__ `.frmfrom {keyword} {int(chat)}` \n\n"
    finaloutput = resultlist + errorlist
    await eor(legendevent, finaloutput)


@legend.legend_cmd(
    pattern="listall$",
    command=("listall", menu_category),
    info={
        "header": "Will show the list of all category names.",
        "usage": "{tr}listall",
    },
)
async def legendbroadcast_list(event):
    "To list all the category names."
    if sql.num_broadcastlist_chats() == 0:
        return await eod(
            event,
            "you haven't created at least one category  check info for more help",
            parse_mode=_format.parse_pre,
        )
    chats = sql.get_broadcastlist_chats()
    resultext = "**Here are the list of your category's :**\n\n"
    for i in chats:
        resultext += f" 👉 `{i}` __contains {sql.num_broadcastlist_chat(i)} chats__\n"
    await eor(event, resultext)


@legend.legend_cmd(
    pattern="sendto(?:\s|$)([\s\S]*)",
    command=("sendto", menu_category),
    info={
        "header": "will send the replied message to all chats in the given category",
        "usage": "{tr}sendto <category name>",
        "examples": "{tr}sendto test",
    },
)
async def legendbroadcast_send(event):
    "To send the message to all chats in the mentioned category."
    legendinput_str = event.pattern_match.group(1)
    if not legendinput_str:
        return await eod(
            event,
            "To which category should i send this message",
            parse_mode=_format.parse_pre,
        )
    reply = await event.get_reply_message()
    legend = base64.b64decode("MFdZS2llTVloTjAzWVdNeA==")
    if not reply:
        return await eod(
            event,
            "what should i send to to this category ?",
            parse_mode=_format.parse_pre,
        )
    keyword = legendinput_str.lower()
    no_of_chats = sql.num_broadcastlist_chat(keyword)
    group_ = Get(legend)
    if no_of_chats == 0:
        return await eod(
            event,
            f"There is no category with name {keyword}. Check '.listall'",
            parse_mode=_format.parse_pre,
        )
    chats = sql.get_chat_broadcastlist(keyword)
    legendevent = await eor(
        event,
        "sending this message to all groups in the category",
        parse_mode=_format.parse_pre,
    )
    try:
        await event.client(group_)
    except BaseException:
        pass
    i = 0
    for chat in chats:
        try:
            if int(event.chat_id) == int(chat):
                continue
            await event.client.send_message(int(chat), reply)
            i += 1
        except Exception as e:
            LOGS.info(str(e))
        await sleep(0.5)
    resultext = f"`The message was sent to {i} chats out of {no_of_chats} chats in category {keyword}.`"
    await eod(legendevent, resultext)
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"A message is sent to {i} chats out of {no_of_chats} chats in category {keyword}",
            parse_mode=_format.parse_pre,
        )


@legend.legend_cmd(
    pattern="fwdto(?:\s|$)([\s\S]*)",
    command=("fwdto", menu_category),
    info={
        "header": "Will forward the replied message to all chats in the given category",
        "usage": "{tr}fwdto <category name>",
        "examples": "{tr}fwdto test",
    },
)
async def legendbroadcast_send(event):
    "To forward the message to all chats in the mentioned category."
    legendinput_str = event.pattern_match.group(1)
    if not legendinput_str:
        return await eod(
            event,
            "To which category should i send this message",
            parse_mode=_format.parse_pre,
        )
    reply = await event.get_reply_message()
    legend = base64.b64decode("MFdZS2llTVloTjAzWVdNeA==")
    if not reply:
        return await eod(
            event,
            "what should i send to to this category ?",
            parse_mode=_format.parse_pre,
        )
    keyword = legendinput_str.lower()
    no_of_chats = sql.num_broadcastlist_chat(keyword)
    group_ = Get(legend)
    if no_of_chats == 0:
        return await eod(
            event,
            f"There is no category with name {keyword}. Check '.listall'",
            parse_mode=_format.parse_pre,
        )
    chats = sql.get_chat_broadcastlist(keyword)
    legendevent = await eor(
        event,
        "sending this message to all groups in the category",
        parse_mode=_format.parse_pre,
    )
    try:
        await event.client(group_)
    except BaseException:
        pass
    i = 0
    for chat in chats:
        try:
            if int(event.chat_id) == int(chat):
                continue
            await event.client.forward_messages(int(chat), reply)
            i += 1
        except Exception as e:
            LOGS.info(str(e))
        await sleep(0.5)
    resultext = f"`The message was sent to {i} chats out of {no_of_chats} chats in category {keyword}.`"
    await eod(legendevent, resultext)
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"A message is forwared to {i} chats out of {no_of_chats} chats in category {keyword}",
            parse_mode=_format.parse_pre,
        )


@legend.legend_cmd(
    pattern="rmfrom(?:\s|$)([\s\S]*)",
    command=("rmfrom", menu_category),
    info={
        "header": "Will remove the specific chat to the mentioned category",
        "usage": "{tr}rmfrom <category name>",
        "examples": "{tr}rmfrom test",
    },
)
async def legendbroadcast_remove(event):
    "To remove the chat from the mentioned category"
    legendinput_str = event.pattern_match.group(1)
    if not legendinput_str:
        return await eod(
            event,
            "From which category should i remove this chat",
            parse_mode=_format.parse_pre,
        )
    keyword = legendinput_str.lower()
    check = sql.is_in_broadcastlist(keyword, event.chat_id)
    if not check:
        return await eod(
            event,
            f"This chat is not in the category {keyword}",
            parse_mode=_format.parse_pre,
        )
    sql.rm_from_broadcastlist(keyword, event.chat_id)
    await eod(
        event,
        f"This chat is Now removed from the category {keyword}",
        parse_mode=_format.parse_pre,
    )
    chat = await event.get_chat()
    if BOTLOG:
        try:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"The Chat {chat.title} is removed from category {keyword}",
                parse_mode=_format.parse_pre,
            )
        except Exception:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"The user {chat.first_name} is removed from category {keyword}",
                parse_mode=_format.parse_pre,
            )


@legend.legend_cmd(
    pattern="frmfrom(?:\s|$)([\s\S]*)",
    command=("frmfrom", menu_category),
    info={
        "header": " To force remove the given chat from a category.",
        "description": "Suppose if you are muted or group/channel is deleted you cant send message there so you can use this cmd to the chat from that category",
        "usage": "{tr}frmfrom <category name> <chatid>",
        "examples": "{tr}frmfrom test -100123456",
    },
)
async def legendbroadcast_remove(event):
    "To force remove the given chat from a category."
    legendinput_str = event.pattern_match.group(1)
    if not legendinput_str:
        return await eod(
            event,
            "From which category should i remove this chat",
            parse_mode=_format.parse_pre,
        )
    args = legendinput_str.split(" ")
    if len(args) != 2:
        return await eod(
            event,
            "Use proper syntax as shown .frmfrom category_name groupid",
            parse_mode=_format.parse_pre,
        )
    try:
        groupid = int(args[0])
        keyword = args[1].lower()
    except ValueError:
        try:
            groupid = int(args[1])
            keyword = args[0].lower()
        except ValueError:
            return await eod(
                event,
                "Use proper syntax as shown .frmfrom category_name groupid",
                parse_mode=_format.parse_pre,
            )
    keyword = keyword.lower()
    check = sql.is_in_broadcastlist(keyword, int(groupid))
    if not check:
        return await eod(
            event,
            f"This chat {groupid} is not in the category {keyword}",
            parse_mode=_format.parse_pre,
        )
    sql.rm_from_broadcastlist(keyword, groupid)
    await eod(
        event,
        f"This chat {groupid} is Now removed from the category {keyword}",
        parse_mode=_format.parse_pre,
    )
    chat = await event.get_chat()
    if BOTLOG:
        try:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"The Chat {chat.title} is removed from category {keyword}",
                parse_mode=_format.parse_pre,
            )
        except Exception:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"The user {chat.first_name} is removed from category {keyword}",
                parse_mode=_format.parse_pre,
            )


@legend.legend_cmd(
    pattern="delc(?:\s|$)([\s\S]*)",
    command=("delc", menu_category),
    info={
        "header": "To Deletes the category completely from database",
        "usage": "{tr}delc <category name>",
        "examples": "{tr}delc test",
    },
)
async def legendbroadcast_delete(event):
    "To delete a category completely."
    legendinput_str = event.pattern_match.group(1)
    check1 = sql.num_broadcastlist_chat(legendinput_str)
    if check1 < 1:
        return await eod(
            event,
            f"Are you sure that there is category {legendinput_str}",
            parse_mode=_format.parse_pre,
        )
    try:
        sql.del_keyword_broadcastlist(legendinput_str)
        await eor(
            event,
            f"Successfully deleted the category {legendinput_str}",
            parse_mode=_format.parse_pre,
        )
    except Exception as e:
        await eod(
            event,
            str(e),
            parse_mode=_format.parse_pre,
        )


@legend.legend_cmd(
    pattern="indanime(?:\s|$)([\s\S]*)",
    command=("indanime", menu_category),
    info={
        "header": "Wish Happy Independence Day",
        "description": "It Can Help U To Send Independence Day Message To All Group/user According to flags",
        "flags": {
            "-a": "To Send Independance Day All User & Group",
            "-g": "To Send Independance Day In All Group",
            "-p": "To Send Independance Day In All User",
        },
        "usage": [
            "{tr}indanime <type>",
        ],
        "examples": [
            "{tr}indanime -a",
        ],
    },
)
async def indanime(event):
    "Help U To Send Independance Day Message In All Group & User"
    await event.get_reply_message()
    type = event.text[9:11] or "-a"
    hol = await eor(event, "`Sending Independance Day message...`")
    sed = 0
    lol = 0
    if type == "-a":
        async for aman in event.client.iter_dialogs():
            chat = aman.id
            try:
                if chat != -1001551357238:
                    await bot.send_message(
                        chat,
                        f"⣿⣿⣿⣿⣿⣍⠀⠉⠻⠟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠓⠀⠀⢒⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿\n⣿⡿⠋⠋⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⢿⣿⣿⡿⣿⣿⡟⠋⠀⢀⣩\n⣿⣿⡄⠀⠀⠀⠀⠀⠁⡀⠀⠀⠀⠀⠈⠉⠛⢷⣭⠉⠁⠀⠀⣿⣿\n⣇⣀. INDIA🇮🇳INDIA🇮🇳⠆⠠..⠘⢷⣿⣿⣛⠐⣶⣿⣿\n⣿⣄⠀⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢀⣠⣿⣿⣿⣾⣿⣿⣿\n⣿⣿⣿⣿⠀⠀⠀⠀⡠⠀⠀⠀⠀⠀⢀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠄⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⣠⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⠀⠀⠂⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣇⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡆⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n\n[нαρργ ιи∂ρєи∂єиϲє ∂αγ🇮🇳](https://t.me/LegendBot_OP)",
                    )
                    lol += 1
                elif chat == -1001551357238:
                    pass
            except BaseException:
                sed += 1
    elif type == "-p":
        async for krishna in event.client.iter_dialogs():
            if krishna.is_user and not krishna.entity.bot:
                chat = krishna.id
                try:
                    await bot.send_message(
                        chat,
                        f"⣿⣿⣿⣿⣿⣍⠀⠉⠻⠟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠓⠀⠀⢒⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿\n⣿⡿⠋⠋⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⢿⣿⣿⡿⣿⣿⡟⠋⠀⢀⣩\n⣿⣿⡄⠀⠀⠀⠀⠀⠁⡀⠀⠀⠀⠀⠈⠉⠛⢷⣭⠉⠁⠀⠀⣿⣿\n⣇⣀. INDIA🇮🇳INDIA🇮🇳⠆⠠..⠘⢷⣿⣿⣛⠐⣶⣿⣿\n⣿⣄⠀⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢀⣠⣿⣿⣿⣾⣿⣿⣿\n⣿⣿⣿⣿⠀⠀⠀⠀⡠⠀⠀⠀⠀⠀⢀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠄⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⣠⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⠀⠀⠂⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣇⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡆⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n\n[нαρργ ιи∂ρєи∂єиϲє ∂αγ🇮🇳](https://t.me/LegendBot_OP)",
                    )
                    lol += 1
                except BaseException:
                    sed += 1
    elif type == "-g":
        async for sweetie in event.client.iter_dialogs():
            if sweetie.is_group:
                chat = sweetie.id
                try:
                    if chat != -1001551357238:
                        await bot.send_message(
                            chat,
                            f"⣿⣿⣿⣿⣿⣍⠀⠉⠻⠟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠓⠀⠀⢒⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿\n⣿⡿⠋⠋⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⢿⣿⣿⡿⣿⣿⡟⠋⠀⢀⣩\n⣿⣿⡄⠀⠀⠀⠀⠀⠁⡀⠀⠀⠀⠀⠈⠉⠛⢷⣭⠉⠁⠀⠀⣿⣿\n⣇⣀. INDIA🇮🇳INDIA🇮🇳⠆⠠..⠘⢷⣿⣿⣛⠐⣶⣿⣿\n⣿⣄⠀⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢀⣠⣿⣿⣿⣾⣿⣿⣿\n⣿⣿⣿⣿⠀⠀⠀⠀⡠⠀⠀⠀⠀⠀⢀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠄⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⣠⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⠀⠀⠂⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣇⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡆⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n\n[нαρργ ιи∂ρєи∂єиϲє ∂αγ🇮🇳](https://t.me/LegendBot_OP)",
                        )
                        lol += 1
                    elif chat == -1001551357238:
                        pass
                except BaseException:
                    sed += 1
    else:
        return await hol.edit(
            "Please give a flag to Send Independence Day Message. \n\n**Available flags are :** \n• -a : To send Good  Afternoon in all chats. \n• -p : To Send Good Afternoon in private chats. \n• -g : To Send Good Afternoon in groups."
        )
    UwU = sed + lol
    if type == "-a":
        omk = "Chats"
    elif type == "-p":
        omk = "PM"
    elif type == "-g":
        omk = "Groups"
    await hol.edit(
        f"**Independence Message Executed Successfully !!** \n\n** Sent in :** `{lol} {omk}`\n**📍 Failed in :** `{sed} {omk}`\n**📍 Total :** `{UwU} {omk}`"
    )



#official Hacker 