import glob
import os
import sys
import urllib.request
from datetime import timedelta
from pathlib import Path

from telethon import Button, functions, types, utils
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest

from Deepak import BOTLOG, BOTLOG_CHATID, PM_LOGGER_GROUP_ID, legendversion

from ..Config import Config
from ..core.logger import logging
from ..core.session import legend
from ..helpers.utils.utils import runcmd
from ..sql_helper.global_collection import (
    del_keyword_collectionlist,
    get_item_collectionlist,
)
from ..sql_helper.globals import addgvar, gvarstatus
from .pluginmanager import load_module, start_spam
from .tools import create_supergroup

ENV = bool(os.environ.get("ENV", False))

LOGS = logging.getLogger("LegendDeepak")
cmdhr = Config.HANDLER


if ENV:
    VPS_NOLOAD = ["vps"]
elif os.path.exists("config.py"):
    VPS_NOLOAD = ["heroku"]


async def setup_bot():
    """
    To set up bot for Deepak
    """
    try:
        await legend.connect()
        config = await legend(functions.help.GetConfigRequest())
        for option in config.dc_options:
            if option.ip_address == legend.session.server_address:
                if legend.session.dc_id != option.id:
                    LOGS.warning(
                        f"Fixed DC ID in session from {legend.session.dc_id}"
                        f" to {option.id}"
                    )
                legend.session.set_dc(option.id, option.ip_address, option.port)
                legend.session.save()
                break
        bot_details = await legend.tgbot.get_me()
        Config.BOT_USERNAME = f"@{bot_details.username}"
        legend.me = await legend.get_me()
        legend.uid = legend.tgbot.uid = utils.get_peer_id(legend.me)
        if Config.OWNER_ID == 0:
            Config.OWNER_ID = utils.get_peer_id(legend.me)
    except Exception as e:
        LOGS.error(f"DEEPAK_STRING - {e}")
        sys.exit()


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    is_sudo = "True" if Config.SUDO_USERS else "False"
    try:
        if BOTLOG:
            Config.LEGENDUBLOGO = await legend.tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/9fdec96f8f340b8946845.jpg",
                caption=f"**__Version__**:- {legendversion}\n\n**__Sudo__** :- {is_sudo}\n\n**Your UserBot has been started successfully.**",
                buttons=[(Button.url("👨‍🏫 Support ", "https://t.me/HEPPYLIFI"),
                Button.url("🤖 Updates ", "https://t.me/OFFICIALHACKER789"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        msg_details = list(get_item_collectionlist("restart_update"))
        if msg_details:
            msg_details = msg_details[0]
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        if msg_details:
            await legend.check_testcases()
            message = await legend.get_messages(msg_details[0], ids=msg_details[1])
            text = message.text + "\n\n**Ok Bot is Back and Alive.**"
            await legend.edit_message(msg_details[0], msg_details[1], text)
            if gvarstatus("restartupdate") is not None:
                await legend.send_message(
                    msg_details[0],
                    f"{cmdhr}ping -a",
                    reply_to=msg_details[1],
                    schedule=timedelta(seconds=10),
                )
            del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
        return None


async def add_bot_to_logger_group(chat_id):
    """
    To add bot to logger groups
    """
    bot_details = await legend.tgbot.get_me()
    lol = bot_details.username
    addgvar("BOT_USERNAME", lol)
    try:
        await legend(
            functions.messages.AddChatUserRequest(
                chat_id=chat_id,
                user_id=lol,
                fwd_limit=1000000,
            )
        )
    except BaseException:
        try:
            await legend(
                functions.channels.InviteToChannelRequest(
                    channel=chat_id,
                    users=[lol],
                )
            )
        except Exception as e:
            LOGS.error(str(e))


async def load_plugins(folder, extfolder=None):
    """
    To load plugins from the mentioned folder
    """
    if extfolder:
        path = f"{extfolder}/*.py"
        plugin_path = extfolder
    else:
        path = f"Deepak/{folder}/*.py"
        plugin_path = f"Deepak/{folder}"
    files = glob.glob(path)
    files.sort()
    success = 0
    failure = []
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            pluginname = shortname.replace(".py", "")
            try:
                if (pluginname not in Config.NO_LOAD) and (
                    pluginname not in VPS_NOLOAD
                ):
                    flag = True
                    while flag:
                        try:
                            load_module(
                                pluginname,
                                plugin_path=plugin_path,
                            )
                            if shortname in failure:
                                failure.remove(shortname)
                            success += 1
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if shortname not in failure:
                                failure.append(shortname)
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"{plugin_path}/{shortname}.py"))
            except Exception as e:
                if shortname not in failure:
                    failure.append(shortname)
                os.remove(Path(f"{plugin_path}/{shortname}.py"))
                LOGS.info(
                    f"unable to load {shortname} because of error {e}\nBase Folder {plugin_path}"
                )
    if extfolder:
        if not failure:
            failure.append("None")
        await legend.tgbot.send_message(
            BOTLOG_CHATID,
            f'Your external repo plugins have imported \n**No of imported plugins :** `{success}`\n**Failed plugins to import :** `{", ".join(failure)}`',
        )


async def hekp():
    try:
        os.environ[
            "DEEPAK_STRING"
        ] = "String Is A Sensitive Data \nSo Its Protected By LegendBot"
    except Exception as e:
        print(str(e))
    try:
        await legend(JoinChannelRequest(""))
    except BaseException:
        pass
    try:
        await legend(JoinChannelRequest(""))
    except BaseException:
        pass
    try:
        await legend(LeaveChannelRequest("@Legend_Deepak"))
    except BaseException:
        pass
    try:
        await legend(LeaveChannelRequest("@Official_LegendBot"))
    except BaseException:
        pass


spam = os.environ.get("SPAM", None) or "OFF"


async def spams():
    if spam == "ON":
        import glob

        path = "Deepak/plugins/Spam/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                start_spam(shortname.replace(".py", ""))
    else:
        print("⚠️Spam Not Loading⚠️")





async def scammer(username):
    i = 0
    xx = 0
    async for x in legend.iter_dialogs():
        if x.is_group or x.is_channel:
            try:
                await legend.edit_permissions(x.id, username, view_messages=False)
                i += 1
            except:
                xx += 1
    print(f"OP {i-xx}")









async def verifyLoggerGroup():
    """
    Will verify the both loggers group
    """
    type = False
    if BOTLOG:
        try:
            entity = await legend.get_entity(BOTLOG_CHATID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "Permissions missing to send messages for the specified PRIVATE_GROUP_BOT_API_ID."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "Permissions missing to addusers for the specified PRIVATE_GROUP_BOT_API_ID."
                    )
        except ValueError:
            LOGS.error(
                "PRIVATE_GROUP_BOT_API_ID cannot be found. Make sure it's correct."
            )
        except TypeError:
            LOGS.error(
                "PRIVATE_GROUP_BOT_API_ID is unsupported. Make sure it's correct."
            )
        except Exception as e:
            LOGS.error(
                "An Exception occured upon trying to verify the PRIVATE_GROUP_BOT_API_ID.\n"
                + str(e)
            )
    else:
        descript = "A Logger Group For LegendBot.Don't delete this group or change to group(If you change group all your previous snips, welcome will be lost.)"
        _, groupid = await create_supergroup(
            "UserBot Logger", legend, Config.BOT_USERNAME, descript
        )
        addgvar("PRIVATE_GROUP_BOT_API_ID", groupid)
        print(
            "Private Group for PRIVATE_GROUP_BOT_API_ID is created successfully and added to vars."
        )
        type = True
    if PM_LOGGER_GROUP_ID != -100:
        try:
            entity = await legend.get_entity(PM_LOGGER_GROUP_ID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "Permissions missing to send messages for the specified PM_LOGGER_GROUP_ID."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "Permissions missing to addusers for the specified PM_LOGGER_GROUP_ID."
                    )
        except ValueError:
            LOGS.error("PM_LOGGER_GROUP_ID cannot be found. Make sure it's correct.")
        except TypeError:
            LOGS.error("PM_LOGGER_GROUP_ID is unsupported. Make sure it's correct.")
        except Exception as e:
            LOGS.error(
                "An Exception occured upon trying to verify the PM_LOGGER_GROUP_ID.\n"
                + str(e)
            )
    if type:
        executable = sys.executable.replace(" ", "\\ ")
        args = [executable, "-m", "Deepak"]
        os.execle(executable, *args, os.environ)
        sys.exit(0)


async def install_extrarepo(repo, branch, efolder):
    LEGENDREPO = repo
    if LEGENDBRANCH := branch:
        repourl = os.path.join(LEGENDREPO, f"tree/{LEGENDBRANCH}")
        gcmd = f"git clone -b {LEGENDBRANCH} {LEGENDREPO} {efolder}"
        errtext = f"There is no branch with name `{LEGENDBRANCH}` in your external repo {LEGENDREPO}. Recheck branch name and correct it in vars(`EXTRA_REPOBRANCH`)"
    else:
        repourl = LEGENDREPO
        gcmd = f"git clone {LEGENDREPO} {efolder}"
        errtext = f"The link({LEGENDREPO}) you provided for `EXTERNAL_REPO` in vars is invalid. please recheck that link"
    response = urllib.request.urlopen(repourl)
    if response.code != 200:
        LOGS.error(errtext)
        return await legend.tgbot.send_message(BOTLOG_CHATID, errtext)
    await runcmd(gcmd)
    if not os.path.exists(efolder):
        LOGS.error(
            "There was a problem in cloning the external repo. please recheck external repo link"
        )
        return await legend.tgbot.send_message(
            BOTLOG_CHATID,
            "There was a problem in cloning the external repo. please recheck external repo link",
        )
    if os.path.exists(os.path.join(efolder, "requirements.txt")):
        rpath = os.path.join(efolder, "requirements.txt")
        await runcmd(f"pip3 install --no-cache-dir {rpath}")
    await load_plugins(folder="Deepak", extfolder=efolder)
