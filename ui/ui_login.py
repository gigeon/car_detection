# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginxCDjkz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(828, 633)
        Login.setMinimumSize(QSize(828, 633))
        Login.setMaximumSize(QSize(828, 633))
        self.id_label = QLabel(Login)
        self.id_label.setObjectName(u"id_label")
        self.id_label.setGeometry(QRect(340, 390, 81, 16))
        self.login_btn = QPushButton(Login)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(410, 460, 75, 25))
        self.id_txt = QLineEdit(Login)
        self.id_txt.setObjectName(u"id_txt")
        self.id_txt.setGeometry(QRect(420, 390, 113, 20))
        self.pwd_txt = QLineEdit(Login)
        self.pwd_txt.setObjectName(u"pwd_txt")
        self.pwd_txt.setGeometry(QRect(420, 420, 113, 21))
        self.pwd_label = QLabel(Login)
        self.pwd_label.setObjectName(u"pwd_label")
        self.pwd_label.setGeometry(QRect(340, 420, 81, 16))
        self.logo_lbl = QLabel(Login)
        self.logo_lbl.setObjectName(u"logo_lbl")
        self.logo_lbl.setGeometry(QRect(290, 140, 291, 161))
        self.logo_lbl.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.id_label.setText(QCoreApplication.translate("Login", u"\uc544\uc774\ub514", None))
        self.login_btn.setText(QCoreApplication.translate("Login", u"\ub85c\uadf8\uc778", None))
        self.pwd_label.setText(QCoreApplication.translate("Login", u"\ube44\ubc00\ubc88\ud638", None))
        self.logo_lbl.setText(QCoreApplication.translate("Login", u"TextLabel", None))
    # retranslateUi

