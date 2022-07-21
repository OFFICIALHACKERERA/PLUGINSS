import random

from telethon.errors.rpcbaseerrors import ForbiddenError
from telethon.errors.rpcerrorlist import PollOptionInvalidError
from telethon.tl.types import InputMediaPoll, Poll

from Deepak import legend

from ..core.managers import eor
from . import Build_Poll, reply_id

menu_category = "extra"


@legend.legend_cmd(
    pattern="poll(?:\s|$)([\s\S]*)",
    command=("poll", menu_category),
    info={
        "header": "To create a poll.",
        "description": "If you doesnt give any input it sends a default poll",
        "usage": ["{tr}poll", "{tr}poll question ; option 1; option2"],
        "examples": "{tr}poll Are you an early bird or a night owl ;Early bird ; Night owl",
    },
)
async def pollcreator(owopoll):
    "To create a poll"
    reply_to_id = await reply_id(owopoll)
    string = "".join(owopoll.text.split(maxsplit=1)[1:])
    if not string:
        options = Build_Poll(["Yah sure 😊✌️", "Nah 😏😕", "Whatever die sur 🥱🙄"])
        try:
            await owopoll.client.send_message(
                owopoll.chat_id,
                file=InputMediaPoll(
                    poll=Poll(
                        id=random.getrandbits(32),
                        question="👆👆So do you guys agree with this?",
                        answers=options,
                    )
                ),
                reply_to=reply_to_id,
            )
            await owopoll.delete()
        except PollOptionInvalidError:
            await eor(
                owopoll, "`A poll option used invalid data (the data may be too long).`"
            )
        except ForbiddenError:
            await eor(owopoll, "`This chat has forbidden the polls`")
        except exception as e:
            await eor(owopoll, str(e))
    else:
        legendinput = string.split(";")
        if len(legendinput) > 2 and len(legendinput) < 12:
            options = Build_Poll(legendinput[1:])
            try:
                await owopoll.client.send_message(
                    owopoll.chat_id,
                    file=InputMediaPoll(
                        poll=Poll(
                            id=random.getrandbits(32),
                            question=legendinput[0],
                            answers=options,
                        )
                    ),
                    reply_to=reply_to_id,
                )
                await owopoll.delete()
            except PollOptionInvalidError:
                await eor(
                    owopoll,
                    "`A poll option used invalid data (the data may be too long).`",
                )
            except ForbiddenError:
                await eor(owopoll, "`This chat has forbidden the polls`")
            except Exception as e:
                await eor(owopoll, str(e))
        else:
            await eor(
                owopoll,
                "Make sure that you used Correct syntax `.poll question ; option1 ; option2`",
            )
