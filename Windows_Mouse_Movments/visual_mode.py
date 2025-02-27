from pynput.keyboard import Controller
import keyboard

from common.mode import Mode
d_mode, g_mode = False,False
kb_controller = Controller()

def visual_on_key_event(event) -> Mode: #Visual Mode Function
    global d_mode, g_mode
    if event.event_type != 'down':
        return Mode.VISUAL
    #Only want to do an action when the key down
    if not d_mode and not g_mode:# Checks for special Cases
        match event.name: # Vim commands on visual mode
            case "h":
                keyboard.send("right shift+left shift+left_arrow")
                return Mode.VISUAL
            case "j":
                keyboard.send("right shift+left shift+down_arrow")
                return Mode.VISUAL
            case "k":
                keyboard.send("right shift+left shift+up_arrow")
                return Mode.VISUAL
            case "l":
                keyboard.send("right shift+left shift+right_arrow")
                return Mode.VISUAL
            case "b":
                keyboard.send("ctrl+right shift+left shift+left_arrow")
                return Mode.VISUAL
            case "w":
                keyboard.send("ctrl+right shift+left shift+right_arrow")
                return Mode.VISUAL
            case "0":
                keyboard.send("right shift+left shift+home")
                keyboard.send("right shift+left shift+home")
                return Mode.VISUAL
            case "^":
                keyboard.send("right shift+left shift+home")
                keyboard.release("shift")
                return Mode.VISUAL
            case "$":
                keyboard.send("right shift+left shift+end")
                keyboard.release("shift")
                return Mode.VISUAL
            case "G":
                keyboard.send("ctrl+right shift+left shift+end")
                keyboard.release("shift")
                return Mode.VISUAL
            case "g":
                g_mode = True
                return Mode.VISUAL
            case "y":
                keyboard.press_and_release("ctrl + c")
                keyboard.press_and_release("left_arrow")
                keyboard.press_and_release("right_arrow")
                return Mode.NORMAL
            case "x":
                keyboard.send("backspace")
                return Mode.NORMAL
    elif g_mode: #G mode 
        match event.name:
            case "g":
                keyboard.send("ctrl+right shift+left shift+home")
        g_mode = Mode.VISUAL
        return Mode.VISUAL
    return Mode.VISUAL
