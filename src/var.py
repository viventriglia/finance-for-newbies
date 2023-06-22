import pathlib 
from PIL import Image
import os
import numpy as np

script_running_path = str(pathlib.Path(__file__).parent.resolve())
split_script_running_path =  np.char.rpartition(script_running_path, '/')
assets_path= str(split_script_running_path[0])

GLOBAL_STREAMLIT_STYLE = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

DATA_PATH = pathlib.Path(assets_path, "data", "in")

FAVICON = Image.open(pathlib.Path(assets_path, "images", "favicon.ico"))
