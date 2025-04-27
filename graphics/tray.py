from typing import Any, Callable
from pystray import Icon
from common.mode_manager import ModeManager
# from graphics.gui import run_window
from time import sleep
from images.images import load_image 



def load_icon(mode_manager: ModeManager) -> Callable[[Any], None]:
    def setup(icon) -> None:
        icon.visible = True
        previous = None
        while icon.visible:  # Ensure the thread stops if the icon is closed
            current = mode_manager.get_mode()
            if current != previous:
                previous = current
                icon.icon = load_image(current)
            sleep(0.1)  # Avoid 100% CPU usage
    return setup


def run_icon(mode_manager: ModeManager):
    mode = mode_manager.get_mode()
    icon = Icon(
        "omnivim",
        load_image(mode),
        # menu=Menu(
        #     MenuItem("Open", lambda: run_window(mode_manager), default=True),
        # ),
    )
    setup = load_icon(mode_manager)
    icon.run(setup)
