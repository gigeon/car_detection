from PySide2.QtWidgets import QApplication
import sys
from layout.loginLayout import loginLayoutClass
from lib.db import DBController


def main():
    dbc = DBController()
    app = QApplication(sys.argv)
    loginUi = loginLayoutClass(app, dbc)
    loginUi.show()
    app.exec_()
    
if __name__ == "__main__" :
    main()