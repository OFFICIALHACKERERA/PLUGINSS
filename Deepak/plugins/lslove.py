from Deepak import legend

from . import mention

menu_category = "fun"

import asyncio
import random

NUMBER = ["0", "1"]

MEDHU = [
    "HATE ME I DONT CARE",
    "LEAVE ME I DONT CARE",
    "EK TU H TU H RHYGII",
    "TERE BIN MAR JAUNGA",
    "TU MERI H SMJI?",
    "KOI TERE MERE BEECH AYA MARDUNGA OSE",
    "TERE LIYE MAR B SKTA HU MAR B SKTA HU",
    "TERE SE JITNA MRJI GUSSA HO JAUN BUT I LOVE U YARR",
    "TERE LIE IS DUNIA SE LAD JAUNGA",
    "ANKO SE ANKHE MILAKE KHWAB CHURA LU TERE",
    "TERA ISHQ PANE LIE KITNE BETAN HU KESE BATAU TUJE",
    "ME JO JEE RHA HU WAJH TUM HO",
    "TU H TO M HU TUJSE M HU",
    "TUJE KITNA CHAHNE LAGE HAM KI SHBO M BYAN NA KAR PAYNGE",
    "CURRENT STATUS  I WANT TO HUG YOU AND WANAA CARRY LOUD",
    "I NEED YOU IN MY BAD IN MY GOOD",
    "HMESHA TERE SATH HU",
    "TERE SE KADM SE KDM MILAKE CHALNA CHHTA HU",
    "TUJE APNI SHOTI SI DUNIA KA EK BHT BADA HISA BANANA CHAHTA HU",
    "KYA JANE TU MERE IRADHE LE JAUNGA TERI SANSE CHURAKE",
    "DIL KHE RHA KI GUNHGAGAR BAN JA BADA SKOON H IN GUNAHO M",
    "MERI KHUSHNMA SUBH H TU",
    "MERI JAAN H TU",
    "EVEN TUJE IDEA B NHI H KI TERE EK SINGLE MESSAGE KA WAIT KRTE KRTE KITAN ROYA HU",
    "TUJE PANE LIE BHT TDFA HU",
    "KABI KABI LGTA H KI TUN MUJSE NHT DUR JA RHI H",
    "I DONT CARE ABOUT WORD BS I NEED YOU",
    "TUN BAS MERI H MERI RHNA",
    "BHT ROTA HU TERE LIE AKELA ME",
    "H YE NSHA YAN H JEHAR IS PYAR KO KYA NAM DU",
    "HMARE PYAR KI H YE ADHURI DASTA KI TUN PASS HOKE B BHT DOOR H",
    "PLZZ KABI MAT SHODNA MUJE I CANT LIVE WITHOUT YOU",
    "DO JISM H BUT EK JAAN H HAM DO",
    "MUJE BAS TU CHHIE NAHI PTA KYU BUT CHHIE TU H",
    "THERE ARE MANY PEOPLE IN WORLD BUT I ONLY NEED YOU",
    "WO TERA GUSSA HONA JHGDE KRNE I MISS YOU",
    "BHT PYAR KRTA HU TERE SE PLZZ DONT LEAVE ME",
]

que = {}


@legend.legend_cmd(incoming=True, edited=False)
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(MEDHU)),
            reply_to=event.message.id,
        )


@legend.legend_cmd(
    pattern="lslovee$",
    command=("lslovee", menu_category),
    info={
        "header": "To Activate Automatically Send Love Type messages",
        "description": "Reply to user with this cmd so from then his every text reply with some random love type message.",
        "usage": "{tr}lslove <reply>",
    },
)
async def _(event):
    global que
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await eor(event, "TUJE KITNA CHAANE LAGE HUM....")
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"TERE BIN NHI RH SKTA ME {mention}")
    else:
        user = event.pattern_match.group(1)
        event = await eor(event, "LOVE U YAR PLZZ BAN JA MERI JAAN....")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"EK TU H MERI M KYA DUNIA TO LENA. {ALIVE_NAME}")


@legend.legend_cmd(
    pattern="nofeelings$",
    command=("nofeelings", menu_category),
    info={
        "header": "To stop sending lslove paticular user messages.",
        "description": "Reply to user with this cmd to stop sending lslove",
        "usage": "{tr}nofeelings <reply>",
    },
)
async def _(event):
    global que
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await eor(event, "I KNOW U DONT LOVE ME....")
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"TUJE KITNA CHTA HU KABI BTAYA H NHI")
    else:
        user = event.pattern_match.group(1)
        event = await eor(event, "Reply Raid De-activating....")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"TUJE KHONE KE DAR SE KABI PAYA H NAHI {mention}")


@legend.legend_cmd(
    pattern="lsmarry$",
    command=("lsmarry", menu_category),
    info={
        "header": "Try With Yourself",
        "usage": "{tr}lsmarry <reply>",
    },
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("I")
        await asyncio.sleep(0.7)
        await event.edit("LOVE")
        await asyncio.sleep(1)
        await event.edit("YOU")
        await asyncio.sleep(0.8)
        await event.edit("MY ")
        await asyncio.sleep(0.9)
        await event.edit("JAAN")
        await asyncio.sleep(1)
        await event.edit("WILL")
        await asyncio.sleep(0.8)
        await event.edit("YOU")
        await asyncio.sleep(0.7)
        await event.edit("MAARY ME IN FUTURE")
        await asyncio.sleep(0.9)
        await event.edit("I CAN DO ANYTHING FOR YOU")
        await asyncio.sleep(0.8)
        await event.edit("MARRY ME I WILL FILL YOUR EVERYDAY WITH HAPPYNESS")
        await event.edit(
            "I LOVE YOU MY JAAN WILL U MARRY ME IN FUTURE I CAN DO ANYTHING FOR YOU MARRY ME I WILL FILL YOUR EVERYDAY WITH HAPPYNESS 😍💍"
        )


@legend.legend_cmd(
    pattern="lsnehi$",
    command=("lsnehi", menu_category),
    info={
        "header": "Try With Yourself",
        "usage": "{tr}lsnehi <reply>",
    },
)
async def _(event):
    await event.edit("AB DRAME NA KAR I LOVE YOU TOO BOL DAL❤️")
    await asyncio.sleep(50)
