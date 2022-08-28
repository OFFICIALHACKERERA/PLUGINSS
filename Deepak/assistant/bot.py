import os

from telethon import Button, events

from Deepak import bot

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/5edf1b910c71e385e5d57.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@Timesisnotwaiting"
)

CAPTION = f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{ALIVE}』"


@bot.on(events.NewMessage(pattern="^/p"))
async def _(event):
    UMM = [[Button.url("⚜ Cԋαɳɳҽʅ ⚜", "https://t.me/TheUpdatesChannel")]]
    await bot.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)





@bot.on(events.NewMessage(pattern="^[/?!]end"))
async def vc_end(event, perm):
    chat_id = event.chat_id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await event.reply("**Streaming Ended**")
        except Exception as e:
            await event.reply(f"**ERROR:** `{e}`")
    else:
        await event.reply("**Ntg is Streaming**")
