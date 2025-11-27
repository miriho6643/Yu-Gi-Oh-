import os, importlib
from utilities import *
from characters import *
libs = ["pyttsx3", "time", "random"]

for lib in libs:
    try:
        importlib.import_module(lib)
    except ImportError:
        os.system(f"python -m pip install {lib}")
        importlib.import_module(lib)

gameplay.connect("spielwiese.local")