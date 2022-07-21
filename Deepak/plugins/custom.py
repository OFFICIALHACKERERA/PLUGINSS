from telegraph import upload_file
from validators.url import url

from userbot import legend
from userbot.core.logger import logging

from ..Config import Config
from ..core.managers import eod, eor
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG_CHATID

menu_category = "utils"
LOGS = logging.getLogger(__name__)
cmdhd = Config.HANDLER


vlist = [
    "ABUSE",
    "ABUSE_PIC",
    "ADMIN_PIC",
    "AFKFWD",
    "ALIVE_PIC",
    "ALIVE_EMOJI",
    "ALIVE_TEXT",
    "ALIVE_TEMPLATE",
    "ALLOW_NSFW",
    "CHANGE_TIME",
    "DEFAULT_BIO",
    "DEFAULT_NAME",
    "DEFAULT_PIC",
    "DEFAULT_USER",
    "DIGITAL_PIC",
    "FIRST_NAME",
    "HELP_EMOJI",
    "HELP_TEXT",
    "HELP_IMG",
    "IALIVE_PIC",
    "LAST_NAME",
    "PING_IMG",
    "PING_TEMPLATE",
    "PM_IMG",
    "PM_TEXT",
    "PM_BLOCK",
    "MAX_FLOOD_IN_PMS",
    "START_TEXT",
    "BOT_START_PIC",
    "COLUMNS_IN_HELP",
    "ROWS_IN_HELP",
    "CUSTOM_STICKER_PACKNAME",
    "CUSTOM_STICKER_SETNAME",
]

oldvars = {
    "PM_PIC": "pmpermit_pic",
    "PM_TEXT": "pmpermit_txt",
    "PM_BLOCK": "pmblock",
}


@legend.legend_cmd(
    pattern="(set|get|del)db(?: |$)([\s\S]*)",
    command=("db", menu_category),
    info={
        "header": "Set vars in database or Check or Delete",
        "description": "Set , Fetch or Delete values or vars directly in database without restart or heroku vars.\n\nYou can set multiple pics by giving space after links in alive, ialive, pm permit.",
        "flags": {
            "set": "To set new var in database or modify the old var",
            "get": "To show the already existing var value.",
            "del": "To delete the existing value",
        },
        "var name": "**[List of Database Vars]**",
        "usage": [
            "{tr}setdb <var name> <var value>",
            "{tr}getdb <var name>",
            "{tr}deldb <var name>",
        ],
        "examples": [
            "{tr}setdb ALIVE_PIC <pic link>",
            "{tr}setdb ALIVE_PIC <pic link 1> <pic link 2>",
            "{tr}getdb ALIVE_PIC",
            "{tr}deldb ALIVE_PIC",
        ],
    },
)
async def bad(event):  # sourcery no-metrics
    "To manage vars in database"
    cmd = event.pattern_match.group(1).lower()
    vname = event.pattern_match.group(2)
    vnlist = "".join(f"{i}. `{each}`\n" for i, each in enumerate(vlist, start=1))
    if not vname:
        return await eod(
            event, f"**📑 Give correct var name from the list :\n\n**{vnlist}", time=60
        )
    vinfo = None
    if " " in vname:
        vname, vinfo = vname.split(" ", 1)
    reply = await event.get_reply_message()
    if not vinfo and reply:
        vinfo = reply.text
    if vname in vlist:
        if vname in oldvars:
            vname = oldvars[vname]
        if cmd == "set":
            if vname == "DEFAULT_USER":
                if not vinfo or vinfo != "Me":
                    return await eod(
                        event,
                        "**To save your Current Profile info Set the value:**\\n `.setdv DEFAULT_USER Me`",
                    )

                USERINFO = await legend.get_entity(legebd.uid)
                FULL_USERINFO = (await legend(GetFullUserRequest(legend.uid))).full_user
                addgvar("FIRST_NAME", USERINFO.first_name)
                addgvar("DEFAULT_NAME", USERINFO.first_name)
                if USERINFO.last_name:
                    addgvar(
                        "DEFAULT_NAME",
                        f"{USERINFO.first_name}  {USERINFO.first_name}",
                    )
                    addgvar("LAST_NAME", USERINFO.last_name)
                elif gvarstatus("LAST_NAME"):
                    delgvar("LAST_NAME")
                if FULL_USERINFO.about:
                    addgvar("DEFAULT_BIO", FULL_USERINFO.about)
                elif gvarstatus("DEFAULT_BIO"):
                    delgvar("DEFAULT_BIO")
                try:
                    photos = await legend.get_profile_photos(legend.uid)
                    myphoto = await legend.download_media(photos[0])
                    myphoto_urls = upload_file(myphoto)
                    addgvar("DEFAULT_PIC", f"https://telegra.ph{myphoto_urls[0]}")
                except IndexError:
                    if gvarstatus("DEFAULT_PIC"):
                        delgvar("DEFAULT_PIC")
                usrln = gvarstatus("LAST_NAME") or None
                usrbio = gvarstatus("DEFAULT_BIO") or None
                usrphoto = gvarstatus("DEFAULT_PIC") or None
                vinfo = f'**Name:** `{gvarstatus("DEFAULT_NAME")}`\n**First Name:** `{gvarstatus("FIRST_NAME")}`\n**Last Name:** `{usrln}`\n**Bio:** `{usrbio}`\n**Photo:** `{usrphoto}`'
            else:
                if not vinfo and vname == "ALIVE_TEMPLATE":
                    return await eod(event, "Check @LegendBot_Alive")
                if not vinfo:
                    return await eod(
                        event,
                        f"Give some values which you want to save for **{vname}**",
                    )
                check = vinfo.split(" ")
                for i in check:
                    if vname == "DEFAULT_PIC" and not url(i):
                        return await eod(event, "**Give me a correct link...**")
                    elif vname == "DIGITAL_PIC" and not url(i):
                        return await eod(event, "**Give me a correct link...**")
                    elif (("PIC" in vname) or ("pic" in vname)) and not url(i):
                        return await eod(event, "**Give me a correct link...**")
                    elif (
                        vname == "DIGITAL_PIC"
                        or vname == "DEFAULT_PIC"
                        or vname == "BOT_START_PIC"
                    ) and url(i):
                        vinfo = i
                        break
                    elif not "PIC" in vname:
                        break
                if vname == "DEFAULT_BIO" and len(vinfo) > 70:
                    return await eor(
                        event,
                        f"No of characters in your bio must not exceed 70 so compress it and set again\n`{vinfo}`",
                    )
                addgvar(vname, vinfo)
            if BOTLOG_CHATID:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    f"#SET_DATAVAR\
                    \n**{vname}** is updated newly in database as below",
                )
                await event.client.send_message(BOTLOG_CHATID, vinfo, silent=True)
            await eod(
                event, f"📑 Value of **{vname}** is changed to :- `{vinfo}`", time=20
            )
        if cmd == "get":
            var_data = gvarstatus(vname)
            await eod(event, f"📑 Value of **{vname}** is  ```{var_data}```", time=20)
        elif cmd == "del":
            if vname == "DEFAULT_USER":
                delgvar("FIRST_NAME")
                delgvar("DEFAULT_NAME")
                if gvarstatus("LAST_NAME"):
                    delgvar("LAST_NAME")
                if gvarstatus("DEFAULT_BIO"):
                    delgvar("DEFAULT_BIO")
                if gvarstatus("DEFAULT_PIC"):
                    delgvar("DEFAULT_PIC")
            delgvar(vname)
            if BOTLOG_CHATID:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    f"#DEL_DATAVAR\
                    \n**{vname}** is deleted from database",
                )
            await eod(
                event,
                f"📑 Value of **{vname}** is now deleted & set to default.",
                time=20,
            )
    else:
        await eod(
            event, f"**📑 Give correct var name from the list :\n\n**{vnlist}", time=60
        )


@legend.legend_cmd(
    pattern="custom (pmpermit|pmblock|startmsg)$",
    command=("custom", menu_category),
    info={
        "header": "To customize your LegendUserBot.",
        "options": {
            "pmpermit": "To customize pmpermit text. ",
            "pmblock": "To customize pmpermit block message.",
            "startmsg": "To customize startmsg of bot when some one started it.",
        },
        "custom": {
            "{mention}": "mention user",
            "{first}": "first name of user",
            "{last}": "last name of user",
            "{fullname}": "fullname of user",
            "{username}": "username of user",
            "{userid}": "userid of user",
            "{my_first}": "your first name",
            "{my_last}": "your last name ",
            "{my_fullname}": "your fullname",
            "{my_username}": "your username",
            "{my_mention}": "your mention",
            "{totalwarns}": "totalwarns",
            "{warns}": "warns",
            "{remwarns}": "remaining warns",
        },
        "usage": "{tr}custom <option> reply",
        "NOTE": "You can set,fetch or delete these by `{tr}setdv` , `{tr}getdv` & `{tr}deldv` as well.",
    },
)
async def custom_LegendUserBot(event):
    "To customize your LegendUserBot."
    reply = await event.get_reply_message()
    text = None
    if reply:
        text = reply.text
    if text is None:
        return await eod(event, "__Reply to custom text or url__")
    input_str = event.pattern_match.group(1)
    if input_str == "pmpermit":
        addgvar("pmpermit_txt", text)
    if input_str == "pmblock":
        addgvar("pmblock", text)
    if input_str == "startmsg":
        addgvar("START_TEXT", text)
    if input_str == "pmpic":
        urls = extractor.find_urls(reply.text)
        if not urls:
            return await eor(event, "`the given link is not supported`", 5)
        text = " ".join(urls)
        addgvar("pmpermit_pic", text)
    await eor(event, f"__Your custom {input_str} has been updated__")
    if BOTLOG_CHATID:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#SET_DATAVAR\
                    \n**{input_str}** is updated newly in database as below",
        )
        await event.client.send_message(BOTLOG_CHATID, text, silent=True)


@legend.legend_cmd(
    pattern="delcustom (pmpermit|pmpic|pmblock|startmsg)$",
    command=("delcustom", menu_category),
    info={
        "header": "To delete costomization of your CatUserbot.",
        "options": {
            "pmpermit": "To delete custom pmpermit text",
            "pmblock": "To delete custom pmpermit block message",
            "pmpic": "To delete custom pmpermit pic.",
            "startmsg": "To delete custom start message of bot when some one started it.",
        },
        "usage": [
            "{tr}delcustom <option>",
        ],
        "NOTE": "You can set,fetch or delete these by `{tr}setdb` , `{tr}getdb` & `{tr}deldb` as well.",
    },
)
async def custom_ksks(event):
    "To delete costomization of your CatUserbot."
    input_str = event.pattern_match.group(1)
    if input_str == "pmpermit":
        if gvarstatus("pmpermit_txt") is None:
            return await eod(event, "__You haven't customzied your pmpermit.__")
        delgvar("pmpermit_txt")
    if input_str == "pmblock":
        if gvarstatus("pmblock") is None:
            return await eod(event, "__You haven't customzied your pmblock.__")
        delgvar("pmblock")
    if input_str == "pmpic":
        if gvarstatus("pmpermit_pic") is None:
            return await eod(event, "__You haven't customzied your pmpic.__")
        delgvar("pmpermit_pic")
    if input_str == "startmsg":
        if gvarstatus("START_TEXT") is None:
            return await eod(event, "__You haven't customzied your start msg in bot.__")
        delgvar("START_TEXT")
    await eor(event, f"__successfully deleted your customization of {input_str}.__")
    if BOTLOG_CHATID:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#DEL_DATAVAR\
                    \n**{input_str}** is deleted from database",
        )
