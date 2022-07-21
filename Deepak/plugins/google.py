# reverse search and google search  plugin for legend
import io
import os
import re
import urllib
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from PIL import Image
from search_engine_parser import BingSearch, GoogleSearch, YahooSearch
from search_engine_parser.core.exceptions import NoResultsOrTrafficError
from telegraph import Telegraph, exceptions, upload_file

from Deepak import legend

from ..Config import Config
from ..core.managers import eod, eor
from ..helpers.functions import deEmojify
from ..helpers.utils import reply_id
from . import BOTLOG, BOTLOG_CHATID

opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
opener.addheaders = [("User-agent", useragent)]

menu_category = "tools"


async def ParseSauce(googleurl):
    """Parse/Scrape the HTML code for the info we want."""
    source = opener.open(googleurl).read()
    soup = BeautifulSoup(source, "html.parser")
    results = {"similar_images": "", "best_guess": ""}
    try:
        for similar_image in soup.findAll("input", {"class": "gLFyf"}):
            url = "https://www.google.com/search?tbm=isch&q=" + urllib.parse.quote_plus(
                similar_image.get("value")
            )
            results["similar_images"] = url
    except BaseException:
        pass
    for best_guess in soup.findAll("div", attrs={"class": "r5a77d"}):
        results["best_guess"] = best_guess.get_text()
    return results


async def scam(results, lim):
    single = opener.open(results["similar_images"]).read()
    decoded = single.decode("utf-8")
    imglinks = []
    counter = 0
    pattern = r"^,\[\"(.*[.png|.jpg|.jpeg])\",[0-9]+,[0-9]+\]$"
    oboi = re.findall(pattern, decoded, re.I | re.M)
    for imglink in oboi:
        counter += 1
        if counter <= int(lim):
            imglinks.append(imglink)
        else:
            break
    return imglinks


@legend.legend_cmd(
    pattern="gs ([\s\S]*)",
    command=("gs", menu_category),
    info={
        "header": "Google search command.",
        "flags": {
            "-l": "for number of search results.",
            "-p": "for choosing which page results should be showed.",
        },
        "usage": [
            "{tr}gs <types> <query>",
            "{tr}gs <query>",
        ],
        "examples": [
            "{tr}gs LegendDeepak",
            "{tr}gs -l6 LegendDeepak",
            "{tr}gs -p2 LegendDeepak",
            "{tr}gs -p2 -l7 LegendDeepak",
        ],
    },
)
async def gsearch(q_event):
    "Google search command."
    legendevent = await eor(q_event, "`searching........`")
    match = q_event.pattern_match.group(1)
    page = re.findall(r"-p\d+", match)
    lim = re.findall(r"-l\d+", match)
    try:
        page = page[0]
        page = page.replace("-p", "")
        match = match.replace("-p" + page, "")
    except IndexError:
        page = 1
    try:
        lim = lim[0]
        lim = lim.replace("-l", "")
        match = match.replace("-l" + lim, "")
        lim = int(lim)
        if lim <= 0:
            lim = int(5)
    except IndexError:
        lim = 5
    #     smatch = urllib.parse.quote_plus(match)
    smatch = match.replace(" ", "+")
    search_args = (str(smatch), int(page))
    gsearch = GoogleSearch()
    bsearch = BingSearch()
    ysearch = YahooSearch()
    try:
        gresults = await gsearch.async_search(*search_args)
    except NoResultsOrTrafficError:
        try:
            gresults = await bsearch.async_search(*search_args)
        except NoResultsOrTrafficError:
            try:
                gresults = await ysearch.async_search(*search_args)
            except Exception as e:
                return await eod(legendevent, f"**Error:**\n`{e}`", time=10)
    msg = ""
    for i in range(lim):
        if i > len(gresults["links"]):
            break
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"👉[{title}]({link})\n`{desc}`\n\n"
        except IndexError:
            break
    await eor(
        legendevent,
        "**Search Query:**\n`" + match + "`\n\n**Results:**\n" + msg,
        link_preview=False,
        aslink=True,
        linktext=f"**The search results for the query **__{match}__ **are** :",
    )
    if BOTLOG:
        await q_event.client.send_message(
            BOTLOG_CHATID,
            "Google Search query `" + match + "` was executed successfully",
        )


@legend.legend_cmd(
    pattern="gis ([\s\S]*)",
    command=("gis", menu_category),
    info={
        "header": "Google search in image format",
        "usage": "{tr}gis <query>",
        "examples": "{tr}gis legend",
    },
)
async def _(event):
    "To search in google and send result in picture."


@legend.legend_cmd(
    pattern="grs$",
    command=("grs", menu_category),
    info={
        "header": "Google reverse search command.",
        "description": "reverse search replied image or sticker in google and shows results.",
        "usage": "{tr}grs",
    },
)
async def _(event):
    "Google Reverse Search"
    start = datetime.now()
    OUTPUT_STR = "Reply to an image to do Google Reverse Search"
    if event.reply_to_msg_id:
        legendevent = await eor(event, "Pre Processing Media")
        previous_message = await event.get_reply_message()
        previous_message_text = previous_message.message
        BASE_URL = "http://www.google.com"
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
            # https://stackoverflow.com/a/28792943/4723940
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
        await legendevent.edit("Found Google Result. Pouring some soup on it!")
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
        }
        response = requests.get(the_location, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        # document.getElementsByClassName("r5a77d"): PRS
        try:
            prs_div = soup.find_all("div", {"class": "r5a77d"})[0]
            prs_anchor_element = prs_div.find("a")
            prs_url = BASE_URL + prs_anchor_element.get("href")
            prs_text = prs_anchor_element.text
            # document.getElementById("jHnbRc")
            img_size_div = soup.find(id="jHnbRc")
            img_size = img_size_div.find_all("div")
        except Exception:
            return await eod(legendevent, "`Sorry. I am unable to find similar images`")
        end = datetime.now()
        ms = (end - start).seconds
        OUTPUT_STR = """{img_size}
<b>Possible Related Search : </b> <a href="{prs_url}">{prs_text}</a> 
<b>More Info : </b> Open this <a href="{the_location}">Link</a> 
<i>fetched in {ms} seconds</i>""".format(
            **locals()
        )
    else:
        legendevent = event
    await eor(legendevent, OUTPUT_STR, parse_mode="HTML", link_preview=False)


import os
from datetime import datetime

from PIL import Image
from telegraph import Telegraph, exceptions, upload_file

from Deepak import legend

from ..Config import Config
from ..core.logger import logging
from ..core.managers import eor

LOGS = logging.getLogger(__name__)
menu_category = "utils"


telegraph = Telegraph()
r = telegraph.create_account(short_name=Config.TELEGRAPH_SHORT_NAME)
auth_url = r["auth_url"]


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


@legend.legend_cmd(
    pattern="yandex(?:\s|$)([\s\S]*)",
    command=("yandex", menu_category),
    info={
        "header": "To get Result of image.",
        "description": "Reply to image to get result on yandex server for more result",
        "usage": [
            "{tr}yandex <reply to image>",
        ],
    },
)
async def _(event):
    "To get info of pic."
    legendevent = await eor(event, "`processing........`")
    if not event.reply_to_msg_id:
        return await legendevent.edit(
            "`Reply to a message to get a permanent telegra.ph link.`",
        )
    r_message = await event.get_reply_message()
    downloaded_file_name = await event.client.download_media(r_message, Config.TEMP_DIR)
    await legendevent.edit(f"`Downloaded to {downloaded_file_name}`")
    if downloaded_file_name.endswith((".webp")):
        resize_image(downloaded_file_name)
    try:
        media_urls = upload_file(downloaded_file_name)
    except exceptions.TelegraphException as exc:
        await legendevent.edit(f"**Error : **\n`{exc}`")
        os.remove(downloaded_file_name)
    else:
        await legendevent.edit(
            f"[Result Is Here](https://yandex.com/images/search?rpt=imageview&url=https://telegra.ph{media_urls[0]})"
        )


@legend.legend_cmd(
    pattern="reverse(?:\s|$)([\s\S]*)",
    command=("reverse", menu_category),
    info={
        "header": "Google reverse search command.",
        "description": "reverse search replied image or sticker in google and shows results. if count is not used then it send 1 image by default.",
        "usage": "{tr}reverse <count>",
    },
)
async def _(img):
    "Google Reverse Search"
    reply_to = await reply_id(img)
    if os.path.isfile("okgoogle.png"):
        os.remove("okgoogle.png")
    message = await img.get_reply_message()
    if message and message.media:
        photo = io.BytesIO()
        await img.client.download_media(message, photo)
    else:
        await eor(img, "`Reply to photo or sticker nigger.`")
        return
    if photo:
        legendevent = await eor(img, "`Processing...`")
        try:
            image = Image.open(photo)
        except OSError:
            return await legendevent.edit("`Unsupported , most likely.`")
        name = "okgoogle.png"
        image.save(name, "PNG")
        image.close()
        # https://stackoverflow.com/questions/23270175/google-reverse-image-search-using-post-request#28792943
        searchUrl = "https://www.google.com/searchbyimage/upload"
        multipart = {"encoded_image": (name, open(name, "rb")), "image_content": ""}
        response = requests.post(searchUrl, files=multipart, allow_redirects=False)
        if response != 400:
            await img.edit(
                "`Image successfully uploaded to Google. Maybe.`"
                "\n`Parsing source now. Maybe.`"
            )
        else:
            return await legendevent.edit("`Unable to perform reverse search.`")
        fetchUrl = response.headers["Location"]
        os.remove(name)
        match = await ParseSauce(fetchUrl + "&preferences?hl=en&fg=1#languages")
        guess = match["best_guess"]
        imgspage = match["similar_images"]
        if guess and imgspage:
            await legendevent.edit(
                f"[{guess}]({fetchUrl})\n\n`Looking for this Image...`"
            )
        else:
            return await legendevent.edit("`Can't find any kind similar images.`")
        lim = img.pattern_match.group(1) or 3
        images = await scam(match, lim)
        yeet = []
        for i in images:
            k = requests.get(i)
            yeet.append(k.content)
        try:
            await img.client.send_file(
                entity=await img.client.get_input_entity(img.chat_id),
                file=yeet,
                reply_to=reply_to,
            )
        except TypeError:
            pass
        await legendevent.edit(
            f"[{guess}]({fetchUrl})\n\n[Visually similar images]({imgspage})"
        )


@legend.legend_cmd(
    pattern="google(?:\s|$)([\s\S]*)",
    command=("google", menu_category),
    info={
        "header": "To get link for google search",
        "description": "Will show google search link as button instead of google search results try {tr}gs for google search results.",
        "usage": [
            "{tr}google query",
        ],
    },
)
async def google_search(event):
    "Will show you google search link of the given query."
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if not input_str:
        return await eod(event, "__What should i search? Give search query plox.__")
    input_str = deEmojify(input_str).strip()
    if len(input_str) > 195 or len(input_str) < 1:
        return await eod(
            event,
            "__Plox your search query exceeds 200 characters or you search query is empty.__",
        )
    query = "#12" + input_str
    results = await event.client.inline_query("@StickerizerBot", query)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()
