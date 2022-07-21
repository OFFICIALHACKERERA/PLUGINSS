import asyncio

from .. import legend
from ..core.logger import logging
from ..core.managers import eor

menu_category = "tools"

LOGS = logging.getLogger(__name__)


@legend.legend_cmd(
    pattern="hdd(?:\s|$)([\s\S]*)",
    command=("hdd", menu_category),
    info={
        "header": "To Wish Diwali",
        "description": "It Can Help U To Send Diwali Message",
    },
)
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 50)
    await event.edit("Happy Diwali Dosto🤗")
    animation_chars = [
        """-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙""",
        """💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
-#--💙happy💙diwali💙
#----💙happy💙diwali💙
#-----💙happy💙diwali💙
#-----💙happy💙diwali💙
#-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜""",
        """"💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖 
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖""",
        """❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖 
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖 
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙""",
        """💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖 
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖 
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️""",
        """💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
---💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💜happy💜diwali💜
----💜happy💜diwali💜
---💜happy💜diwali💜
--💜happy💜diwali💜
-💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💜happy💜diwali💜
💜happy💜diwali💜
💜happy💜diwali💜
-💜happy💜diwali💜
--💜happy💜diwali💜
----💜happy💜diwali💜
-----💜happy💜diwali💜
-----💖happy💖diwali💖
-----💖happy💖diwali💖
-----💖happy💖diwali💖
----💖happy💖diwali💖
---💖happy💖diwali💖
--💖happy💖diwali💖
-💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖 
💖happy💖diwali💖
💖happy💖diwali💖
💖happy💖diwali💖
-💖happy💖diwali💖
--💖happy💖diwali💖
---💖happy💖diwali💖
----💖happy💖diwali💖 
---💙happy💙diwali💙
----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
-----💙happy💙diwali💙
----💙happy💙diwali💙
---💙happy💙diwali💙
--💙happy💙diwali💙
-💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
💙happy💙diwali💙
-💙happy💙diwali💙
--💙happy💙diwali💙
--♥️happy❤️diwali♥️
---❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
-----♥️happy❤️diwali♥️
-----❤️happy♥️diwali❤️
----♥️happy❤️diwali♥️
---♥️happy❤️diwali❤️
--♥️happy❤️diwali♥️
-♥️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
❤️happy♥️diwali❤️
❤️happy♥️diwali♥️
❤️happy♥️diwali♥️
-❤️happy♥️diwali♥️
-💚happy💚diwali💚
--💚happy💚diwali💚
---💚happy💚diwali💚
----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
-----💚happy💚diwali💚
----💚happy💚diwali💚
---💚happy💚diwali💚
--💚happy💚diwali💚
-💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚
💚happy💚diwali💚""",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])


@legend.legend_cmd(
    pattern="dosto(?:\s|$)([\s\S]*)",
    command=("dosto", menu_category),
    info={
        "header": "To Wish Diwali",
        "description": "It Can Help U To Send Diwali Message",
    },
)
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 20)
    await event.edit("❤Happy Diwali Dosto❤")
    animation_chars = [
        "💖happy💖diwali💖",
        "💙happy💙diwali💙",
        "❤️happy♥️diwali❤️",
        "💚happy💚diwali💚",
        "💜happy💜diwali💜",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 20])


@legend.legend_cmd(
    pattern="diwali(?:\s|$)([\s\S]*)",
    command=("diwali", menu_category),
    info={
        "header": "To Wish Diwali",
        "description": "It Can Help U To Send Diwali Message",
    },
)
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 22)
    await event.edit("❤Dosto❤")
    animation_chars = [
        """💜💜                        💜💜
💜💜                        💜💜
💜💜                        💜💜
💜💜                        💜💜
💜💜💜💜💜💜💜💜💜
💜💜💜💜💜💜💜💜💜
💜💜                        💜💜
💜💜                        💜💜
💜💜                        💜💜
💜💜                        💜💜""",
        """ㅤㅤㅤㅤㅤ ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ
                    💙💙
                 💙💙💙
             💙💙💙💙
            💙💙 💙💙
          💙💙    💙💙
        💙💙       💙💙
     💙💙💙💙💙💙
      💙💙💙💙💙💙
   💙💙                 💙💙
  💙💙                    💙💙
💙💙                       💙💙""",
        """💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚                     💚💚
💚💚                     💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚
💚💚
💚💚
💚💚
💚💚""",
        """💛💛💛💛💛💛
💛💛💛💛💛💛💛
💛💛                💛💛
💛💛                💛💛
💛💛💛💛💛💛💛
💛💛💛💛💛💛
💛💛
💛💛
💛💛
💛💛""",
        """💜💜                    💜💜
   💜💜              💜💜
      💜💜        💜💜
         💜💜  💜💜
            💜💜💜
              💜💜
              💜💜
              💜💜
              💜💜
              💜💜""",
        """💖💖💖💖💖💖💖
💖💖💖💖💖💖💖💖
💖💖                      💖💖
💖💖                         💖💖
💖💖                         💖💖
💖💖                         💖💖
💖💖                         💖💖
💖💖                      💖💖
💖💖💖💖💖💖💖💖
💖💖💖💖💖💖💖""",
        """💝💝💝💝💝💝
💝💝💝💝💝💝
          💝💝
          💝💝
          💝💝
          💝💝
          💝💝
          💝💝
💝💝💝💝💝💝
💝💝💝💝💝💝""",
        """💖💖                               💖💖
💖💖                               💖💖
💖💖                               💖💖
💖💖                               💖💖
💖💖              💖            💖💖
 💖💖           💖💖          💖💖
 💖💖        💖💖💖       💖💖
  💖💖   💖💖  💖💖   💖💖
   💖💖💖💖      💖💖💖💖
    💖💖💖             💖💖💖""",
        """ㅤㅤㅤㅤㅤ ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ
                    💙💙
                 💙💙💙
             💙💙💙💙
            💙💙 💙💙
          💙💙    💙💙
        💙💙       💙💙
     💙💙💙💙💙💙
      💙💙💙💙💙💙
   💙💙                 💙💙
  💙💙                    💙💙
💙💙                       💙💙""",
        """💘💘
💘💘
💘💘
💘💘
💘💘
💘💘
💘💘
💘💘
💘💘💘💘💘💘💘💘
💘💘💘💘💘💘💘💘""",
        """💝💝💝💝💝💝
💝💝💝💝💝💝
          💝💝
          💝💝
          💝💝
          💝💝
          💝💝
          💝💝
💝💝💝💝💝💝
💝💝💝💝💝💝""",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 22])


@legend.legend_cmd(
    pattern="wishdiwali(?:\s|$)([\s\S]*)",
    command=("wishdiwali", menu_category),
    info={
        "header": "To Wish Diwali",
        "description": "It Can Help U To Send Diwali Message To All Group/user According to type",
        "flags": {
            "-a": "To Send Diwali Wish In All User & Group",
            "-g": "To Send Diwali Wish In All Group",
            "-p": "To Send Diwali Wish In All User",
        },
        "usage": [
            "{tr}wishdiwali <type>",
        ],
        "examples": [
            "{tr}wishdiwali -a",
        ],
    },
)
async def xd(event):
    "Help U To Send Diwali Message In All Group & User"
    await event.get_reply_message()
    type = event.text[7:9] or "-a"
    hol = await eor(event, "`Sending Diwali message...`")
    sed = 0
    lol = 0
    if type == "-a":
        async for aman in event.client.iter_dialogs():
            chat = aman.id
            try:
                if chat != -1001551357238:
                    await bot.send_message(
                        chat,
                        f"⁭💖💖                        💖💖\n 💖💖                      💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n💖💖💖💖💖💖💖💖💖\n💖💖💖💖💖💖💖💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n\n                    💖\n                  💖💖\n               💖💖💖\n            💖💖 💖💖\n          💖💖    💖💖\n        💖💖       💖💖\n      💖💖💖💖💖💖\n     💖💖💖💖💖💖💖\n   💖💖                 💖💖\n  💖💖                    💖💖\n💖💖                       💖💖\n\n💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗💗\n💗💗                     💗💗\n💗💗                     💗💗\n💗💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗\n💗💗\n💗💗\n💗💗\n💗💗\n\n💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗💗\n💗💗                     💗💗\n💗💗                     💗💗\n💗💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗\n💗💗\n💗💗\n💗💗\n💗💗\n\n💙💙                    💙💙\n   💙💙              💙💙\n      💙💙        💙💙\n         💙💙  💙💙\n            💙💙💙\n              💙💙\n              💙💙\n              💙💙\n              💙💙\n              💙💙\n h💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙\n💙💙                      💙💙\n💙💙                         💙💙\n💙💙                         💙💙\n💙💙                         💙💙\n💙💙                         💙💙\n💙💙                      💙💙\n💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙\n\n💗💗💗💗💗💗\n💗💗💗💗💗💗\n          💗💗\n         💗💗\n          💗💗\n          💗💗\n          💗💗\n          💗💗\n💗💗💗💗💗💗\n💗💗💗💗💗💗\n⁭\n💗💗                               💗💗\n💗💗                               💗💗\n💗💗                               💗💗\n💗💗                               💗💗\n💗💗              💗            💗💗\n 💗💗           💗💗          💗💗\n 💗💗        💗💗💗       💗💗\n  💗💗   💗💗  💗💗   💗💗\n   💗💗💗💗      💗💗💗💗\n    💗💗💗             💗💗💗\n⁭\n                    💖\n                  💖💖\n               💖💖💖\n            💖💖 💖💖\n          💖💖    💖💖\n        💖💖       💖💖\n      💖💖💖💖💖💖\n     💖💖💖💖💖💖💖\n   💖💖                 💖💖\n  💖💖                    💖💖\n💖💖                       💖💖\n⁭\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟💟💟💟💟💟💟\n💟💟💟💟💟💟💟💟\n⁭\n💗💗💗💗💗💗\n💗💗💗💗💗💗\n          💗💗\n          💗💗\n          💗💗\n          💗💗\n          💗💗\n          💗💗\n💗💗💗💗💗💗\n💗💗💗💗💗💗",
                    )
                    lol += 1
                elif chat == -1001551357238:
                    pass
            except BaseException:
                sed += 1
    elif type == "-p":
        async for krishna in event.client.iter_dialogs():
            if krishna.is_user and not krishna.entity.bot:
                chat = krishna.id
                try:
                    await bot.send_message(
                        chat,
                        f"⁭💖💖                        💖💖\n 💖💖                      💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n💖💖💖💖💖💖💖💖💖\n💖💖💖💖💖💖💖💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n\n                    💖\n                  💖💖\n               💖💖💖\n            💖💖 💖💖\n          💖💖    💖💖\n        💖💖       💖💖\n      💖💖💖💖💖💖\n     💖💖💖💖💖💖💖\n   💖💖                 💖💖\n  💖💖                    💖💖\n💖💖                       💖💖\n\n💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗💗\n💗💗                     💗💗\n💗💗                     💗💗\n💗💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗\n💗💗\n💗💗\n💗💗\n💗💗\n\n💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗💗\n💗💗                     💗💗\n💗💗                     💗💗\n💗💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗\n💗💗\n💗💗\n💗💗\n💗💗\n\n💙💙                    💙💙\n   💙💙              💙💙\n      💙💙        💙💙\n         💙💙  💙💙\n            💙💙💙\n              💙💙\n              💙💙\n              💙💙\n              💙💙\n              💙💙\n h💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙\n💙💙                      💙💙\n💙💙                         💙💙\n💙💙                         💙💙\n💙💙                         💙💙\n💙💙                         💙💙\n💙💙                      💙💙\n💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙\n\n💗💗💗💗💗💗\n💗💗💗💗💗💗\n          💗💗\n         💗💗\n          💗💗\n          💗💗\n          💗💗\n          💗💗\n💗💗💗💗💗💗\n💗💗💗💗💗💗\n⁭\n💗💗                               💗💗\n💗💗                               💗💗\n💗💗                               💗💗\n💗💗                               💗💗\n💗💗              💗            💗💗\n 💗💗           💗💗          💗💗\n 💗💗        💗💗💗       💗💗\n  💗💗   💗💗  💗💗   💗💗\n   💗💗💗💗      💗💗💗💗\n    💗💗💗             💗💗💗\n⁭\n                    💖\n                  💖💖\n               💖💖💖\n            💖💖 💖💖\n          💖💖    💖💖\n        💖💖       💖💖\n      💖💖💖💖💖💖\n     💖💖💖💖💖💖💖\n   💖💖                 💖💖\n  💖💖                    💖💖\n💖💖                       💖💖\n⁭\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟💟💟💟💟💟💟\n💟💟💟💟💟💟💟💟\n⁭\n💗💗💗💗💗💗\n💗💗💗💗💗💗\n          💗💗\n          💗💗\n          💗💗\n          💗💗\n          💗💗\n          💗💗\n💗💗💗💗💗💗\n💗💗💗💗💗💗",
                    )
                    lol += 1
                except BaseException:
                    sed += 1
    elif type == "-g":
        async for sweetie in event.client.iter_dialogs():
            if sweetie.is_group:
                chat = sweetie.id
                try:
                    if chat != -1001551357238:
                        await bot.send_message(
                            chat,
                            f"⁭💖💖                        💖💖\n 💖💖                      💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n💖💖💖💖💖💖💖💖💖\n💖💖💖💖💖💖💖💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n\n                    💖\n                  💖💖\n               💖💖💖\n            💖💖 💖💖\n          💖💖    💖💖\n        💖💖       💖💖\n      💖💖💖💖💖💖\n     💖💖💖💖💖💖💖\n   💖💖                 💖💖\n  💖💖                    💖💖\n💖💖                       💖💖\n\n💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗💗\n💗💗                     💗💗\n💗💗                     💗💗\n💗💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗\n💗💗\n💗💗\n💗💗\n💗💗\n\n💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗💗\n💗💗                     💗💗\n💗💗                     💗💗\n💗💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗\n💗💗\n💗💗\n💗💗\n💗💗\n\n💙💙                    💙💙\n   💙💙              💙💙\n      💙💙        💙💙\n         💙💙  💙💙\n            💙💙💙\n              💙💙\n              💙💙\n              💙💙\n              💙💙\n              💙💙\n h💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙\n💙💙                      💙💙\n💙💙                         💙💙\n💙💙                         💙💙\n💙💙                         💙💙\n💙💙                         💙💙\n💙💙                      💙💙\n💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙\n\n💗💗💗💗💗💗\n💗💗💗💗💗💗\n          💗💗\n         💗💗\n          💗💗\n          💗💗\n          💗💗\n          💗💗\n💗💗💗💗💗💗\n💗💗💗💗💗💗\n⁭\n💗💗                               💗💗\n💗💗                               💗💗\n💗💗                               💗💗\n💗💗                               💗💗\n💗💗              💗            💗💗\n 💗💗           💗💗          💗💗\n 💗💗        💗💗💗       💗💗\n  💗💗   💗💗  💗💗   💗💗\n   💗💗💗💗      💗💗💗💗\n    💗💗💗             💗💗💗\n⁭\n                    💖\n                  💖💖\n               💖💖💖\n            💖💖 💖💖\n          💖💖    💖💖\n        💖💖       💖💖\n      💖💖💖💖💖💖\n     💖💖💖💖💖💖💖\n   💖💖                 💖💖\n  💖💖                    💖💖\n💖💖                       💖💖\n⁭\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟💟💟💟💟💟💟\n💟💟💟💟💟💟💟💟\n⁭\n💗💗💗💗💗💗\n💗💗💗💗💗💗\n          💗💗\n          💗💗\n          💗💗\n          💗💗\n          💗💗\n          💗💗\n💗💗💗💗💗💗\n💗💗💗💗💗💗",
                        )
                        lol += 1
                    elif chat == -1001551357238:
                        pass
                except BaseException:
                    sed += 1
    else:
        return await hol.edit(
            "Please give a flag to Send Diwali Wishes . \n\n**Available flags are :** \n• -a : To Wish Diwali in all chats. \n• -p : To Wish Diwali in private chats. \n• -g : To Wish Diwali in groups."
        )
    UwU = sed + lol
    if type == "-a":
        omk = "Chats"
    elif type == "-p":
        omk = "PM"
    elif type == "-g":
        omk = "Groups"
    await hol.edit(
        f"**Diwali Message Executed Successfully !!** \n\n** Sent in :** `{lol} {omk}`\n**📍 Failed in :** `{sed} {omk}`\n**📍 Total :** `{UwU} {omk}`"
    )





#official Hacker 