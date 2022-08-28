


import glob
from pathlib import Path
from Deepak.utils import load_assistant
import logging
from Deepak import Deepak

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "Deepak/assistant/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_assistant(plugin_name.replace(".py", ""))
    
print("Successfully Started Bot!")
print("Visit @TheUpdatesChannel")

if __name__ == "__main__":
    Deepak.run_until_disconnected()
