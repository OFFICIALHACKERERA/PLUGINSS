from .extdl import *
from .paste import *

type = True
check = 0
while type:
    try:
        from . import format as _format
        from . import tools as _legendtools
        from . import utils as _legendutils
        from .events import *
        from .format import *
        from .tools import *
        from .utils import *

        break
    except ModuleNotFoundError as e:
        install_pip(e.name)
        check += 1
        if check > 5:
            break
