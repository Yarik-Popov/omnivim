import keyboard
from Windows_Mouse_Movments.normal_mode import normal_on_key_event as normal
from Windows_Mouse_Movments.mouse_mode import mouse_on_key_event as mouse
from Windows_Mouse_Movments.visual_mode import visual_on_key_event as visual
from common.mode import Mode
from common.mode_manager import ModeManager


ctrl_mode = False
shift_mode = False

# wrapper function required for main.py to run
def run_windows(mode_manager: ModeManager):

    def on_key_event(event):
        global ctrl_mode,shift_mode
        mode = mode_manager.get_mode()

        if event.event_type == 'down':

            # only allow switching to other modes from normal mode
            if mode == Mode.NORMAL:

                match event.name:
                    case "i":
                        mode_manager.set_mode(Mode.INSERT)
                        return False
                    case "v":
                        mode_manager.set_mode(Mode.VISUAL)
                        return False
                    case "m":
                        mode_manager.set_mode(Mode.MOUSE)
                        return False

                # saving in normal mode
                if ctrl_mode and event.name == "s":
                    keyboard.press_and_release("ctrl+s")
                    ctrl_mode = False
                    return False

            # exit back to normal mode
            elif ((ctrl_mode and event.name == "c") or event.name=="esc") and mode != Mode.OFF:
                keyboard.release("ctrl")
                keyboard.release("shift")
                mode_manager.set_mode(Mode.NORMAL)
                ctrl_mode=False
                return False
            match mode:
                case Mode.VISUAL:
                    if event.name == "shift":
                        shift_mode = True
                    if event.name == "ctrl":
                        ctrl_mode = True
                    elif shift_mode and ctrl_mode:
                        if event.name == "q":
                            mode_manager.set_mode(Mode.OFF)
                    else:
                        mode_manager.set_mode(visual(event))
                case Mode.NORMAL:
                    if event.name == "shift":
                        shift_mode = True
                    if event.name == "ctrl":
                        ctrl_mode = True
                    elif shift_mode and ctrl_mode:
                        if event.name == "Q":
                            mode_manager.set_mode(Mode.OFF)
                    else:
                        mode_manager.set_mode(normal(event))

                case Mode.MOUSE:
                    if event.name == "shift":
                        shift_mode = True 
                    if event.name == "ctrl":
                        ctrl_mode = True
                    elif shift_mode and ctrl_mode:
                        if event.name == "q":
                            mode_manager.set_mode(Mode.OFF)
                    else:
                        mode_manager.set_mode(mouse(event))
                        shift_mode = False
                        ctrl_mode = False

                case Mode.INSERT | Mode.OFF:
                    if event.event_type == "down":
                        # allows for default key-binds to be used in insert mode
                        if event.name == "ctrl":
                            keyboard.press(event.name)
                            ctrl_mode = True
                        # allows for typing shifted keys
                        if event.name =="shift":
                            shift_mode = True
                        if shift_mode and not ctrl_mode:
                            # if alphabetic and one character long (not SPACE, BACKSPACE, or ENTER)
                            if event.name.isalpha() and len(event.name) == 1:
                                keyboard.write(event.name.upper())
                                return False
                            elif event.name in ["up","down","left","right"]:
                                keyboard.send(f"right shift + left shift + {event.name}")
                                return False
                            else:

                                # hard coded because shift + = returns errors
                                if event.name == "+":
                                    keyboard.send("+")
                                else:
                                    keyboard.press(f"shift+{event.name}")
                                return False
                        elif shift_mode and ctrl_mode:
                            if event.name == "q":
                                mode_manager.set_mode(Mode.NORMAL if mode == Mode.OFF else Mode.OFF)
                            elif event.name in ["up","down","left","right"]:
                                keyboard.send(f"ctrl+right shift + left shift + {event.name}")
                                return False
                            else:
                                keyboard.send(f"ctrl+shift+{event.name}")
                        else:
                            keyboard.press(event.name)
                            return False
                    return False

        # release held keys for mouse navigation
        elif event.event_type == 'up' and mode == "mouse":
            mode_manager.set_mode(mouse(event))
            return False

        # release held keys for multi key combos 
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
