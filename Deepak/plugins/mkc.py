@legend.legend_cmd(
    pattern="^Hello$",
    command=("^Hello$", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}Hello",
    },
)
async def viello(event):
    "fun art command"
    reply_to_id = await reply_id(event)
    event = await eor(event, "**(❛ HI ❜!**")
    HELL_PIC = "https://telegra.ph/file/d199f6089ac8b014afc09.jpg"
    K_PIC = "https://telegra.ph/file/dd5689b532b4fa5ac70d4.jpg"
    L_PIC = "https://telegra.ph/file/cf7c2624f4b1a658b7dbc.jpg"
    M_PIC = "https://telegra.ph/file/daf4f760b650632050353.jpg"
    if HELL_PIC:
        HELLO =  f"•♥•[ HELLO ]•♥•"            
        on = await event.client.send_file(
            event.chat_id, file=HELL_PIC, caption=HELLO, reply_to=reply_to_id
        )
        await asyncio.sleep(3)
        ok = await event.client.edit_message(event.chat_id, on, file=K_PIC)
        await asyncio.sleep(3)
        ok1 = await event.client.edit_message(event.chat_id, on, file=L_PIC)
        await asyncio.sleep(3)
        ok2 = await event.client.edit_message(event.chat_id, ok1, file=M_PIC)
        await asyncio.sleep(5)
        ok3 = await event.client.edit_message(event.chat_id, ok2, file=L_PIC)
        await asyncio.sleep(5)
        ok4 = await event.client.edit_message(event.chat_id, ok3, file=K_PIC)
        await asyncio.sleep(5)
        ok5 = await event.client.edit_message(event.chat_id, ok4, file=HELL_PIC)
        await event.delete()
