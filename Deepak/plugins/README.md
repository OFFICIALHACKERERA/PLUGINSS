## Mandatory Imports
```python3
from Deepak import legend

from ..core.managers import eod, eor

menu_category="extra"
```

### Formation
This below one is Sample format of making plugin
```python3
from Deepak import legend

from ..core.managers import eod, eor

menu_category="extra"

#regex 

@legend.legend_cmd(
    pattern="hilegend(?:\s|$)([\s\S]*)",
    command=("hilegend", menu_category),
    info={
        "header": "Just to say hi to other user.",
        "description": "input string along with cmd will be added to your hi text",
        "usage": "{tr}hilegend <text>",
        "examples": "{tr}hilegend how are you bro",
    },
)
async def hi_legend(event):
    "Just to say hi to other user."
    input_str= event.pattern_match.group(1)
    if not input_str:
        await eod(event,"No input is found. Use proper syntax.")
        return
    outputtext= f"+-+-+-+-+-+\n|h|e|l|l|o|\n+-+-+-+-+-+\n{input_str}"
    await eor(event,outputtext)
```

Arguments in legend_cmd are as follows:
```

pattern="Regex for command"
command=("Just command name", menu_category) use menu_category name from predefined names (admin,bot,utils,tools,extra,fun,misc)
info={
        "header":string - "intro for command",
        "description": string - "Description for command\
            \nNote: If Note U Can Write Here ",
        "flags": dict or string - "Types u are using in your plugin",
        "options": dict or string - "Options u are using in your plugin",
        "types": list or string - "types u are using in your plugin",
        "usage": "Usage for your command",
        "examples": "Example for the command",
        "your custom name if you want to use other": str or list or dict - "data/information about it",
    },

groups_only=True or False(by default False) - Either your command should work only in group or not
allow_sudo=True or False(by default True) - Should your sudo users need to have access or not,
edited=True or False(by default True) - If suppose you entered wrong command syntax and if you edit it correct should it work or not.
forword=True or False(by deafult False) - Is forword messages should react or not.
disable_errors=True or False(by default False) - if any error occured during the command usage should it log or not.
require_admin=True or False(by default False) - Are u admin in group is required or not
```
