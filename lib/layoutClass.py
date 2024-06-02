from PySide2.QtWidgets import (
    QMainWindow,
)
from PySide2.QtGui import QPixmap
from PySide2.QtCore import (
    Qt,
)


class layoutClass(QMainWindow):
    def set_logo(self):
        pixmap = QPixmap('images/tino.png')
        pixmap = pixmap.scaled(self.logo_lbl.size(),Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logo_lbl.setPixmap(pixmap)