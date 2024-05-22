from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import (
    Slot,
)
from ui.ui_login import Ui_Login
from db import DBController

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
        row = self.dbc.select("SELECT ID, PWD from CONFIG")
