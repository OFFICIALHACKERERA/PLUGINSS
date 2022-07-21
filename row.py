from userbot import legend

from ..core.managers import eor

menu_category = "useless"


@legend.legend_cmd(
    pattern="row(?: |$)([\s\S]*)",
    command=("row", menu_category),
    info={
        "header": "It help u to get button text and data of that reply button.",
        "note": "U Must Have to reply to a button to get this module work.",
        "usage": [
            "{tr}row <row> ; <button> <reply to button>",
        ],
    },
)
async def button(event):
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        a = (await event.get_reply_message()).reply_markup
        if ";" in input_str:
            tol, sk = input_str.split(";")
            olo = 1 - int(tol)
            text = 1 - int(sk)
        else:
            await eor(event, "Check Syntax Of this cmd")
        try:
            b = a.rows[olo].buttons[text].text
            c = a.rows[olo].buttons[text].url
            sweetie = f"👩‍💻 **Text** : `{b}`\n✓ **URL** :`{c}`"
            await eor(event, sweetie)
        except Exception as e:
            await eor(event, f"Use Proper Synatx \n {e}")
    else:
        await eor(event, "Check information of this cmd")
