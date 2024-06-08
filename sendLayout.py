from ui.ui_send import Ui_Send
from lib.layoutClass import layoutClass

class sendLayoutClass(layoutClass, Ui_Send):
    def __init__(self, app, dbc):
        super(sendLayoutClass, self).__init__()
        self.setupUi(self)
        self.set_logo()
        self.app = app
        self.dbc = dbc
        self.logo_btn.clicked.connect(self.close_layout)
        

        