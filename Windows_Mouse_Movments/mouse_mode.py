import threading
import time

import pyautogui
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Button, Controller

from common.mode import Mode

mouse = Controller()
kb_controller = KeyboardController()

# Flags to control mouse movement
moving_left = False 
moving_right = False 
moving_up = False 
moving_down = False 
scrolling_down = False 
scrolling_up = False 
speed_multiplier = 1

# Get screen size
screen_width, screen_height = pyautogui.size()

# Define screen segments (4 horizontal, 3 vertical)
segment_width = screen_width // 4
segment_height = screen_height // 3
segments = [
    (0, 0),
    (segment_width, 0),
    (2 * segment_width, 0),
    (3 * segment_width, 0),
    (0, segment_height),
    (segment_width, segment_height),
    (2 * segment_width, segment_height),
    (3 * segment_width, segment_height),
    (0, 2 * segment_height),
    (segment_width, 2 * segment_height),
    (2 * segment_width, 2 * segment_height),
    (3 * segment_width, 2 * segment_height),
]


def move_mouse_left():
    global moving_left, speed_multiplier
    while moving_left:
        mouse.move(-4 * speed_multiplier, 0)
        time.sleep(0.01)


def move_mouse_right():
    global moving_right, speed_multiplier
    while moving_right:
        mouse.move(4 * speed_multiplier, 0)
        time.sleep(0.01)


def move_mouse_up():
    global moving_up, speed_multiplier
    while moving_up:
        mouse.move(0, -4 * speed_multiplier)
        time.sleep(0.01)


def move_mouse_down():
    global moving_down, speed_multiplier
    while moving_down:
        mouse.move(0, 4 * speed_multiplier)
        time.sleep(0.01)

def scroll_down():
    global scrolling_down,speed_multiplier
    while scrolling_down:
        mouse.scroll(0,-0.33*speed_multiplier)
        time.sleep(0.01)

def scroll_up():
    global scrolling_up,speed_multiplier
    while scrolling_up:
        mouse.scroll(0,0.33*speed_multiplier)
        time.sleep(0.01)


def mouse_on_key_event(event) -> Mode:
    global moving_left, moving_right, moving_up, moving_down, speed_multiplier,scrolling_up,scrolling_down
    if event.event_type == "down":
        match event.name:
            case "h" | "l" | "k" | "j"| "u" | "i":
                speed_multiplier = 1
            case "H" | "L" | "K" | "J"| "U" | "I":
                speed_multiplier = 3

        if event.name in ["h", "H"] and not moving_left:
            moving_left = True
            threading.Thread(target=move_mouse_left, daemon=True).start()
            return Mode.MOUSE
        elif event.name in ["l", "L"] and not moving_right:
            moving_right = True
            threading.Thread(target=move_mouse_right, daemon=True).start()
            return Mode.MOUSE
        elif event.name in ["k", "K"] and not moving_up:
            moving_up = True
            threading.Thread(target=move_mouse_up, daemon=True).start()
            return Mode.MOUSE
        elif event.name in ["j", "J"] and not moving_down:
            moving_down = True
            threading.Thread(target=move_mouse_down, daemon=True).start()
            return Mode.MOUSE
        elif event.name in ["i", "I"] and not moving_down:
            scrolling_down = True
            threading.Thread(target=scroll_down, daemon=True).start()
            return Mode.MOUSE
        elif event.name in ["u", "U"] and not moving_up:
            scrolling_up = True
            threading.Thread(target=scroll_up, daemon=True).start()
            return Mode.MOUSE
        elif event.name in ["q", "w", "e", "r", "a", "s", "d", "f", "z", "x", "c", "v"]:
            segment_index = {
                "q": 0,
                "w": 1,
                "e": 2,
                "r": 3,
                "a": 4,
                "s": 5,
                "d": 6,
                "f": 7,
                "z": 8,
                "x": 9,
                "c": 10,
                "v": 11,
            }
            x, y = segments[segment_index[event.name]]
            mouse.position = (
                x + segment_width // 2,
                y + segment_height // 2,
            )  # Center of the segment
            return Mode.MOUSE
        elif event.name == "space":
            mouse.click(Button.left)
            return Mode.MOUSE
        elif event.name == "n":
            mouse.click(Button.right)
            return Mode.MOUSE
    elif event.event_type == "up":
        match event.name:
            case "h" | "H":
                moving_left = False
            case "l" | "L":
                moving_right = False
            case "k" | "K":
                moving_up = False
            case "j" | "J":
                moving_down = False
            case "u" | "U":
                scrolling_up = False
            case "i" | "I":
                scrolling_down = False
        return Mode.MOUSE
    return Mode.MOUSE
