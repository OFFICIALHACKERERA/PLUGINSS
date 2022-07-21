import asyncio
import json

# credit To LegendBoy
import requests
from telethon.utils import get_display_name

from Deepak import legend

from ..core.managers import eod, eor
from ..sql_helper.schatbot_sql import (
    saddecho,
    sget_all_echos,
    sget_echos,
    sis_echo,
    sremove_all_echos,
    sremove_echo,
    sremove_echos,
)
from . import get_user_from_event

menu_category = "fun"


@legend.legend_cmd(
    pattern="addai$",
    command=("addai", menu_category),
    info={
        "header": "To Start ChatBot.",
        "description": "Reply to user with this cmd so from then his every text and sticker it will reply With Ai Answer messages will be repeated back to him.",
        "usage": "{tr}addai <reply>",
    },
)
async def echo(event):
    "To start chatbot to the user messages by legendboy"
    if event.reply_to_msg_id is None:
        return await eor(event, "`Reply to a User's message to echo his messages`")
    legendevent = await eor(event, "`See Magic`")
    user, rank = await get_user_from_event(event, legendevent, nogroup=True)
    if not user:
        return
    reply_msg = await event.get_reply_message()
    chat_id = event.chat_id
    user_id = reply_msg.sender_id
    if event.is_private:
        chat_name = user.first_name
        chat_type = "Personal"
    else:
        chat_name = get_display_name(await event.get_chat())
        chat_type = "Group"
    user_name = user.first_name
    user_username = user.username
    if sis_echo(chat_id, user_id):
        return await eor(event, "The user is already enabled with Chatbot ")
    try:
        saddecho(chat_id, user_id, chat_name, user_name, user_username, chat_type)
    except Exception as e:
        await eod(legendevent, f"**Error:**\n`{e}`")
    else:
        await eor(legendevent, "Hi")


@legend.legend_cmd(
    pattern="rmai$",
    command=("rmai", menu_category),
    info={
        "header": "To stop repeating paticular user messages.",
        "description": "Reply to user with this cmd to stop repeating his messages back.",
        "usage": "{tr}rmai <reply>",
    },
)
async def echo(event):
    "To stop chatbot the user messages"
    if event.reply_to_msg_id is None:
        return await eor(event, "Reply to a User's message to echo his messages")
    reply_msg = await event.get_reply_message()
    user_id = reply_msg.sender_id
    chat_id = event.chat_id
    if sis_echo(chat_id, user_id):
        try:
            sremove_echo(chat_id, user_id)
        except Exception as e:
            await eod(legendevent, f"**Error:**\n`{e}`")
        else:
            await eor(event, "Ai Chat has been stopped for the user")
    else:
        await eor(event, "The user is not activated with Ai Chat")


@legend.legend_cmd(
    pattern="delai( -a)?",
    command=("delai", menu_category),
    info={
        "header": "To delete echo in this chat.",
        "description": "To stop Chatbot users messages of all enabled users in the paticular chat or all chats.",
        "flags": {"a": "To stop in all chats"},
        "usage": [
            "{tr}delai",
            "{tr}delai -a",
        ],
    },
)
async def chatbot(event):
    "To delete chatbot in this chat."
    input_str = event.pattern_match.group(1)
    if input_str:
        lecho = sget_all_echos()
        if len(lecho) == 0:
            return await eod(
                event, "You havent enabled chatbot atleast for one user in any chat."
            )
        try:
            sremove_all_echos()
        except Exception as e:
            await eod(event, f"**Error:**\n`{str(e)}`", 10)
        else:
            await eor(event, "Deleted chatbot for all enabled users in all chats.")
    else:
        lecho = sget_echos(event.chat_id)
        if len(lecho) == 0:
            return await eod(
                event, "You havent enabled echo atleast for one user in this chat."
            )
        try:
            sremove_echos(event.chat_id)
        except Exception as e:
            await eod(event, f"**Error:**\n`{e}`", 10)
        else:
            await eor(event, "Deleted chatbot for all enabled users in this chat")


@legend.legend_cmd(
    pattern="listai( -a)?$",
    command=("listai", menu_category),
    info={
        "header": "shows the list of users for whom you enabled chatbot",
        "flags": {
            "a": "To list chatbot users in all chats",
        },
        "usage": [
            "{tr}listai",
            "{tr}listai -a",
        ],
    },
)
async def echo(event):  # sourcery no-metrics
    "To list all users on who you enabled chatbot."
    input_str = event.pattern_match.group(1)
    private_chats = ""
    output_str = "**Chatbot enabled users:**\n\n"
    if input_str:
        lsts = sget_all_echos()
        group_chats = ""
        if len(lsts) <= 0:
            return await eor(event, "There are no chatbot enabled users")
        for chatbot in lsts:
            if chatbot.chat_type == "Personal":
                if chatbot.user_username:
                    private_chats += f"✓ [{chatbot.user_name}](https://t.me/{chatbot.user_username})\n"
                else:
                    private_chats += (
                        f"✓ [{chatbot.user_name}](tg://user?id={chatbot.user_id})\n"
                    )
            elif chatbot.user_username:
                group_chats += f"✓ [{chatbot.user_name}](https://t.me/{chatbot.user_username}) in chat {chatbot.chat_name} of chat id `{chatbot.chat_id}`\n"
            else:
                group_chats += f"✓ [{chatbot.user_name}](tg://user?id={chatbot.user_id}) in chat {chatbot.chat_name} of chat id `{chatbot.chat_id}`\n"

        if private_chats != "":
            output_str += "**Private Chats**\n" + private_chats + "\n\n"
        if group_chats != "":
            output_str += "**Group Chats**\n" + group_chats
    else:
        lsts = sget_echos(event.chat_id)
        if len(lsts) <= 0:
            return await eor(event, "There are no chatbot enabled users in this chat")

        for chatbots in lsts:
            if echos.user_username:
                private_chats += (
                    f"✓ [{chatbots.user_name}](https://t.me/{chatbots.user_username})\n"
                )
            else:
                private_chats += (
                    f"✓ [{chatbots.user_name}](tg://user?id={chatbots.user_id})\n"
                )
        output_str = "**Chatbot enabled users in this chat are:**\n" + private_chats

    await eor(event, output_str)


@legend.legend_cmd(incoming=True, edited=False)
async def sareply(event):
    if sis_echo(event.chat_id, event.sender_id) and (
        event.message.text or event.message.sticker
    ):
        loll = event.text
        sweetie = loll.replace(" ", "%20")
        url = f"https://kukiapi.xyz/api/apikey=1356469075-KUKIkq4WMg5FV4/LegendBoyAssistance/LegendBoy/message={sweetie}"
        request = requests.get(url)
        results = json.loads(request.text)
        boyresult = f"{results['reply']}"
        # await event.reply(boyresult)
        async with event.client.action(event.chat_id, "typing"):
            await asyncio.sleep(0.5)
        async with event.client.action(event.chat_id, "typing"):
            await event.client.send_message(
                entity=event.chat_id,
                message="""{}""".format(boyresult),
                reply_to=event.message.id,
            )
