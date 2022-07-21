import os
from asyncio import sleep

import requests
from bs4 import BeautifulSoup

from Deepak import legend

from ..Config import Config
from ..core.managers import eod, eor
from ..helpers import progress
from ..sql_helper.husbando_sql import add_grp, get_all_grp, is_husbando, rm_grp

sex = "A husbando appeared!"

menu_category = "useless"


def progress(current, total):
    logger.info(
        "Downloaded {} of {}\nCompleted {}".format(
            current, total, (current / total) * 100
        )
    )


@legend.legend_cmd(
    pattern="at$",
    command=("at", menu_category),
    info={
        "header": "Auto Protecc the Replied Husbando Pic",
        "usage": [
            "{tr}at <reply to pic>",
        ],
    },
    groups_only=True,
)
async def at(event):
    """Auto Protecc the Replied Husbando Pic"""
    sweetie = await eor(event, "Hmm.. Reply To Husbando Pic")
    BASE_URL = "http://images.google.com"
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        previous_message_text = previous_message.message
        if previous_message.media:
            downloaded_file_name = await event.client.download_media(
                previous_message, Config.TMP_DOWNLOAD_DIRECTORY
            )
            SEARCH_URL = "{}/searchbyimage/upload".format(BASE_URL)
            multipart = {
                "encoded_image": (
                    downloaded_file_name,
                    open(downloaded_file_name, "rb"),
                ),
                "image_content": "",
            }
            google_rs_response = requests.post(
                SEARCH_URL, files=multipart, allow_redirects=False
            )
            the_location = google_rs_response.headers.get("Location")
            os.remove(downloaded_file_name)
        else:
            previous_message_text = previous_message.message
            SEARCH_URL = "{}/searchbyimage?image_url={}"
            request_url = SEARCH_URL.format(BASE_URL, previous_message_text)
            google_rs_response = requests.get(request_url, allow_redirects=False)
            the_location = google_rs_response.headers.get("Location")
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
        }
        response = requests.get(the_location, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        prs_div = soup.find_all("div", {"class": "r5a77d"})[0]
        prs_anchor_element = prs_div.find("a")
        prs_url = BASE_URL + prs_anchor_element.get("href")
        prs_text = prs_anchor_element.text
        img_size_div = soup.find(id="jHnbRc")
        img_size = img_size_div.find_all("div")
        OUTPUT_STR = """/protecc {prs_text}""".format(**locals())
        await sweetie.edit(OUTPUT_STR, parse_mode="HTML", link_preview=False)


@legend.legend_cmd(incoming=True, edited=False)
async def on_husbando(event):
    if not event.media:
        return
    if not sex in event.text:
        return
    if not event.sender_id == 1964681186:
        return
    all_grp = get_all_grp()
    if len(all_grp) == 0:
        return
    for grps in all_grp:
        if int(grps.chat_id) == event.chat_id:
            try:
                dl = await event.client.download_media(event.media, "resources/")
                file = {"encoded_image": (dl, open(dl, "rb"))}
                grs = requests.post(
                    "https://www.google.com/searchbyimage/upload",
                    files=file,
                    allow_redirects=False,
                )
                loc = grs.headers.get("Location")
                response = requests.get(
                    loc,
                    headers={
                        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
                    },
                )
                qtt = BeautifulSoup(response.text, "html.parser")
                div = qtt.find_all("div", {"class": "r5a77d"})[0]
                alls = div.find("a")
                text = alls.text
                try:
                    if "cg" in text:
                        return
                    if "fictional character" in text:
                        return
                except:
                    pass
                krishna = await event.client.send_message(
                    event.chat_id, f"/protecc {text}"
                )
                await sleep(5)
                await krishna.delete()
                os.remove(dl)
            except:
                pass
        else:
            pass


@legend.legend_cmd(
    pattern="ah$",
    command=("ah", menu_category),
    info={
        "header": "Add The current Group in husbando database",
        "description": "Add the current group to husbando Database.",
        "usage": [
            "{tr}ah",
        ],
    },
    groups_only=True,
)
async def ah(event):
    "Add The current Group in husbando database"
    if not event.is_group:
        await eod(event, "Auto Husbando works in Groups Only !!")
        return
    if is_husbando(str(event.chat_id)):
        await eod(event, "This Chat is Has Already In Auto Husbando Database!!")
        return
    add_grp(str(event.chat_id))
    await eod(
        event,
        f"👨‍💻 **Added Chat** {event.chat.title} **With Id** `{event.chat_id}` **To Husbando Database.**",
    )


@legend.legend_cmd(
    pattern="rmah$",
    command=("rmah", menu_category),
    info={
        "header": "Remove Group From Auto Husbando  Databse",
        "description": "Removes the group from Auto Husbando Database",
        "usage": [
            "{tr}rmah",
        ],
    },
    groups_only=True,
)
async def rmah(event):
    "Remove Group From Auto Husbando Databse"
    if not event.is_group:
        await eod(event, "Auto Husbando works in groups only !!")
        return
    if not is_husbando(str(event.chat_id)):
        await eod(event, "Auto Husbando was already disabled here.")
        return
    rm_grp(str(event.chat_id))
    await eod(
        event,
        f"👨‍💻 **Removed Chat** {event.chat.title} **With Id** `{event.chat_id}` **From Auto Husbando Database Successfully**",
    )


@legend.legend_cmd(
    pattern="listah$",
    command=("listah", menu_category),
    info={
        "header": "List Of All Chats Auto Husbando Enabled",
        "description": "Gives the list of all chats with Auto Husbando enabled.",
        "usage": [
            "{tr}listah",
        ],
    },
    groups_only=True,
)
async def listah(event):
    "List Of All Chats Auto Husbando Enabled"
    swt = await eor(event, "Fetching Auto Husbando chats...")
    all_grp = get_all_grp()
    x = "**Auto Husbando enabled chats :** \n\n"
    for i in all_grp:
        ch = i.chat_id
        cht = int(ch)
        x += f"♦️ `{cht}`\n"
    await swt.edit(x)
