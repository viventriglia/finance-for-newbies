from pathlib import Path, PurePath
from PIL import Image

script_running_path = str(Path(__file__).parent.resolve())
split_script_running_path = path_split = PurePath(script_running_path).parts
assets_path = str(split_script_running_path[0])

GLOBAL_STREAMLIT_STYLE = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .css-15zrgzn {display: none}
            </style>
            """

DATA_PATH = Path(assets_path, "data", "in")

CACHE_EXPIRE_SECONDS = 600

# FAVICON = Image.open(Path(assets_path, "images", "favicon.ico"))
