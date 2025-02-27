from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys
import os

from common.mode import Mode
from common.mode_manager import ModeManager

class MainWindow(QWidget):

    def __init__(self, mode_manager: ModeManager):
        super(MainWindow, self).__init__()
        self._mode_manger = mode_manager

        self.layout = QVBoxLayout()
        self.label = QLabel(self)

        pixmap = QPixmap("Images/omnivimtitle.png")  # Replace with actual image path
        self.label.setPixmap(pixmap.scaled(354, 72, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

        self.layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setWindowTitle("Omnivim")
        self.setLayout(self.layout)
        self.extratext = ""
        
        typ = mode_manager.get_mode()
        
        if typ == Mode.OFF:
            self.extratext = "Turn on"
        else:
            self.extratext = "Turn off"

        script_dir = os.path.dirname(os.path.abspath(__file__))
        font_path = os.path.join(script_dir, "Ibm.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)
        font_family = QFontDatabase.applicationFontFamilies(font_id)
        if font_id == -1:
            print("Error: Font not loaded.")
            return
        font = QFont(font_family)

        self.button = QPushButton(f'{self.extratext} Omnivim')
        self.button.setFont(font)

        font.setPointSize(24)
        font.setWeight(900)
        self.text = QLabel('Vim motions, made global')
        self.text.setFont(font)
        self.layout.addWidget(self.text, alignment=Qt.AlignmentFlag.AlignCenter)

        self.button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button.clicked.connect(self.on_button_click)

        self.layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.textbox = QPlainTextEdit(self)
        self.textbox.setPlainText("Try me out!")
        self.layout.addWidget(self.textbox, alignment=Qt.AlignmentFlag.AlignCenter)

    def on_button_click(self):
        # Update the text based on the state
        if self.extratext == "Turn on":
            self._mode_manger.set_mode(Mode.NORMAL)
            self.extratext = "Turn off"
        else:
            self._mode_manger.set_mode(Mode.OFF)
            self.extratext = "Turn on"

        # Update the button text directly without recreating the button
        self.button.setText(f'{self.extratext} Omnivim')

        # Optionally trigger an update if needed
        self.update()

    def paintEvent(self, event):
        # No need to recreate the button here, just call the parent class's paintEvent
        super().paintEvent(event)

def load_stylesheet(filename):
    file = QFile(filename)
    file.open(QFile.OpenModeFlag.ReadOnly)
    stream = QTextStream(file)
    return stream.readAll()

from PyQt6.QtWidgets import QApplication

app = None  # Store QApplication globally
mw = None   # Store MainWindow globally

def run_window(mode_manager: ModeManager) -> None:
    global app, mw

    if mw and mw.isVisible():  # If the window is already open, bring it to the front
        mw.raise_()
        mw.activateWindow()
        return

    if not app:  # Create QApplication only if it doesn't exist
        app = QApplication.instance() or QApplication(sys.argv)
        stylesheet = load_stylesheet("style.css")
        app.setStyleSheet(stylesheet)
    mw = MainWindow(mode_manager)
    mw.resize(1, 400)
    mw.show()
