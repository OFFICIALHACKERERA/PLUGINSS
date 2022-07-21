import asyncio
from random import choice, randint

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins, ChatAdminRights

from userbot import legend

from ..core.managers import eod, eor
from ..helpers.utils import get_user_from_event
from . import ALIVE_NAME

menu_category = "fun"


@legend.legend_cmd(
    pattern="scam(?:\s|$)([\s\S]*)",
    command=("scam", menu_category),
    info={
        "header": "To show fake actions for a paticular period of time",
        "description": "if time is not mentioned then it may choose random time 5 or 6 mintues for mentioning time use in seconds",
        "usage": [
            "{tr}scam <action> <time(in seconds)>",
            "{tr}scam <action>",
            "{tr}scam",
        ],
        "examples": "{tr}scam photo 300",
        "actions": [
            "typing",
            "contact",
            "game",
            "location",
            "voice",
            "round",
            "video",
            "photo",
            "document",
        ],
    },
)
async def _(event):
    options = [
        "typing",
        "contact",
        "game",
        "location",
        "voice",
        "round",
        "video",
        "photo",
        "document",
    ]
    input_str = event.pattern_match.group(1)
    args = input_str.split()
    if len(args) == 0:
        scam_action = choice(options)
        scam_time = randint(300, 360)
    elif len(args) == 1:
        try:
            scam_action = str(args[0]).lower()
            scam_time = randint(300, 360)
        except ValueError:
            scam_action = choice(options)
            scam_time = int(args[0])
    elif len(args) == 2:
        try:
            scam_action = str(args[0]).lower()
            scam_time = int(args[1])
        except ValueError:
            return await eod(event, "`Invalid Syntax !!`")
    else:
        return await eod(event, "`Invalid Syntax !!`")
    try:
        if scam_time > 0:
            await event.delete()
            async with event.client.action(event.chat_id, scam_action):
                await asyncio.sleep(scam_time)
    except BaseException:
        return


@legend.legend_cmd(
    pattern="prankpromote(?:\s|$)([\s\S]*)",
    command=("prankpromote", menu_category),
    info={
        "header": "To promote a person without admin rights",
        "note": "You need proper rights for this",
        "usage": [
            "{tr}prankpromote <userid/username/reply>",
            "{tr}prankpromote <userid/username/reply> <custom title>",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def _(event):
    "To promote a person without admin rights"
    new_rights = ChatAdminRights(post_messages=True)
    legendevent = await eor(event, "`Promoting...`")
    user, rank = await get_user_from_event(event, legendevent)
    if not rank:
        rank = "Admin"
    if not user:
        return
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, new_rights, rank))
    except BadRequestError:
        return await legendevent.edit(
            "__I think you don't have permission to promote__"
        )
    except Exception as e:
        return await eod(legendevent, f"__{e}__", time=10)
    await legendevent.edit("`Promoted Successfully! Now gib Party`")


@legend.legend_cmd(
    pattern="padmin$",
    command=("padmin", menu_category),
    info={
        "header": "Fun animation for faking user promotion",
        "description": "An animation that shows enabling all permissions to him that he is admin(fake promotion)",
        "usage": "{tr}padmin",
    },
    groups_only=True,
)
async def _(event):
    "Fun animation for faking user promotion."
    animation_interval = 1
    animation_ttl = range(20)
    event = await eor(event, "`promoting.......`")
    animation_chars = [
        "**Promoting User As Admin...**",
        "**Enabling All Permissions To User...**",
        "**(1) Send Messages: ☑️**",
        "**(1) Send Messages: ✅**",
        "**(2) Send Media: ☑️**",
        "**(2) Send Media: ✅**",
        "**(3) Send Stickers & GIFs: ☑️**",
        "**(3) Send Stickers & GIFs: ✅**",
        "**(4) Send Polls: ☑️**",
        "**(4) Send Polls: ✅**",
        "**(5) Embed Links: ☑️**",
        "**(5) Embed Links: ✅**",
        "**(6) Add Users: ☑️**",
        "**(6) Add Users: ✅**",
        "**(7) Pin Messages: ☑️**",
        "**(7) Pin Messages: ✅**",
        "**(8) Change Chat Info: ☑️**",
        "**(8) Change Chat Info: ✅**",
        "**Permission Granted Successfully**",
        f"**pRoMooTeD SuCcEsSfUlLy bY: {ALIVE_NAME}**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 20])


@legend.legend_cmd(
    pattern="fgben$",
    command=("fgben", menu_category),
    info={
        "header": "Fun animation for faking user Banned",
        "description": "An animation that shows Banning him that he is Getting ban ",
        "usage": "{tr}fgben",
    },
    groups_only=True,
)
async def gbun(event):
    if event.fwd_from:
        return
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    mentions = "`Warning!! User 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...\n`"
    no_reason = "__Reason: Madarchod Saala"
    await event.edit("** Nikal Lawde❗️⚜️☠️**")
    asyncio.sleep(3.5)
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(reply_message.sender_id)
        ).full_user
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.sender_id
        if idd == 5122474448:
            await reply_message.reply(
                "`Wait a second, This is my master!`\n**How dare you threaten to ban my master nigger!**\n\n__Your account has been hacked! Pay 99$ to my master__ [LegendBoy](https://t.me/LegendBoy_XD) __to release your account__😏"
            )
        else:
            jnl = (
                "`Warning!! `"
                "[{}](tg://user?id={})"
                "` 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...\n\n`"
                "**Person's Name: ** __{}__\n"
                "**ID : ** `{}`\n"
            ).format(firstname, idd, firstname, idd)
            if usname == None:
                jnl += "**Victim Nigga's username: ** `Doesn't own a username!`\n"
            elif usname != "None":
                jnl += "**Victim Nigga's username** : @{}\n".format(usname)
            if len(gbunVar) > 0:
                gbunm = "`{}`".format(gbunVar)
                gbunr = "**Reason: **" + gbunm
                jnl += gbunr
            else:
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention = "`Warning!! User 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...\nReason: Not Given `"
        await event.reply(mention)
    await event.delete()


@legend.legend_cmd(
    pattern="fgban$",
    command=("fgban", menu_category),
    info={
        "header": "Fun animation for fucking fake Gban",
        "description": "An animation that shows  globally Banning all in Group to him that he is gbanned(fake gban)",
        "usage": "{tr}fgben",
    },
    groups_only=True,
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Preparing to gban this nub nibba....")
        await asyncio.sleep(2)
        await event.edit("Gbanning user.....")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 1 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 5 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 10 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 15 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 20 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 25 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 30 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 35 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 40 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 45 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 50 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 55 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 60 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 65 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 70 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 75 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 80 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 85 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 90 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 95 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 100 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 105 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 110 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 115 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 120 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 125 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 130 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 135 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 140 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 145 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 150 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 155 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 160 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 165 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 170 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 175 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 180 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 185 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 190 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 200 chats")
        await asyncio.sleep(2)
        await event.edit("Gbanning user... \n 204 chats")
        await asyncio.sleep(1.5)
        await event.edit(
            "Gbanned this nub nibba successfully in😏: 204 chats.\nBlocked and added to gban watch!"
        )


@legend.legend_cmd(
    pattern="fungban$",
    command=("fungben", menu_category),
    info={
        "header": "Fun animation for fucking fake unGban",
        "description": "An animation that shows  globally UnBanning all in Group to him that he is ungbanned(fake ungban)",
        "usage": "{tr}fungben",
    },
    groups_only=True,
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "Preparing to Ungban this nub nibba please weit for a while....."
        )
        await asyncio.sleep(2)
        await event.edit("UnGbanning user.....")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 1 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 5 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 10 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 15 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 20 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 25 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 30 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 35 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 40 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 45 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 50 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 55 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 60 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 65 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 70 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 75 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 80 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 85 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 90 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 95 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 100 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 105 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 110 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 115 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 120 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 125 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 130 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 135 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 140 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 145 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 150 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 155 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 160 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 165 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 170 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 175 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 180 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 185 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 190 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 200 chats")
        await asyncio.sleep(2)
        await event.edit("UnGbanning user... \n 204 chats")
        await asyncio.sleep(1.5)
        await event.edit(
            "UnGbanned this nub nibba successfully in 204 chats.\nUnBlocked and removed from gban watch"
        )


@legend.legend_cmd(
    pattern="fmute$",
    command=("fmute", menu_category),
    info={
        "header": "A kind of fake gmute try it yourself",
        "description": "An animation that shows  globally Muted all in Group to him that he is gmutted(fake gmute)",
        "usage": "{tr}fmute",
    },
    groups_only=True,
)
async def gmute(event):
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    mentions = "**Warning!! User Gmuted By Admin...\n**"
    no_reason = "__Reason: ab sale Globally mute hi rah"
    await event.edit("** Gmutting...**")
    asyncio.sleep(2)
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(reply_message.sender_id)
        ).full_user
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.sender_id
        # make meself invulnerable cuz why not xD
        if idd == 5122474448:
            await reply_message.reply(
                "`Wait a second, This is my master!`\n**How dare you threaten to Mute my master nigger!**\n\n__Your account has been hacked! Pay 99$ to my master__ [LegendBoy](https://t.me/LegendBoy_XD) __to release your account__😏"
            )
        else:
            jnl = (
                "`Warning!! `"
                "[{}](tg://user?id={})"
                "` Gmutted By Admin...\n\n`"
                "**Name: ** __{}__\n"
                "**ID : ** `{}`\n"
            ).format(firstname, idd, firstname, idd)
            if usname == None:
                jnl += "**Victim Nigga's username: ** `Doesn't have a username!`\n"
            elif usname != "None":
                jnl += "**Victim Nigga's username** : @{}\n".format(usname)
            if len(gbunVar) > 0:
                gbunm = "`{}`".format(gbunVar)
                gbunr = "**Reason: **" + gbunm
                jnl += gbunr
            else:
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention = "**Warning!! User Gmutted By Admin...\nReason: Not Given **"
        await event.reply(mention)
    await event.delete()


@legend.legend_cmd(
    pattern="funmute$",
    command=("funmute", menu_category),
    info={
        "header": "A kind of fake ungmute try it yourself",
        "description": "An animation that shows  globally UnMuted all in Group to him that he is ungmutted(fake ungmute)",
        "usage": "{tr}fmute",
    },
    groups_only=True,
)
async def gbun(event):
    gbunVar = event.text
    gbunVar = gbunVar[8:]
    mentions = "**Warning!! User Unmuted By Admin...\n**"
    no_reason = "__Reason: Purani bat Bhool ja __ Wo pakar ke jhool jha__"
    await event.edit("**Ungmutting...**")
    asyncio.sleep(2)
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(reply_message.sender_id)
        ).full_user
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.sender_id
        # make meself invulnerable cuz why not xD
        if idd == 5122474448:
            await reply_message.reply(
                "Wait a second. Maine Gmute kab kiya Owner ko toh main unmute karu!!!"
            )
        else:
            jnl = (
                "`Warning!! `"
                "[{}](tg://user?id={})"
                "` Ungmutted By Admin...\n\n`"
                "**Name: ** __{}__\n"
                "**ID : ** `{}`\n"
            ).format(firstname, idd, firstname, idd)
            if usname == None:
                jnl += "**Victim Nigga's username: ** `Doesn't have a username!`\n"
            elif usname != "None":
                jnl += "**Victim Nigga's username** : @{}\n".format(usname)
            if len(gbunVar) > 0:
                gbunm = "`{}`".format(gbunVar)
                gbunr = "**Reason: **" + gbunm
                jnl += gbunr
            else:
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention = "**Warning!! User Gmutted By Admin...\nReason: Not Given **"
        await event.reply(mention)
    await event.delete()
