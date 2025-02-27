from threading import Thread
from Windows_Mouse_Movments.main_windows import run_windows
from common.mode import Mode
from common.mode_manager import ModeManager
from graphics.tray import run_icon



def main():  # Start program
    default_mode = Mode.NORMAL
    set_callbacks = []
    mode_manager = ModeManager(default_mode, set_callbacks)
    t1 = Thread(target=lambda: run_windows(mode_manager), daemon=True)
    t1.start()
    run_icon(mode_manager)




if __name__ == "__main__":
    main()
