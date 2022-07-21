from telegraph import Telegraph
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions

from .. import legend
from ..core.managers import eod, eor

telegraph = Telegraph()
mee = telegraph.create_account(short_name="yohohehe")


menu_category = "tools"


@legend.legend_cmd(
    pattern="recognize(?:\s|$)([\s\S]*)",
    command=("recognize", menu_category),
    info={
        "header": "to recognize the img।",
        "description": "suppose u have to find text in img. Then use this cmd as pic. do with the answer of",
        "usage": [
            "{tr}recognize <reply to pic>",
        ],
        "examples": "{tr}recognize <reply to pic>",
    },
)
async def _(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to any user's media file")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("reply to media file")
        return
    chat = "@Rekognition_Bot"
    if reply_message.sender.bot:
        await event.edit("Reply to real user message।")
        return
    await event.edit("Recognizing this media.")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461083923)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.client(functions.contacts.UnblockRequest("@Rekognition_Bot"))
            await eod("successfully unlocked try again now")
            return
        if response.text.startswith("see next message"):
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461083923)
            )
            response = await response
            oye = response.message.message
            await eod(oye)
            return
        else:
            await eod("sorry, I couldnt find it")


@legend.legend_cmd(
    pattern="history(?:\s|$)([\s\S]*)",
    command=("history", menu_category),
    info={
        "header": "To get history of any user।",
        "description": "If username changes then it is best to use cmd to get history of any user,",
        "usage": [
            "{tr}history <reply to user>",
        ],
    },
)
async def _(event):
    if not event.reply_to_msg_id:
        await eod(event, "`Please Reply To A User To Get This Module Work`")
        return
    reply_message = await event.get_reply_message()
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
        await eod(event, "Real users are required. no boats")
        return
    lol = await eor(event, "Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            first = await conv.send_message(f"/search_id {victim}")
            response1 = await conv.get_response()
            response2 = await conv.get_response()
        except YouBlockedUserError:
            await event.client(functions.contacts.UnblockRequest("@Sangmatainfo_bot"))
            await eod(event, "Done unblocked @Sangmatainfo_bot Try again now")
            return
        if response1.text.startswith("Name History"):
            await lol.edit(response1.text)
            await event.client.delete_messages(
                conv.chat_id, [first.id, response1.id, response2.id]
            )
        elif response2.text.startswith("Name History"):
            await lol.edit(response2.text)
            await event.client.delete_messages(
                conv.chat_id, [first.id, response1.id, response2.id]
            )
        else:
            await lol.edit("No Records Found !")


@legend.legend_cmd(
    pattern="uhistory(?:\s|$)([\s\S]*)",
    command=("uhistory", menu_category),
    info={
        "header": "To Get History Of Username Of Any User.",
        "usage": "{tr}uhistory reply to message",
    },
)
async def _(event):
    if not event.reply_to_msg_id:
        await eod(
            event,
            "`Please reply to a user to get this CMD working`",
        )
        return
    reply_message = await event.get_reply_message()
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
        await eod(event, "Need actual users. Not Bots")
        return
    lol = await eor(event, "Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            first = await conv.send_message(f"/search_id {victim}")
            response1 = await conv.get_response()
            response2 = await conv.get_response()
            response3 = await conv.get_response()
        except YouBlockedUserError:
            await event.client(functions.contacts.UnblockRequest("@Sangmatainfo_bot"))
            await eod(event, "Unblocked @Sangmatainfo_bot and try again now")
            return
        if response1.text.startswith("Username History"):
            await lol.edit(response1.text)
            await event.client.delete_messages(
                conv.chat_id, [first.id, response1.id, response2.id, response3.id]
            )
        elif response2.text.startswith("Username History"):
            await lol.edit(response2.text)
            await event.client.delete_messages(
                conv.chat_id, [first.id, response1.id, response2.id, response3.id]
            )
        else:
            await lol.edit("No Records Found !")


@legend.legend_cmd(
    pattern="limit(?:\s|$)([\s\S]*)",
    command=("limit", menu_category),
    info={
        "header": "Whether your account is limited to receive",
        "description": "If your account is limited then you cannot DM anyone till ur limited open this bot help. To find out if your account is limited.",
        "usage": [
            "{tr}limit",
        ],
    },
)
async def _(event):
    bot = "@SpamBot"
    await eor(event, "Processing....")
    async with event.client.conversation(bot) as conv:
        try:
            first = await conv.send_message("/start")
            yup = await conv.get_response()
            sweetie = yup.text
            if sweetie.startswith("Good"):
                response = await conv.send_message("Cool, thanks")
                await eor(event, "Congratulations, there is no limit")
                await event.client.delete_messages(
                    conv.chat_id, [first.id, yup.id, response.id]
                )
            elif "automatically" in sweetie:
                await conv.send_message("I was wrong, please release me now")
                await eor(
                    event, f"Your account is limited [click here](https://t.me/spambot)"
                )
            else:
                await eor(event, sweetie)
        except YouBlockedUserError:
            await event.client(functions.contacts.UnblockRequest("@spambot"))
            await eor(event, "**Done unblocked @spambot and try again now**")
            return
