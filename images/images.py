from PIL.ImageFile import ImageFile
from common.mode import Mode
from PIL import Image


def load_image(mode: Mode) -> ImageFile:
    images = {
        Mode.NORMAL: "images/omnivimn.png",
        Mode.VISUAL: "images/omnivimv.png",
        Mode.INSERT: "images/omnivimi.png",
        Mode.MOUSE: "images/omnivimm.png",
    }

    if mode not in images:  # Catch errors
        return Image.open("images/omnivim.png")
    return Image.open(images[mode])
