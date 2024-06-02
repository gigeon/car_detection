from lib.layoutClass import layoutClass
from PySide2.QtCore import (
    Slot,
    Qt,
)
from PySide2.QtGui import QPixmap
from ui.ui_main import Ui_Main
from db import DBController

class mainLayoutClass(layoutClass, Ui_Main) :
    def __init__(self, app, dbc):
        super(mainLayoutClass, self).__init__()
        self.setupUi(self)
        self.app = app
        self.dbc = dbc
        self.set_logo()
        
        query = "SELECT SPOT_NAME FROM CONFIG"
        rows = dbc.select(query)
        self.spot_lbl.setText(rows[0]["spot_name"])
        
        query = "SELECT ID, CAR_NO FROM NUMBER"
        rows = dbc.select(query)
        for row in rows:
            self.number_list.append(row['car_no'])
    
    