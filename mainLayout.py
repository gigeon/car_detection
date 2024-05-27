from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import (
    Slot,
)
from ui.ui_main import Ui_Main
from db import DBController

class mainLayoutClass(QMainWindow, Ui_Main) :
    def __init__(self, app):
        super(mainLayoutClass, self).__init__()
        self.app = app