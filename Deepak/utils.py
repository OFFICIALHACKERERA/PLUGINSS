import sys
import logging
import importlib
from pathlib import Path

def load_assistant(plugin_name):
    path = Path(f"Deepak/assistant/{plugin_name}.py")
    name = "Deepak.assistant.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["Deepak.assistant." + plugin_name] = load
    print("Bot has Started " + plugin_name)
