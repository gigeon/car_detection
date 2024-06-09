from PySide2.QtWidgets import QMainWindow
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import Qt


class layoutClass(QMainWindow):
    def set_logo(self):
        pixmap = QPixmap('images/tino.png')
        pixmap = pixmap.scaled(self.logo_btn.size(),Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon = QIcon(pixmap)
        self.logo_btn.setIcon(icon)
        self.logo_btn.setIconSize(pixmap.size())

    