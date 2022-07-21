from faker import Faker

from . import eor, legend

menu_category = "useless"


@legend.legend_cmd(
    pattern="gencc(?:\s|$)([\s\S]*)",
    command=("gencc", menu_category),
    info={
        "header": "To Make Fake Credit Card in short help u to generate fake cc",
        "usage": [
            "{tr}gencc",
        ],
    },
)
async def _(LEGENDevent):
    if LEGENDevent.fwd_from:
        return
    LEGENDcc = Faker()
    LEGENDname = LEGENDcc.name()
    LEGENDadre = LEGENDcc.address()
    LEGENDcard = LEGENDcc.credit_card_full()

    await eor(
        LEGENDevent,
        f"__**👤 NAME :- **__\n`{LEGENDname}`\n\n__**🏡 ADDRESS :- **__\n`{LEGENDadre}`\n\n__**💸 CARD :- **__\n`{LEGENDcard}`",
    )


#official Hacker 