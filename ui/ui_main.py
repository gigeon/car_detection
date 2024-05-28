# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWTuDpp.ui'
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
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.vid_lbl = QLabel(self.centralwidget)
        self.vid_lbl.setObjectName(u"vid_lbl")
        self.vid_lbl.setGeometry(QRect(40, 120, 481, 391))
        self.vid_lbl.setAutoFillBackground(False)
        self.vid_lbl.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.vid_lbl.setAlignment(Qt.AlignCenter)
        self.logo_lbl = QLabel(self.centralwidget)
        self.logo_lbl.setObjectName(u"logo_lbl")
        self.logo_lbl.setGeometry(QRect(720, 10, 70, 70))
        self.logo_lbl.setStyleSheet(u"")
        self.logo_lbl.setAlignment(Qt.AlignCenter)
        self.number_list = QTextEdit(self.centralwidget)
        self.number_list.setObjectName(u"number_list")
        self.number_list.setGeometry(QRect(560, 220, 231, 191))
        self.spot_lbl = QLabel(self.centralwidget)
        self.spot_lbl.setObjectName(u"spot_lbl")
        self.spot_lbl.setGeometry(QRect(560, 160, 231, 41))
        self.spot_lbl.setStyleSheet(u"background-color: rgb(200,200,200);")
        self.spot_lbl.setAlignment(Qt.AlignCenter)
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"MainWindow", None))
        self.vid_lbl.setText(QCoreApplication.translate("Main", u"TextLabel", None))
        self.logo_lbl.setText(QCoreApplication.translate("Main", u"tino", None))
        self.spot_lbl.setText(QCoreApplication.translate("Main", u"TextLabel", None))
    # retranslateUi

