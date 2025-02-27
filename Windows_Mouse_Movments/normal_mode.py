from pynput.keyboard import Controller, Key
import keyboard

from common.mode import Mode
d_mode, g_mode = False,False
kb_controller = Controller()


def normal_on_key_event(event) -> Mode:# Initialize Function for normal mode
    global d_mode, g_mode #Special Cases
    if event.event_type != 'down':
        return Mode.NORMAL
    # Event type must be down for us to change the type
    if not d_mode and not g_mode: # Not special Cases
        match event.name:
            case "h":
                keyboard.press_and_release("left_arrow")
                return Mode.NORMAL
            case "j":
                keyboard.press_and_release("down_arrow")
                return Mode.NORMAL
            case "k":
                keyboard.press_and_release("up_arrow")
                return Mode.NORMAL
            case "l":
                keyboard.press_and_release("right_arrow")
                return Mode.NORMAL
            case "b":
                keyboard.press_and_release("ctrl+left_arrow")
                return Mode.NORMAL
            case "w":
                keyboard.press_and_release("ctrl+right_arrow")
                return Mode.NORMAL
            case "0":
                keyboard.press_and_release("left_arrow")
                keyboard.press_and_release("home")
                keyboard.press_and_release("home")
                return Mode.NORMAL
            case "^":
                keyboard.press_and_release("home")
                keyboard.release("shift")
                return Mode.NORMAL
            case "$":
                keyboard.press_and_release("end")
                keyboard.release("shift")
                return Mode.NORMAL
            case "G":
                keyboard.press_and_release("ctrl+end")
                keyboard.release("shift")
                return Mode.NORMAL
            case "D":
                keyboard.press_and_release("left shift + right shift + end")
                keyboard.send("backspace")
                keyboard.release("shift")
                return Mode.NORMAL
            case "d":
                d_mode = True
                return Mode.NORMAL
            case "g":
                g_mode = True
                return Mode.NORMAL
            case "x":
                keyboard.press_and_release("backspace")
                return Mode.NORMAL
            case "p":
                keyboard.press_and_release("ctrl+v")
                return Mode.NORMAL
            case "o":
                keyboard.press_and_release("end")
                keyboard.press_and_release("enter")
                return Mode.INSERT
            case "O": 
                keyboard.press_and_release("up_arrow")
                keyboard.press_and_release("end")
                keyboard.press_and_release("enter")
                return Mode.INSERT
            case "u":
                keyboard.press_and_release("ctrl + z")
                return Mode.NORMAL
            case "r":
                keyboard.press_and_release("ctrl + shift + z")
                return Mode.NORMAL
            
    elif d_mode: #  Special Case D
        match event.name:
            case "d":
                keyboard.press_and_release("end")
                keyboard.press_and_release("left shift + right shift + home")
                keyboard.press_and_release("left shift + right shift + home")
                keyboard.press_and_release("space")
                keyboard.press_and_release("backspace")
                keyboard.press_and_release("backspace")
            case "w":
                keyboard.press_and_release("ctrl+left")
                keyboard.press_and_release("ctrl+right")
                keyboard.send("ctrl + right shift + left shift + left")
                keyboard.press_and_release("backspace")
        d_mode = False 
        return Mode.NORMAL
    elif g_mode: #  Special Case G
        match event.name:
            case "g":
                keyboard.press_and_release("ctrl+home")
        g_mode = False 
        return Mode.NORMAL
    return Mode.NORMAL
    



