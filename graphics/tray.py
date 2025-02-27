from typing import Any, Callable
from PIL.ImageFile import ImageFile
from pystray import Icon, MenuItem, Menu
from common.mode_manager import ModeManager
from common.mode import Mode
from graphics.gui import run_window
from PIL import Image
from time import sleep

def load_image(mode_manager: ModeManager) -> ImageFile:
    typ = mode_manager.get_mode()
    images = {
        Mode.NORMAL: "Images/omnivimn.png",
        Mode.VISUAL: "Images/omnivimv.png",
        Mode.INSERT: "Images/omnivimi.png",
        Mode.MOUSE: "Images/omnivimm.png",
    }

    if typ not in images:  # Catch errors
        return Image.open("Images/omnivim.png")
    return Image.open(images[typ])



def load_icon(mode_manager: ModeManager) -> Callable[[Any], None]:
    def setup(icon) -> None:
        icon.visible = True
        while icon.visible:  # Ensure the thread stops if the icon is closed
            icon.icon = load_image(mode_manager)
            sleep(0.1)  # Avoid 100% CPU usage
    return setup


def run_icon(mode_manager: ModeManager):
    icon = Icon(
        "omnivim",
        load_image(mode_manager),
        menu=Menu(
            MenuItem("Open", lambda: run_window(mode_manager), default=True),
        ),
    )
    setup = load_icon(mode_manager)
    icon.run(setup)
