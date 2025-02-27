from enum import Enum, auto
from typing import Callable

class Mode(Enum):
    NORMAL = auto()
    OFF = auto()
    VISUAL = auto()
    INSERT = auto()
    MOUSE = auto()

type ModeCallback = Callable[[Mode], None]
     
