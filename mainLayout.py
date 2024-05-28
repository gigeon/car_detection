from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import (
    Slot,
    Qt,
)
from PySide2.QtGui import QPixmap
from ui.ui_main import Ui_Main
from db import DBController
class mainLayoutClass(QMainWindow, Ui_Main) :
    def __init__(self, app):
        super(mainLayoutClass, self).__init__()
        self.setupUi(self)
        self.app = app
        pixmap = QPixmap('images/tino.png')
        pixmap = pixmap.scaled(self.logo_lbl.size(),Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logo_lbl.setPixmap(pixmap)