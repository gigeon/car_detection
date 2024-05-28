from lib.layoutClass import layoutClass
from PySide2.QtCore import (
    Slot,
)
from ui.ui_login import Ui_Login
from mainLayout import mainLayoutClass

class loginLayoutClass(layoutClass, Ui_Login) :
    def __init__(self, app, dbc):
        super(loginLayoutClass, self).__init__()
        self.setupUi(self)
        self.app = app
        self.dbc = dbc
        self.set_logo()
        self.login_btn.clicked.connect(self.login)
        
    def login(self):
        self.id = self.id_txt.text()
        self.pwd = self.pwd_txt.text()
        # query = "SELECT USER_ID, USER_PWD FROM CONFIG"
        # rows = self.dbc.select(query)
        # if self.id == rows[0]['user_id'] and self.pwd == rows[0]['user_pwd'] :
        #     mainLayout = mainLayoutClass(self.app)
        #     self.setCentralWidget(mainLayout)
        mainLayout = mainLayoutClass(self.app, self.dbc)
        self.setCentralWidget(mainLayout)
        
    