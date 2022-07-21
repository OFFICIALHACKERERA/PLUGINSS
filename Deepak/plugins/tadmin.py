"""
idea from lynda and rose bot
made by @LEGEND_K_BOY
"""
from telethon.errors import BadRequestError
from telethon.errors.rpcerrorlist import UserAdminInvalidError, UserIdInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
from telethon.utils import get_display_name

from Deepak import legend

from ..core.managers import eor
from ..helpers.utils import _format
from . import BOTLOG, BOTLOG_CHATID, extract_time, get_user_from_event

menu_category = "admin"

# =================== CONSTANT ===================
NO_ADMIN = "`I am not an admin nub nibba!`"
NO_PERM = "`I don't have sufficient permissions! This is so sed. Alexa play despacito`"


@legend.legend_cmd(
    pattern="tmute(?:\s|$)([\s\S]*)",
    command=("tmute", menu_category),
    info={
        "header": "To stop sending messages permission for that user",
        "description": "Temporary mutes the user for given time.",
        "Time units": {
            "s": "seconds",
            "m": "minutes",
            "h": "Hours",
            "d": "days",
            "w": "weeks",
        },
        "usage": [
            "{tr}tmute <userid/username/reply> <time>",
            "{tr}tmute <userid/username/reply> <time> <reason>",
        ],
        "examples": ["{tr}tmute 2d to test muting for 2 days"],
    },
    groups_only=True,
    require_admin=True,
)
async def tmuter(event):  # sourcery no-metrics
    "To mute a person for specific time"
    legendevent = await eor(event, "`muting....`")
    user, reason = await get_user_from_event(event, legendevent)
    if not user:
        return
    if not reason:
        return await legendevent.edit("you haven't mentioned time, check `.help tmute`")
    reason = reason.split(" ", 1)
    hmm = len(reason)
    swttime = reason[0].strip()
    reason = "".join(reason[1:]) if hmm > 1 else None
    ctime = await extract_time(legendevent, swttime)
    if not ctime:
        return
    if user.id == event.client.uid:
        return await legendevent.edit("Sorry, I can't mute myself")
    try:
        await legendevent.client(
            EditBannedRequest(
                event.chat_id,
                user.id,
                ChatBannedRights(until_date=ctime, send_messages=True),
            )
        )
        # Announce that the function is done
        if reason:
            await legendevent.edit(
                f"{_format.mentionuser(user.first_name ,user.id)} was muted in {get_display_name(await event.get_chat())}\n"
                f"**Muted for : **{swttime}\n"
                f"**Reason : **__{reason}__"
            )
            if BOTLOG:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "#TMUTE\n"
                    f"**User : **[{user.first_name}](tg://user?id={user.id})\n"
                    f"**Chat : **{get_display_name(await event.get_chat())}(`{event.chat_id}`)\n"
                    f"**Muted for : **`{swttime}`\n"
                    f"**Reason : **`{reason}``",
                )
        else:
            await legendevent.edit(
                f"{_format.mentionuser(user.first_name ,user.id)} was muted in {get_display_name(await event.get_chat())}\n"
                f"Muted for {swttime}\n"
            )
            if BOTLOG:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "#TMUTE\n"
                    f"**User : **[{user.first_name}](tg://user?id={user.id})\n"
                    f"**Chat : **{get_display_name(await event.get_chat())}(`{event.chat_id}`)\n"
                    f"**Muted for : **`{swttime}`",
                )
        # Announce to logging group
    except UserIdInvalidError:
        return await legendevent.edit("`Uh oh my mute logic broke!`")
    except UserAdminInvalidError:
        return await legendevent.edit(
            "`Either you're not an admin or you tried to mute an admin that you didn't promote`"
        )
    except Exception as e:
        return await legendevent.edit(f"`{e}`")


@legend.legend_cmd(
    pattern="tban(?:\s|$)([\s\S]*)",
    command=("tban", menu_category),
    info={
        "header": "To remove a user from the group for specified time.",
        "description": "Temporary bans the user for given time.",
        "Time units": {
            "s": "seconds",
            "m": "minutes",
            "h": "Hours",
            "d": "days",
            "w": "weeks",
        },
        "usage": [
            "{tr}tban <userid/username/reply> <time>",
            "{tr}tban <userid/username/reply> <time> <reason>",
        ],
        "examples": ["{tr}tban 2d to test baning for 2 days"],
    },
    groups_only=True,
    require_admin=True,
)
async def tban(event):  # sourcery no-metrics
    "To ban a person for specific time"
    legendevent = await eor(event, "`banning....`")
    user, reason = await get_user_from_event(event, legendevent)
    if not user:
        return
    if not reason:
        return await legendevent.edit("you haven't mentioned time, check `.help tban`")
    reason = reason.split(" ", 1)
    hmm = len(reason)
    swttime = reason[0].strip()
    reason = "".join(reason[1:]) if hmm > 1 else None
    ctime = await extract_time(legendevent, swttime)
    if not ctime:
        return
    if user.id == event.client.uid:
        return await legendevent.edit("Sorry, I can't ban myself")
    await legendevent.edit("`Whacking the pest!`")
    try:
        await event.client(
            EditBannedRequest(
                event.chat_id,
                user.id,
                ChatBannedRights(until_date=ctime, view_messages=True),
            )
        )
    except UserAdminInvalidError:
        return await legendevent.edit(
            "`Either you're not an admin or you tried to ban an admin that you didn't promote`"
        )
    except BadRequestError:
        return await legendevent.edit(NO_PERM)
    # Helps ban group join spammers more easily
    try:
        reply = await event.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        return await legendevent.edit(
            "`I dont have message nuking rights! But still he was banned!`"
        )
    # Delete message and then tell that the command
    # is done gracefully
    # Shout out the ID, so that fedadmins can fban later
    if reason:
        await legendevent.edit(
            f"{_format.mentionuser(user.first_name ,user.id)} was banned in {get_display_name(await event.get_chat())}\n"
            f"banned for {swttime}\n"
            f"Reason:`{reason}`"
        )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#TBAN\n"
                f"**User : **[{user.first_name}](tg://user?id={user.id})\n"
                f"**Chat : **{get_display_name(await event.get_chat())}(`{event.chat_id}`)\n"
                f"**Banned untill : **`{swttime}`\n"
                f"**Reason : **__{reason}__",
            )
    else:
        await legendevent.edit(
            f"{_format.mentionuser(user.first_name ,user.id)} was banned in {get_display_name(await event.get_chat())}\n"
            f"banned for {swttime}\n"
        )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#TBAN\n"
                f"**User : **[{user.first_name}](tg://user?id={user.id})\n"
                f"**Chat : **{get_display_name(await event.get_chat())}(`{event.chat_id}`)\n"
                f"**Banned untill : **`{swttime}`",
            )
