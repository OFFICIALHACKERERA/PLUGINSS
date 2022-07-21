import nekos

from Deepak import legend

from ..core.managers import eor

menu_category = "fun"


@legend.legend_cmd(
    pattern="why$",
    command=("why", menu_category),
    info={
        "header": "Sends you some random Funny questions",
        "usage": "{tr}why",
    },
)
async def hmm(legend):
    "Some random Funny questions"
    lol = nekos.why()
    await eor(legend, lol)


@legend.legend_cmd(
    pattern="fact$",
    command=("fact", menu_category),
    info={
        "header": "Sends you some random facts",
        "usage": "{tr}fact",
    },
)
async def hmm(legend):
    "Some random facts"
    tol = nekos.fact()
    await eor(legend, tol)
