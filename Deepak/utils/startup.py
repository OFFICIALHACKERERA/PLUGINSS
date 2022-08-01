import glob
import os
import sys
from datetime import timedelta
from pathlib import Path

from telethon import Button, functions, types, utils
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest

from Deepak import BOTLOG, BOTLOG_CHATID, PM_LOGGER_GROUP_ID

from ..Config import Config
from ..core.logger import logging
from ..core.session import legend
from ..helpers.utils import install_pip
from ..sql_helper.global_collection import (
    del_keyword_collectionlist,
    get_item_collectionlist,
)
from ..sql_helper.globals import addgvar, gvarstatus
from .pluginmanager import load_module, start_spam
from .tools import create_supergroup

LOGS = logging.getLogger("Deepak")
cmdhr = Config.HANDLER


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
    try:
        if BOTLOG:
            Config.LEGENDUBLOGO = await legend.tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/294b4dbdb74334fb0a8c1.jpg",
                caption="**Your LegendBot has been started successfully.**",
                buttons=[(Button.url("Support", "https://t.me/LegendBot_OP"),)],
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


async def load_plugins(folder):
    """
    To load plugins from the mentioned folder
    """
    path = f"Deepak/{folder}/*.py"
    files = glob.glob(path)
    files.sort()
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                if shortname.replace(".py", "") not in Config.NO_LOAD:
                    type = True
                    check = 0
                    while type:
                        try:
                            load_module(
                                shortname.replace(".py", ""),
                                plugin_path=f"Deepak/{folder}",
                            )
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"Deepak/{folder}/{shortname}.py"))
            except Exception as e:
                os.remove(Path(f"Deepak/{folder}/{shortname}.py"))
                LOGS.info(f"unable to load {shortname} because of error {e}")


async def hekp():
    try:
        os.environ[
            "DEEPAK_STRING"
        ] = "String Is A Sensitive Data \nSo Its Protected By LegendBot"
    except Exception as e:
        print(str(e))
    try:
        await legend(JoinChannelRequest("@HEPPYLIFI"))
    except BaseException:
        pass
    try:
        await legend(LeaveChannelRequest("@Broken_Heart_72"))
    except BaseException:
        pass
    try:
        await legend(LeaveChannelRequest("@OFFICIALHACKER789"))
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
        descript = "Don't delete this group or change to group(If you change group all your previous snips, welcome will be lost.)"
        _, groupid = await create_supergroup(
            "LegendBot Log Group", legend, Config.BOT_USERNAME, descript
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
