from telethon.tl.types import ChannelParticipantsAdmins

from userbot import legend

from ..helpers.utils import get_user_from_event, reply_id

menu_category = "extra"


@legend.legend_cmd(
    pattern="(tagall|all)(?:\s|$)([\s\S]*)",
    command=("tagall", menu_category),
    info={
        "header": "tags recent 100 persons in the group may not work for all",
        "usage": [
            "{tr}all <text>",
            "{tr}tagall",
        ],
    },
)
async def tagall(event):
    "To tag all."
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(2)
    mentions = input_str or "@all"
    chat = await event.get_input_chat()
    async for x in event.client.iter_participants(chat, 100):
        mentions += f" \n♦️ [{x.first_name}](tg://user?id={x.id})"  # [\u2063]
    await event.client.send_message(event.chat_id, mentions, reply_to=reply_to_id)
    await event.delete()


@legend.legend_cmd(
    pattern="(luckydraw|ld)(?:\s|$)([\s\S]*)",
    command=("luckydraw", menu_category),
    info={
        "header": "To Get Luckydraw in group",
        "usage": [
            "{tr}ld",
            "{tr}luckydraw",
        ],
    },
)
async def luckydraw(event):
    "To Select 2 Luckydraw Person."
    reply_to_id = await reply_id(event)
    event.pattern_match.group(2)
    mentions = "💝 **Our Lucky Draw Person Name** 💝"
    chat = await event.get_input_chat()
    async for x in event.client.iter_participants(chat, 2):
        mentions += f"\n☞ [{x.first_name}](tg://user?id={x.id})"  # [\u2063]
    await event.client.send_file(
        event.chat_id,
        "https://telegra.ph/file/071765255640f7c40c506.jpg",
        caption=mentions,
        reply_to=reply_to_id,
    )
    await event.delete()


@legend.legend_cmd(
    pattern="report$",
    command=("report", menu_category),
    info={
        "header": "To tags admins in group.",
        "usage": "{tr}report",
    },
)
async def report(event):
    "To tags admins in group."
    mentions = "@admin: **Spam Spotted**"
    chat = await event.get_input_chat()
    reply_to_id = await reply_id(event)
    async for x in event.client.iter_participants(
        chat, filter=ChannelParticipantsAdmins
    ):
        if not x.bot:
            mentions += f"[\u2063](tg://user?id={x.id})"
    await event.client.send_message(event.chat_id, mentions, reply_to=reply_to_id)
    await event.delete()


@legend.legend_cmd(
    pattern="men ([\s\S]*)",
    command=("mention", menu_category),
    info={
        "header": "Tags that person with the given custom text.",
        "usage": [
            "{tr}men username/userid text",
            "text (username/mention)[custom text] text",
        ],
        "examples": ["{tr}men @LegendBoy_XD hi", "Hi @LegendBoy_XD[How are you?]"],
    },
)
async def mention(event):
    "Tags that person with the given custom text."
    user, input_str = await get_user_from_event(event)
    if not user:
        return
    reply_to_id = await reply_id(event)
    await event.delete()
    await event.client.send_message(
        event.chat_id,
        f"<a href='tg://user?id={user.id}'>{input_str}</a>",
        parse_mode="HTML",
        reply_to=reply_to_id,
    )
