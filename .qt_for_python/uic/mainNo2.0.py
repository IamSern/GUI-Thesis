# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainNo2.0.ui'
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
        MainWindow.resize(1080, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 30))
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setStyleSheet(u"background-color: rgb(161, 99, 127);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.info_present = QFrame(self.frame_2)
        self.info_present.setObjectName(u"info_present")
        self.info_present.setFrameShape(QFrame.StyledPanel)
        self.info_present.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.info_present)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.thongtincanhan = QFrame(self.info_present)
        self.thongtincanhan.setObjectName(u"thongtincanhan")
        self.thongtincanhan.setMaximumSize(QSize(16777215, 400))
        self.thongtincanhan.setFrameShape(QFrame.StyledPanel)
        self.thongtincanhan.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.thongtincanhan)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.thongtincanhan)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 60))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.thongtincanhan)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(9)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(20, 0, 20, 0)
        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(70, 16777215))
        font1 = QFont()
        font1.setPointSize(14)
        self.comboBox.setFont(font1)

        self.gridLayout.addWidget(self.comboBox, 1, 3, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font1)

        self.gridLayout.addWidget(self.lineEdit_2, 2, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        font2 = QFont()
        font2.setPointSize(16)
        self.lineEdit.setFont(font2)

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 5)

        self.radioButton_2 = QRadioButton(self.frame_3)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setMinimumSize(QSize(70, 0))
        self.radioButton_2.setFont(font2)

        self.gridLayout.addWidget(self.radioButton_2, 0, 6, 1, 1)

        self.radioButton = QRadioButton(self.frame_3)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMinimumSize(QSize(70, 0))
        self.radioButton.setFont(font2)

        self.gridLayout.addWidget(self.radioButton, 0, 5, 1, 1)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 3)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.thongtincanhan)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 150))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, 0, 20, 6)
        self.textEdit = QTextEdit(self.frame_5)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit.setFont(font1)

        self.horizontalLayout_3.addWidget(self.textEdit)

        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(80, 30))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.pushButton.setFont(font3)

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.thongtincanhan)

        self.ketquado = QFrame(self.info_present)
        self.ketquado.setObjectName(u"ketquado")
        self.ketquado.setMinimumSize(QSize(0, 350))
        self.ketquado.setStyleSheet(u"background-color: rgb(75, 180, 222);")
        self.ketquado.setFrameShape(QFrame.StyledPanel)
        self.ketquado.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.ketquado)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 10, 0, 0)
        self.frame_7 = QFrame(self.ketquado)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(259, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer_3)


        self.gridLayout_3.addWidget(self.frame_7, 1, 1, 1, 1)

        self.label_4 = QLabel(self.ketquado)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 50))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 2)

        self.frame_6 = QFrame(self.ketquado)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_6)
        self.formLayout.setObjectName(u"formLayout")
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        font4 = QFont()
        font4.setPointSize(12)
        self.label_5.setFont(font4)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.lineTemp = QLineEdit(self.frame_6)
        self.lineTemp.setObjectName(u"lineTemp")
        self.lineTemp.setFont(font4)
        self.lineTemp.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineTemp)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.lineHeight = QLineEdit(self.frame_6)
        self.lineHeight.setObjectName(u"lineHeight")
        self.lineHeight.setFont(font4)
        self.lineHeight.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineHeight)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.lineWeight = QLineEdit(self.frame_6)
        self.lineWeight.setObjectName(u"lineWeight")
        self.lineWeight.setFont(font4)
        self.lineWeight.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineWeight)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_9)

        self.linePressure = QLineEdit(self.frame_6)
        self.linePressure.setObjectName(u"linePressure")
        self.linePressure.setFont(font4)
        self.linePressure.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.linePressure)

        self.linePulse = QLineEdit(self.frame_6)
        self.linePulse.setObjectName(u"linePulse")
        self.linePulse.setFont(font4)
        self.linePulse.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.linePulse)


        self.gridLayout_3.addWidget(self.frame_6, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.ketquado)


        self.horizontalLayout.addWidget(self.info_present)

        self.history = QFrame(self.frame_2)
        self.history.setObjectName(u"history")
        self.history.setStyleSheet(u"background-color: rgb(239, 219, 203);")
        self.history.setFrameShape(QFrame.StyledPanel)
        self.history.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.history)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalSpacer = QSpacerItem(488, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer)


        self.horizontalLayout.addWidget(self.history)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TH\u00d4NG TIN", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1990", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"1991", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"1992", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"1993", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"1994", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"1995", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"1996", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"1997", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"1998", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"1999", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"2000", None))

        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"H\u1ecd v\u00e0 t\u00ean", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"N\u1eef", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Nam", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 b\u1ec7nh nh\u00e2n", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"N\u0103m sinh", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"L\u00ed do kh\u00e1m", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"L\u01b0u", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"K\u1ebeT QU\u1ea2 \u0110O", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nhi\u1ec7t \u0111\u1ed9", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Chi\u1ec1u cao", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"C\u00e2n n\u1eb7ng", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Huy\u1ebft \u00e1p", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Nh\u1ecbp tim", None))
    # retranslateUi

