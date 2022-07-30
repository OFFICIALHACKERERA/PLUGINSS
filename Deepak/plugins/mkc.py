import asyncio



@legend.legend_cmd(
    pattern="^Mkc$",
    command=("^Mkc$", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}Mkc",
    },
)
async def viello(event):
    "fun art command"
    reply_to_id = await reply_id(event)
    event = await eor(event, "**(❛ HI ❜!**")
    HELL_PIC = "https://telegra.ph/file/d199f6089ac8b014afc09.jpg"
    if HELL_PIC:         
        on = await event.client.send_file(
            event.chat_id, file=HELL_PIC, caption=Mkc, reply_to=reply_to_id
        )
        await asyncio.sleep(3)
        await event.client.edit_message(event.chat_id,file=HELL_PIC)
        await event.delete()
