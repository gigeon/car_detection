from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import (
    Slot,
)
from ui.ui_login import Ui_Login
from mainLayout import mainLayoutClass

class loginLayoutClass(QMainWindow, Ui_Login) :
    def __init__(self, app, dbc):
        super(loginLayoutClass, self).__init__()
        self.setupUi(self)
        self.app = app
        self.dbc = dbc
        self.login_btn.clicked.connect(self.login)
        
    def login(self):
        self.id = self.id_txt.text()
        self.pwd = self.pwd_txt.text()
        query = "SELECT USER_ID, USER_PWD FROM CONFIG"
        row = self.dbc.select(query)
        # if self.id == row[0]['user_id'] and self.pwd == row[0]['user_pwd'] :
        #     mainLayout = mainLayoutClass(self.app)
        #     self.setCentralWidget(mainLayout)
        mainLayout = mainLayoutClass(self.app)
        self.setCentralWidget(mainLayout)