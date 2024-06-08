# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sendAZJeFu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Send(object):
    def setupUi(self, Send):
        if not Send.objectName():
            Send.setObjectName(u"Send")
        Send.resize(828, 633)
        Send.setMinimumSize(QSize(828, 633))
        Send.setMaximumSize(QSize(828, 633))
        self.centralwidget = QWidget(Send)
        self.centralwidget.setObjectName(u"centralwidget")
        self.number_list = QTextEdit(self.centralwidget)
        self.number_list.setObjectName(u"number_list")
        self.number_list.setGeometry(QRect(299, 220, 231, 191))
        self.excel_btn = QPushButton(self.centralwidget)
        self.excel_btn.setObjectName(u"excel_btn")
        self.excel_btn.setGeometry(QRect(299, 430, 101, 26))
        self.api_btn = QPushButton(self.centralwidget)
        self.api_btn.setObjectName(u"api_btn")
        self.api_btn.setGeometry(QRect(429, 430, 101, 26))
        self.logo_lbl = QLabel(self.centralwidget)
        self.logo_lbl.setObjectName(u"logo_lbl")
        self.logo_lbl.setGeometry(QRect(720, 10, 70, 70))
        self.logo_lbl.setStyleSheet(u"")
        self.logo_lbl.setAlignment(Qt.AlignCenter)
        Send.setCentralWidget(self.centralwidget)

        self.retranslateUi(Send)

        QMetaObject.connectSlotsByName(Send)
    # setupUi

    def retranslateUi(self, Send):
        Send.setWindowTitle(QCoreApplication.translate("Send", u"MainWindow", None))
        self.excel_btn.setText(QCoreApplication.translate("Send", u"\uc5d1\uc140 \uc800\uc7a5", None))
        self.api_btn.setText(QCoreApplication.translate("Send", u"API \uc804\uc1a1", None))
        self.logo_lbl.setText(QCoreApplication.translate("Send", u"tino", None))
    # retranslateUi

