from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from Deepak import legend

from ..core.logger import logging
from ..core.managers import eod, eor

LOGS = logging.getLogger(__name__)

menu_category = "utils"


async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call))
    return xx.call





def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


@legend.legend_cmd(
    pattern="invitevc$",
    command=("invitevc", menu_category),
    info={
        "header": "Invite All The Latest Online Member To Vc",
        "description": "This Cmd  Is Used To Invite All Members Of Group In Voice Call",
        "usage": [
            "{tr}invitevc",
        ],
    },
    groups_only=True,
)
async def vcinvite(e):
    "Invite All The Latest Online Member To Vc"
    ok = await eor(e, "`Inviting Members to Voice Chat...`")
    users = []
    z = 0
    async for x in e.client.iter_participants(e.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await e.client(invitetovc(call=await get_call(e), users=p))
            z += 6
        except BaseException:
            pass
    await ok.edit(f"`Invited {z} users`")


@legend.legend_cmd(
    pattern="stopvc$",
    command=("stopvc", menu_category),
    info={
        "header": "To Stop Vc",
        "description": "Use this cmd to stop voice call of the  Group",
        "usage": [
            "{tr}stopvc",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def stopvc(e):
    "To Stop Vc"
    try:
        await e.client(stopvc(await get_call(e)))
        await eor(e, "`Voice Chat Stopped Successfully...`")
    except Exception as ex:
        await eor(e, f"`{str(ex)}`")


@legend.legend_cmd(
    pattern="startvc$",
    command=("startvc", menu_category),
    info={
        "header": "To start vc of the group",
        "description": "To start the voice call of group",
        "usage": [
            "{tr}startvc",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def startvc(e):
    "To start vc of the group"
    try:
        await e.client(startvc(e.chat_id))
        await eor(e, "`Voice Chat Started Successfully...`")
    except Exception as ex:
        await eor(e, f"`{str(ex)}`")


@legend.legend_cmd(
    pattern="vctitle(?:\s|$)([\s\S]*)",
    command=("vctitle", menu_category),
    info={
        "header": "To start vc of the group",
        "description": "To start the voice call of group",
        "usage": [
            "{tr}vctitle",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def vctitle(e):
    title = e.pattern_match.group(1)
    if not title:
        return await eod(e, "Send Me Text of Title")
    try:
        await e.client(settitle(call=await get_call(e), title=title.strip()))
        await eod(e, f"Done Voice call title changed to {title}")
    except Exception as ex:
        await eor(f"`{ex}`")
