from telethon.tl import functions

from .. import legend
from ..Config import Config
from ..core.managers import eod, eor
from ..utils.tools import create_supergroup

menu_category = "tools"


@legend.legend_cmd(
    pattern="create (b|g|c) ([\s\S]*)",
    command=("create", menu_category),
    info={
        "header": "To create a private group/channel with Deepak.",
        "description": "Use this cmd to create super group , normal group or channel.",
        "flags": {
            "b": "to create a private super group",
            "g": "To create a private basic group.",
            "c": "to create a private channel",
        },
        "usage": "{tr}create (b|g|c) <name of group/channel>",
        "examples": "{tr}create b LegendDeepak",
    },
)
async def _(event):
    "To create a private group/channel with Deepak"
    type_of_group = event.pattern_match.group(1)
    group_name = event.pattern_match.group(2)
    if type_of_group == "c":
        descript = "This is a Test Channel created using LegendDeepak"
    else:
        descript = "This is a Test Group created using LegendDeepak"
    if type_of_group == "g":
        try:
            result = await event.client(
                functions.messages.CreateChatRequest(
                    users=[Config.BOT_USERNAME],
                    # Not enough users (to create a chat, for example)
                    # Telegram, no longer allows creating a chat with ourselves
                    title=group_name,
                )
            )
            created_chat_id = result.chats[0].id
            result = await event.client(
                functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                )
            )
            await eor(
                event, f"Group `{group_name}` created successfully. Join {result.link}"
            )
        except Exception as e:
            await eod(event, f"**Error:**\n{str(e)}")
    elif type_of_group == "c":
        try:
            r = await event.client(
                functions.channels.CreateChannelRequest(
                    title=group_name,
                    about=descript,
                    megagroup=False,
                )
            )
            created_chat_id = r.chats[0].id
            result = await event.client(
                functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                )
            )
            await eor(
                event,
                f"Channel `{group_name}` created successfully. Join {result.link}",
            )
        except Exception as e:
            await eod(event, f"**Error:**\n{e}")
    elif type_of_group == "b":
        answer = await create_supergroup(
            group_name, event.client, Config.BOT_USERNAME, descript
        )
        if answer[0] != "error":
            await eor(
                event,
                f"Mega group `{group_name}` created successfully. Join {answer[0].link}",
            )
        else:
            await eod(event, f"**Error:**\n{answer[1]}")
    else:
        await eod(event, "Read `.help create` to know how to use me")
