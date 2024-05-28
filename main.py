from PySide2.QtWidgets import (
    QMainWindow,
    QApplication
)
import sys
import logging
from loginLayout import loginLayoutClass
from db import DBController

file_logger = logging.getLogger("log")

def main():
    dbc = DBController()
    app = QApplication(sys.argv)
    loginUi = loginLayoutClass(app, dbc)
    loginUi.show()
    app.exec_()
    
if __name__ == "__main__" :
    main()