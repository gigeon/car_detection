# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginIajmql.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(382, 280)
        self.id_label = QLabel(Form)
        self.id_label.setObjectName(u"id_label")
        self.id_label.setGeometry(QRect(90, 150, 56, 12))
        self.login_btn = QPushButton(Form)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(150, 210, 75, 23))
        self.id_txt = QLineEdit(Form)
        self.id_txt.setObjectName(u"id_txt")
        self.id_txt.setGeometry(QRect(160, 140, 113, 20))
        self.pwd_txt = QLineEdit(Form)
        self.pwd_txt.setObjectName(u"pwd_txt")
        self.pwd_txt.setGeometry(QRect(160, 170, 113, 21))
        self.pwd_label = QLabel(Form)
        self.pwd_label.setObjectName(u"pwd_label")
        self.pwd_label.setGeometry(QRect(90, 180, 56, 12))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.id_label.setText(QCoreApplication.translate("Form", u"\uc544\uc774\ub514", None))
        self.login_btn.setText(QCoreApplication.translate("Form", u"\ub85c\uadf8\uc778", None))
        self.pwd_label.setText(QCoreApplication.translate("Form", u"\ube44\ubc00\ubc88\ud638", None))
    # retranslateUi

