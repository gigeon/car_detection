# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainObszSU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(828, 633)
        Main.setMinimumSize(QSize(828, 633))
        Main.setMaximumSize(QSize(828, 633))
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.vid_lbl = QLabel(self.centralwidget)
        self.vid_lbl.setObjectName(u"vid_lbl")
        self.vid_lbl.setGeometry(QRect(40, 120, 481, 391))
        self.vid_lbl.setAutoFillBackground(False)
        self.vid_lbl.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.vid_lbl.setAlignment(Qt.AlignCenter)
        self.number_list = QTextEdit(self.centralwidget)
        self.number_list.setObjectName(u"number_list")
        self.number_list.setGeometry(QRect(560, 220, 231, 191))
        self.spot_lbl = QLabel(self.centralwidget)
        self.spot_lbl.setObjectName(u"spot_lbl")
        self.spot_lbl.setGeometry(QRect(560, 160, 231, 41))
        self.spot_lbl.setStyleSheet(u"background-color: rgb(200,200,200);")
        self.spot_lbl.setAlignment(Qt.AlignCenter)
        self.send_btn = QPushButton(self.centralwidget)
        self.send_btn.setObjectName(u"send_btn")
        self.send_btn.setGeometry(QRect(560, 430, 231, 41))
        self.file_btn = QPushButton(self.centralwidget)
        self.file_btn.setObjectName(u"file_btn")
        self.file_btn.setGeometry(QRect(240, 520, 100, 31))
        self.pwd_lbl = QLineEdit(self.centralwidget)
        self.pwd_lbl.setObjectName(u"pwd_lbl")
        self.pwd_lbl.setGeometry(QRect(170, 40, 191, 25))
        self.pwd_lbl.setMaxLength(10)
        self.text_lbl = QLabel(self.centralwidget)
        self.text_lbl.setObjectName(u"text_lbl")
        self.text_lbl.setGeometry(QRect(90, 40, 71, 20))
        self.text_lbl.setStyleSheet(u"font: 8pt \"Agency FB\";")
        self.ok_btn = QPushButton(self.centralwidget)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setGeometry(QRect(370, 40, 51, 26))
        self.ok_btn.setStyleSheet(u"font: 8pt \"Agency FB\";")
        self.logo_btn = QPushButton(self.centralwidget)
        self.logo_btn.setObjectName(u"logo_btn")
        self.logo_btn.setGeometry(QRect(720, 10, 70, 70))
        self.logo_btn.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: none")
        self.hide_btn = QPushButton(self.centralwidget)
        self.hide_btn.setObjectName(u"hide_btn")
        self.hide_btn.setGeometry(QRect(70, 20, 371, 71))
        self.hide_btn.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: none")
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"MainWindow", None))
        self.vid_lbl.setText(QCoreApplication.translate("Main", u"\ud45c\ucd9c\ud55c \uc774\ubbf8\uc9c0 \ud30c\uc77c \uc5c6\uc74c.", None))
        self.spot_lbl.setText(QCoreApplication.translate("Main", u"TextLabel", None))
        self.send_btn.setText(QCoreApplication.translate("Main", u"\uc804\uc1a1", None))
        self.file_btn.setText(QCoreApplication.translate("Main", u"\ud30c\uc77c \uc5c5\ub85c\ub4dc", None))
        self.text_lbl.setText(QCoreApplication.translate("Main", u"\ube44\ubc00\ubc88\ud638", None))
        self.ok_btn.setText(QCoreApplication.translate("Main", u"\ud655\uc778", None))
        self.logo_btn.setText("")
        self.hide_btn.setText("")
    # retranslateUi

