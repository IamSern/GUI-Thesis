# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LV_GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1045, 519)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QSize(1045, 0))
        self.centralwidget.setAutoFillBackground(False)
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font = QFont()
        font.setFamilies([u"MV Boli"])
        self.stackedWidget.setFont(font)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.frame_ten_gioitinh = QFrame(self.page)
        self.frame_ten_gioitinh.setObjectName(u"frame_ten_gioitinh")
        self.frame_ten_gioitinh.setGeometry(QRect(60, 40, 781, 111))
        self.frame_ten_gioitinh.setFrameShape(QFrame.StyledPanel)
        self.frame_ten_gioitinh.setFrameShadow(QFrame.Raised)
        self.enterName = QLineEdit(self.frame_ten_gioitinh)
        self.enterName.setObjectName(u"enterName")
        self.enterName.setGeometry(QRect(50, 0, 521, 41))
        font1 = QFont()
        font1.setPointSize(14)
        self.enterName.setFont(font1)
        self.checkBox = QCheckBox(self.frame_ten_gioitinh)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(580, 10, 70, 17))
        self.checkBox.setAutoExclusive(True)
        self.checkBox_2 = QCheckBox(self.frame_ten_gioitinh)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(630, 10, 70, 17))
        self.checkBox_2.setAutoExclusive(True)
        self.checkBox_2.setTristate(False)
        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -1, 61, 391))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.page)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(60, 170, 261, 141))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.temp = QLabel(self.gridLayoutWidget)
        self.temp.setObjectName(u"temp")
        font2 = QFont()
        font2.setFamilies([u"Cambria Math"])
        font2.setPointSize(14)
        self.temp.setFont(font2)

        self.gridLayout.addWidget(self.temp, 2, 0, 1, 1)

        self.height = QLabel(self.gridLayoutWidget)
        self.height.setObjectName(u"height")
        self.height.setFont(font2)

        self.gridLayout.addWidget(self.height, 1, 0, 1, 1)

        self.weight = QLabel(self.gridLayoutWidget)
        self.weight.setObjectName(u"weight")
        self.weight.setFont(font2)

        self.gridLayout.addWidget(self.weight, 0, 0, 1, 1)

        self.height_kq = QLineEdit(self.gridLayoutWidget)
        self.height_kq.setObjectName(u"height_kq")
        self.height_kq.setFont(font1)

        self.gridLayout.addWidget(self.height_kq, 0, 1, 1, 1)

        self.temp_kq = QLineEdit(self.gridLayoutWidget)
        self.temp_kq.setObjectName(u"temp_kq")
        self.temp_kq.setFont(font1)

        self.gridLayout.addWidget(self.temp_kq, 1, 1, 1, 1)

        self.weight_kq = QLineEdit(self.gridLayoutWidget)
        self.weight_kq.setObjectName(u"weight_kq")
        self.weight_kq.setFont(font1)

        self.gridLayout.addWidget(self.weight_kq, 2, 1, 1, 1)

        self.horizontalLayoutWidget = QWidget(self.page)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(489, 159, 351, 141))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox_3 = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout.addWidget(self.checkBox_3)

        self.radioButton = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout.addWidget(self.radioButton)

        self.commandLinkButton = QCommandLinkButton(self.horizontalLayoutWidget)
        self.commandLinkButton.setObjectName(u"commandLinkButton")

        self.horizontalLayout.addWidget(self.commandLinkButton)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1045, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.enterName.setText("")
        self.enterName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"H\u1ecd v\u00e0 T\u00ean", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Nam", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"N\u1eef", None))
        self.temp.setText(QCoreApplication.translate("MainWindow", u"Nhi\u1ec7t \u0111\u1ed9", None))
        self.height.setText(QCoreApplication.translate("MainWindow", u"Chi\u1ec1u cao", None))
        self.weight.setText(QCoreApplication.translate("MainWindow", u"C\u00e2n n\u1eb7ng", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
    # retranslateUi

