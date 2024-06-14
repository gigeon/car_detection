from PySide2.QtWidgets import QMainWindow
from ui.ui_login import Ui_Login
from layout.mainLayout import mainLayoutClass
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtCore import Qt

class loginLayoutClass(QMainWindow, Ui_Login) :
    def __init__(self, app, dbc):
        super(loginLayoutClass, self).__init__()
        self.setupUi(self)
        self.app = app
        self.dbc = dbc
        self.login_btn.clicked.connect(self.login)
        pixmap = QPixmap('images/tino.png')
        pixmap = pixmap.scaled(self.logo_lbl.size(),Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logo_lbl.setPixmap(pixmap)
        self.setWindowTitle('carDetection')
        self.setWindowIcon(QIcon('images/tino.png'))
        
        
    def login(self):
        self.id = self.id_txt.text()
        self.pwd = self.pwd_txt.text()
        query = "SELECT USER_ID, USER_PWD FROM CONFIG"
        rows = self.dbc.select(query)
        if self.id == rows[0]['user_id'] and self.pwd == rows[0]['user_pwd'] :
            mainLayout = mainLayoutClass(self.app, self.dbc)
            self.setCentralWidget(mainLayout)
        
    