from pynput.mouse import Button, Controller
from pynput.keyboard import Controller, Key
import keyboard
from Windows_Mouse_Movments.normal_mode import normal_on_key_event as normal
from Windows_Mouse_Movments.mouse_mode import mouse_on_key_event as mouse
from Windows_Mouse_Movments.visual_mode import visual_on_key_event as visual



ctrl_mode = False
shift_mode = False

def run_windows():
    def write_mode(mode):
        with open("vimmode.txt", "w") as f:
            f.truncate(0)
            f.write(mode)
        f.close()
    def on_key_event(event):
        global ctrl_mode,shift_mode
        with open("vimmode.txt", "r") as f:
            mode = f.read().strip()
        f.close()
        if event.event_type == 'down':
            if mode == "normal":
                match event.name:
                    case "i":
                        write_mode("insert")
                        return False
                    case "v":
                        write_mode("visual")
                        return False
                    case "m":
                        write_mode("mouse")
                        return False
            elif (ctrl_mode and event.name == "c") or event.name=="esc":
                keyboard.release("ctrl")
                write_mode("normal")
                ctrl_mode=False
                return False
            match mode:
                case "visual":
                    if event.name == "ctrl":
                        ctrl_mode = True
                        return False
                    else:
                        visual(event)   
                case "normal":
                    if event.name == "ctrl":
                        ctrl_mode = True
                        return False
                    else:
                        normal(event)
                case "mouse":
                    if event.name == "ctrl":
                        ctrl_mode = True
                        return False
                    else:
                        mouse(event)
                case "insert":
                    if event.event_type == "down":
                        if event.name == "ctrl":
                            keyboard.press(event.name) 
                            ctrl_mode = True
                            return False
                        elif event.name =="shift":
                            shift_mode = True
                            return False
                        elif shift_mode:
                            if event.name.isalpha():  # Check if it's a letter
                                keyboard.write(event.name.upper())  # Convert to uppercase directly
                            else:
                                keyboard.write("event.name")  # Use shift for non-letters
                            return False

                        else:
                            keyboard.press(event.name)
                            return False
        elif event.event_type == 'up' and mode == "mouse":
            mouse(event)
            return False
        elif event.event_type == "up":
            if event.name == "ctrl":
                keyboard.release(event.name)
                ctrl_mode = False
            elif event.name == "shift":
                keyboard.release(event.name)
                shift_mode = False
            else:
                keyboard.release(event.name)
    keyboard.hook(on_key_event, suppress=True)
    # keyboard.wait("ctrl+f4") QPDfGJCBm shift + )shift + _shift + _shift + _
