# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainxuRRCS.ui'
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
        Main.resize(830, 640)
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 120, 481, 391))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.logo_lbl = QLabel(self.centralwidget)
        self.logo_lbl.setObjectName(u"logo_lbl")
        self.logo_lbl.setGeometry(QRect(700, 10, 70, 70))
        self.logo_lbl.setStyleSheet(u"")
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Main", u"TextLabel", None))
        self.logo_lbl.setText(QCoreApplication.translate("Main", u"tino", None))
    # retranslateUi

